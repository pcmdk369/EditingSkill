# CT-13 Professional Lab 01 — Dialogue Cleanup, Mix and Loudness Validation

- Level: Advanced / Professional
- Estimated time: 4–6 hours
- Environment: DAW/audio editor and loudness meter; record OS/app/version
- Lab status: Authored procedure; not executed in this session

## Brief
Edit and mix a 60-second dialogue scene with ambience, music and effects. Deliver a final mix and requested stems against a supplied technical specification.

## Prerequisites
Complete CT-13 Lessons 01–05. Use learner-recorded or licensed media. Obtain exact loudness, true-peak, sample-rate, bit-depth and channel-layout requirements from the brief.

## Structure
```text
ct13-audio-lab/
  source/
  session/
  exports/review/
  exports/final/
  stems/
  rights/
  qc/
  delivery/
```

## Procedure
1. Inventory source audio and inspect format/channel metadata.
2. Create a session using the approved sample rate.
3. Organize dialogue, ambience, music and effects on labeled tracks.
4. Edit dialogue with context, room tone and smooth fades.
5. Apply conservative noise cleanup, EQ and dynamics as needed.
6. Route groups to buses and automate music under dialogue.
7. Check sync against the picture reference at multiple points.
8. Measure mix loudness and true peak against the provided spec.
9. Export a short proof and remeasure the rendered file.
10. Export final mix and stems with correct channel mapping.
11. Play every output from start to end.
12. Package session, dependencies, rights log and manifest.

## Expected artifacts
Final stereo mix, dialogue/music/effects stems, editable session, settings, loudness report, rights log and QC report.

## Validation
| Test | Method | Expected result |
|---|---|---|
| Edits | Full listening | No clicks/pops/unintended gaps |
| Dialogue | Speaker playback | Intelligible throughout |
| Sync | Compare multiple points | No unintended drift |
| Loudness | Measure rendered file | Within supplied target |
| True peak | Meter final file | Within supplied ceiling |
| Channel map | Inspect stems | Correct routing |
| Rights | Check asset log | Authorized use |

## Troubleshooting
Denoise artifacts: reduce processing. Pumping: adjust compression. Loudness mismatch: measure final render and revise. Wrong stem: inspect bus routing. Sync drift: inspect source frame-rate/clock behavior.

## Assessment — 100 points
Session/source handling 10; dialogue edit 15; cleanup/mix 20; routing/sync 15; loudness/true peak 15; stems/export 10; rights 5; handoff/QC 10. Pass 80/100; rights and technical compliance are mandatory.

## Handoff
Submit master, stems, session, dependency list, loudness report, rights record and manifest.
