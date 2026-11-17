# CT-02 Lesson 06 — Multicamera Editing and Synchronization

- **Course:** CT-02 — Film & Cinematic Editing
- **Level:** Advanced
- **Estimated study time:** 5–7 hours, including a practical synchronization exercise
- **Prerequisites:** Lessons 01–05; basic timeline editing, audio fundamentals, frame-rate terminology and media-management practice
- **Required environment:** Any non-linear editor (NLE) that can align and edit multiple sources, or a manual multi-track timeline; a media-information utility is useful but not mandatory
- **Software policy:** The procedures below are tool-independent. Application menu names, multicamera features and supported synchronization metadata vary by product, edition and version. Record the exact application, version and operating system used in the practical submission.
- **Lesson revision:** 2.0 — expanded academic lesson, 2026-11-17

---

## Learning outcomes

By the end of this lesson, the learner will be able to:

1. Distinguish timecode, synchronization, clock reference, fixed offset and sync drift, using accurate technical language.
2. Inventory at least two camera sources and one external audio source, recording the metadata required to make a repeatable sync decision.
3. Select and justify a synchronization method based on the available evidence and its limitations.
4. Align at least three sources to a common event and document the chosen reference.
5. Measure synchronization at the beginning, middle and end of a recording, separating fixed offset from changing drift.
6. Diagnose common causes of sync failure without applying an unexplained global offset or destructive speed change.
7. Construct a labeled multicamera source group or equivalent synchronized multi-track timeline.
8. Select camera angles according to dramatic beats, performance, screen direction, eyelines and sound continuity.
9. Produce a short multicamera edit with an unambiguous master-audio strategy and a recoverable source structure.
10. Submit a synchronization report, editorial rationale, quality-control record and versioned project handoff.

**Evidence standard:** A learner must provide a source inventory, sync map, start/middle/end verification, an editable synchronized structure, a review export and a written explanation of any limitations or corrections. A claim that sources are synchronized is not sufficient without evidence.

## Prerequisites and preparation

Before starting:

- Complete CT-02 Lessons 01–05, especially scene geography, coverage, continuity and pacing.
- Understand frame rate as a rate of image presentation or capture, not merely a project setting.
- Understand that audio sample rate describes the number of audio samples represented per second.
- Know how to preserve camera originals, create working copies or proxies, and save a new project version.
- Obtain footage that was recorded simultaneously or that contains clearly identifiable shared events.
- Confirm that the footage is original, licensed or otherwise authorized for the intended exercise. Do not upload confidential or identifiable footage to a cloud synchronization service without permission.

If no multicamera footage is available, use a controlled exercise: record the same visible hand clap with two devices and a separate audio recorder. This is a synchronization exercise, not a substitute for a real production's camera and audio workflow.

## Key definitions and terminology

| Term | Definition | Practical significance |
|---|---|---|
| Multicamera editing | Constructing one programme from multiple camera recordings of the same event | Provides editorial choice while requiring a stable shared timeline |
| Synchronization | Establishing the correct temporal relationship between recordings of the same event | Ensures picture and sound describe the same moment |
| Sync reference | A common event or signal used to align sources | May be a slate, clap, timecode label, waveform event or visible action |
| Timecode | A structured address that labels frames using hours, minutes, seconds and frame count | Helps locate and align media, but matching labels alone do not prove that devices captured the same instant |
| Jam sync | A process in which devices are set from a common timecode source | Reduces timecode disagreement; it must be configured and verified |
| Genlock / reference sync | A timing reference used to coordinate video capture or signal timing between devices | Relevant to certain multi-camera and broadcast systems; it is not the same thing as merely matching file timecode |
| Offset | A fixed difference between two sources at a particular point | Can often be corrected by moving one source by a known amount |
| Drift | A difference that changes over the duration of a recording | Requires diagnosis of timebase, clock or media interpretation rather than a single start offset |
| Sync point | A precise location in a source that corresponds to the same event in another source | A clap transient or a visible contact frame can be used |
| Dual-system sound | Audio recorded separately from the camera picture | Requires a reliable relationship between the recorder and camera recordings |
| Multicam source | A grouped or nested structure containing synchronized camera angles | Allows angle selection while retaining the underlying synchronized relationship |
| Master audio | The selected production or post-production audio source used as the primary sound reference | Prevents unintended doubled microphones, phase problems or changing room tone |
| Camera angle / camera label | An editorial identity assigned to a camera position or source group | Prevents ambiguous angle selection |
| Frame-rate mismatch | Different capture or interpretation rates among sources | Can create duration and sync problems if handled incorrectly |
| Variable frame rate (VFR) | Media whose frame presentation intervals vary rather than following one constant frame interval | May complicate time-based alignment and some NLE workflows |
| Sync map | A record of sources, sync references, measured offsets and corrections | Makes synchronization reviewable and recoverable |

