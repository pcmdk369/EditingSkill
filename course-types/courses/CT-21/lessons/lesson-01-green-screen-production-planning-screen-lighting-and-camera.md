# CT-21 Lesson 01 — Green Screen Planning, Screen Lighting and Camera

- Course: CT-21 — Green Screen & Chroma Key
- Level: Foundation / Beginner
- Estimated time: 120–180 minutes
- Prerequisites: Basic video capture and compositing concepts
- Tools/environment: Video editor/compositor with keying, masks and tracking; record OS/app/version and camera metadata
- Version/review date: Tool-neutral; verify capture and delivery specifications

## Learning outcomes
Plan a chroma-key shoot with even screen illumination, subject separation, camera exposure and source metadata.

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
Keying quality is largely determined during capture. Screen should be lit evenly and separately from subject. Avoid spill, wrinkles, shadows and compression artifacts. Camera exposure, focus and motion blur affect edge quality. Record camera/lens/frame rate and color settings for post-production.

## Tools, requirements and alternatives
Use a current compositor/video editor with keying and mask tools. Record camera/lens/frame rate, color settings, source resolution and alpha convention. Preserve original plates and use authorized footage.

## Procedure
1. Confirm shot framing and key color. 2. Separate subject from screen. 3. Light screen evenly. 4. Light subject independently. 5. Avoid reflective/transparent wardrobe conflicts. 6. Set exposure, focus and white balance. 7. Record test frames and motion. 8. Document camera/lens/settings.

## Worked example
A presenter stands several feet from a uniformly lit green screen with separate key/fill lighting and no visible shadows.

## Dry run
Subject wears green clothing. Change wardrobe or use a different key color; do not expect keyer to preserve same-color subject detail automatically.

## Guided practice
Plan and capture a 10-second green-screen test with metadata.

## Independent assignment
Apply the workflow to a second clip with different wardrobe, lighting or camera movement. Submit source, matte, final composite, settings and QC report.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit lighting diagram, camera settings and test clip. | Keying issue | Inspect source lighting, matte and composite | Correct and review full motion |

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
