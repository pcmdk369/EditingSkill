# CT-20 Lesson 03 — Keying, Screen Cleanup and Spill Suppression

- Course: CT-20 — Visual Effects & Compositing
- Level: Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-20 lessons and authorized footage/assets
- Tools/environment: Compositing application with node/layer, tracking and render support; record OS/app/version
- Version/review date: Tool-neutral; verify pipeline specifications and software behavior

## Learning outcomes
Key a green/blue screen, clean uneven backgrounds and suppress spill while preserving natural edges and color.

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
Chroma keying uses color separation to create a matte. Lighting uniformity and subject separation improve results. Spill suppression removes screen color reflected onto subject. Over-keying can erase transparent or similarly colored details. Use garbage mattes and holdout mattes where appropriate.

## Tools, requirements and alternatives
Use a current compositing application and media inspector. Record source frame rate, resolution, color space, alpha convention and application version. Preserve original plates and use authorized footage/assets.

## Procedure
1. Inspect screen lighting and source exposure. 2. Create garbage matte. 3. Sample key color. 4. Adjust matte density and softness. 5. Clean holes and edge noise. 6. Suppress spill conservatively. 7. Match foreground/background light and color. 8. Review on light/dark backgrounds and in motion.

## Worked example
A presenter is keyed from a green screen and placed in a studio environment with matching light direction.

## Dry run
Green clothing disappears with background. Use a holdout/alternate matte or different source rather than destroying detail.

## Guided practice
Key a 5-second green-screen clip and composite onto a background.

## Independent assignment
Apply the workflow to another shot. Submit source plate, editable comp, render, dependency list and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit key settings, matte view and final composite. | Compositing issue | Inspect matte, track, color and frame range | Correct and re-render |

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