### Important distinction: timecode is an address, not proof of a shared clock

Timecode is a frame-addressing system. Two files can display matching timecode values without necessarily having been captured at the same instant. The devices may not have been jam-synchronized, timecode may have been restarted, or unrelated clips may contain overlapping labels. Use camera identity, recording context and a second synchronization reference where possible.

Timecode and genlock solve related but different problems. Timecode labels positions in a sequence; genlock/reference timing coordinates video timing in systems designed to use it. A small production may not have genlock at all. Do not infer genlock merely because timecode matches.

## Purpose and professional relevance

A multicamera edit is only as reliable as its synchronization and source organization. A technically aligned sequence can still be editorially weak if it switches angles without purpose, changes screen direction unexpectedly or replaces a strong performance with a less effective one.

Synchronization creates a common temporal foundation. Editorial judgment then determines which camera best communicates each beat. The two tasks must be evaluated separately:

- **Technical question:** Do the camera and audio sources represent the same moment?
- **Editorial question:** Which source should the audience see or hear at this moment, and why?

In a dialogue scene, one camera may provide a stable master shot, another may cover Speaker A, and a third may cover Speaker B or a reaction. The editor should not switch simply because another angle exists. A cut should clarify information, reveal a reaction, support a performance beat, maintain geography or change point of view intentionally.

Multicamera workflows are common in interviews, live events, concerts, panel discussions, dramatic scenes and instructional productions. Each has different priorities. A live performance may prioritize continuity and musical timing; a dramatic scene may prioritize emotional reaction and performance; an interview may prioritize clean speech, natural pauses and the interviewee's eyeline.

## Theory and technical principles

### 1. Synchronization methods and their limits

| Method | How it works | Strength | Limitation / verification |
|---|---|---|---|
| Shared timecode | Aligns sources using timecode metadata | Efficient when all devices were configured correctly | Matching labels can be misleading; inspect actual events and clip identity |
| Slate or clap | Aligns a visible slate closure and its audible transient | Clear, human-readable production reference | Slate may be out of frame, obscured, clipped or recorded poorly |
| Waveform matching | Compares common recorded sound across sources | Useful when cameras and recorder capture the same event | Different microphones, noise, automatic gain or silence may prevent a reliable match |
| Visual event | Aligns a distinctive event visible in multiple cameras | Useful when audio is absent or unreliable | Rolling shutter, occlusion and frame-rate differences can make the exact frame ambiguous |
| Manual offset / in-out marks | Aligns known matching points by measured positions | Transparent and works without automatic multicam features | Requires careful measurement and independent checking |
| External synchronization reference | Uses a production timecode or reference system | Can support larger coordinated productions | Requires compatible equipment, configuration and monitoring |

No method is universally best. Choose the method supported by the actual recordings. Record why it was chosen and what could make it unreliable.

### 2. Fixed offset versus drift

A fixed offset exists when one source is consistently early or late by approximately the same amount throughout the recording. A single movement may correct it, provided the reference and source interpretation are valid.

Drift exists when the difference changes over time. If the sources align at the beginning but not at the end, a single global offset cannot correct the whole recording. Investigate:

