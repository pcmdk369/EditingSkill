# CT-20 Lesson 06 — VFX Supervision, Shot Breakdown and Review

- Course: CT-20 — Visual Effects & Compositing
- Level: Master
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-20 lessons and authorized footage/assets
- Tools/environment: Compositing application with node/layer, tracking and render support; record OS/app/version
- Version/review date: Tool-neutral; verify pipeline specifications and software behavior

## Learning outcomes
Plan a multi-shot VFX sequence, define shot dependencies and govern review, versioning and final approvals.

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
Master VFX supervision connects editorial, plate photography, tracking, CG, compositing and finishing. Shot breakdowns identify requirements, risks and dependencies. Review notes should identify frame/timecode, expected behavior and severity. A shot should not be approved based only on a still frame.

## Tools, requirements and alternatives
Use a current compositing application and media inspector. Record source frame rate, resolution, color space, alpha convention and application version. Preserve original plates and use authorized footage/assets.

## Procedure
1. Break script/edit into VFX shots. 2. Record plates, handles, lens and camera data. 3. Identify roto/track/key/CG dependencies. 4. Estimate complexity and risk. 5. Define color/format pipeline. 6. Review temp comps and iterate. 7. Maintain shot status and versions. 8. Lock approved shots and archive evidence.

## Worked example
A five-shot sequence has a breakdown with plate, tracking, roto, CG and final comp tasks assigned.

## Dry run
A late editorial change invalidates tracking. Reopen affected shot, update handles and revalidate downstream comps.

## Guided practice
Create a shot breakdown and supervise one representative composite.

## Independent assignment
Apply the workflow to another shot. Submit source plate, editable comp, render, dependency list and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit breakdown, review log, version manifest and approved comp. | Compositing issue | Inspect matte, track, color and frame range | Correct and re-render |

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
