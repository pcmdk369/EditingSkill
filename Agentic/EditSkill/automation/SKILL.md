---
name: editskill-automation
description: Specialist agent instructions for editing automation within the universal EditSkill architecture.
---

# Editing Automation — EditSkill Specialist Module

## Scope
Build repeatable media pipelines for batch conversion, proxy creation, transcoding, metadata, naming, rendering and delivery.

## Activation and intake

Activate this module for repeatable batch processing, transcoding, proxy creation, metadata extraction, watch-folder workflows, scripted edits, queue orchestration or automated delivery. Coordinate with software-tools for environment compatibility and quality-control for independent output testing.

Define the input set and file-selection rules, expected counts, output structure, naming convention, target formats, application/command versions, resource limits, logging needs and retry policy. Identify which operations are read-only, reversible or destructive; specify whether overwrite is prohibited and who can authorize it. Require a dry run or small sample before a full batch, an idempotency strategy where possible, failure isolation and a recovery plan. Never assume a script, binary, codec or filesystem permission exists until verified.

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
- Consult the matching course in `../../../course-types/courses/` and existing repository references before inventing a new teaching sequence.
- Do not claim execution or successful export without tool confirmation.
- Preserve originals and request authorization before destructive, paid or externally published actions.
- If required tooling is unavailable, provide reproducible user-executable steps and clearly label them as instructions.

## Handoff
State inputs consumed, operations completed, output specification, QC result, known limitations and the next required human decision.

## PCMDK369™ academic and professional module compliance
This specialist module is governed by the [repository-wide Professional Developer & Academic Course Standard](../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md) and [agent module requirements](../references/course-standard.md). For teaching requests, use the shared academic lesson structure and provide measurable outcomes, prerequisites, definitions, theory, verified tools/alternatives, reproducible steps, worked examples, practice, troubleshooting, assessment evidence and QC. For implementation requests, document the brief, environment/version, inputs and rights, architecture, safe procedure, expected outputs, validation tests, recovery and handoff. Include discipline-specific risks and quality criteria; preserve human approval for consequential or external actions. Report actual evidence and limitations without inventing tool execution or test results.


## Operational architecture and decision gates

### Intake contract
Require source root, output root, file-selection rule, target specification, naming rule, overwrite policy, maximum concurrency, retention policy and failure owner. Refuse ambiguous destructive operations. A dry-run must enumerate the exact planned input/output pairs and collisions.

### Pipeline state model
Use explicit states: DISCOVERED → VALIDATED → QUEUED → RUNNING → OUTPUT_WRITTEN → QC_PASSED → RELEASED. Terminal states include REJECTED and FAILED. Do not mark a job complete merely because a process returned exit code zero.

### Safe implementation pattern
1. Discover files without following unintended symlinks.
2. Validate file stability, type, readability and size.
3. Assign an idempotency key based on stable source identity and requested operation.
4. Write to a unique temporary output path.
5. Validate streams, duration, metadata and playback.
6. Atomically move a passed result to the release path.
7. Write a structured log and manifest row.
8. Quarantine permanent failures and cap transient retries.

### Example metadata probe
```bash
ffprobe -v error -show_entries format=filename,duration,size:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of json "input.mp4"
```
This is a read-only example; confirm FFprobe availability and options locally.

### Operational controls
- Use least-privilege file access and keep credentials out of scripts/logs.
- Bound CPU/GPU, memory, storage and queue concurrency.
- Make cancellation and restart behavior explicit.
- Record tool versions, commands, configuration hashes and timestamps.
- Keep source, temporary, failed and released outputs in separate locations.

### Failure and recovery
| Failure | Safe response |
|---|---|
| Partial input copy | Wait for stability/checksum; do not process |
| Output collision | Stop and request a version/path decision |
| Encoder unavailable | Report installed build and select an approved alternative |
| Corrupt output | Quarantine; retain logs; rerun from original |
| Repeated transient failure | Exponential backoff with retry cap |
| QC mismatch | Block release and open a defect record |

### Acceptance tests
Test empty folders, spaces/unicode in names, duplicate basenames, corrupt media, missing audio, zero-byte files, variable frame rate, cancellation, retry, interrupted writes and rerun idempotency. Report actual test evidence only.


## 13. Course-specific learning route

For responsible social-video automation and repeatable multi-format delivery, use [CT-03 Lesson 07 — AI-Assisted Social Editing and Automation](../../../course-types/courses/CT-03/lesson-07-ai-assisted-social-editing-and-automation.md) and [Lab 02 — Multi-Format Versioning and Batch Delivery](../../../course-types/courses/CT-03/labs/lab-02-multi-format-versioning-and-batch-delivery.md). The canonical sequence and assessment are listed in the [CT-03 course outline](../../../course-types/courses/CT-03-short-form-social-video.md). Treat all automation examples as procedures until the exact environment is confirmed and the run is independently evidenced.
