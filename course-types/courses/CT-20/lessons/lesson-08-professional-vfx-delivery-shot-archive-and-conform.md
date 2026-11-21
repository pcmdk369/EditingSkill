# CT-20 Lesson 08 — Professional VFX Delivery, Shot Archive and Conform

- Course: CT-20 — Visual Effects & Compositing
- Level: Professional Practice
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-20 lessons and authorized footage/assets
- Tools/environment: Compositing application with node/layer, tracking and render support; record OS/app/version
- Version/review date: Tool-neutral; verify pipeline specifications and software behavior

## Learning outcomes
Deliver final comps, mattes, plates, render passes and project dependencies with frame handles, color pipeline and version traceability.

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
VFX handoff requires shot IDs, frame range/handles, resolution, frame rate, color space, alpha convention and version. Conform ensures shots align to editorial timeline. Archive should preserve source plates, renders, mattes, scripts/nodes and dependencies.

## Tools, requirements and alternatives
Use a current compositing application and media inspector. Record source frame rate, resolution, color space, alpha convention and application version. Preserve original plates and use authorized footage/assets.

## Procedure
1. Confirm shot IDs and delivery spec. 2. Verify frame range and handles. 3. Check color/alpha convention. 4. Render final and review all frames. 5. Compare against editorial reference. 6. Package comp project, plates, mattes and passes. 7. Record software/plugins/scripts. 8. Create manifest and version log. 9. Transfer securely and archive.

## Worked example
A VFX shot is delivered as EXR sequence with alpha and a review MP4, plus project and plate references.

## Dry run
Sequence starts one frame late due to handle mismatch. Reconcile editorial frame range and rerender affected frames.

## Guided practice
Prepare a final VFX shot package with plate, matte, comp and render passes.

## Independent assignment
Apply the workflow to another shot. Submit source plate, editable comp, render, dependency list and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit final sequence, project, dependencies, manifest and QC. | Compositing issue | Inspect matte, track, color and frame range | Correct and re-render |

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
