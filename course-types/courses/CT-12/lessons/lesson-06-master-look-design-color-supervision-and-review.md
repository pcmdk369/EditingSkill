# CT-12 Lesson 06 — Look Design, Color Supervision and Review

- Course: CT-12 — Color Correction & Color Grading
- Level: Master
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-12 lessons and authorized footage
- Tools/environment: Color-managed NLE or grading application; record OS/app/version, display and color pipeline
- Version/review date: Tool-neutral; verify delivery color requirements with client/platform

## Learning outcomes
Develop a coherent show/campaign look, supervise collaborative grading and manage approval/version changes with reference evidence.

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
Master-level grading translates visual direction into repeatable decisions. The look bible should define contrast, saturation, hue relationships, skin/object priorities, highlight behavior and exceptions. Review must distinguish technical mismatch from subjective preference and preserve approved references.

## Tools, requirements and alternatives
Use a current NLE or dedicated grading application with scopes and color management. Record source camera profile, working space, monitoring conditions and delivery transform. Exact controls vary by software/version. Use authorized footage.

## Procedure
1. Define visual intent and scene requirements. 2. Create look references and a written look bible. 3. Grade hero shots and difficult edge cases. 4. Review across displays and scene contexts. 5. Establish shot-matching and exception rules. 6. Manage review notes by timecode/frame. 7. Lock approved look and version. 8. Record changes and final approval.

## Worked example
A series alternates daylight and night scenes. The look system maintains coherent contrast/color while allowing each scene to retain believable lighting.

## Dry run
Stakeholder asks for “more cinematic.” Translate into specific choices and compare reference stills rather than applying an arbitrary preset.

## Guided practice
Create a look bible and grade a five-shot sequence.

## Independent assignment
Apply the workflow to a second scene with different lighting or camera source. Submit editable grade, reference frames, scopes and delivery QC.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit look bible, hero frames, version log and review record. | Color workflow issue | Inspect source transform, scopes and reference | Correct and render a proof |

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
