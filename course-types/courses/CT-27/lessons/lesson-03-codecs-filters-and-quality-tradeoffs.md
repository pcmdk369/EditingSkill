# CT-27 Lesson — Codecs, Filters and Quality Trade-offs

- Course: CT-27 — Batch Editing & Media Automation
- Level: Intermediate
- Estimated time: 90–180 minutes
- Prerequisites: File management and basic media concepts; command-line familiarity increases with level
- Environment: Record OS, shell, FFmpeg/FFprobe version and available codecs; use test copies
- Version/review: Verify commands against installed tool version before production use

## Learning outcomes
Explain the key concepts, build a reproducible workflow, diagnose common failures and submit evidence for review.

## Definition and terminology
A codec encodes/decodes media; a container packages streams; filters transform audio/video. Quality, compatibility, size and processing time trade off.

## Purpose and professional relevance
Choose settings from actual destination requirements; avoid repeated lossy encoding; understand scaling, frame-rate conversion, audio resampling and color conversion.

## Tools and alternatives
FFmpeg/FFprobe are common options but builds differ. A GUI batch processor or application-native queue may be suitable. Record exact version and codec support. Use scripts with explicit input/output paths, safe quoting and logging. Do not run unreviewed destructive commands against original media.

## Step-by-step procedure
Define target; inspect source; select codec/preset/pixel format; apply only necessary filters; render a short sample; compare quality and file size; validate timestamps/audio; record settings.

## Worked example
A 4K source needs a 1080p review file. Scale once from original and preserve a high-quality master for future derivatives.

## Guided practice
Compare two encodes at matched duration and inspect motion, gradients, text and audio.

## Independent assignment
Apply the workflow to a new set of authorized sample files. Include dry-run evidence, commands/configuration, expected and actual outputs, errors, rollback and review notes.

## Common errors and recovery
Chasing tiny file size; unintended frame interpolation; wrong pixel format. Recheck target compatibility and use source master.

## Assessment evidence
Submit test matrix and recommended preset with evidence.

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
