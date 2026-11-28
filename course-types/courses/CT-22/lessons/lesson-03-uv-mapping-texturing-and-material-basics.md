# CT-22 Lesson 03 — UV Mapping, Texturing and Material Basics

- Course: CT-22 — 3D Modeling, Materials & Rendering
- Level: Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-22 lessons and authorized 3D assets
- Tools/environment: Current 3D modeling application with mesh, UV, materials and render support; record OS/app/version/hardware
- Version/review date: Tool-neutral; interchange and renderer behavior varies

## Learning outcomes
Create UV layouts, assign materials and texture maps with appropriate scale, resolution and color interpretation.

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
UV mapping places a 2D texture coordinate layout over a 3D surface. Seams, distortion and texel density affect texture quality. Material parameters such as base color, roughness and metallic response vary by renderer. Color textures and data maps may require different color-space interpretation.

## Tools, requirements and alternatives
Use a current 3D application with modeling, UV, material and render capability. Record units, axis convention, renderer and app/version. Use original or licensed assets and preserve source projects.

## Procedure
1. Identify material regions. 2. Mark seams strategically. 3. Unwrap mesh. 4. Inspect distortion and texel density. 5. Pack UV islands with padding. 6. Create or assign textures. 7. Set material parameters. 8. Check texture color-space settings and render.

## Worked example
A product prop has separate UV islands for body and label, with consistent texel density.

## Dry run
Texture stretches around corners. Add seams and re-unwrap; inspect checker pattern.

## Guided practice
UV unwrap and texture a prop with two materials.

## Independent assignment
Apply the technique to a second asset. Submit native file, interchange export, textures, test render and QC notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit UV layout, texture maps, material graph and render. | 3D asset issue | Inspect mesh, UV, material and target app | Correct and re-export |

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
