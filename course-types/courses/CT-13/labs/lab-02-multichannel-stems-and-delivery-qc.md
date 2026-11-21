# CT-13 Professional Lab 02 — Multichannel Session, Stem Integrity and Delivery QC

- Course: CT-13 — Audio Editing
- Level: Advanced / Professional
- Estimated time: 4–6 hours
- Environment: DAW/audio editor, headphones and monitors, loudness/true-peak meter and file inspector
- Lab status: Authored procedure; no acoustic calibration or broadcast compliance certification is claimed

## 1. Scenario
Prepare a short program mix and a set of editable stems for a client who may revise dialogue, music and effects independently. The delivery brief specifies format, sample rate, bit depth, channel layout and loudness target. Learners must validate routing, phase, clipping and stem recombination.

## 2. Learning objectives
- organize a reproducible DAW session;
- route dialogue, music and effects to separate buses;
- create stems that recombine to the approved full mix;
- measure integrated loudness and peak according to the supplied target;
- validate channel layout, sync, phase and file integrity.

## 3. Inputs and setup
Use learner-created or licensed audio. Record DAW/version, OS, interface, sample rate, buffer settings and monitoring chain. Obtain the exact client/platform specification. Do not invent a loudness target; if absent, request one or mark the target unresolved.

## 4. Session architecture
```text
SESSION
  DIALOGUE tracks -> DIALOGUE BUS ----  MUSIC tracks    -> MUSIC BUS --------> MASTER
  FX tracks       -> FX BUS -----------/
  MASTER -> PRINT MIX
  DIALOGUE BUS -> DIALOGUE STEM
  MUSIC BUS -> MUSIC STEM
  FX BUS -> FX STEM
```

Document inserts, sends, automation, pan law, routing and any master processing. State whether stems are pre- or post-master processing.

## 5. Procedure
1. Duplicate and back up the session.
2. Verify all source files, sample rates, channel layouts and sync references.
3. Organize tracks and label dialogue, music and effects groups.
4. Check polarity/phase for related microphones and stereo pairs.
5. Set routing to dedicated buses and verify no track is accidentally double-routed.
6. Create the full mix using the approved processing chain.
7. Measure loudness and peak against the supplied specification.
8. Create stems using a documented print method and identical start/end boundaries.
9. Decide and record whether stems include bus processing, automation and master processing.
10. Re-import stems into a clean session at the same start time.
11. Sum stems and compare with the approved full mix; investigate differences caused by nonlinear master processing or routing.
12. Check mono compatibility and channel order where required.
13. Export final mix and stems with exact naming, format and metadata.
14. Reopen every file and listen to beginning, middle and end; inspect the complete program where practical.
15. Generate a manifest with checksum if available, duration, sample rate, bit depth, channel layout, loudness, peak and version.

## 6. Technical concepts
- **Sample peak:** Highest digital sample value.
- **True peak:** Estimated inter-sample peak that may exceed sample peak after reconstruction.
- **Integrated loudness:** Program-level loudness measurement over the measured duration, using the selected standard/meter.
- **Phase cancellation:** Reduction or change when correlated signals combine with different phase relationships.
- **Stem:** A submix containing a defined group of program elements.
- **Print master:** Final approved full mix.
- **Dither:** Noise-shaped or random process used when reducing bit depth, applied according to workflow requirements.

## 7. Validation matrix
| Test | Method | Pass condition |
|---|---|---|
| Session integrity | Open copied project | No missing media |
| Routing | Solo/mute each bus | Correct signal path |
| Phase | Polarity/mono check | No unintended cancellation |
| Stem alignment | Re-import at common start | Same duration/start boundary |
| Stem recombination | Sum stems and compare | Matches within documented processing differences |
| Loudness/peak | Meter full program | Meets supplied target |
| Channel layout | Inspect file metadata and listen | Correct mapping/order |
| File integrity | Reopen and play exports | No corruption or truncation |
| Handoff | Compare manifest | Exact versions and properties |

## 8. Troubleshooting
- Stem sum differs: check master bus compression/limiting, sends and nonlinear processing.
- Phase loss in mono: inspect polarity, mic spacing and stereo processing.
- Loudness mismatch: confirm meter standard, gating, measurement range and export normalization.
- Click at edit: refine crossfade and inspect waveform at sample level.
- Missing channel: inspect routing and export channel mapping.
- Different start times: print all stems from the same timeline boundary.

## 9. Deliverables
DAW session, full mix, dialogue/music/effects stems, routing diagram, loudness report, stem-recombine test, rights/source log and delivery manifest.

## 10. Assessment — 100 points
Session organization 10; routing 15; clean mix 15; stem integrity 20; loudness/peak validation 15; phase/channel checks 10; documentation/handoff 15. Pass 80/100. Clipped, corrupt or incorrectly mapped delivery requires remediation.

## 11. Completion checklist
- [ ] Session backed up and dependencies verified.
- [ ] Routing diagram matches actual session.
- [ ] Phase and mono compatibility checked.
- [ ] Stem start/end boundaries match.
- [ ] Stem recombination tested.
- [ ] Loudness target sourced from brief.
- [ ] Metadata and channel layout inspected.
- [ ] Exports reopened and manifest completed.
