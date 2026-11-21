# CT-02 Lab 04 — Picture Lock, Finishing Handoff and Quality Control

**Level:** Advanced → Professional Practice  
**Estimated time:** 2–4 hours  
**Software:** NLE plus media player capable of inspecting the rendered file; optional audio meter and file metadata inspector.  
**Output:** Approved short scene export, handoff package and completed QC report.

## Learning outcomes
The learner can prepare a fine cut for review, document picture lock, create a controlled finishing handoff, export to a stated specification and inspect the actual delivered file.

## Prerequisites and materials
- CT-02 Labs 01–03 or equivalent experience.
- A completed 1–3 minute scene.
- Written delivery specification. If none is supplied, the learner must create and label a clearly provisional specification rather than claiming it is an industry standard.
- Rights/consent records for all media.

## Concepts
**Picture lock** is formal approval of picture timing for downstream finishing. **Conform** reconnects or rebuilds the approved edit from intended sources. **Quality control (QC)** is a documented check that the delivered file meets creative, technical and contractual requirements.

## Procedure

### A. Prepare for picture lock
1. Save a new fine-cut version.
2. Review the full scene at normal speed.
3. Check story completeness, performance, continuity, screen direction and pacing.
4. Confirm titles, credits, subtitles and graphic placeholders are resolved or clearly marked.
5. Record all outstanding issues and their owners.
6. Obtain documented approval from the responsible reviewer or mark the sequence as learner-approved for the exercise.

### B. Freeze and document the approved edit
1. Duplicate or tag the approved sequence as `PICTURE_LOCK`.
2. Record sequence frame rate, frame size, duration, audio layout and version ID.
3. Export or save an edit decision/reference record if the NLE supports it.
4. Store the locked version as read-only or protect it using the production's version-control method.
5. Any later picture change must have a change request with timecode, reason, approval and downstream impact.

### C. Prepare the handoff
Include only authorized materials:
- approved picture-locked project or interchange file where supported;
- media inventory and relink instructions;
- source and proxy relationship notes;
- title/graphics assets;
- music and footage license records;
- version/change log;
- delivery specification;
- unresolved issue list, if any.

Do not assume the recipient has access to your local drives or cloud accounts.

### D. Export
1. Confirm the requested container, codec, frame size, frame rate, scan type, audio channels, sample rate and any loudness/peak requirement.
2. Verify color space and transfer characteristics against the brief and workflow.
3. Choose an export preset only after checking its actual settings.
4. Export to a new delivery folder; never overwrite the approved master without authorization.
5. Record export filename, software/version, date, duration and relevant settings.

### E. Inspect the actual delivered file
1. Confirm the file exists and its size is plausible.
2. Open it in a separate media player.
3. Watch the complete file from beginning to end.
4. Check first and last frames, black gaps, flash frames, missing shots, freeze frames and unintended overlays.
5. Listen to the complete audio, checking dialogue intelligibility, missing channels, clipping, sync, abrupt cuts and unintended silence.
6. Inspect titles, spelling, captions, credits and safe placement.
7. Compare file properties with the written delivery specification.
8. Record each result as Pass, Fail or Not Applicable.
9. Correct failures, re-export to a new version and repeat the full QC pass.

## Worked example
The delivery brief requests a 1920×1080 progressive file at a specified frame rate with stereo audio. The export preset is named “1080p master,” but its audio is mono. The preset name is not proof of compliance: inspect actual metadata, correct the channel mapping, export a new version and recheck the delivered file.

## QC checklist

| Check | Result (Pass/Fail/N/A) | Evidence/notes |
|---|---|---|
| Correct version and filename | | |
| Correct duration and frame rate | | |
| Correct frame size and scan type | | |
| Correct codec/container | | |
| Correct audio channel layout | | |
| Dialogue sync and intelligibility | | |
| No unintended black/frozen/flash frames | | |
| No missing media or offline graphics | | |
| Titles/captions/credits checked | | |
| Rights and consent records present | | |
| Complete file played from start to end | | |
| Handoff files and relink notes included | | |

## Troubleshooting
| Failure | Likely cause | Response |
|---|---|---|
| Export has wrong dimensions | Sequence or export scaling | Compare sequence and export settings with brief |
| Audio channel mismatch | Incorrect routing or preset | Inspect track routing and rendered metadata |
| Missing titles/media | Unavailable assets or broken links | Relink authorized assets and export a new version |
| Picture differs from approved cut | Wrong sequence/version exported | Reconfirm version ID and export from locked sequence |
| File plays only partly | Incomplete render or storage issue | Check render completion and available storage; render a new version |

## Submission evidence
- Picture-lock approval record or learner approval statement.
- Version/change log.
- Delivery specification.
- Handoff folder inventory.
- Final export.
- Completed QC checklist with evidence.
- Reflection describing one defect found during QC and how it was corrected.

## Assessment — 30 points
- Picture-lock discipline: 6
- Handoff completeness: 6
- Export specification accuracy: 6
- Full-file QC and evidence: 8
- Rights/version documentation: 4

**Pass:** 21/30. Any uncorrected rights violation, missing source preservation or knowingly misrepresented technical compliance is a critical failure.

## Quality gate
The exported file—not merely the timeline—has been fully reviewed; actual file properties match the brief; the approved sequence is identifiable; handoff assets are traceable; rights and version records are present.
