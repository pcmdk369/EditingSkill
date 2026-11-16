# CT-01 — Advanced: Multicamera Editing and Complex Sequence Management

**Course:** Video Editing  
**Pathway stage:** Advanced

## Learning outcomes
Synchronize multiple cameras and external audio; build a multicamera edit; manage nested sequences; use track labels and version checkpoints; troubleshoot drift and sync errors.

## Prerequisites
Lessons 01–09 and at least two recordings of the same event.

## Key definitions
- Multicamera edit: selecting between synchronized camera angles during playback or in a dedicated multicamera sequence.
- Sync point: shared event used to align recordings.
- Timecode: time reference used to identify frames.
- Jam sync: process of aligning device timecode generators.
- Waveform sync: alignment using matching audio waveforms.
- Nested sequence: sequence placed inside another sequence as a single editable unit.
- Precompose/compound clip: application-specific grouping of layers or clips into a reusable unit.
- Drift: gradual loss of synchronization over time.
- Offline media: project reference whose source file is unavailable.

## Why it matters
Complex projects multiply the risk of sync errors, broken links and accidental changes. A reliable multicamera workflow preserves source relationships and makes revisions manageable.

## Theory
Sync can use matching timecode, a visible/audio sync event, waveform matching or manual alignment. Timecode is only reliable when devices were configured consistently. Long recordings from devices with different clocks may drift even when the beginning aligns. Check sync at both beginning and end.

Multicamera tools differ by application. If no multicamera mode exists, stack synchronized angles on tracks and cut visibility manually. Nested sequences help manage complexity but can hide underlying edits; keep clear naming and avoid unnecessary nesting.

## Tools and alternatives
NLE multicamera function, waveform display, timecode metadata, external recorder, clap/slate or visual sync flash. A spreadsheet sync log is useful for larger shoots.

## Procedure
1. Back up all camera and audio originals.
2. Inventory cameras, recording start times, frame rates, audio sources and timecode availability.
3. Identify a shared sync event or reliable timecode reference.
4. Align each camera and external audio at the sync point.
5. Check sync near the beginning, middle and end.
6. If drift appears, determine whether it is constant offset or progressive drift.
7. Correct constant offset by shifting the track; correct drift only with a validated time-stretch, conform or segmented-sync workflow.
8. Create a multicamera group/sequence if supported; otherwise stack aligned angles.
9. Label angles by camera, position and lens/shot type.
10. Perform a first pass selecting angles based on content and performance, not random switching.
11. Refine cut points and audio source; preserve a clean master audio track where appropriate.
12. Nest only when it improves organization; document nested sequence dependencies.
13. Save checkpoints and test project reopening with all media online.

## Worked example
Two cameras record a 20-minute interview, with a separate recorder capturing audio. Align the opening clap across all sources. Check the clap or a clear mouth/consonant event near the end. If the audio gradually drifts, do not simply shift it by a fixed amount; diagnose clock/frame-rate mismatch and apply a controlled correction.

## Dry run
Align two 5-minute clips using a clap at the start. Compare sync at the final minute. Record whether the error is constant or grows over time. This distinguishes offset from drift.

## Guided exercise
Create a two-angle 60-second multicamera sequence. Use external audio as the primary dialogue source and check sync at start, middle and end.

## Independent assignment
Edit a 2–3 minute multicamera interview or performance. Submit angle map, sync report, project structure, final edit and notes explaining five angle choices.

## Common errors and recovery
- Wrong sync event: locate a clearer shared event and realign.
- Drift mistaken for offset: compare multiple points across duration.
- Frame-rate mismatch: inspect actual source properties and conform carefully.
- Angle labels unclear: rename tracks/groups with camera and shot details.
- Nested sequence hides source edits: open the nested sequence and document the hierarchy.
- Project opens with offline files: relink using the stable source folder and retest.

## Knowledge check
1. What is the difference between offset and drift?
2. Why check sync at the end as well as the start?
3. Name three sync methods.
4. What is a nested sequence?
5. What should determine multicamera angle selection?

## Answer key
1. Offset is a fixed timing difference; drift is a difference that grows over time.
2. To detect clock or frame-rate drift.
3. Timecode, waveform, clap/slate or visual event.
4. A sequence placed inside another sequence.
5. Story clarity, performance, action and visual continuity.

## Assessment rubric — 30 points
Sync method and report 8; drift diagnosis 6; multicamera construction 6; angle choices and continuity 6; project organization and handoff 4. Pass 24/30.

## Quality-control checklist
- [ ] Originals backed up.
- [ ] Sync checked at beginning, middle and end.
- [ ] Drift/offset diagnosed correctly.
- [ ] Angles labeled clearly.
- [ ] Primary audio source is consistent.
- [ ] Project reopens with media online.

## Further study
Study timecode standards, variable frame rate, audio sample rates and multicamera conform workflows.
