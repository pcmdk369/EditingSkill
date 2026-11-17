---
name: editskill-vfx
description: Specialist agent instructions for visual effects within the universal EditSkill architecture.
---

# Visual Effects — EditSkill Specialist Module

## Scope
Integrate effects into live-action or animated footage through tracking, keying, roto, compositing, simulation and finishing.

## Activation and intake

Activate this module for tracking, keying, rotoscoping, cleanup, compositing, simulation integration or visual-effects finishing. Coordinate with video-editing for editorial handles and with color-grading for the plate-to-composite color pipeline.

Collect the approved plate, frame range, frame rate, source raster, camera/lens metadata where available, color-space interpretation, handles, reference frames, required elements/passes, alpha convention, target resolution and delivery format. Identify whether the shot is locked and who approves changes to the plate. Record the source and license of stock elements, generated assets, textures and simulations. If camera metadata, plate references or alpha requirements are missing, mark them as unresolved rather than inventing a match.

## Core principles
Match perspective, lens, lighting, grain, motion blur and color; use plate preparation and clean handoffs; keep elements separated.

## Task procedure
Inspect plate and metadata; plan layers/passes; track or key; refine mattes; composite in linear/color-managed space where appropriate; compare against plate.

## Quality-control requirements
Check edge chatter, spill, track drift, matte holes, grain mismatch, color mismatch, temporal artifacts and render boundaries.

## Required task record
For substantial work, record the brief, assumptions, source assets, rights/consent notes, selected software and version, key settings, steps performed, output paths, validation evidence and unresolved issues.

## Boundaries
- Load `../SKILL.md` for universal execution, safety and reporting rules.
- Consult the matching course in `../../../course-types/courses/` and existing repository references before inventing a new teaching sequence.
- Do not claim execution or successful export without tool confirmation.
- Preserve originals and request authorization before destructive, paid or externally published actions.
- If required tooling is unavailable, provide reproducible user-executable steps and clearly label them as instructions.

## Handoff
State inputs consumed, operations completed, output specification, QC result, known limitations and the next required human decision.

## PCMDK369™ academic and professional module compliance
This specialist module is governed by the [repository-wide Professional Developer & Academic Course Standard](../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md) and [agent module requirements](../references/course-standard.md). For teaching requests, use the shared academic lesson structure and provide measurable outcomes, prerequisites, definitions, theory, verified tools/alternatives, reproducible steps, worked examples, practice, troubleshooting, assessment evidence and QC. For implementation requests, document the brief, environment/version, inputs and rights, architecture, safe procedure, expected outputs, validation tests, recovery and handoff. Include discipline-specific risks and quality criteria; preserve human approval for consequential or external actions. Report actual evidence and limitations without inventing tool execution or test results.


## VFX shot workflow and technical controls

### Intake
Record plate frame rate, resolution, lens/camera data, color space, alpha convention, render passes, handles, shot range and target comp/export requirements.

### Procedure
1. Inspect plate and source passes; confirm frame range and metadata.
2. Establish color-managed linear compositing where required.
3. Build roto/key/tracking elements with versioned mattes.
4. Verify premultiplication and edge color.
5. Integrate lighting, shadow, reflection, depth of field, motion blur and grain.
6. Review temporal stability across the full shot.
7. Render a proof and compare with reference.
8. Export with agreed codec, bit depth, color and alpha.
9. Reopen in receiving application and validate.
10. Package comp script, LUTs, caches, plates, passes and manifest.

### QC
Inspect matte chatter, edge fringing, tracking drift, flicker, color mismatch, missing frames, alpha inversion, render noise and dependency portability. Do not call a shot final until the receiving pipeline has checked it.
