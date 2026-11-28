---
name: editskill-audio-editing
description: Specialist agent instructions for audio editing within the universal EditSkill architecture.
---

# Audio Editing — EditSkill Specialist Module

## Scope
Edit dialogue, podcasts, music and sound effects; clean noise; manage levels; mix, master and export audio deliverables.

## Activation and intake

Activate this module for dialogue, podcast, music, sound-effect or multichannel audio editing, cleanup, mixing, mastering preparation or audio-delivery diagnosis. Coordinate with video-editing when synchronization or picture-locked delivery is involved.

Collect the original recordings and channel/stem layout, sample rate, bit depth, duration, sync reference, intended use, delivery format, loudness/peak requirements and monitoring constraints. Identify the source of every music, effect and voice asset and confirm performer/recording permissions. Ask whether noise removal, pitch correction, time compression or other processing may alter meaning or performance. Preserve untreated originals and record the exact audio version used for each approved mix.

## Core principles
Preserve original recordings; use gain staging and non-destructive processing; distinguish loudness from peak level; avoid over-processing and phase problems.

## Task procedure
Inspect channels, sample rate, bit depth, clipping, noise and phase; edit with room tone; process conservatively; balance sources; export to the specified format.

## Quality-control requirements
Listen on headphones and speakers; inspect peaks, clipping, loudness, true peak where available, channel mapping, duration, silence and encoding.

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


## Detailed audio production workflow

### Intake and technical inspection
Confirm intended use, delivery standard, sample rate, bit depth, channel layout, loudness target and whether stems/session files are required. Inspect source duration, channels, clipping, noise, phase, sample rate and sync before editing.

### Editing and processing order
1. Preserve and duplicate originals.
2. Organize tracks and identify approved takes.
3. Edit timing with room tone and clean crossfades.
4. Correct polarity/phase and remove only unwanted noise.
5. Apply corrective EQ and dynamics conservatively.
6. Balance dialogue, music and effects; automate levels.
7. Check mono compatibility and channel routing.
8. Measure integrated loudness, sample peak and true peak using the specified meter/standard.
9. Export a proof, listen completely and inspect metadata.
10. Export final mix and stems with common start/end boundaries.

### Stem integrity
Document whether stems are pre/post bus processing, include sends/automation, and how master-bus nonlinear processing affects recombination. Re-import stems into a clean session and compare against the approved mix.

### QC gates
Check clicks, pops, clipping, distortion, room tone, edits, phase, mono fold-down, sync, loudness, true peak, channel order, silence, duration and encoding. Listen on headphones and a second playback system where available.

### Troubleshooting
- Clicks: inspect edit boundaries and add appropriate crossfade.
- Hollow voice: check phase and mic alignment.
- Pumping: reduce excessive compression or limiter input.
- Harsh sibilance: use targeted de-essing, not blanket dulling.
- Loudness mismatch: verify meter standard and measurement range.
- Stem sum mismatch: inspect routing and master processing.

Never invent a universal loudness target; follow the approved destination specification.
