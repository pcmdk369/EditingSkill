# CT-27 Lesson — Media Automation Foundations and Safe File Operations

- Course: CT-27 — Batch Editing & Media Automation
- Level: Foundation / Beginner
- Estimated time: 90–180 minutes
- Prerequisites: File management and basic media concepts; command-line familiarity increases with level
- Environment: Record OS, shell, FFmpeg/FFprobe version and available codecs; use test copies
- Version/review: Verify commands against installed tool version before production use

## Learning outcomes
Explain the key concepts, build a reproducible workflow, diagnose common failures and submit evidence for review.

## Definition and terminology
Media automation applies repeatable operations to many files. A safe pipeline starts with inventory, explicit inputs/outputs, predictable naming and reversible operations.

## Purpose and professional relevance
Use a working copy; never point a first-run batch at the only copy of original media. Define allowed extensions, destination, collision behavior and rollback before execution.

## Tools and alternatives
FFmpeg/FFprobe are common options but builds differ. A GUI batch processor or application-native queue may be suitable. Record exact version and codec support. Use scripts with explicit input/output paths, safe quoting and logging. Do not run unreviewed destructive commands against original media.

## Step-by-step procedure
Inventory files; record size/duration/metadata; define naming rules; dry-run planned operations; write to a new output directory; log each result; compare expected and actual counts.

## Worked example
A folder has 120 camera clips. Generate a manifest first, then test the operation on three copies before running the full batch.

## Guided practice
Create a dry-run plan for renaming 20 files and prove no originals are changed.

## Independent assignment
Apply the workflow to a new set of authorized sample files. Include dry-run evidence, commands/configuration, expected and actual outputs, errors, rollback and review notes.

## Common errors and recovery
Wildcard too broad; path spaces; filename collisions; overwriting source. Restrict input patterns, quote paths and fail on collisions.

## Assessment evidence
Submit inventory, dry-run log, naming specification and rollback plan.

## Knowledge check
1. Explain the principal concept in this lesson.
2. What failure mode can occur if the workflow is not idempotent or reversible?
3. How do you validate the output independently of process exit status?
4. What evidence is required for handoff?

## Answer guidance
1. Use the definition and distinguish the concept from adjacent pipeline stages.
2. Duplicate jobs, overwrite, partial files, unbounded retries or loss of source assets.
3. Probe metadata, check stream presence, inspect playback and reconcile manifest.
4. Tool versions, configuration, logs, source/output manifest, test results and rollback.

## Quality-control checklist
- [ ] Inputs authorized and originals preserved.
- [ ] Tool versions and codec support recorded.
- [ ] Dry-run/test sample completed.
- [ ] Output paths and collision behavior safe.
- [ ] Logs and failure states captured.
- [ ] Metadata and full playback validated.
- [ ] Manifest reconciled and rollback documented.

## Further study
Use current FFmpeg/FFprobe documentation and the official documentation for the chosen queue/orchestration platform. Commands and codecs are version/build dependent.