- capture clock differences;
- incorrect or inconsistent frame-rate interpretation;
- variable-frame-rate media;
- audio sample-rate interpretation or conversion;
- timecode configuration or restart;
- recording pauses, file segmentation or dropped frames;
- an accidental speed change or retiming operation;
- an incorrect sync point or a misleading repeated waveform.

Do not assume that every end-of-recording mismatch is clock drift. A wrong camera angle, a different take, a recorder edit or an incorrect slate match can produce a similar symptom.

### 3. Measuring synchronization

Choose a recognizable event that is present in at least two sources. Record the relative offset at three or more positions:

- near the beginning;
- near the middle;
- near the end.

Use the same event definition at each check. For picture and dialogue, compare a visible mouth closure or plosive with the corresponding audio transient. For a slate, compare the first clear contact frame with the transient, taking account of the fact that the visual and audio events may not be perceived at exactly the same instant.

A simple diagnostic model is:

- **Offset at a check:** the measured timing difference between source B and the chosen reference source A.
- **Change in offset:** offset at a later check minus offset at the earlier check.
- **Residual drift:** the change that remains after any fixed starting offset has been removed.

For a frame-based comparison:

[
	ext{milliseconds per frame} = rac{1000}{	ext{frames per second}}
]

At 25 frames per second, one frame represents 40 milliseconds. At approximately 23.976 frames per second, one frame is approximately 41.7 milliseconds. These values help describe the measurement; they do not prove that a viewer will perceive a particular offset in every situation.

When comparing audio, a waveform transient may be measurable at a finer time scale than a video frame. Record the unit used. Do not mix frame counts, milliseconds and timecode labels without converting or identifying them.

### 4. Frame rate, audio sample rate and duration

Video frame rate and audio sample rate are different quantities. A video recording may use a nominal frame rate such as 24, 25, 29.97 or 30 frames per second, while audio may use a sample rate such as 48 kHz. The values must be interpreted correctly by the media pipeline.

Do not change a clip's frame-rate interpretation simply because its displayed metadata differs from the project setting. A reinterpretation may alter duration and motion. Likewise, do not resample audio as a blind synchronization fix. Determine whether the problem is metadata interpretation, a true clock difference, a fixed offset or a recording interruption.

Drop-frame timecode is a numbering convention used with certain fractional frame-rate systems; it does not drop picture frames. Non-drop-frame timecode counts labels differently. Confusing the two can create apparent timecode discrepancies. Use the actual media frame-rate/timecode metadata and the production's documented convention.

### 5. Audio strategy and channel management

Camera scratch microphones can help with waveform synchronization, but they are not automatically the correct final sound source. External production audio may provide cleaner dialogue. Establish a master-audio strategy before editing:

1. Identify the intended primary dialogue or production-audio recording.
2. Record channel names and channel assignments.
3. Confirm whether each source is mono, stereo or multichannel.
4. Listen for clipping, handling noise, radio interference, phase problems and missing channels.
5. Decide whether camera audio is retained as a reference, muted, or used for a specific purpose.
6. Avoid leaving several similar microphones active without checking for comb filtering, echo or changing room tone.
7. Preserve useful isolated tracks for later sound editing.

Do not assume that a stereo file contains two different microphones. Listen and inspect channel content before assigning roles.

### 6. Multicamera editorial logic

After synchronization, angle selection should follow the dramatic structure established in earlier lessons:

- Use a master or wide angle when the audience needs spatial orientation.
- Use a speaker angle when a line or performance detail requires emphasis.
- Use a reaction angle when the listener's response changes the meaning of the exchange.
- Preserve eyeline direction and the established axis unless a motivated transition changes the spatial model.
- Avoid cutting on every sentence or every camera movement.
- Protect pauses, overlaps, breaths and listening behavior when they carry dramatic meaning.
- Check that the selected angle actually contains the performance moment being heard.

The best multicamera edit is not necessarily the one with the most angle changes. It is the one that uses available coverage to construct a clear and meaningful experience.

## Tools, requirements and alternatives

### Required

