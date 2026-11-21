# CT-23 Lesson 01 — Captioning, Accessibility and Transcript Basics

- Course: CT-23 — Subtitles, Captions & Localization
- Level: Foundation / Beginner
- Estimated time: 120–180 minutes
- Prerequisites: Basic language/media literacy and audio playback
- Tools/environment: Subtitle editor, text editor and target media player; record OS/app/version and locale
- Version/review date: Tool-neutral; verify current platform/accessibility specifications

## Learning outcomes
Understand captions/subtitles, accessibility goals, transcript types and source-audio review.

## Key definitions
- **Caption:** Timed text representing speech and, where required, meaningful non-speech audio.
- **Subtitle:** Timed text representing dialogue, often translated or adapted.
- **Cue:** One timed text event.
- **Reading speed:** Text amount relative to display duration.
- **SDH:** Subtitles for the deaf and hard of hearing.
- **Locale:** Language and regional conventions.
- **Glossary:** Approved terminology list.
- **Sidecar file:** Separate subtitle/caption file accompanying video.

## Purpose and theory
Captions represent spoken dialogue and may include relevant non-speech audio; subtitles often focus on dialogue and translation, but usage differs by region/platform. Accessibility requires accurate content, readable timing and meaningful sound cues. Automated transcripts are drafts, not ground truth.

## Tools, requirements and alternatives
Use a current subtitle editor and target playback tool. Record source master version, language/locale, file format and encoding. Use authorized media and protect sensitive recordings. Confirm destination requirements rather than assuming one universal reading-speed rule.

## Procedure
1. Identify audience, language and accessibility need. 2. Confirm exact video/audio version. 3. Create source transcript. 4. Mark speakers and meaningful non-speech audio. 5. Verify names/numbers/negation. 6. Choose caption/subtitle convention. 7. Record destination format and reading rules. 8. Preserve source and transcript versions.

## Worked example
A documentary interview requires captions including speaker labels and meaningful sound cues; a translated subtitle version is a separate deliverable.

## Dry run
Transcript says “fifteen” but audio says “fifty.” Correct against recording and update every downstream file.

## Guided practice
Create a verbatim transcript for a one-minute clip and mark uncertainty.

## Independent assignment
Apply the workflow to a second clip or target locale. Submit source transcript, subtitle file, reviewer notes and validation evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit transcript, audio verification notes and caption brief. | Subtitle issue | Compare with source media and target player | Correct and retest |

## Knowledge check
1. Why should captions be checked against audio?
2. What affects reading speed and cue segmentation?
3. How do SRT and WebVTT differ?
4. Why is localization more than literal translation?
5. What can automated QA not reliably verify?

## Answer guidance
1. ASR can mishear names, numbers, negation and speakers.
2. Text length, complexity, duration, language and audience.
3. They use different syntax/metadata conventions.
4. It adapts locale, idiom, culture, units and meaning.
5. Semantic accuracy, cultural nuance and accessibility context.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Transcript accuracy | 4 | Source comparison |
| Timing/segmentation | 4 | Cue review |
| Format/encoding | 4 | Parser/player test |
| Translation/accessibility | 4 | Glossary/reviewer notes |
| Versioning/handoff | 4 | Manifest and QA log |

Pass: 16/20. Misleading translation, missing negation or unauthorized processing requires remediation.

## Quality-control checklist
- [ ] Exact source master identified.
- [ ] Transcript verified against audio.
- [ ] Cue timing and reading speed checked.
- [ ] Text segmentation and line breaks reviewed.
- [ ] Translation reviewed by competent human.
- [ ] Encoding/syntax tested in target player.
- [ ] Language/version and delivery manifest complete.

## Further study
- [W3C — WebVTT](https://www.w3.org/TR/webvtt1/)
- [W3C — Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/)
- Confirm current platform caption/subtitle guidance.

## Version and change notes
Tool-neutral. Reading-speed limits and caption conventions vary by audience, platform and jurisdiction; follow the project specification.
