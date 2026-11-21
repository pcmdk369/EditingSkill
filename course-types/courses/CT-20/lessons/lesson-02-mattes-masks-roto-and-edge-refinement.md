# CT-20 Lesson 02 — Mattes, Masks, Rotoscoping and Edge Refinement

- Course: CT-20 — Visual Effects & Compositing
- Level: Beginner / Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-20 lessons and authorized footage/assets
- Tools/environment: Compositing application with node/layer, tracking and render support; record OS/app/version
- Version/review date: Tool-neutral; verify pipeline specifications and software behavior

## Learning outcomes
Create clean mattes and animated masks, refine edges and preserve motion continuity.

## Key definitions
- **Compositing:** Combining image elements into one visual result.
- **Matte:** Image/channel defining foreground transparency.
- **Rotoscoping:** Creating animated masks around moving subjects.
- **Spill suppression:** Reducing reflected screen color on subject edges.
- **Tracking:** Estimating motion from image features.
- **Matchmove:** Recreating camera motion for CG integration.
- **Render pass:** Separate component of a rendered image.
- **Conform:** Aligning shots to the final editorial timeline.

## Purpose and theory
A matte separates foreground from background. Rotoscoping traces moving subjects over time. Edge quality depends on motion blur, hair, transparency and camera movement. A matte must be reviewed across the entire shot, not just one frame.

## Tools, requirements and alternatives
Use a current compositing application and media inspector. Record source frame rate, resolution, color space, alpha convention and application version. Preserve original plates and use authorized footage/assets.

## Procedure
1. Choose key frames and analyze motion. 2. Create initial mask/matte. 3. Track or animate shape. 4. Refine edge softness and motion blur. 5. Check hair/transparency separately. 6. Review matte on contrasting backgrounds. 7. Correct temporal chatter. 8. Render test frames.

## Worked example
A person is isolated from a static background using a tracked mask and local edge refinement.

## Dry run
Mask slips during movement. Inspect keyframes and tracking points, correct drift and review full shot.

## Guided practice
Rotoscope a 5-second moving subject.

## Independent assignment
Apply the workflow to another shot. Submit source plate, editable comp, render, dependency list and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit matte, mask animation and before/after composite. | Compositing issue | Inspect matte, track, color and frame range | Correct and re-render |

## Knowledge check
1. What does an alpha channel represent?
2. Why should a matte be checked across the whole shot?
3. What can cause tracking drift?
4. Why must render passes be recombined according to renderer conventions?
5. What belongs in a VFX shot handoff?

## Answer guidance
1. Transparency.
2. Motion/occlusion can create temporal errors not visible in one frame.
3. Feature loss, blur, parallax, occlusion or bad solve.
4. Passes and color spaces have specific mathematical conventions.
5. Shot ID, frame range/handles, color/alpha, project, plates, mattes and dependencies.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Source/pipeline setup | 4 | Metadata and project |
| Matte/track quality | 5 | Matte/track review |
| Integration and color | 4 | Composite and reference |
| Temporal consistency | 4 | Full playback |
| Rights, archive and handoff | 3 | Manifest |

Pass: 16/20. Unauthorized identity manipulation or missing source integrity requires remediation.

## Quality-control checklist
- [ ] Plates and frame ranges match.
- [ ] Alpha convention is correct.
- [ ] Matte/track remains stable throughout.
- [ ] Color, grain, blur and perspective integrate.
- [ ] AI/synthetic changes are authorized and reviewed.
- [ ] All frames and dependencies are present.
- [ ] Project and shot manifest are archived.

## Further study
- [Foundry Nuke documentation](https://learn.foundry.com/nuke/)
- Selected compositing application's official current documentation.

## Version and change notes
Tool-neutral. Alpha, color management and render-pass conventions vary; verify source renderer and receiving pipeline.
