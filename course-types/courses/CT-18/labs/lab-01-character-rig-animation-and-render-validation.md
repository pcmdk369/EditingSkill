# CT-18 Professional Lab 01 — Character Rig, Animation and Render Validation

- Level: Advanced / Professional
- Estimated time: 5–7 hours
- Environment: 3D application with rigging and rendering; record OS/app/version, renderer and hardware
- Lab status: Authored procedure; not executed in this session

## Brief
Animate a 5-second character action using a provided or original rig. Deliver a playblast and final render with a reproducible scene package.

## Prerequisites
Complete CT-18 Lessons 01–05. Use original or authorized character assets. Record frame rate, units, frame range and output spec.

## Procedure
1. Create scene and record units, frame rate and render settings.
2. Import or build character mesh and rig.
3. Inspect joint hierarchy and object origins.
4. Test deformation at shoulders, elbows and hips.
5. Correct weights/topology as required.
6. Block key poses for a simple action.
7. Refine interpolation, arcs and camera.
8. Add secondary motion or a simple simulation only if appropriate.
9. Create a playblast and review silhouette, timing and deformation.
10. Test representative render frames.
11. Verify textures, caches, frame range and color management.
12. Render final sequence/video and inspect all frames.
13. Package scene, rig, textures, caches and dependency list.

## Expected artifacts
Editable scene, rig, animation, playblast, final render, render settings, dependency manifest and QC report.

## Validation
| Test | Method | Expected result |
|---|---|---|
| Rig | Pose test | No severe deformation |
| Motion | Playblast | Clear timing and performance |
| Camera | Full playback | Staging readable |
| Render | Test frames | Correct light/material/color |
| Sequence | Frame count and playback | No missing frames |
| Dependencies | Reopen package | Textures/caches linked |

## Troubleshooting
Joint collapse: revise weights/topology. Jitter: simplify keys/constraints. Missing textures: relink and package. Render mismatch: compare color transform and renderer settings.

## Assessment — 100 points
Scene setup 10; rig/deformation 20; animation performance 20; camera/staging 10; render quality 15; pipeline/dependencies 10; QC 10; rights/documentation 5. Pass 80/100.

## Handoff
Submit scene, playblast, final render, dependencies, settings, manifest and QC notes.
