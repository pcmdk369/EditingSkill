# CT-06 Professional Lab 02 — Multicamera Sync Drift, Music Rights and Delivery Audit

- Course: CT-06 — Music Video & Performance Editing
- Level: Advanced / Expert
- Estimated time: 3–5 hours
- Environment: NLE with waveform or multicamera tools, media metadata inspector and spreadsheet
- Lab status: Authored procedure; no execution or device-specific compatibility is claimed

## 1. Scenario
A performance was recorded on three cameras and a separate audio recorder. One camera uses a different frame rate, one recording starts late, and the client requests a master plus two teasers. The learner must diagnose sync, preserve the approved audio, and prove that each asset is cleared for its intended use.

## 2. Learning objectives
- distinguish initial sync offset from cumulative drift;
- identify frame-rate and variable-frame-rate risks;
- build a repeatable sync validation plan;
- map separate music, recording, performance, footage and artwork rights;
- validate derivative versions and document limitations.

## 3. Inputs and safety
Use learner-created or licensed performance footage and audio. Preserve originals. Record camera, recorder, frame-rate and timecode metadata. Do not upload unreleased artist material to an external AI service without authorization.

## 4. Rights matrix
| Asset layer | Example evidence | Check |
|---|---|---|
| Musical composition | Publisher/songwriter authorization | Territory, term, media |
| Sound recording/master | Label/master-owner permission | Exact recording and edit |
| Performer | Appearance/performance release | Uses and restrictions |
| Camera footage | Producer/cinematographer agreement | Ownership and delivery rights |
| Lyrics | Lyric authorization where required | Display, translation and excerpt |
| Artwork/branding | License or brand approval | Territory, term and context |
| Location | Location release/permit if applicable | Intended distribution |

## 5. Implementation procedure
1. Create a verified backup and source inventory.
2. Inspect each file's duration, frame rate, timecode, audio sample rate and channel layout.
3. Identify a common sync event such as slate/clap or a clear waveform transient.
4. Align each source at the start and record its offset.
5. Check a second and third sync point later in the recording.
6. Calculate whether the error remains constant or increases over time.
7. If drift increases, investigate frame-rate mismatch, variable-frame-rate media, recorder clock drift or incorrect conform settings.
8. Test a correction on a duplicate sequence; preserve the unmodified source.
9. Recheck sync at beginning, middle and end, including visible lip or instrument action.
10. Lock the approved audio master and record its exact filename/version.
11. Build the rights matrix for every asset and intended derivative.
12. Create the master and two teasers as distinct sequences; do not change music without approval.
13. Review every cut for performance continuity and musical phrase.
14. Export review copies, inspect metadata and watch/listen completely.
15. Create a manifest with sync method, residual issue, rights state, version and approval.

## 6. Diagnostic model
- **Constant offset:** all later sync points show approximately the same displacement; likely alignment offset.
- **Increasing offset:** displacement grows over time; investigate clock or frame-rate/conform issue.
- **Irregular offset:** jumps occur; inspect dropped frames, edit points or damaged media.
- **Correct waveform but wrong performance:** source may be a different take or playback; use matching take or approved audio.

Do not apply arbitrary speed changes until the cause is identified.

## 7. Validation matrix
| Test | Procedure | Pass condition |
|---|---|---|
| Initial sync | Compare first clear event | Within project tolerance |
| Midpoint sync | Compare later event | No unexplained drift |
| End sync | Compare final event | No cumulative mismatch |
| Performance | Inspect mouth/instrument action | Correct take and timing |
| Audio identity | Compare master filename/checksum if available | Approved audio version |
| Rights | Review all asset layers | Permission covers each intended use |
| Derivatives | Watch each teaser | Correct music, framing and approvals |
| Delivery | Compare exports with manifest | Exact files and settings |

## 8. Troubleshooting and rollback
If sync correction damages pitch or motion, undo and test a different conform method on a duplicate. If the recording is damaged or lacks reliable sync references, document uncertainty and request a source replacement. If any right is missing, block that asset/version rather than assuming the master license covers all layers.

## 9. Deliverables
Synchronized project, source metadata sheet, sync-point table, drift diagnosis, approved audio record, rights matrix, master and two teasers, QC report and delivery manifest.

## 10. Assessment — 100 points
Metadata/source inventory 10; drift diagnosis 20; sync correction and verification 20; musical/performance continuity 15; rights matrix 15; derivative adaptation 10; QC/handoff 10. Pass 80/100. Unauthorized use or unverified sync is a mandatory remediation gate.

## 11. Completion checklist
- [ ] Originals preserved and backup verified.
- [ ] Metadata recorded for all sources.
- [ ] Start/middle/end sync points checked.
- [ ] Drift cause distinguished from fixed offset.
- [ ] Approved audio master identified.
- [ ] Rights matrix covers each layer and use.
- [ ] Each derivative reviewed independently.
- [ ] Full playback and manifest completed.

## 12. Further study
Consult current official documentation for the selected NLE's multicamera, frame-rate conform and audio synchronization features. Rights questions require qualified advice in the relevant territory.