- Original or authorized camera recordings of the same event.
- External audio where available.
- A source inventory or camera report.
- A method to compare source playback and locate a common event.
- An NLE or manual multi-track editor capable of preserving source alignment.
- A storage location with enough space for source media, project files and working copies.
- The CT-02 workbook, Section 9 — Multicamera Sync Record.

### Optional

- A slate or clap captured by all cameras.
- Jam-synchronized timecode devices.
- Genlock/reference synchronization where the production system supports it.
- A media-information utility for inspecting frame rate, duration, audio channels and timecode.
- Waveform display and audio meters.
- Proxies for performance on limited hardware.
- A checksum or verified-copy process for source-media integrity.

### Tool-independent alternatives

If the NLE has no multicamera feature, create a synchronized multi-track timeline with one camera per video track and a clearly designated audio track. Align all sources to the same reference, lock their positions, and cut visibility or use track-based edits.

If waveform synchronization is unavailable, use a slate, a visible event or measured in/out marks. If timecode is unavailable, do not invent it; document the manual sync reference and its uncertainty.

If the computer cannot play all angles in real time, create proxies or use a lower-resolution review workflow. Proxy creation must preserve the relationship to original media and must not replace the camera originals.

### Source safety

- Keep original media read-only where possible.
- Do not rename, overwrite or delete camera originals to make a sync operation easier.
- Use working copies, proxies or a separate project structure.
- Keep a record of relinking or conforming operations.
- Do not upload private or unreleased footage to an external service without authorization.
- Do not treat an automatic sync result as verified until it passes the checks below.

## Reproducible procedure

### Phase A — Prepare and inventory

1. Create a project folder with separate locations for camera originals, external audio, proxies, project files, review exports and reports.
2. Copy or ingest the authorized source media using the production's approved process.
3. Verify that copies are readable. Where the production requires it, compare checksums or use a verified-copy tool.
4. Do not alter original filenames. Assign editorial IDs in the inventory.
5. Record for every source:
   - camera or recorder ID;
   - original filename;
   - clip duration;
   - frame rate and whether it is constant or variable if known;
   - resolution and codec where available;
   - timecode start and timecode type if present;
   - audio channel count and sample rate;
   - recording start/stop notes;
   - any known camera or recorder interruptions.
6. Identify which sources overlap in actual recorded time. Do not group clips merely because their timecode labels look similar.

### Phase B — Select the sync reference

1. Review the available slate, clap, waveform or visible action.
2. Select the clearest common event shared by the relevant sources.
3. Confirm that the event belongs to the same take and recording instance.
4. Note the source time position for each angle and audio recording.
5. Record the chosen method and any limitation.
6. If two references disagree, stop and investigate before building the multicamera source.

### Phase C — Establish initial alignment

1. Create a new synchronized group, multicamera source or manual multi-track sequence.
2. Place the reference source at the agreed timeline origin.
3. Align each additional source to the selected common event.
4. Name each source clearly, for example CAM_A_WIDE, CAM_B_LEFT, CAM_C_RIGHT and AUDIO_MIX.
5. Confirm that the intended audio channels are identifiable.
6. Lock or group the aligned sources to reduce accidental movement.
7. Save a new project version before editorial cutting.

### Phase D — Verify at multiple points

1. Check a second shared event near the beginning.
2. Check another event near the midpoint.
3. Check another event near the end.
4. At each point, record the measured difference and the measurement unit.
5. Compare the differences:
   - same difference at all points: likely fixed offset;
   - steadily changing difference: possible clock or timebase drift;
   - sudden change: possible recording interruption, dropped segment, retime or incorrect event match;
   - inconsistent measurements: reference may be ambiguous or the sources may not represent the same event.
6. Repeat the check using another event if the result is uncertain.
7. Do not declare synchronization complete while a material discrepancy remains unexplained.

### Phase E — Diagnose and correct

