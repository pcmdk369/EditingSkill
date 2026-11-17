---
name: editskill-3d-editing
description: Specialist agent instructions for 3d editing within the universal EditSkill architecture.
---

# 3D Editing — EditSkill Specialist Module

## Scope
Create and modify 3D assets and scenes, including meshes, UVs, materials, lighting, cameras and renders.

## Core principles
Use clean topology and scale; keep transforms and naming organized; manage UVs and texture resolution; consider performance and target engine.

## Task procedure
Inspect scene units, transforms and dependencies; model/edit; unwrap UVs; assign materials; light and frame; test renders before final output.

## Quality-control requirements
Check normals, topology, UVs, missing textures, clipping, render noise, color management, scale and interchange compatibility.

## Required task record
For substantial work, record the brief, assumptions, source assets, rights/consent notes, selected software and version, key settings, steps performed, output paths, validation evidence and unresolved issues.

## Boundaries
- Load `../SKILL.md` for universal execution, safety and reporting rules.
- Consult the matching course in `../../../../course-types/courses/` and existing repository references before inventing a new teaching sequence.
- Do not claim execution or successful export without tool confirmation.
- Preserve originals and request authorization before destructive, paid or externally published actions.
- If required tooling is unavailable, provide reproducible user-executable steps and clearly label them as instructions.

## Handoff
State inputs consumed, operations completed, output specification, QC result, known limitations and the next required human decision.

## PCMDK369™ academic and professional module compliance
This specialist module is governed by the [repository-wide Professional Developer & Academic Course Standard](../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md) and [agent module requirements](../references/course-standard.md). For teaching requests, use the shared academic lesson structure and provide measurable outcomes, prerequisites, definitions, theory, verified tools/alternatives, reproducible steps, worked examples, practice, troubleshooting, assessment evidence and QC. For implementation requests, document the brief, environment/version, inputs and rights, architecture, safe procedure, expected outputs, validation tests, recovery and handoff. Include discipline-specific risks and quality criteria; preserve human approval for consequential or external actions. Report actual evidence and limitations without inventing tool execution or test results.


## Production 3D asset workflow

### Intake
Confirm downstream target (film, game, product render, AR/VR or print), units, axis, polygon/texture budget, renderer, frame range, color pipeline and interchange format.

### Procedure
1. Establish scene units, naming and collection/layer structure.
2. Block silhouette and scale before adding detail.
3. Inspect topology, normals, non-manifold edges and transforms.
4. Build UVs with documented texel density and padding.
5. Create materials with explicit color-space interpretation.
6. Light and render a neutral inspection turntable.
7. Optimize geometry, texture memory and render settings against target.
8. Export native and agreed interchange formats.
9. Import into a clean scene/target application and verify scale, axes, normals, UVs, textures and material differences.
10. Package scene, linked assets, caches, fonts/scripts, render settings and manifest.

### QC
Check topology, shading, UV stretching, texture paths, scale, axis, animation/cache dependencies, render noise, flicker and portability. Never claim an interchange file is validated until it has been reopened downstream.
