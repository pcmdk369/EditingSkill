# CT-02 Lesson 08 — Finishing, Delivery and Quality Control

- Course: CT-02 — Film & Cinematic Editing
- Level: Professional Practice
- Estimated time: 4–5 hours
- Prerequisites: Lesson 07 and an approved picture-lock version
- Environment: NLE plus reliable playback/inspection tools
- Version/review date: 1.0 — 2026-11-16

## Learning outcomes
Learners can prepare a finishing turnover, verify picture/audio/subtitle requirements, export a controlled master and review the actual file rather than trusting export settings.

## Key terms
- **Master:** approved high-quality deliverable used as the source for distribution versions.
- **Mezzanine:** high-quality intermediate file suitable for downstream processing.
- **Turnover:** handoff of locked picture, references, notes and dependencies.
- **QC:** systematic quality control against written acceptance criteria.
- **Checksum:** value used to detect whether a file has changed or transferred incorrectly.
- **Conform:** rebuild/prepare a sequence from approved edit decisions and source media.

## Professional principles
Finishing is specification-driven. “High quality” is not a sufficient delivery instruction. Confirm container, codec, resolution, frame rate, scan/progressive format, color properties, audio layout/loudness, caption format, runtime, naming, version and destination. Requirements differ by broadcaster, platform, festival and client. Never invent a universal specification.

## Procedure
1. Obtain the approved picture-lock sequence ID and change-freeze status.
2. Confirm the delivery specification in writing with the responsible stakeholder.
3. Check media relinking, sequence settings, handles, titles, graphics, VFX and source dependencies.
4. Confirm color-management assumptions and that the grade/online workflow matches the intended output.
5. Confirm audio stems, channel layout, sample rate, loudness/true-peak requirements and sync.
6. Confirm subtitle/caption language, timing, safe area, spelling and requested file format.
7. Create a pre-export checklist and a unique output filename including project, version, format and date.
8. Export a master and required access/review copies using the approved settings.
9. Inspect the exported file's metadata with a trusted tool.
10. Watch/listen to the actual export from beginning to end where feasible; at minimum, use a documented full-QC process rather than spot-checking alone.
11. Check first/last frames, black/freeze frames, flash frames, missing media, sync, audio peaks, captions, title spelling and end credits.
12. Verify file opens and plays on a second player/device where practical.
13. Record actual properties and pass/fail results. Re-export after corrections and repeat affected checks.
14. Package project, media dependencies, exports, captions, notes, version manifest and checksum where required.

## Worked example
A festival requests a progressive 1920×1080 master at a specified frame rate, stereo audio and separate English subtitle file. The editor does not assume a codec or loudness target: these must come from the festival's current written specification. After export, metadata and full playback are checked; the subtitle file is tested for encoding and timing.

## Dry run
Create a fictional delivery spec and a matching export checklist. Mark any unspecified field as “confirmation required.” Do not fill unknown requirements with guesses.

## Guided practice
Export a short approved scene to a review file. Inspect metadata, play the entire export and complete a QC report listing test, expected result, actual result and evidence.

## Independent assignment
Prepare a finishing package for a 3–5 minute scene, including master/review versions, subtitle file if required, project handoff, delivery manifest and QC report.

## Common errors and recovery
| Symptom | Likely cause | Recovery |
|---|---|---|
| Export differs from timeline | Wrong range, sequence or render setting | Compare sequence ID and export metadata |
| Captions clipped | Safe-area or format mismatch | Correct and re-test on target frame |
| Audio missing on playback | Channel mapping/layout error | Inspect streams and re-export |
| File corrupt or incomplete | Interrupted export/storage failure | Re-export to verified storage and test |
| Wrong frame rate | Preset not aligned with spec | Correct settings; verify actual output |

## Knowledge check
1. Why is a written delivery spec essential? — It defines measurable acceptance criteria.
2. Why inspect the rendered file? — Export settings alone do not prove output integrity.
3. What is a turnover package? — The files, references and notes needed for downstream work.

## Assessment rubric (100)
Specification accuracy 20; project/turnover integrity 15; export settings 20; playback/metadata QC 25; documentation and packaging 20. Pass 80 and all critical delivery checks must pass.

## QC checklist
- [ ] Approved sequence and spec identified.
- [ ] Actual export metadata recorded.
- [ ] Full playback/QC completed.
- [ ] Audio, captions and titles checked.
- [ ] Deliverables and project dependencies packaged.

## Version notes
Use current client/platform documentation. This lesson intentionally avoids prescribing a codec or loudness value without a delivery specification.