1. Confirm the camera and recorder identities.
2. Re-check the common event and take identity.
3. Inspect the frame-rate and timecode interpretation of each source.
4. Check for variable-frame-rate media and recording interruptions.
5. Confirm audio sample-rate interpretation and channel mapping.
6. Determine whether the problem is a fixed offset, linear drift, discontinuity or incorrect source selection.
7. Select a correction appropriate to the cause:
   - fixed offset: adjust the working source alignment;
   - constant drift: use a documented timebase or conform strategy supported by the NLE and media;
   - discontinuity: segment and re-synchronize the affected sections;
   - wrong source or take: replace it with the correct recording;
   - uncertain cause: preserve the current work and escalate for technical review.
8. Never apply an unexplained speed change, pitch change or destructive overwrite.
9. Re-check the beginning, middle and end after correction.
10. Record the before/after measurements and the reason for the correction.

### Phase F — Build and edit the multicamera scene

1. Confirm that all angle labels are unique and descriptive.
2. Identify the master or wide angle and the intended master-audio source.
3. Review the entire scene once without making angle changes.
4. Mark dramatic beats, speaker changes, reactions and important overlaps.
5. Create a first angle pass that prioritizes clear story information and performance.
6. Create a second pass to refine reaction shots, pauses, movement and emphasis.
7. Check each cut for screen direction, eyeline, action continuity and sync.
8. Listen to the audio continuously while reviewing angle changes.
9. Confirm that cuts do not unintentionally change the active audio source.
10. Preserve the synchronized source structure so later angle revisions remain possible.

### Phase G — Handoff and evidence

1. Save a clearly named project version.
2. Export a review copy using a documented temporary specification.
3. Re-open or play the exported file from its delivery location.
4. Complete the sync map and QC checklist.
5. Include the project application/version, source inventory, sync method, measurements, corrections and unresolved limitations.
6. Preserve the source media and project relationship for later relinking or finishing.

## Worked example — Three cameras and one external recorder

### Production setup

A fictional three-minute dialogue scene uses:

- Camera A: wide master;
- Camera B: close-up on Speaker 1;
- Camera C: close-up on Speaker 2;
- Recorder D: external dialogue mix.

A visible slate clap is recorded by all four sources. Camera A is chosen as the initial reference. The editor aligns the clap and records the relative offset of Recorder D at three later events.

The following measurements are illustrative training data, not a claim about a real recording:

| Check | Approximate scene position | Recorder D relative to Camera A after initial alignment |
|---|---:|---:|
| Start | 00:00 | 0 frames |
| Middle | 01:30 | +1 frame |
| End | 03:00 | +2 frames |

At 25 fps, the measured change from start to end is 2 frames, or approximately 80 ms. The result suggests a small increasing timing difference, but the three measurements alone do not prove the cause. The editor must inspect media frame-rate interpretation, recorder settings, interruptions and the exact event match before deciding on correction.

The editor should not simply move Recorder D by two frames at the start. That would make the end appear better while making the start wrong. If the difference is confirmed as steady drift, a documented conform or segment-based correction may be appropriate. If the mismatch comes from an incorrect reference, the measurements must be redone.

After correction, the editor repeats all three checks and records the new results. The external dialogue mix becomes the designated master audio. Camera audio is retained only as reference unless a specific sound is needed. The first angle pass follows dramatic beats; the second pass refines reaction shots and listening moments.

### Editorial decision example

Speaker 1 says, “I thought you had left.” Speaker 2 does not answer immediately. Camera B shows Speaker 1 waiting; Camera C shows Speaker 2 looking away before responding. The editor may hold on Speaker 2's reaction because the pause changes the meaning of the answer. A cut to Camera C should be checked for matching eyeline and for the correct audio source. A technically synchronized angle is not automatically the best dramatic choice.

## Dry run / annotated walkthrough

**Objective:** Demonstrate a repeatable synchronization test before editing a full scene.

**Inputs:**
- two camera clips covering the same 60-second action;
- one external audio recording;
- one clear slate clap near the beginning;
- a second visible/audible event near the middle;
- a final clear event near the end.

**Walkthrough:**

