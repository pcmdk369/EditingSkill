#!/usr/bin/env python3
"""Dependency-free repository checks for PCMDK369 EditingSkill.

Checks canonical course entry points, all 16 specialist skill entry points,
and local Markdown links. This script does not validate lesson quality or run
external editing applications.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
COURSES = [
    "CT-01-video-editing.md",
    "CT-02-film-cinematic-editing.md",
    "CT-03-short-form-social-video.md",
    "CT-04-documentary-interview-editing.md",
    "CT-05-commercial-advertisement-editing.md",
    "CT-06-music-video-performance-editing.md",
    "CT-07-photo-image-editing.md",
    "CT-08-digital-illustration-graphic-editing.md",
    "CT-09-portrait-beauty-retouching.md",
    "CT-10-product-ecommerce-image-editing.md",
    "CT-11-photo-restoration-manipulation.md",
    "CT-12-color-correction-grading.md",
    "CT-13-audio-editing.md",
    "CT-14-dialogue-voice-podcast-editing.md",
    "CT-15-sound-design-foley.md",
    "CT-16-music-production-audio-mixing.md",
    "CT-17-2d-animation.md",
    "CT-18-3d-animation.md",
    "CT-19-motion-graphics-kinetic-typography.md",
    "CT-20-vfx-compositing.md",
    "CT-21-green-screen-chroma-key.md",
    "CT-22-3d-modeling-materials-rendering.md",
    "CT-23-subtitles-captions-localization.md",
    "CT-24-ai-assisted-image-editing.md",
    "CT-25-ai-assisted-video-editing.md",
    "CT-26-ai-voice-dubbing-speech.md",
    "CT-27-batch-editing-media-automation.md",
    "CT-28-live-streaming-content-editing.md",
    "CT-29-mobile-editing-creator-workflows.md",
    "CT-30-professional-post-production-finishing.md",
]
SKILLS = [
    "video-editing", "audio-editing", "image-editing", "photo-editing",
    "graphic-design", "animation", "motion-graphics", "3d-editing", "vfx",
    "subtitles", "color-grading", "ai-editing", "automation",
    "software-tools", "workflows", "quality-control",
]
PRACTICE_CSV = {
    "practice-assets/asset-manifest.csv": ("asset_id", "filename", "rights_status", "checksum_sha256"),
    "practice-assets/shot-log.csv": ("clip_id", "source_in", "source_out", "editorial_decision"),
    "practice-assets/rights-and-consent-register.csv": ("asset_id", "permission_scope", "approval_evidence", "release_gate"),
}
PRACTICE_FILES = [
    "practice-assets/README.md",
    "practice-assets/transcript.srt",
    "practice-assets/delivery-qc-checklist.md",
]
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def slug(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return re.sub(r"\s+", "-", text)


def strip_fences(text: str) -> str:
    return re.sub(r"(?ms)^\s*```.*?^\s*```\s*$", "", text)


def check_markdown_links() -> int:
    errors = 0
    for md in ROOT.rglob("*.md"):
        try:
            content = strip_fences(md.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            fail(f"not UTF-8: {md.relative_to(ROOT)}")
            errors += 1
            continue
        anchors: set[str] = set()
        for line in content.splitlines():
            match = HEADING_RE.match(line)
            if match:
                anchors.add(slug(match.group(1)))
        for match in LINK_RE.finditer(content):
            target = match.group(1) or match.group(2) or ""
            target = target.strip()
            if not target or target.startswith("#"):
                continue
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc:
                continue
            path_part = unquote(parsed.path)
            if not path_part:
                continue
            candidate = (md.parent / path_part).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repository: {md.relative_to(ROOT)} -> {target}")
                errors += 1
                continue
            if not candidate.exists():
                fail(f"broken link: {md.relative_to(ROOT)} -> {target}")
                errors += 1
                continue
            if parsed.fragment and candidate.is_file() and candidate.suffix.lower() == ".md":
                try:
                    linked_text = strip_fences(candidate.read_text(encoding="utf-8"))
                    linked_anchors = {
                        slug(m.group(1))
                        for row in linked_text.splitlines()
                        if (m := HEADING_RE.match(row))
                    }
                    if unquote(parsed.fragment).lower() not in linked_anchors:
                        fail(f"missing heading anchor: {md.relative_to(ROOT)} -> {target}")
                        errors += 1
                except (UnicodeDecodeError, OSError):
                    pass
    return errors


def check_practice_assets() -> int:
    errors = 0
    for relative in PRACTICE_FILES:
        if not (ROOT / relative).is_file():
            fail(f"missing practice resource: {relative}")
            errors += 1
    for relative, required_headers in PRACTICE_CSV.items():
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing practice dataset: {relative}")
            errors += 1
            continue
        try:
            with path.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                missing = [header for header in required_headers if header not in (reader.fieldnames or [])]
                rows = list(reader)
            if missing:
                fail(f"{relative}: missing CSV columns: {', '.join(missing)}")
                errors += 1
            if not rows:
                fail(f"{relative}: dataset has no data rows")
                errors += 1
        except (OSError, UnicodeDecodeError, csv.Error) as exc:
            fail(f"{relative}: cannot parse CSV ({exc})")
            errors += 1

    transcript = ROOT / "practice-assets/transcript.srt"
    if transcript.is_file():
        try:
            content = transcript.read_text(encoding="utf-8").strip()
            blocks = re.split(r"\\n\\s*\\n", content)
            if not blocks or any(not re.match(r"^\\d+\\n\\d{2}:\\d{2}:\\d{2},\\d{3} --> \\d{2}:\\d{2}:\\d{2},\\d{3}\\n.+", block, re.S) for block in blocks):
                fail("practice-assets/transcript.srt: malformed SRT cue block")
                errors += 1
        except (OSError, UnicodeDecodeError) as exc:
            fail(f"practice-assets/transcript.srt: cannot read ({exc})")
            errors += 1
    return errors


def main() -> int:
    errors = 0
    course_root = ROOT / "course-types" / "courses"
    for course in COURSES:
        path = course_root / course
        if not path.is_file():
            fail(f"missing course entry point: {path.relative_to(ROOT)}")
            errors += 1
    for skill in SKILLS:
        path = ROOT / "Agentic" / "EditSkill" / skill / "SKILL.md"
        if not path.is_file():
            fail(f"missing specialist skill: {path.relative_to(ROOT)}")
            errors += 1
    if not (ROOT / "docs" / "COURSE-COMPLETION-REGISTER.md").is_file():
        fail("missing course completion register")
        errors += 1
    errors += check_practice_assets()\n    errors += check_markdown_links()
    if errors:
        print(f"Repository validation failed: {errors} issue(s).")
        return 1
    print(f"Repository validation passed: {len(COURSES)} course entry points, {len(SKILLS)} specialist skills, practice datasets and SRT structure, Markdown links checked.")
    print("Note: this validates repository structure and local links, not pedagogical quality, legal compliance, application execution or media renders.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
