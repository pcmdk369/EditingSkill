# CT-03 Professional Lab 02 — Multi-Format Versioning and Batch Delivery

- Course: CT-03 — Short-Form & Social Video Editing
- Level: Advanced / Professional implementation
- Estimated time: 3–5 hours
- Environment: Any NLE with sequence duplication and batch export; record OS, editor/version and hardware
- Lab status: Authored instructional procedure; not executed or tool-tested in this authoring session

## 1. Professional brief
A client has approved one 30-second campaign master. Produce vertical, square and landscape adaptations, each with a separate export, caption-safe composition and manifest. Preserve the master.

## 2. Learning and implementation objectives
- create traceable derivatives without modifying the approved master;
- recompose shots and graphics for three aspect ratios;
- batch export using verified settings;
- validate every output and create a handoff manifest.

## 3. Prerequisites and setup
Complete CT-03 Lessons 01–04. Use an editor supporting multiple sequences or project copies. Exact menu paths are application/version-specific; consult the selected editor's official manual. Create a backup and a dedicated output folder.

## 4. Inputs and asset rights
Use learner-created or licensed footage, graphics and audio. Record source filenames, license/consent and any restrictions. Inputs: approved master project, source media, transcript, brand graphics and signed-off delivery specification.

## 5. Architecture and project structure
```text
campaign-delivery/
  source-master/
  project/
    master/
    vertical-9x16/
    square-1x1/
    landscape-16x9/
  exports/
    review/
    approved/
  captions/
  manifests/
  qc/
```

## 6. Implementation procedure
1. Copy the approved project to a working location; verify the backup opens.
2. Record master filename, version, duration and approval state.
3. Create three derivative sequences with explicit dimensions and frame-rate settings from the brief.
4. Reframe every shot; inspect subject position, action and text-safe placement.
5. Adjust title/caption placement separately for each sequence.
6. Compare each adaptation to the approved message and required evidence.
7. Name each sequence and export with project, platform, aspect ratio, language, version and date.
8. Configure batch export only after confirming every sequence's output settings.
9. Render a short proof from each sequence and inspect it.
10. Render full outputs into the review folder.
11. Run metadata checks and full playback on every export.
12. Correct defects, increment version and rerun affected tests.
13. Obtain authorized approval before moving files into the approved folder.
14. Create manifest with exact filenames, dimensions, duration, frame rate, captions and approval status.

## 7. Expected artifacts
- one untouched approved master;
- three editable derivative sequences;
- three review/final exports;
- captions or transcript as specified;
- asset/rights log;
- delivery manifest and QC report.

## 8. Validation and tests
| Test | Method | Expected result | Actual result/evidence |
|---|---|---|---|
| Master preservation | Compare master project/version | Unchanged approved master | Learner records |
| Dimensions | Metadata inspection | Matches each format brief | Learner records |
| Framing | Full playback | Subject/action visible throughout | Learner records |
| Text | Phone/desktop preview | No clipping or obstruction | Learner records |
| Audio/captions | Full playback + transcript check | Sync and accuracy pass | Learner records |
| Naming | Compare manifest | Exact match | Learner records |
| Approval | Confirm authorized reviewer | Approved state recorded | Learner records |

## 9. Troubleshooting and rollback
If the wrong sequence is exported, stop batch delivery and inspect export queue mapping. If the master changed, restore the verified backup. If crops fail, reframe the individual shot rather than stretching footage. Keep failed review exports in a separate folder for traceability.

## 10. Performance, security and portability
Batch export can consume substantial CPU/GPU and storage. Avoid overwriting existing deliverables. Protect client media, limit access and use approved transfer methods. Document fonts, plugins and linked media needed to reopen the project.

## 11. Submission and handoff
Submit project package, three exports, captions, rights log, manifest, QC report and screenshots or metadata evidence where available.

## 12. Assessment rubric — 100 points
Master integrity 10; three format adaptations 25; visual/text composition 15; batch-export correctness 15; QC evidence 15; rights/privacy 10; manifest/handoff 10. Pass: 80/100; master preservation and rights are mandatory.

## 13. Lab quality checklist
- [ ] Application/version and environment recorded.
- [ ] Source assets and rights documented.
- [ ] Master remains unchanged.
- [ ] Three sequences are independently composed.
- [ ] Export queue/settings verified.
- [ ] Every output played and inspected.
- [ ] Manifest and approvals are complete.

## References and version notes
Use the selected editor's official current documentation for sequence settings, batch rendering and project packaging. This lab is software-neutral and does not claim execution or compatibility testing.
