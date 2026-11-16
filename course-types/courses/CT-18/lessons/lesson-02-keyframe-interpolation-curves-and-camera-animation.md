# CT-18 Lesson 02 — Keyframe Interpolation, Curves and Camera Animation

- Course: CT-18 — 3D Animation
- Level: Beginner / Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-18 lessons and authorized 3D assets
- Tools/environment: Current 3D application with animation timeline, rigging and render capability; record OS/app/version/hardware
- Version/review date: Tool-neutral; renderer and delivery settings vary

## Learning outcomes
Control interpolation with animation curves, manage ease and arcs, and animate a camera that supports action readability.

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
Interpolation determines how values change between keyframes. Bezier curves allow easing; linear interpolation creates constant rate; stepped interpolation holds values. Camera movement should support composition and not distract. Use graph editor to diagnose overshoot and uneven motion.

## Tools, requirements and alternatives
Use a current 3D application and record version, renderer, scene units, frame rate and hardware. Keep source assets and caches organized. Use authorized character/performer data and respect motion-capture consent.

## Procedure
1. Set start/end keys. 2. Open graph/curve editor. 3. Choose interpolation type. 4. Adjust handles for acceleration/deceleration. 5. Inspect overshoot and tangents. 6. Animate camera position/rotation. 7. Check focal length and framing. 8. Preview at full frame rate.

## Worked example
A camera move eases into a close-up, pauses for action and eases out without overshoot.

## Dry run
Camera accelerates unexpectedly due to curve handles. Inspect tangents and simplify curve.

## Guided practice
Animate a camera move around a rotating object.

## Independent assignment
Apply the technique to a second object or shot. Submit editable scene, playblast/render, settings and validation notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit curve screenshots and preview. | 3D workflow issue | Inspect scene, rig, cache and render settings | Correct and test a short range |

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
