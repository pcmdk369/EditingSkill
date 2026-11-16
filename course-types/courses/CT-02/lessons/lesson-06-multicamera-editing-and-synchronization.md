# CT-02 Lesson 06 — Multicamera Editing and Synchronization

- Course: CT-02 — Film & Cinematic Editing
- Level: Advanced
- Estimated time: 4–5 hours
- Prerequisites: Lessons 01–05; basic timeline and audio knowledge
- Environment: Any NLE with synchronized/multicam or manual grouped-track editing; record application and version
- Version/review date: 1.0 — 2026-11-16

## Learning outcomes
By the end, learners can synchronize at least two camera angles and a production-audio source, diagnose drift, create a multicamera source sequence, select angles without breaking continuity, and deliver a documented synchronized sequence.

## Key definitions
| Term | Definition | Example |
|---|---|---|
| Multicamera | Editing a shared event from multiple synchronized camera sources | Two cameras covering a dialogue scene |
| Sync point | A shared event used to align recordings | Slate clap or waveform transient |
| Timecode sync | Alignment using matching timecode metadata | Jam-synced cameras |
| Waveform sync | Alignment by matching recorded audio waveforms | Clap captured by both cameras |
| Drift | Increasing timing offset during a recording | Camera audio gradually moves out of sync |
| Multicam source sequence | A synchronized container of angle sources | A/B/C angles plus external audio |

## Purpose and theory
Multicamera editing expands editorial choice but adds synchronization and media-management risk. A strong sync method is repeatable and independently checked. Matching waveforms can fail when cameras recorded different audio, when a track is silent, or when room noise is similar. Timecode can fail if devices were not correctly jam-synced or use different frame-rate assumptions. A slate/clap provides a visible and audible reference, but the editor must still inspect lip sync and long-duration drift.

## Tools and alternatives
Use an NLE multicamera feature where available. A manual alternative is to place each angle on a separate track, align a common sync point, lock track positions, and cut visibility. External audio may be used as the master reference. Do not assume a menu name or automatic-sync feature is present in every edition.

## Procedure
1. Duplicate and checksum/verify source media where practical; never rename or overwrite camera originals.
2. Inventory camera name, clip name, frame rate, start timecode, duration, audio channels and recording notes.
3. Identify the strongest common sync reference: jam-synced timecode, slate/clap, or waveform.
4. Test alignment near the beginning. Compare the slate transient and a clear mouth movement.
5. Inspect a second point near the middle and end. Record any offset change.
6. If drift exists, diagnose frame-rate mismatch, variable-frame-rate media, sample-rate mismatch, clock drift or incorrect timecode.
7. Correct only on working copies. Use a documented conform, resample or segmented sync workflow; do not stretch media blindly.
8. Build the multicam source sequence with descriptive angle names and external audio mapped clearly.
9. Select angles based on performance, screen direction, eyelines, shot size and dramatic emphasis—not merely camera order.
10. Review every cut for sync, continuity, unwanted camera bumps and audio transitions.
11. Save a sync report and preserve the original synchronized sequence before editorial restructuring.

## Worked example
A three-minute dialogue scene has Camera A wide, Camera B on Speaker 1, Camera C on Speaker 2, and a separate recorder. Align the clap at 00:00:12:08. At the midpoint, check a plosive and mouth movement; at the end, check the final line. If the end is 4 frames late, do not simply offset the whole clip: compare frame rates, audio sample rates and whether the drift grows linearly. Correct the cause, then verify start, middle and end again.

## Dry run
- Input: A/B/C clips, external WAV, one slate clap.
- Expected: one synchronized sequence with four clearly named sources.
- Checks: first/middle/end sync, no muted required angle, no channel swap, no accidental source slip.
- Evidence: screenshot or written sync map plus playback notes.

## Guided practice
Synchronize two angles and one external audio recording. Create five angle changes while preserving the dialogue performance. Submit the source sequence and a 1-page sync report.

## Independent assignment
Synchronize a 5–10 minute multicamera interview. Include a sync map, chosen master audio, drift findings, and an exported review file.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Correct at start, wrong at end | Clock/frame-rate drift | Compare multiple sync points | Conform/resample a copy or segment sync |
| Auto-sync fails | No common waveform or noisy audio | Inspect slate/timecode | Use manual sync reference |
| Lip sync appears wrong | Wrong angle/audio mapping | Check mouth movement and channel map | Relink correct audio and re-verify |
| Angle cut jumps screen direction | Poor coverage plan | Review geography and eyelines | Choose a matching angle or motivated neutral shot |

## Knowledge check and answers
1. Why check sync at multiple points? — To detect drift, not just initial offset.
2. Which method is always best? — None; choose the most reliable available reference and verify it.
3. Why preserve a sync map? — It makes the process reviewable and recoverable.

## Assessment rubric (100 points)
- Media inventory and rights-safe handling: 15
- Correct synchronization and drift diagnosis: 30
- Multicam organization and naming: 15
- Editorial choices and continuity: 20
- Validation evidence and handoff: 20
Pass: 75/100 and no unresolved sync failure.

## Quality-control checklist
- [ ] Source media preserved.
- [ ] Start, middle and end sync checked.
- [ ] Audio channels and angle labels verified.
- [ ] Drift diagnosed and correction documented.
- [ ] Multicam sequence saved and independently reviewed.

## References and version notes
Use the selected NLE's official multicamera and synchronization documentation. Feature availability varies by application, edition and version; this lesson teaches transferable principles and does not claim a specific UI was tested.
