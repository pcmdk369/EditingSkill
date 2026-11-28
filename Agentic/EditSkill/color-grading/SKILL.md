---
name: editskill-color-grading
description: Specialist agent instructions for color grading within the universal EditSkill architecture.
---

# Color Grading — EditSkill Specialist Module

## Scope
Manage color spaces and transform footage through technical correction, shot matching and creative grading.

## Activation and intake

Activate this module for technical color normalization, shot matching, look development, color-space conversion, HDR/SDR preparation or color-related export diagnosis. Coordinate with video-editing for editorial changes and quality-control for independent output verification.

Before proposing a transform, identify camera/source format, log or scene-referred encoding, gamut/primaries, transfer function, input/output color-management settings, timeline working space, display target and delivery specification. Ask whether a reference still or approved look exists and whether the viewing display/environment is calibrated or merely approximate. Inventory LUTs and transforms, including their source and license. Do not guess the camera input space, stack transforms without tracing the signal path or promise color-critical accuracy from an unverified display. Record monitoring limitations and all version-dependent color-management settings.

## Core principles
Know the source color space and display transform; distinguish correction from creative look; avoid clipping and inconsistent skin tones; monitor scopes.

## Task procedure
Identify camera/log/gamut; set color management; normalize; balance exposure and white balance; match shots; apply look; review on target display.

## Quality-control requirements
Check legal range where required, gamut, clipping, banding, skin consistency, shot continuity, metadata and export transform.

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


## Color pipeline implementation

### Source-to-output chain
Record source camera/log/gamut, input transform, working space, timeline settings, monitoring/display transform, creative look and output transform. Keep technical normalization separate from creative look development.

### Procedure
1. Inventory sources and group by camera/profile.
2. Confirm timeline frame rate and color-management mode.
3. Set one intentional input-transform strategy; avoid double transforms.
4. Balance exposure and white balance using scopes and reference frames.
5. Match shots before applying creative look.
6. Use secondary keys/masks only where justified and inspect edges.
7. Check skin/object hues, highlight roll-off, shadow detail and saturation.
8. Create separate output transforms for each requested delivery target.
9. Render short proofs and inspect metadata and playback.
10. Record LUT versions, color configuration and limitations.

### Scope interpretation
Use waveform for signal level, RGB parade for channel balance and vectorscope for hue/saturation. Verify scale, legal/full range and transfer assumptions before applying numeric thresholds.

### QC and troubleshooting
Check clipping, gamut excursions, banding, noise, shot jumps, skin consistency, LUT double-application, range tags, output transform and metadata. If devices disagree, verify profiles and display state before changing the grade.

Do not claim calibrated color accuracy unless the monitoring chain has been measured and documented. HDR and SDR are separate targets requiring explicit transforms and review.
