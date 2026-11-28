# CT-22 Lesson 05 — Procedural Modeling, Asset Reuse and Optimization

- Course: CT-22 — 3D Modeling, Materials & Rendering
- Level: Expert
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-22 lessons and authorized 3D assets
- Tools/environment: Current 3D modeling application with mesh, UV, materials and render support; record OS/app/version/hardware
- Version/review date: Tool-neutral; interchange and renderer behavior varies

## Learning outcomes
Build reusable procedural assets, manage modifiers/instances and optimize scenes for rendering and interchange.

## Key definitions
- **Vertex/edge/face:** Basic polygon mesh components.
- **Topology:** Arrangement of mesh components.
- **Edge loop:** Connected path of edges.
- **Bevel:** Rounded/chamfered edge treatment.
- **UV map:** 2D coordinates mapping textures to 3D surfaces.
- **Texel density:** Texture pixel density across a model surface.
- **Material:** Surface response definition for a renderer.
- **Procedural modeling:** Geometry generation through parameters/rules.
- **LOD:** Level of detail representation.

## Purpose and theory
Procedural modeling uses parameters, nodes or modifiers to generate geometry. Reusable assets improve consistency but require clear controls and fallback meshes. Optimization should focus on measured bottlenecks: polygon count, texture memory, shader complexity and render settings.

## Tools, requirements and alternatives
Use a current 3D application with modeling, UV, material and render capability. Record units, axis convention, renderer and app/version. Use original or licensed assets and preserve source projects.

## Procedure
1. Identify repeatable asset parameters. 2. Build modifier/node-based generator. 3. Expose safe controls. 4. Create reusable asset library. 5. Apply naming/version rules. 6. Measure scene/render performance. 7. Optimize geometry/textures/materials. 8. Export and validate interchange format.

## Worked example
A railing generator exposes length, spacing and height while preserving a manual override.

## Dry run
Procedural modifier breaks on export. Apply/bake a copy and verify target format; keep procedural master.

## Guided practice
Build a procedural repeated asset and optimized export copy.

## Independent assignment
Apply the technique to a second asset. Submit native file, interchange export, textures, test render and QC notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit generator, parameters, performance notes and export test. | 3D asset issue | Inspect mesh, UV, material and target app | Correct and re-export |

## Knowledge check
1. Why does topology matter?
2. What do UV seams control?
3. Why must color and data textures be interpreted differently?
4. What should be measured before optimizing a scene?
5. What belongs in an interchange asset package?

## Answer guidance
1. It affects shading, deformation and subdivision.
2. They define where the 3D surface is cut/unwrapped into 2D space.
3. Color textures represent appearance; data maps encode values and should not be color transformed.
4. Polygon/texture memory, shader and render bottlenecks.
5. Geometry, scale/axis, UVs, textures, materials, rights and test renders.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Scene/model setup | 4 | Native file and scale |
| Topology/UV quality | 5 | Wireframe and UV map |
| Materials/lighting | 4 | Material graph and render |
| Optimization/export | 4 | Performance and interchange test |
| Rights/handoff | 3 | Asset manifest |

Pass: 16/20. Unauthorized asset use or broken interchange output requires remediation.

## Quality-control checklist
- [ ] Scene units and axis conventions documented.
- [ ] Mesh topology and normals checked.
- [ ] UVs and texture padding validated.
- [ ] Materials use correct color-space interpretation.
- [ ] Lighting/render tests inspected.
- [ ] Interchange export reimported/tested.
- [ ] Dependencies and licenses archived.

## Further study
- [Blender Manual — Modeling](https://docs.blender.org/manual/en/latest/modeling/index.html)
- [Khronos glTF specification](https://registry.khronos.org/glTF/)
- Selected 3D application's official documentation.

## Version and change notes
Tool-neutral. Interchange support, units and renderer settings vary; verify target application and version.
