# CT-12 Lesson 08 — Professional Color Delivery, QC and Archive

- Course: CT-12 — Color Correction & Color Grading
- Level: Professional Practice
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-12 lessons and authorized footage
- Tools/environment: Color-managed NLE or grading application; record OS/app/version, display and color pipeline
- Version/review date: Tool-neutral; verify delivery color requirements with client/platform

## Learning outcomes
Deliver graded masters and review references with color-space metadata, LUT/node documentation, version control and verified playback.

## Key definitions
- **Color correction:** Technical normalization and matching of image color.
- **Color grading:** Creative shaping of color and contrast.
- **Color space:** Defined range/organization of colors.
- **LUT:** Lookup table mapping input color values to output values.
- **Waveform:** Scope displaying signal level over image position.
- **RGB parade:** Separate red, green and blue signal views.
- **Vectorscope:** Scope displaying chroma/hue distribution.
- **Conform:** Preparing media/timeline for finishing or a different pipeline.

## Purpose and theory
Professional color handoff must identify the output transform, codec, bit depth, frame rate, data levels and any client-specified HDR/SDR requirements. A still reference and project archive help future revisions. Do not assume a file is HDR because it looks bright or a label says “HDR.”

## Tools, requirements and alternatives
Use a current NLE or dedicated grading application with scopes and color management. Record source camera profile, working space, monitoring conditions and delivery transform. Exact controls vary by software/version. Use authorized footage.

## Procedure
1. Confirm approved output specification. 2. Verify final color transform and metadata. 3. Render a short test and inspect scopes/playback. 4. Check highlights, blacks, skin and saturation. 5. Compare export to approved reference. 6. Package project, LUTs and dependencies where permitted. 7. Record versions and settings. 8. Generate manifest and archive. 9. Confirm client approval and future revision path.

## Worked example
A graded master is delivered with reference stills, LUT register, project and technical specification sheet.

## Dry run
Export metadata says one color space but project output uses another. Stop delivery, correct settings and render proof again.

## Guided practice
Prepare a color handoff package for a five-shot sequence.

## Independent assignment
Apply the workflow to a second scene with different lighting or camera source. Submit editable grade, reference frames, scopes and delivery QC.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit master, reference stills, node/project archive, LUT register, QC report and manifest. | Color workflow issue | Inspect source transform, scopes and reference | Correct and render a proof |

## Knowledge check
1. How do correction and grading differ?
2. What can waveform and vectorscope show?
3. Why should technical matching precede creative look application?
4. What is a LUT and why does its input matter?
5. What should be checked in a color handoff?

## Answer guidance
1. Correction normalizes/matches; grading shapes creative appearance.
2. Signal levels/position and chroma/hue distribution respectively.
3. It creates a stable base and prevents the look from exaggerating source differences.
4. A color mapping; wrong input transform causes incorrect output.
5. Output transform, codec/bit depth, levels, metadata, project/LUTs and QC.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Color management and source handling | 4 | Pipeline notes |
| Primary correction | 4 | Scopes and before/after |
| Secondary/look quality | 4 | Node/mask graph |
| Shot matching | 4 | Reference comparison |
| Delivery and QC | 4 | Metadata and playback report |

Pass: 16/20. Incorrect output transform or unverified delivery settings require correction.

## Quality-control checklist
- [ ] Source and output color spaces recorded.
- [ ] Correct transform order confirmed.
- [ ] Exposure and channels checked on scopes.
- [ ] Skin/object color preserved.
- [ ] Shots match in motion.
- [ ] Export metadata matches brief.
- [ ] Reference stills and project archived.

## Further study
- [Blackmagic Design — DaVinci Resolve Training](https://www.blackmagicdesign.com/products/davinciresolve/training)
- [International Color Consortium](https://www.color.org/)
- Verify current camera, display and delivery specifications.

## Version and change notes
Tool-neutral. Color pipelines are version- and delivery-dependent. No software execution is claimed.
