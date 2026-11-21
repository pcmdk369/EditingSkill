# CT-27 Lesson — Professional Automation Release Testing and Archive

- Course: CT-27 — Batch Editing & Media Automation
- Level: Professional Practice
- Estimated time: 90–180 minutes
- Prerequisites: File management and basic media concepts; command-line familiarity increases with level
- Environment: Record OS, shell, FFmpeg/FFprobe version and available codecs; use test copies
- Version/review: Verify commands against installed tool version before production use

## Learning outcomes
Explain the key concepts, build a reproducible workflow, diagnose common failures and submit evidence for review.

## Definition and terminology
A production release is a versioned, tested pipeline with reproducible dependencies, documented inputs and a rollback path.

## Purpose and professional relevance
A successful script exit does not prove media quality. Test outputs, job recovery, logs, storage and handoff before production use.

## Tools and alternatives
FFmpeg/FFprobe are common options but builds differ. A GUI batch processor or application-native queue may be suitable. Record exact version and codec support. Use scripts with explicit input/output paths, safe quoting and logging. Do not run unreviewed destructive commands against original media.

## Step-by-step procedure
Pin tool versions; test representative edge cases; verify output metadata and full playback; test failure/retry; compare manifests; package scripts/config safely; document environment; tag release; archive source and logs; define rollback.

## Worked example
A job reports success but produces a silent video. Add audio-stream and playback validation before release.

## Guided practice
Prepare a release checklist and test matrix for a batch transcode service.

## Independent assignment
Apply the workflow to a new set of authorized sample files. Include dry-run evidence, commands/configuration, expected and actual outputs, errors, rollback and review notes.

## Common errors and recovery
Relying on exit code only; no version pin; missing logs. Add media-level validation and reproducible environment.

## Assessment evidence
Submit release package, test evidence, runbook, manifest and rollback instructions.

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
