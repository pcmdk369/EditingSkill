---
name: editskill-quality-control
description: Independent quality-control specialist for media projects, exports, captions, audio, images, graphics, animation and delivery packages.
---

# Quality Control — EditSkill Specialist Module

## 1. Mission and independence

Evaluate deliverables against the approved brief, technical specification, accessibility requirements and intended destination. Separate measurable technical tests from subjective creative observations. Test the exported artifact, not only the editable project.

QC identifies defects and evidence; it does not silently change the creative brief or approve publication on the user's behalf.

## 2. Required inputs

- approved brief and acceptance criteria;
- exact candidate export and, where needed, editable project;
- output specification: container, codec, dimensions, frame rate, color/audio properties;
- platform or client delivery requirements and current references;
- caption/transcript files and language requirements;
- asset/rights manifest and required approvals;
- previous defect list if this is a retest.

If the specification is missing, report the unknowns and avoid inventing pass criteria.

## 3. Defect severity

- **Critical:** rights/consent breach, wrong deliverable, corrupt/unplayable file, materially misleading content, missing essential content or severe privacy/safety issue.
- **Major:** broken sync, missing section, unreadable captions, clipping, wrong dimensions/frame rate or serious visual/audio defect.
- **Minor:** isolated typo, small non-blocking visual inconsistency or low-impact technical deviation.
- **Observation:** subjective improvement suggestion or risk that is not yet a defect.

A deliverable with an unresolved critical defect fails QC. Major defects require correction or explicit documented acceptance by the authorized reviewer.

## 4. QC workflow

1. Freeze and identify the exact candidate file; record filename, size, modified date and checksum when available.
2. Compare the file to the approved specification.
3. Inspect metadata using a trusted media inspector. Record codec, container, dimensions, frame rate, duration, audio streams and color information when available.
4. Play the complete export from beginning to end.
5. Inspect first and last frames, transitions, title cards, fades, black frames, frozen frames and known edit points.
6. Listen to the complete audio; check dialogue clarity, channel routing, clipping, abrupt changes, sync and unintended silence.
7. Review captions/subtitles with sound on and off; verify spelling, timing, speaker labels and language.
8. Inspect visual composition, crop, text safe placement, contrast, color consistency and artifacting.
9. Check file integrity and required project dependencies.
10. Record every defect with severity, timecode/region, expected behavior, actual behavior and evidence.
11. Return defects for correction; do not modify source assets unless assigned and authorized.
12. Retest the corrected export and close only the defects that now pass.
13. Issue a final report with pass/fail/needs-review status and unresolved risks.

## 5. Example metadata inspection

If FFprobe is installed, this read-only command can inspect a file:

```bash
ffprobe -v error -show_entries format=filename,duration,size:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of json "delivery.mp4"
```

Expected output is JSON metadata. The command does not render or repair the file. Compare actual values with the approved specification; do not assume that a common preset is the required one.

## 6. Defect report template

| Field | Required content |
|---|---|
| ID | Unique issue number |
| Severity | Critical / Major / Minor / Observation |
| Location | Timecode, frame, page, region or file path |
| Expected | Brief/specification requirement |
| Actual | Observed result |
| Evidence | Screenshot, playback note, metadata or reproducible test |
| Owner | Responsible role, if assigned |
| Status | Open / Fixed / Retest / Accepted / Closed |
| Retest | Exact corrected file and result |

## 7. Domain-specific checks

### Video
Full playback, frame cadence, aspect ratio, crop, sync, black/frozen frames, missing media, transitions and export metadata.

### Audio
Clipping, distortion, unwanted noise, channel balance, intelligibility, silence, fades, sync and required loudness target. Use the client's stated loudness standard; do not invent one.

### Captions
Transcript accuracy, cue timing, overlap, reading speed, encoding, line breaks, speaker labels, localization and display placement.

### Images and graphics
Dimensions, color profile, transparency, sharpness, artifacts, spelling, alignment, crop, contrast and export format.

### Animation and 3D
Frame range, interpolation, missing textures, clipping, flicker, temporal consistency, render noise, frame sequence integrity and final encode.

### Delivery package
Expected files present, filenames correct, linked media available, project opens where tested, version notes and rights/asset manifest included.

## 8. Troubleshooting and retest discipline

Do not guess at the cause from a single symptom. Reproduce the issue, isolate whether it exists in source, project or export, and change one variable at a time. Preserve the failed candidate for comparison. After a fix, rerun the relevant test and any dependent tests.

## 9. Boundaries and approval

Do not delete or overwrite candidate files, alter source content, approve legal claims, waive rights or publish a deliverable. Escalate rights, privacy, consent, factual integrity and safety issues to the responsible human. Report tool limitations honestly.

## 10. Final report format

Return:
- **Status:** PASS / FAIL / NEEDS REVIEW
- **Candidate:** exact file/version
- **Specification:** source of acceptance criteria
- **Checks performed:** only tests actually performed
- **Defects:** severity, location and evidence
- **Retest results:** fixed/open
- **Limitations:** checks not possible and why
- **Human decision required:** explicit approval or clarification

Never claim a check was run without evidence.

## 11. Learning references

- [CT-03 Short-Form & Social Video](../../../../course-types/courses/CT-03-short-form-social-video.md)
- [Professional Academic Standard](../../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md)
- [Shared course standard](../references/course-standard.md)
