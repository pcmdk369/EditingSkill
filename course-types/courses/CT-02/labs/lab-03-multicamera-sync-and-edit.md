# CT-02 Lab 03 — Multicamera Synchronization and Editing

**Level:** Intermediate → Advanced  
**Estimated time:** 2–3 hours  
**Software:** NLE with multicamera or synchronized-sequence capability; manual synchronization is acceptable.  
**Output:** A synchronized two-camera scene with external audio and a sync verification report.

## Learning outcomes
The learner can inventory camera/audio sources, choose a synchronization method, validate sync at multiple points, organize angles and edit a short scene while preserving performance and geography.

## Prerequisites and materials
- Two camera recordings of the same event.
- One external audio recording, if available.
- Shared timecode, slate/clap or a clear common waveform event.
- CT-02 workbook multicamera sync record.

## Concepts
**Synchronization** aligns recordings of the same event. **Offset** is a fixed timing difference. **Drift** is a timing difference that changes over time. **Multicamera editing** selects among synchronized camera angles while the event plays.

## Procedure

### A. Inventory
1. Create a separate folder for each camera and the external audio.
2. Record filenames, camera IDs, frame rates, resolution, codec, audio sample rate, timecode source and recording duration.
3. Check for variable-frame-rate media or recording interruptions.
4. Preserve source files and create working copies or proxies if required by the system.

### B. Select a sync method
Use a reliable common reference:
- shared, correctly configured timecode;
- slate/clap with visible frame and audible transient;
- waveform matching when sources contain the same recorded sound;
- a distinct visual event visible in multiple cameras.

Record the chosen method and its limitations. Do not assume two devices share accurate timecode merely because displayed time values look similar.

### C. Synchronize
1. Create a synchronized group, multicamera source or aligned timeline.
2. Align the common reference.
3. Label each angle consistently.
4. Confirm audio channel identity and choose the intended production or external audio source.
5. Lock or group synchronized sources to prevent accidental movement.
6. Save a new project version.

### D. Verify drift
1. Check a clear sync event near the start.
2. Check another event near the midpoint.
3. Check another event near the end.
4. Record any offset at each point.
5. If offset increases over time, investigate frame-rate/timebase mismatch, variable-frame-rate media, sample-rate interpretation or recording clock differences.
6. Correct using a documented method appropriate to the media; do not stretch or resample without understanding the effect on pitch, motion and duration.

### E. Edit the scene
1. Create a multicamera sequence or a timeline with synchronized angles.
2. Play through the scene and choose angles based on dramatic beats and performance.
3. Preserve screen direction and eyelines.
4. Avoid changing angles simply to create activity.
5. Review all angle changes for sync, continuity and performance.
6. Export a review file using a documented temporary specification.

## Worked example
Camera A and Camera B both record a hand clap at the beginning. External audio records the same clap. Align the clap transient and verify the mouth/hand action. Then compare a second shared event near the end. If the clap aligns but the later event does not, the issue is drift, not a simple start offset.

## Troubleshooting
| Problem | Possible cause | Investigation |
|---|---|---|
| All sources start out of sync by same amount | Fixed offset | Re-align the common reference |
| Sync is correct at start but wrong at end | Drift | Check timebase, variable frame rate and sample rate |
| Waveform matching fails | Different microphone perspective/noise | Use slate or visual event |
| Audio doubles or echoes | Multiple camera mics active | Choose intended audio and mute unused tracks |
| Angle changes damage geography | Camera axis or angle selection | Recheck scene diagram and screen direction |

## Submission evidence
- Source inventory.
- Synchronization method and reason.
- Start/middle/end sync measurements.
- Labeled multicamera project or synchronized timeline.
- 60–90 second multicamera edit.
- Notes on any limitations or corrections.

## Assessment — 25 points
- Source inventory: 5
- Correct sync method: 5
- Drift verification: 7
- Editorial angle selection and evidence: 8

**Pass:** 18/25.

## Quality gate
The project reopens with sources online; all angles have clear labels; sync is verified at three points; the intended audio is unambiguous; angle changes preserve story, performance and spatial logic.
