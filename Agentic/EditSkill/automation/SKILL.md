---
name: editskill-automation
description: Specialist agent instructions for editing automation within the universal EditSkill architecture.
---

# Editing Automation — EditSkill Specialist Module

## Scope
Build repeatable media pipelines for batch conversion, proxy creation, transcoding, metadata, naming, rendering and delivery.

## Core principles
Use idempotent steps where possible; validate inputs; log operations; isolate failures; avoid destructive overwrites; provide dry-run modes for batch jobs.

## Task procedure
Specify inputs/outputs; define naming and folder rules; test on sample files; implement error handling and retries; log versions/settings; run controlled batches.

## Quality-control requirements
Verify counts, checksums where appropriate, output metadata, failed-item reports, duplicate handling, resource limits and safe reruns.

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