1. Create a source inventory and label the files A, B and AUDIO.
2. Identify the clap in all three sources.
3. Align the clap and record the initial offsets.
4. Find the middle event and compare the sources.
5. Find the end event and compare the sources.
6. Enter the measurements in a table.
7. Classify the result as fixed offset, possible drift, discontinuity or uncertain.
8. Write the next diagnostic action without making an unexplained correction.
9. Save the project and report.

**Expected output:**
- three-source synchronized structure;
- source inventory;
- start/middle/end measurement table;
- one-paragraph diagnosis;
- project version and review notes.

**Dry-run acceptance:** The learner can explain why the sync result is or is not trusted. No angle-editing speed is assessed at this stage.

## Guided practice — Two angles and external dialogue

**Brief:** Build a 60–90 second dialogue scene using two camera angles and one external dialogue recording.

### Tasks

1. Inventory all sources and identify the intended master audio.
2. Choose a sync reference and justify the choice.
3. Align the sources in an NLE or manual multi-track timeline.
4. Verify synchronization at three points.
5. Create a labeled synchronized structure.
6. Make at least six angle decisions based on speaker performance or listener reaction.
7. Preserve the established axis and eyelines.
8. Review the audio for doubling, channel swaps and unwanted camera microphone bleed.
9. Export a review copy and complete the workbook's multicamera sync record.

### Submission

- source inventory;
- sync map;
- start/middle/end measurements;
- editable project or documented track layout;
- 60–90 second review export;
- short explanation of three important angle decisions;
- limitations and unresolved issues.

## Independent assignment — Multicamera interview

**Brief:** Synchronize and edit a 5–10 minute interview recorded with at least two cameras and, where available, a separate audio recorder.

### Required deliverables

1. Media inventory with source identities and technical metadata.
2. Sync-method decision record.
3. Start, midpoint and end sync measurements.
4. Drift diagnosis and correction record, or a documented statement that no material drift was found.
5. Labeled multicamera source or manual synchronized timeline.
6. Master-audio and channel-mapping note.
7. A 2–3 minute edited interview excerpt.
8. QC report and project handoff note.

### Constraints

- Do not remove meaningful pauses solely to make the speaker appear more fluent.
- Do not construct a misleading answer by combining unrelated statements.
- Do not use a reaction shot in a way that falsely implies a response to a statement it did not accompany.
- Preserve the original media and maintain a recoverable edit.
- Record any synthetic, denoised or AI-assisted processing and require human review.

## Common errors, troubleshooting and recovery

| Symptom | Possible cause | Diagnostic action | Safe recovery |
|---|---|---|---|
| Sources are all late by the same amount | Fixed offset or wrong reference origin | Compare the same event in each source | Re-align working copies and record the offset |
| Start is aligned but end is not | Drift or timebase interpretation problem | Compare start, middle and end; inspect media metadata | Diagnose before conforming; re-check after any correction |
| Middle is correct but end suddenly changes | Recording interruption, dropped segment or source splice | Inspect the interval around the change | Segment the source and re-synchronize affected sections |
| Waveform sync cannot find a match | Different microphone perspectives, noise, silence or automatic gain | Listen to each source and locate a slate/visual event | Use a clearer manual reference |
| Timecode matches but picture does not | Devices not actually synchronized, restarted timecode or unrelated clips | Compare slate and distinct visible events | Use verified event alignment; document timecode limitation |
| Dialogue has echo or comb filtering | Several camera microphones are active | Solo channels and compare the sound | Choose a master source and mute or deliberately mix others |
| One camera appears to be a different take | Similar-looking but non-identical recordings | Compare action, slate, dialogue and background events | Remove the incorrect source from the multicam group |
| Sync is good in picture but wrong in audio | Incorrect audio mapping or channel routing | Check channel assignments and transient alignment | Correct mapping and repeat the audio checks |
| Angle cuts reverse screen direction | Camera positions cross the axis or wrong angle is selected | Revisit the scene geography diagram | Select a compatible angle or motivate a new spatial orientation |
| Angle changes cut off a word or reaction | Editorial decisions are based only on camera availability | Review dialogue and dramatic beats | Restore handles and choose an angle that covers the complete beat |
| Project opens with missing sources | Media was moved or relinked incorrectly | Compare source inventory and project paths | Relink to verified originals; do not create duplicate ambiguous copies |
| Proxy playback is synchronized but original is not | Proxy relationship or conform mapping is incorrect | Compare proxy and original at identical source events | Rebuild or verify proxy mapping before finishing |
| A correction changes pitch or motion | Uncontrolled speed change or resampling | Compare duration, pitch and source properties | Restore the untouched source and use an appropriate documented conform process |

