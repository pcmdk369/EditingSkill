# CT-22 Lesson 08 — Professional 3D Asset Delivery, Render and Archive

- Course: CT-22 — 3D Modeling, Materials & Rendering
- Level: Professional Practice
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-22 lessons and authorized 3D assets
- Tools/environment: Current 3D modeling application with mesh, UV, materials and render support; record OS/app/version/hardware
- Version/review date: Tool-neutral; interchange and renderer behavior varies

## Learning outcomes
Deliver native and interchange assets with geometry, UVs, textures, materials, renderer settings, rights and reproducible dependencies.

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
Professional 3D delivery must identify unit scale, axis convention, object naming, polygon/LOD expectations, texture formats, color spaces and target application. Native project and interchange files may differ. Include test renders and dependency manifests.

## Tools, requirements and alternatives
Use a current 3D application with modeling, UV, material and render capability. Record units, axis convention, renderer and app/version. Use original or licensed assets and preserve source projects.

## Procedure
1. Confirm target app and interchange specification. 2. Validate geometry/normals/scale. 3. Check UVs and texture links. 4. Verify materials in target renderer where possible. 5. Export native and interchange versions. 6. Reimport/test in target environment. 7. Package textures and licenses. 8. Create manifest and version history. 9. Archive source and final outputs.

## Worked example
A prop is delivered as native project plus FBX/glTF where requested, with textures, unit scale and test renders.

## Dry run
FBX import loses material assignment. Reimport into target app, inspect mapping and provide texture manifest/fallback.

## Guided practice
Prepare a complete 3D asset handoff for one product prop.

## Independent assignment
Apply the technique to a second asset. Submit native file, interchange export, textures, test render and QC notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit native file, interchange export, textures, renders, manifest and QC. | 3D asset issue | Inspect mesh, UV, material and target app | Correct and re-export |

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
