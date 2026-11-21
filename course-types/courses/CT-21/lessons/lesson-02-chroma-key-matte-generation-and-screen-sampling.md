# CT-21 Lesson 02 — Chroma-Key Matte Generation and Screen Sampling

- Course: CT-21 — Green Screen & Chroma Key
- Level: Beginner / Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-21 lessons and authorized keyed footage
- Tools/environment: Video editor/compositor with keying, masks and tracking; record OS/app/version and camera metadata
- Version/review date: Tool-neutral; verify capture and delivery specifications

## Learning outcomes
Create a chroma key, sample screen color and adjust matte controls for solid subject coverage and clean transparency.

## Key definitions
- **Chroma key:** Separation based on a selected color range.
- **Matte:** Image/channel describing foreground transparency.
- **Spill:** Screen color reflected onto subject.
- **Garbage matte:** Mask excluding unwanted areas outside subject.
- **Holdout matte:** Mask preserving details that keyer would otherwise remove.
- **Light wrap:** Edge integration technique simulating background light around subject.
- **Parallax:** Apparent relative movement of objects at different depths.
- **Virtual production:** Production methods combining live action and digital environments.

## Purpose and theory
A chroma keyer separates pixels based on color similarity. Screen sampling should avoid shadows and highlights. Matte controls such as clip black/white, tolerance and softness vary by software. Use a matte view to inspect holes and edge chatter rather than judging only the composite.

## Tools, requirements and alternatives
Use a current compositor/video editor with keying and mask tools. Record camera/lens/frame rate, color settings, source resolution and alpha convention. Preserve original plates and use authorized footage.

## Procedure
1. Import source and verify color interpretation. 2. Select representative screen sample. 3. Create initial key. 4. Inspect matte output. 5. Adjust tolerance/density. 6. Remove screen shadows/uneven regions with masks. 7. Protect subject details with holdout mattes. 8. Preview on contrasting backgrounds.

## Worked example
A clean green screen produces a solid subject matte with transparent background and preserved hair edges.

## Dry run
Matte contains holes in dark clothing. Adjust sampling and use a holdout matte rather than increasing key tolerance indiscriminately.

## Guided practice
Create a matte for a 5-second presenter clip.

## Independent assignment
Apply the workflow to a second clip with different wardrobe, lighting or camera movement. Submit source, matte, final composite, settings and QC report.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit key settings, matte view and composite. | Keying issue | Inspect source lighting, matte and composite | Correct and review full motion |

## Knowledge check
1. Why is screen and subject lighting separated?
2. What is the difference between garbage and holdout mattes?
3. Why must hair edges be checked over motion?
4. What makes a keyed subject look like it is floating?
5. What should a professional keying package include?

## Answer guidance
1. To keep screen uniform and subject lighting independent.
2. Garbage matte removes irrelevant regions; holdout matte preserves subject details.
3. Partial transparency and movement reveal temporal chatter.
4. Missing contact/cast shadow, scale or perspective mismatch.
5. Composite, matte/foreground if required, plate, metadata, project and manifest.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Capture/source analysis | 4 | Camera/lighting notes |
| Matte quality | 5 | Alpha inspection |
| Edge/spill control | 4 | Contrasting-background test |
| Background integration | 4 | Full composite playback |
| Rights/handoff | 3 | Manifest and project |

Pass: 16/20. Unauthorized source use or missing frame integrity requires remediation.

## Quality-control checklist
- [ ] Screen lighting and camera settings recorded.
- [ ] Matte has no major holes/chatter.
- [ ] Hair/transparency edges preserved.
- [ ] Spill suppression does not distort subject.
- [ ] Scale, light and perspective match background.
- [ ] Full sequence reviewed.
- [ ] Alpha and dependencies packaged.

## Further study
- [Blackmagic Design — DaVinci Resolve Training](https://www.blackmagicdesign.com/products/davinciresolve/training)
- Selected compositor's official chroma-key documentation.

## Version and change notes
Tool-neutral. Keyer controls and alpha conventions vary; verify exact behavior in the chosen application.
