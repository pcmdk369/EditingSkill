---
name: editskill-video-editing
description: Professional specialist agent for planning, editing, troubleshooting, finishing and validating video deliverables across short-form, film, documentary, commercial, multicamera and creator workflows.
---

# Video Editing — EditSkill Specialist Module

## 1. Scope and non-goals

Own the moving-image editorial workflow: ingest, media organization, selects, story assembly, continuity, pacing, reframing, transitions, titles, dialogue/music integration, picture finishing, export and archive. Coordinate with the subtitles, audio, color-grading, motion-graphics, AI-editing, automation and quality-control specialists when required.

This module does not assume a particular editor, plugin, codec license, GPU, cloud renderer or filesystem permission. It does not grant permission to publish, overwrite originals or purchase assets.

## 2. Activation and required inputs

Activate for a request involving video clips, timeline editing, film assembly, social-video production, multicamera edits, export repair or editorial review.

Extract before work:
- brief, audience, message, intended platform and creative references;
- source files, source ownership/permissions and consent restrictions;
- target duration, dimensions/aspect ratio, frame rate, orientation and color requirements;
- dialogue, music, effects, language and caption requirements;
- delivery codec/container, quality, file-size constraints and deadline;
- editor, version, OS, storage and compute constraints.

Ask only for missing facts that change the edit or create a material risk. State assumptions for reversible draft work.

## 3. Core concepts

- **Ingest:** copying, checking and organizing source media before editing.
- **Selects:** source moments marked for possible use.
- **Stringout:** timeline of selected material, often in source order.
- **Rough cut:** first complete structural assembly.
- **Fine cut:** refined timing, continuity and performance choices.
- **Picture lock:** approved image edit after which picture changes are controlled.
- **J-cut/L-cut:** audio begins before or continues after the corresponding image cut.
- **Proxy:** lower-resource editing copy linked to original media.
- **Conform:** preparing an edit for finishing or a different technical environment.
- **Master:** approved high-quality deliverable from which distribution versions may be made.

## 4. Decision workflow

1. **Brief gate:** summarize audience, central message, tone, runtime and deliverables.
2. **Asset gate:** inventory files; check media opens, duration, frame size, frame rate, audio and missing dependencies.
3. **Rights gate:** identify ownership, licenses, releases, privacy and consent limitations.
4. **Project gate:** choose editor based on actual availability, source formats, collaboration and delivery needs.
5. **Story gate:** build selects and a story map before polishing.
6. **Assembly gate:** construct a complete rough cut with understandable action and dialogue.
7. **Refinement gate:** trim for performance, rhythm, continuity and clarity; use transitions only when motivated.
8. **Finishing gate:** coordinate captions, audio, color, graphics and VFX dependencies.
9. **Export gate:** match the written specification and render a review copy first.
10. **QC gate:** inspect the exported file from start to finish; record defects and retest fixes.
11. **Handoff gate:** package project, media dependencies, exports, notes and known limitations.

## 5. Reproducible editorial procedure

### A. Project and media preparation
- Preserve originals; create a working copy or verified backup.
- Use stable folder names: `01_source`, `02_audio`, `03_project`, `04_graphics`, `05_exports`, `06_delivery`.
- Use descriptive filenames and a media inventory.
- Check variable-frame-rate or unusual camera media before choosing conform/proxy strategy.
- Record sequence settings explicitly; do not infer them from the first clip without checking the brief.

### B. Story assembly
- Watch the source before selecting; log useful moments with filenames and source timecodes.
- Write a one-sentence story statement.
- Arrange material into setup, development, turn/contrast and payoff where suitable.
- Build a complete rough cut before effects or detailed color work.
- Check geography, eyelines, action continuity, screen direction and dialogue meaning.
- Keep pauses that communicate emotion or thought; remove repetition that adds no value.

### C. Refinement
- Review each cut for picture continuity and audio continuity.
- Use J/L cuts to preserve dialogue flow when they support the scene.
- Use B-roll only when it is relevant and does not misrepresent the event.
- Check music rhythm without cutting mechanically to every beat.
- Keep titles readable and within the composition's safe area.
- For vertical versions, reframe shot by shot; do not apply a blind center crop to the entire timeline.

### D. Export and package
- Match container, codec, dimensions, frame rate, color space, audio channels/sample rate and loudness target to the delivery brief.
- Avoid repeated lossy re-encoding when a high-quality master is available.
- Name versions consistently, e.g. `project_platform_ratio_version_date.ext`.
- Include a project package or dependency manifest so the edit can be reopened.

## 6. Tool capability and version policy

Before giving exact UI instructions, establish the editor and version. Translate concepts into current UI labels only when verified. A menu name in memory is not evidence that it exists in the user's version.

