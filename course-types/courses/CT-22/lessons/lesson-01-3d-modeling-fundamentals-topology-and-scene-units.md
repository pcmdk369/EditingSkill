# CT-22 Lesson 01 — 3D Modeling Fundamentals, Topology and Scene Units

- Course: CT-22 — 3D Modeling, Materials & Rendering
- Level: Foundation / Beginner
- Estimated time: 120–180 minutes
- Prerequisites: Basic 3D navigation and file management
- Tools/environment: Current 3D modeling application with mesh, UV, materials and render support; record OS/app/version/hardware
- Version/review date: Tool-neutral; interchange and renderer behavior varies

## Learning outcomes
Understand mesh components, object scale, topology and organized scene setup for a defined modeling/output task.

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
3D models are built from vertices, edges and faces. Topology describes their arrangement and affects deformation, subdivision and shading. Scene units and scale influence lighting, simulation and export. A clean project uses meaningful names, collections and source references.

## Tools, requirements and alternatives
Use a current 3D application with modeling, UV, material and render capability. Record units, axis convention, renderer and app/version. Use original or licensed assets and preserve source projects.

## Procedure
1. Define object purpose and output. 2. Set scene units and scale. 3. Create reference images. 4. Block primary forms. 5. Inspect vertices/edges/faces. 6. Use quads where useful for deformation/subdivision. 7. Name objects and collections. 8. Save versioned project.

## Worked example
A simple product model begins with primitive forms and is refined into clean topology at the required scale.

## Dry run
Non-manifold geometry causes export issues. Run mesh inspection and repair boundaries/overlaps.

## Guided practice
Model a simple product or prop with clean topology and documented scale.

## Independent assignment
Apply the technique to a second asset. Submit native file, interchange export, textures, test render and QC notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit native file, wireframe views and scale notes. | 3D asset issue | Inspect mesh, UV, material and target app | Correct and re-export |

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
