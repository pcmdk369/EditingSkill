# CT-21 Lesson 03 — Edge Detail, Spill and Hair Refinement

- Course: CT-21 — Green Screen & Chroma Key
- Level: Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-21 lessons and authorized keyed footage
- Tools/environment: Video editor/compositor with keying, masks and tracking; record OS/app/version and camera metadata
- Version/review date: Tool-neutral; verify capture and delivery specifications

## Learning outcomes
Refine edges, preserve hair/fine detail and remove color spill without damaging subject color.

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
Edge treatment balances matte softness, detail recovery, despill and light wrap. Hair and motion blur contain partial transparency. Overly hard edges look cut out; excessive softness creates halos. Light wrap can integrate the subject but should not conceal poor keying.

## Tools, requirements and alternatives
Use a current compositor/video editor with keying and mask tools. Record camera/lens/frame rate, color settings, source resolution and alpha convention. Preserve original plates and use authorized footage.

## Procedure
1. Inspect edge at 100% and normal size. 2. Separate core matte from edge detail. 3. Refine hair/transparent regions. 4. Apply spill suppression to affected channels. 5. Check clothing and skin for color shift. 6. Add restrained light wrap only if scene supports it. 7. Test on light/dark backgrounds. 8. Review motion frame-by-frame.

## Worked example
Hair remains partially transparent and natural against a background with similar brightness.

## Dry run
Skin turns magenta after despill. Reduce strength and isolate edge region.

## Guided practice
Refine a presenter matte with hair and moving hands.

## Independent assignment
Apply the workflow to a second clip with different wardrobe, lighting or camera movement. Submit source, matte, final composite, settings and QC report.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit matte breakdown, despill settings and comparison. | Keying issue | Inspect source lighting, matte and composite | Correct and review full motion |

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