If the cause cannot be established, preserve the current project, mark the source as unresolved and request technical review. A transparent limitation is preferable to a hidden sync error.

## Knowledge check

Answer without looking at the guidance first.

1. What is the difference between timecode and synchronization?
2. Why can two sources with matching timecode labels still be out of sync?
3. Explain the difference between fixed offset and drift.
4. Why should synchronization be checked near the beginning, middle and end?
5. Name four possible synchronization references.
6. What is the difference between timecode and genlock/reference sync?
7. Why should camera scratch audio not automatically become the master audio?
8. What does a sudden change in offset suggest compared with a steady gradual change?
9. Why is a manual synchronized multi-track timeline a valid alternative to a dedicated multicamera feature?
10. Give three editorial reasons to choose a reaction angle.
11. What evidence should accompany a claim that a multicamera sequence is synchronized?
12. Why must an editor re-check synchronization after a conform or correction?

## Answer key / instructor guidance

1. Timecode labels positions; synchronization establishes the actual temporal relationship between recordings.
2. Timecode may have been restarted, configured independently, duplicated across files or not tied to a shared capture reference.
3. Fixed offset is approximately constant; drift changes over time.
4. Multiple checks reveal changing timing relationships and possible discontinuities that a single start alignment cannot reveal.
5. Shared timecode, slate/clap, common waveform, visible event, manual in/out reference or an external synchronization system.
6. Timecode is an address/label; genlock/reference sync coordinates video timing where supported.
7. Camera microphones may be distant, noisy, clipped or different from the intended production mix; multiple active microphones can cause echo or phase effects.
8. A sudden change may indicate a recording interruption, segment splice, dropped frames or wrong event match; steady change may indicate clock/timebase drift.
9. It preserves a common timeline and allows manual angle selection without depending on a specific software feature.
10. To reveal a change in understanding, show listening behavior, emphasize a reaction, or shift the audience's point of view.
11. Source inventory, chosen sync method, sync map, measurements at multiple points, correction notes and verified playback.
12. A correction can alter duration, timing, mapping or audio interpretation; the result must be checked again rather than assumed correct.

## Assessment rubric — 100 points

| Criterion | Evidence | Points |
|---|---|---:|
| Source inventory and media preservation | Correct identities, metadata, safe handling and clear organization | 10 |
| Sync-method selection | Appropriate reference chosen and limitations explained | 10 |
| Initial synchronization | Sources aligned to a valid shared event | 15 |
| Multi-point verification | Start/middle/end measurements recorded and interpreted correctly | 15 |
| Drift diagnosis and correction | Cause investigated; correction is justified, non-destructive and re-verified | 15 |
| Multicamera organization | Clear angle labels, source grouping, audio mapping and recoverability | 10 |
| Editorial angle selection | Decisions support dramatic beats, performance and point of view | 10 |
| Continuity and sound | Screen direction, eyelines, dialogue and audio transitions reviewed | 5 |
| Handoff and evidence | Project, review export, sync report and limitations documented | 10 |
| **Total** | | **100** |

**Pass threshold:** 75/100 and no critical failure in source preservation, unexplained synchronization error, or unambiguous master-audio mapping.

A learner who cannot establish reliable synchronization should receive feedback and repeat the technical portion. Do not award full synchronization credit for an attractive edit whose sync has not been verified.

## Quality-control checklist

