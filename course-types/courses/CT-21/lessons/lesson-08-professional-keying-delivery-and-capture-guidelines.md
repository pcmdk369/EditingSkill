# CT-21 Lesson 08 — Professional Keying Delivery and Capture Guidelines

- Course: CT-21 — Green Screen & Chroma Key
- Level: Professional Practice
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-21 lessons and authorized keyed footage
- Tools/environment: Video editor/compositor with keying, masks and tracking; record OS/app/version and camera metadata
- Version/review date: Tool-neutral; verify capture and delivery specifications

## Learning outcomes
Deliver keying comps and reusable capture guidance with source plates, mattes, camera metadata, color pipeline and reproducible project files.

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
Professional keying packages may include final composite, clean plate, matte, foreground, background, camera metadata and project dependencies. Clear alpha convention and frame range prevent downstream problems. Capture guidance improves future production quality.

## Tools, requirements and alternatives
Use a current compositor/video editor with keying and mask tools. Record camera/lens/frame rate, color settings, source resolution and alpha convention. Preserve original plates and use authorized footage.

## Procedure
1. Confirm output spec, alpha and frame range. 2. Preserve original plate and camera metadata. 3. Validate matte and edge quality. 4. Export composite and requested foreground/matte. 5. Check alpha convention and color profile. 6. Play full sequence. 7. Package project, background and dependencies. 8. Create capture recommendations and manifest. 9. Archive securely.

## Worked example
A studio receives final composite, clean foreground, matte, camera notes and reusable lighting diagram.

## Dry run
Client expects a matte but only composite was rendered. Re-export required channels and test alpha in target app.

## Guided practice
Prepare a delivery package and capture guide for a keyed presenter shot.

## Independent assignment
Apply the workflow to a second clip with different wardrobe, lighting or camera movement. Submit source, matte, final composite, settings and QC report.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit final, matte, source plate, metadata, lighting guide, project and QC. | Keying issue | Inspect source lighting, matte and composite | Correct and review full motion |

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