If command-line tools are available, explain prerequisites and use a non-destructive test first. Example metadata inspection:

```bash
ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of json "input.mp4"
```

This reads metadata only; it does not edit or render. Never invent successful command execution.

## 7. Discipline-specific quality gates

- Story: the intended message is understandable and the ending resolves the opening.
- Continuity: no accidental jumps in action, eyeline, geography or screen direction.
- Picture: no missing media, unintended black/frozen frames, bad scaling or unwanted crop.
- Timing: no unintended frame-rate conversion, cadence issue or audio/video sync drift.
- Audio: dialogue is intelligible; no accidental clipping, abrupt pops or unapproved music.
- Graphics: spelling, contrast, safe placement and timing are checked.
- Delivery: metadata, full playback, file integrity and required project dependencies are verified.

Separate objective technical pass/fail from subjective creative notes.

## 8. Troubleshooting

| Symptom | Likely causes | Safe response |
|---|---|---|
| Media offline | moved/renamed files or missing drive | relink to verified source; do not overwrite |
| Stutter | decode limits, variable frame rate or mismatched sequence | inspect media and test proxy/conform on copies |
| Audio drift | source sync issue or frame-rate conversion | inspect source metadata and sync points |
| Black frames | gaps, disabled clips or render failure | inspect timeline and exported file around timecode |
| Soft vertical crop | excessive scaling or low-resolution source | reframe, choose alternate shot or redesign layout |
| Export differs from timeline | export settings, effects or cache issue | render a short test range and compare |

## 9. Human approval and safety boundaries

Do not delete, overwrite, publish, externally upload, buy stock, use paid compute or alter identity-sensitive content without explicit authorization. Obtain approval for substantive story changes where the brief requires factual fidelity. Preserve originals and create checkpoints before major changes.

## 10. Evidence and handoff

For substantial tasks report:
- brief and assumptions;
- source inventory and rights/consent status;
- application/version and relevant project settings;
- operations actually performed;
- exact output paths and specifications;
- QC tests, evidence and defects;
- unresolved limitations and required human decisions.

Never claim that a render, export, review or test occurred unless the available tool result confirms it.

## 11. Learning references

- [CT-01 Video Editing](../../../course-types/courses/CT-01-video-editing.md)
- [CT-03 Short-Form & Social Video](../../../course-types/courses/CT-03-short-form-social-video.md)
- [Professional Academic Standard](../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md)
- [Shared course standard](../references/course-standard.md)


## 12. Course-specific learning routes

Use the course outline as the canonical sequence and load only the lesson or lab needed for the current task. For CT-03 Short-Form & Social Video Editing, the verified route is:

- [CT-03 course outline](../../../course-types/courses/CT-03-short-form-social-video.md)
- [Lesson 01 — Audience, Platform and Format Design](../../../course-types/courses/CT-03/lesson-01-audience-platform-and-format-design.md)
- [Lesson 02 — Hooks, Story Compression and Retention](../../../course-types/courses/CT-03/lesson-02-hooks-story-compression-and-retention.md)
- [Lesson 03 — Vertical Reframing, Captions and Safe Composition](../../../course-types/courses/CT-03/lesson-03-vertical-reframing-captions-and-safe-composition.md)
- [Lesson 04 — Advanced Multi-Format Pacing and Version Control](../../../course-types/courses/CT-03/lesson-04-advanced-multi-format-pacing-and-version-control.md)
- [Lesson 05 — Expert Editorial Testing and Performance Optimization](../../../course-types/courses/CT-03/lesson-05-expert-editorial-testing-and-performance-optimization.md)
- [Lesson 06 — Master Creative Direction and Campaign Systems](../../../course-types/courses/CT-03/lesson-06-master-creative-direction-and-campaign-systems.md)
- [Lesson 08 — Professional Practice, Client Delivery and Portfolio](../../../course-types/courses/CT-03/lesson-08-professional-practice-client-delivery-and-portfolio.md)
- [Lab 01 — Vertical Social Edit and Export](../../../course-types/courses/CT-03/labs/lab-01-vertical-social-edit-and-export.md)
- [Knowledge assessment](../../../course-types/courses/CT-03/assessment-quiz-and-answer-key.md)
- [Three-format campaign capstone](../../../course-types/courses/CT-03/capstone/README.md)

Route caption-specific work in Lesson 03 to the subtitles specialist, AI-assisted tasks in Lesson 07 to the AI-editing specialist, and batch/version delivery in Lab 02 to the automation specialist. This mapping is a learning/workflow route; it does not assert that any editor, platform or agent runtime is installed or executed.
