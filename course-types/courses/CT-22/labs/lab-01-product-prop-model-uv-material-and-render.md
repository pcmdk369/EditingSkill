# CT-22 Professional Lab 01 — Product Prop Model, UV, Material and Render

- Level: Advanced / Professional
- Estimated time: 5–7 hours
- Environment: 3D modeling application; record OS/app/version, renderer and hardware
- Lab status: Authored procedure; not executed in this session

## Brief
Model a simple product prop with clean topology, UVs, materials and a studio render. Deliver native source and an interchange file tested in a target application where available.

## Prerequisites
Complete CT-22 Lessons 01–05. Use original or licensed references/assets. Record intended scale, axis and target format.

## Procedure
1. Set scene units and naming.
2. Gather reference images and define dimensions.
3. Block primary forms with primitives.
4. Refine topology and edge loops.
5. Add bevels/support geometry and inspect shading.
6. Unwrap UVs and inspect checker distortion.
7. Create materials and assign correct texture color spaces.
8. Set camera, lighting and ground plane.
9. Render low-cost tests and correct materials/lighting.
10. Optimize geometry/textures based on measured need.
11. Export native and requested interchange format.
12. Reimport interchange file and inspect scale, normals, UVs and materials.
13. Package textures, rights and manifest.

## Expected artifacts
Native project, mesh/wireframe, UV layout, texture/material maps, studio render, interchange export and QC report.

## Validation
| Test | Method | Expected result |
|---|---|---|
| Scale/axis | Inspect transforms | Matches spec |
| Topology | Wireframe and mesh checks | Clean/manifold as required |
| UV | Checker texture | No severe distortion/bleed |
| Material | Test render | Correct surface response |
| Render | Full-size output | No major noise/artifacts |
| Interchange | Reimport to target app | Geometry/materials usable |
| Handoff | Reopen package | Dependencies linked |

## Troubleshooting
Shading artifacts: inspect normals/topology. UV stretch: add seams and re-unwrap. Wrong color: check texture color space. Missing material on export: package maps and verify target shader support.

## Assessment — 100 points
Model form 15; topology 20; UV quality 15; materials 15; lighting/render 15; optimization/interchange 10; rights/handoff 10. Pass 80/100.

## Handoff
Submit native project, interchange export, textures, UVs, render, dependency manifest and QC report.
