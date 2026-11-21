# CT-12 Lesson 07 — AI-Assisted Color Matching and Human Validation

- Course: CT-12 — Color Correction & Color Grading
- Level: AI & Automation
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-12 lessons and authorized footage
- Tools/environment: Color-managed NLE or grading application; record OS/app/version, display and color pipeline
- Version/review date: Tool-neutral; verify delivery color requirements with client/platform

## Learning outcomes
Evaluate automated shot matching, color suggestions and masking while verifying color accuracy and provenance through human review.

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
AI-assisted tools can propose matching, masks, denoise and look variations. They may misread mixed lighting, skin tone, unusual materials or intentional color. Automated matching is a starting point. Keep source grades reversible and compare with references and scopes.

## Tools, requirements and alternatives
Use a current NLE or dedicated grading application with scopes and color management. Record source camera profile, working space, monitoring conditions and delivery transform. Exact controls vary by software/version. Use authorized footage.

## Procedure
1. Define a bounded assistance task. 2. Confirm media privacy and service terms. 3. Preserve original and base grade. 4. Generate a proposed match or mask. 5. Compare to reference still and scopes. 6. Inspect skin, neutral objects and highlights. 7. Correct manually and record changes. 8. Log tool/model/version and reviewer.

## Worked example
Automated match proposes a baseline for a second camera. Colorist checks scope and skin/object fidelity before accepting.

## Dry run
AI neutralizes a warm sunset that is intentional. Reject automatic correction and restore creative intent.

## Guided practice
Compare manual and automated matching across three shots.

## Independent assignment
Apply the workflow to a second scene with different lighting or camera source. Submit editable grade, reference frames, scopes and delivery QC.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit reference set, AI output, final grade and provenance log. | Color workflow issue | Inspect source transform, scopes and reference | Correct and render a proof |

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