### Source and project integrity
- [ ] Original media is preserved.
- [ ] Camera and recorder identities are documented.
- [ ] File names and source IDs are unambiguous.
- [ ] Project and proxy relationships are recoverable.
- [ ] No source was destructively overwritten or silently replaced.

### Synchronization
- [ ] Sync reference is identified and justified.
- [ ] Timecode assumptions are documented.
- [ ] Start, midpoint and end are checked.
- [ ] Fixed offset and drift are not confused.
- [ ] Any correction is documented and re-verified.
- [ ] Unresolved discrepancies are disclosed.

### Audio
- [ ] Master-audio source is named.
- [ ] Channel mapping is verified.
- [ ] Unwanted doubled camera audio is controlled.
- [ ] Dialogue and visible mouth movement are checked.
- [ ] No unintended mute, clip, phase or routing problem remains.

### Editorial continuity
- [ ] Angle labels are descriptive.
- [ ] Angle changes serve performance or story.
- [ ] Eyelines and screen direction are consistent or intentionally re-established.
- [ ] Reactions are not misleadingly reassigned.
- [ ] Dialogue overlaps and pauses remain intentional.

### Delivery
- [ ] Project version is recorded.
- [ ] Review export plays from its delivery location.
- [ ] Sync report and media inventory are included.
- [ ] Application, version and platform are recorded.
- [ ] Limitations and unverified operations are disclosed.

## Further study and references

1. **SMPTE ST 12-1:2014 — Time and Control Code.** The standard defines time-address and timecode transport structures for supported nominal frame rates. It is a technical reference, not a substitute for verifying a production's actual device configuration. [Official SMPTE publication PDF](https://pub.smpte.org/pub/st12-1/st0012-1-2014.pdf).
2. **Adobe Help — Create a multi-camera source sequence in Premiere.** Current documentation describes synchronization options including in/out points, timecode, audio and clip markers. Treat the instructions as application-specific and confirm the installed version before following them. [Adobe documentation](https://helpx.adobe.com/ca/premiere/desktop/edit-projects/set-up-multi-camera-sequences-for-editing/create-a-multi-camera-source-sequence.html).
3. **Blackmagic Design — DaVinci Resolve Cut page.** Official product documentation describes Sync Bin and multicamera-related workflows. Feature availability and exact operation depend on the installed Resolve version and page/workspace. [Blackmagic Design documentation](https://www.blackmagicdesign.com/products/davinciresolve/cut/).
4. **Frame.io — Timecode is Not Time.** An explanatory technical article on why matching timecode labels should not be mistaken for a guaranteed shared capture clock. [Article](https://blog.frame.io/2022/07/11/reinventing-timecode-for-the-cloud/).
5. **PCMDK369™ CT-02 textbook, Chapter 7 — Multicamera Synchronization and Scene Management.** Use this lesson for the detailed practical workflow and evidence requirements.
6. **PCMDK369™ CT-02 Student Notes & Practical Workbook, Section 9 — Multicamera Sync Record.** Use the workbook to record source IDs, sync method, measurements and correction notes.
7. **CT-02 Lab 03 — Multicamera Synchronization and Editing.** Use the lab for a shorter implementation exercise and submission checklist.

External product documentation is supplementary. Do not copy a software workflow into a course exercise unless its application, edition, platform and version have been verified. The tool-independent procedures in this lesson remain the primary learning outcomes.

## Version and change notes

- **2.0 — 2026-11-17:** Expanded definitions, timecode and genlock distinctions, synchronization methods, offset/drift measurement, frame/audio timing principles, audio strategy, reproducible procedure, worked example, dry run, guided and independent practice, troubleshooting, answer guidance, rubric, QC and references.
- **Software coverage:** Tool-independent. No NLE was executed or tested during this lesson revision.
- **Known limitations:** A written lesson cannot prove synchronization of any actual media. Learner evidence must come from the supplied or independently authorized source recordings.
- **Next lesson:** CT-02 Lesson 07 — Assembly, Rough Cut, Fine Cut and Picture Lock.
