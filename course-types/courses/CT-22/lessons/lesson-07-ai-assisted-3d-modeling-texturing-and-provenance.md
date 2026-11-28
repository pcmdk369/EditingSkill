# CT-22 Lesson 07 — AI-Assisted 3D Modeling, Texturing and Provenance

- Course: CT-22 — 3D Modeling, Materials & Rendering
- Level: AI & Automation
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-22 lessons and authorized 3D assets
- Tools/environment: Current 3D modeling application with mesh, UV, materials and render support; record OS/app/version/hardware
- Version/review date: Tool-neutral; interchange and renderer behavior varies

## Learning outcomes
Evaluate AI mesh generation, retopology and texture assistance while checking geometry, rights, provenance and production readiness.

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
AI-generated 3D assets may contain non-manifold geometry, inconsistent scale, poor UVs, texture artifacts or unclear rights. Treat them as drafts and inspect mesh topology, materials and licenses before production. Do not upload confidential designs without authorization.

## Tools, requirements and alternatives
Use a current 3D application with modeling, UV, material and render capability. Record units, axis convention, renderer and app/version. Use original or licensed assets and preserve source projects.

## Procedure
1. Define bounded AI task. 2. Check provider terms and commercial rights. 3. Preserve source reference. 4. Generate draft mesh/texture. 5. Inspect scale, topology, normals and UVs. 6. Retopologize and repair manually. 7. Validate material/texture color space. 8. Log tool/model/version and corrections. 9. Obtain approval.

## Worked example
AI creates a rough prop mesh; artist retopologizes, unwraps and builds production materials.

## Dry run
AI mesh has intersecting faces and no clean UV. Reject as final; repair or rebuild before use.

## Guided practice
Compare manual blockout with AI-generated draft for a non-confidential prop.

## Independent assignment
Apply the technique to a second asset. Submit native file, interchange export, textures, test render and QC notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit source, AI draft, cleaned asset, provenance and rights notes. | 3D asset issue | Inspect mesh, UV, material and target app | Correct and re-export |

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
