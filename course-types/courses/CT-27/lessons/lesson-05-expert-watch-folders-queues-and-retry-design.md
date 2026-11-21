# CT-27 Lesson — Watch Folders, Queues and Retry Design

- Course: CT-27 — Batch Editing & Media Automation
- Level: Expert
- Estimated time: 90–180 minutes
- Prerequisites: File management and basic media concepts; command-line familiarity increases with level
- Environment: Record OS, shell, FFmpeg/FFprobe version and available codecs; use test copies
- Version/review: Verify commands against installed tool version before production use

## Learning outcomes
Explain the key concepts, build a reproducible workflow, diagnose common failures and submit evidence for review.

## Definition and terminology
A watch-folder system detects new inputs and schedules jobs. A queue separates job submission from execution; retries must distinguish transient from permanent failures.

## Purpose and professional relevance
Avoid processing partially copied files, duplicate events, infinite retries and concurrent writes. Use idempotent job IDs and atomic completion markers.

## Tools and alternatives
FFmpeg/FFprobe are common options but builds differ. A GUI batch processor or application-native queue may be suitable. Record exact version and codec support. Use scripts with explicit input/output paths, safe quoting and logging. Do not run unreviewed destructive commands against original media.

## Step-by-step procedure
Wait for file stability; validate input; create unique job ID; enqueue; limit concurrency; capture logs; retry only transient failures with backoff; quarantine permanent failures; publish output atomically; alert on terminal state.

## Worked example
A file-copy event fires before upload completes. Wait for stable size/checksum and a successful probe before processing.

## Guided practice
Design a queue state diagram for pending, running, retry, failed and completed jobs.

## Independent assignment
Apply the workflow to a new set of authorized sample files. Include dry-run evidence, commands/configuration, expected and actual outputs, errors, rollback and review notes.

## Common errors and recovery
Duplicate processing; infinite retries; corrupted partial input. Add idempotency, retry caps and quarantine.

## Assessment evidence
Submit workflow diagram, retry policy and failure test plan.

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
