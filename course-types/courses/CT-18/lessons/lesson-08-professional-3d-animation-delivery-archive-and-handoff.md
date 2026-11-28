# CT-18 Lesson 08 — Professional 3D Animation Delivery, Archive and Handoff

- Course: CT-18 — 3D Animation
- Level: Professional Practice
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-18 lessons and authorized 3D assets
- Tools/environment: Current 3D application with animation timeline, rigging and render capability; record OS/app/version/hardware
- Version/review date: Tool-neutral; renderer and delivery settings vary

## Learning outcomes
Deliver rendered sequences, project files, caches and dependencies with frame range, color, camera and version documentation.

## Key definitions
- **Transform:** Object location, rotation and scale.
- **Keyframe:** Stored parameter value at a specific time.
- **Interpolation:** Method for calculating values between keys.
- **Rig:** Controls and hierarchy used to animate a character/object.
- **Skinning:** Binding mesh deformation to joints through weights.
- **Constraint:** Rule relating one object's transform/motion to another.
- **Cache:** Stored simulation or computed data.
- **Playblast:** Fast preview render for animation review.

## Purpose and theory
Professional 3D handoff requires exact frame range, frame rate, resolution, color transform, alpha settings and renderer/version. Include textures, caches, rigs, fonts and plugins where permitted. A sequence should be checked for missing frames and correct naming.

## Tools, requirements and alternatives
Use a current 3D application and record version, renderer, scene units, frame rate and hardware. Keep source assets and caches organized. Use authorized character/performer data and respect motion-capture consent.

## Procedure
1. Confirm delivery spec and frame range. 2. Lock approved animation and camera. 3. Check rigs, textures, caches and plugins. 4. Render test frames and review. 5. Render final image sequence/video. 6. Check frame count and numbering. 7. Inspect alpha/color and playback. 8. Package scene and dependencies. 9. Create manifest and change log. 10. Transfer and archive.

## Worked example
A shot is delivered as numbered EXR frames and a review MP4, with scene, textures, caches and render settings.

## Dry run
One frame is missing in image sequence. Compare expected range to actual filenames and render only missing frames, then verify sequence.

## Guided practice
Prepare a delivery package for a 5-second 3D shot.

## Independent assignment
Apply the technique to a second object or shot. Submit editable scene, playblast/render, settings and validation notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit final render, scene package, dependencies, manifest and QC. | 3D workflow issue | Inspect scene, rig, cache and render settings | Correct and test a short range |

## Knowledge check
1. What are location, rotation and scale?
2. How does interpolation affect motion?
3. What can cause skin deformation problems?
4. Why test simulation on a short range?
5. What must be checked in a final image sequence?

## Answer guidance
1. Core object transform properties.
2. It controls acceleration, deceleration and motion behavior between keys.
3. Joint placement, topology and skin weights.
4. To identify scale/collision/cache issues before expensive full simulation.
5. Frame count, numbering, frame rate, color/alpha and missing frames.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Scene setup and organization | 4 | Project settings |
| Motion and keyframes | 4 | Timeline/curve evidence |
| Rig/deformation/simulation | 4 | Test playblast |
| Render and technical quality | 4 | Test frames/metadata |
| Rights, dependencies and handoff | 4 | Manifest and consent |

Pass: 16/20. Unauthorized motion-capture use or incomplete final sequence requires remediation.

## Quality-control checklist
- [ ] Scene units/frame rate/output range recorded.
- [ ] Transforms/origins and animation curves checked.
- [ ] Rig deformation and motion continuity reviewed.
- [ ] Simulations/caches reproducible.
- [ ] Textures and external dependencies available.
- [ ] Render frame range and color/alpha verified.
- [ ] Source, project and handoff archived.

## Further study
- [Blender Manual — Animation & Rigging](https://docs.blender.org/manual/en/latest/animation/index.html)
- Selected 3D application's official rigging/render documentation.

## Version and change notes
Tool-neutral. Renderer, rigging and export behavior varies by software/version; verify exact procedures.
