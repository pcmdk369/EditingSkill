# CT-12 Lesson 04 — Shot Matching and Look Development

- Course: CT-12 — Color Correction & Color Grading
- Level: Advanced
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-12 lessons and authorized footage
- Tools/environment: Color-managed NLE or grading application; record OS/app/version, display and color pipeline
- Version/review date: Tool-neutral; verify delivery color requirements with client/platform

## Learning outcomes
Match shots across cameras and lighting, then create a coherent look with controlled contrast, saturation and color separation.

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
Shot matching creates continuity before a creative look is applied. Different cameras, lenses and lighting can respond differently to the same grade. A look should support narrative and art direction while preserving details and consistent skin/object color.

## Tools, requirements and alternatives
Use a current NLE or dedicated grading application with scopes and color management. Record source camera profile, working space, monitoring conditions and delivery transform. Exact controls vary by software/version. Use authorized footage.

## Procedure
1. Group shots by scene/camera. 2. Choose a reference frame. 3. Normalize exposure and white balance. 4. Match contrast and saturation. 5. Compare skin, neutrals and important objects. 6. Apply a look after technical match. 7. Check shot transitions in motion. 8. Save look/version separately from base correction.

## Worked example
Three cameras cover one scene. Match each to a reference before adding a cool-shadow/warm-highlight look.

## Dry run
A look is applied before matching and exaggerates camera differences. Disable look, match first, then reapply consistently.

## Guided practice
Create a matched four-shot scene and one approved creative look.

## Independent assignment
Apply the workflow to a second scene with different lighting or camera source. Submit editable grade, reference frames, scopes and delivery QC.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit reference frame, node graph, scopes and comparison export. | Color workflow issue | Inspect source transform, scopes and reference | Correct and render a proof |

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
