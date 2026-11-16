# CT-12 Lesson 02 — Primary Correction: Exposure, White Balance and Contrast

- Course: CT-12 — Color Correction & Color Grading
- Level: Beginner / Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-12 lessons and authorized footage
- Tools/environment: Color-managed NLE or grading application; record OS/app/version, display and color pipeline
- Version/review date: Tool-neutral; verify delivery color requirements with client/platform

## Learning outcomes
Normalize exposure, white balance and contrast using scopes and visual references while preserving highlight/shadow detail.

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
Primary correction addresses the whole image. Exposure and contrast adjustments should retain detail appropriate to the scene. White balance may be corrected using neutral references, but mixed lighting and intentional color require judgment. Avoid crushing shadows or clipping highlights merely to achieve a fashionable look.

## Tools, requirements and alternatives
Use a current NLE or dedicated grading application with scopes and color management. Record source camera profile, working space, monitoring conditions and delivery transform. Exact controls vary by software/version. Use authorized footage.

## Procedure
1. Confirm correct input transform. 2. Set exposure using waveform and reference. 3. Correct white balance with neutral cue where available. 4. Balance RGB channels. 5. Adjust contrast and pivot carefully. 6. Inspect highlights/shadows for clipping. 7. Compare adjacent shots. 8. Export a short proof and recheck.

## Worked example
Two shots from the same interview have different exposure. Normalize them before creative look development.

## Dry run
A dark scene is lifted until noise becomes dominant. Return to source exposure and balance visibility with intended mood.

## Guided practice
Correct three shots from one scene to a consistent baseline.

## Independent assignment
Apply the workflow to a second scene with different lighting or camera source. Submit editable grade, reference frames, scopes and delivery QC.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit before/after, scope notes and shot-match comparison. | Color workflow issue | Inspect source transform, scopes and reference | Correct and render a proof |

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
