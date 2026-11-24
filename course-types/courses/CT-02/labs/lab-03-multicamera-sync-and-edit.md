# CT-02 Lab 03 — Multicamera Synchronization, Drift Diagnosis and Editorial Assembly

- **Course/discipline:** CT-02 — Film & Cinematic Editing
- **Level:** Intermediate → Advanced
- **Estimated time:** 3–4 hours, excluding media capture or long-form review
- **Environment:** Any NLE or timeline system that can align multiple sources; a paper/timeline worksheet is an analysis-only alternative
- **Application/version:** Not prescribed. Record the exact application, edition, version, operating system and relevant media settings used for an executed submission.
- **Lab status:** Authored, tool-independent, not software-tested
- **Revision:** 2.0 — expanded to the professional lab template, 2026-11-24

> **Execution boundary:** This lab describes a reproducible workflow without assuming a particular application's menus, automatic-sync algorithm, multicamera implementation or export behavior. Those steps vary by product and version. A paper exercise or simulated dataset demonstrates reasoning only; it is not evidence that media was synchronized, edited, exported or reopened in an application.

## 1. Professional brief

A small production has recorded a short interview or dialogue scene with two cameras and a separate audio recorder. The editor must establish a reliable common timeline, detect any timing change across the recording, choose a defensible audio source, and create a short multicamera edit that serves the scene rather than switching angles for novelty.

**Deliverable:** a 60–90 second review edit, an editable synchronized source structure (or documented manual timeline), a source and rights inventory, a three-point synchronization report, an audio-routing note and a handoff record.

### Acceptance criteria

| Requirement | Acceptance evidence |
|---|---|
| Source identity | Every camera and recorder file has a stable ID linked to its original filename |
| Source safety | Originals remain unchanged; working copies/proxies and project versions are identified |
| Sync method | The chosen reference and its limitations are documented |
| Initial alignment | At least one shared event is aligned and independently checked |
| Drift diagnosis | Start, middle and end offsets are measured on a stated timebase |
| Correction decision | Fixed offset, drift, discontinuity or inconclusive evidence is distinguished; any correction is reversible and recorded |
| Audio | The intended dialogue source and channel layout are unambiguous; unwanted doubled audio is absent |
| Editorial result | Angle changes have a documented story, performance or continuity reason |
| Handoff | Project structure, dependencies, limitations and actual execution status are recorded |

Do not invent a broadcaster, client or platform specification. If a delivery specification is not supplied, submit a review copy only under a clearly labeled provisional specification.

## 2. Learning and implementation objectives

By the end of the lab, the learner will be able to:

1. Inventory at least two picture sources and one audio source, retaining original filenames and recording relevant metadata.
2. Select a synchronization method and explain why it is suitable for the available evidence.
3. Align sources to a common event without treating displayed timecode as proof of a shared clock.
4. Measure relative offset near the start, middle and end of a recording using a stated timebase and sign convention.
5. Distinguish a fixed offset from progressive drift, a recording discontinuity and an inconclusive measurement.
6. Calculate an approximate drift rate when the evidence supports that estimate.
7. Document a safe correction or explain why no correction should be attempted.
8. Establish an intentional audio strategy and create a 60–90 second angle edit that preserves performance, geography and chronology.
9. Submit a reproducible validation report and honest handoff record.

## 3. Prerequisites and setup

### Required prior knowledge

- CT-02 Lesson 06 — Multicamera Editing and Synchronization.
- Basic timeline and source-monitor concepts.
- Frame rate, timecode, audio sample rate and waveform terminology.
- Scene geography, screen direction, eyelines, dramatic beats and continuity.
- Non-destructive media management and version naming.

### Required inputs

- Two camera recordings of the same event, preferably with a shared slate, clap or distinct event.
- One separate audio recording where available.
- Production notes or a reliable description of the recording setup.
- Written authorization, license or learner-created source media.
- A project workspace with enough storage for the original media and working files.

### Environment record

Complete this before starting. Do not infer a value from a project preset.

| Field | Record |
|---|---|
| Operating system and version | |
| NLE / timeline tool, edition and version | |
| Hardware and available storage | |
| Project timebase / frame rate | |
| Source frame rates and whether constant or variable is known | |
| Audio sample rate / channel layout | |
| Proxy or optimized-media method, if used | |
| Media-information utility and version, if used | |
| Date and operator | |

**Alternatives:** If no NLE is available, complete the inventory, synchronization decision, measurement worksheet, angle-selection paper edit and QC plan. Mark the submission **paper-only / not executed**. Do not award execution, rendered-file or project-reopen evidence for a paper-only exercise.

## 4. Inputs, asset rights and privacy

Use original learner-created media or media whose license and consent cover the intended exercise. Record:

- source owner and permission basis;
- participant consent or release status where people are identifiable;
- music, archive or third-party asset restrictions;
- whether any source contains confidential, personal or sensitive information;
- whether cloud processing or third-party synchronization is permitted;
- retention and deletion requirements.

Do not upload identifiable or confidential footage to an external service merely to obtain automatic synchronization. If permission is uncertain, stop and use learner-created non-identifiable test footage or a clearly labeled simulated dataset. Preserve the original camera and recorder files; never overwrite them during alignment or correction.

## 5. Project architecture and naming

Create a project structure that separates source media, working media, editorial decisions and evidence. One suitable structure is:

- **01_SOURCE_ORIGINALS** — camera and recorder originals; read-only where practical.
- **02_WORKING_MEDIA** — verified copies, proxies or approved transcodes.
- **03_PROJECT** — native project and dated project versions.
- **04_SYNC_RECORDS** — source inventory, sync map, offset measurements and correction log.
- **05_REVIEW** — review exports and reviewer notes, each tied to a version.
- **06_DELIVERY** — only authorized final or review deliverables.
- **07_HANDOFF** — manifest, relink notes, rights summary and QC record.

Use stable IDs such as CAM-A-001, CAM-B-001 and AUD-REC-001. Preserve each original filename in the manifest. If a camera restarts and creates another file, assign a new segment ID (for example, CAM-B-002) and record the relationship to the preceding segment. Do not rename source media in a way that destroys its identity or production traceability.

## 6. Implementation procedure

### Phase A — Preflight and inventory

1. Confirm that the source media is authorized and that originals are protected.
2. Assign a stable source ID to every camera and recorder file.
3. Record device role, original filename, duration, reported frame rate, resolution, codec/container where known, audio sample rate/channel count, timecode basis and recording interruptions.
4. Identify the origin of every metadata value: file metadata, camera report, slate, operator note or assumption.
5. Mark unknown or conflicting values as **unknown / needs verification**.
6. Identify variable-frame-rate media, split recordings, missing ranges or other conditions that may invalidate a simple continuous-sync assumption.
7. Create a working project version before attempting alignment.

### Phase B — Choose a synchronization reference

Choose the strongest reference actually present in the recordings:

1. **Verified shared timecode:** use only when the timecode format, frame-rate basis and clock/jam-sync arrangement are known. Similar displayed time values alone do not establish a shared clock.
2. **Slate or clap:** locate the same visible event and audible transient. Confirm that the visual and audio event correspond to the same physical action.
3. **Common waveform:** compare a distinct sound captured by the relevant sources. Continuous ambience, music or different microphone perspectives may create ambiguous matches.
4. **Shared visual event:** use a clearly identifiable action visible in multiple cameras. Confirm that the chosen frame represents the same event and account for differing capture rates.
5. **Manual estimate:** if no reliable shared reference exists, record the estimate, uncertainty and reason. Do not report frame-accurate synchronization.

Record the method, reference event, source pair, evidence location and known limitation. Automatic synchronization may suggest an alignment, but the learner must independently verify it.

### Phase C — Establish initial alignment

1. Select a common anchor near the beginning of the shared recording.
2. Align the sources using the chosen reference in the selected application or on a manual timeline.
3. Confirm the visual action and audible transient, not only a waveform peak or timecode display.
4. Label every angle by stable camera ID and editorial role.
5. Identify which audio channels are production dialogue, camera scratch/reference audio, ambience or other sources.
6. Save a new project version and record the alignment decision.
7. Keep unused source audio available until the master-audio decision is verified.

The exact grouping, multicamera-source creation, track locking and angle-labeling controls depend on the chosen NLE/version. Translate the concepts into the selected application only after consulting its current official documentation.

### Phase D — Verify synchronization at three or more points

Use the same identifiable event in each source at:

- **Start:** near the first usable shared event.
- **Middle:** near the midpoint of the overlapping recording.
- **End:** near the final usable shared event.

For each checkpoint, record the event identity, elapsed time from the chosen origin, the observed time in each source and the relative offset.

Use this sign convention:

**Relative offset = time of the event in Source B − time of the same event in Source A.**

- A positive value means the event appears later in Source B.
- A negative value means the event appears earlier in Source B.
- Zero means aligned within the measurement precision used.

Express offsets in milliseconds when source frame rates or timebases differ. If both sources share the same verified frame rate and timebase, frames may also be recorded. State the measurement precision; do not imply sub-frame accuracy from a frame-only inspection.

### Phase E — Classify the timing behavior

| Observation | Likely classification | Required next action |
|---|---|---|
| Offset remains approximately constant at all checkpoints | Fixed offset | Verify the anchor and consider a documented non-destructive slip |
| Offset changes progressively across the recording | Drift | Investigate clock/timebase, frame-rate interpretation, variable frame rate and sample-rate handling |
| Offset changes suddenly after a stop/restart or file boundary | Discontinuity | Treat each continuous recording segment as a separate sync unit |
| Measurements fluctuate without a stable pattern | Inconclusive / possible bad reference or media issue | Add checkpoints, verify event identity and inspect for dropped or duplicated frames |

A single global slip corrects a constant offset; it does not correct a changing offset. Do not apply a speed change, resampling operation or time-stretch merely because the end is out of sync. First identify the cause and confirm that the proposed operation is appropriate for the source, project timebase and intended picture/audio behavior.

### Phase F — Calculate an approximate drift rate

When the measurements support a progressive change, estimate:

- **Drift change:** end relative offset minus start relative offset.
- **Elapsed interval:** elapsed time between the start and end checkpoints.
- **Drift rate:** drift change divided by elapsed interval.
- **Parts per million (ppm):** drift rate multiplied by 1,000,000.

Use seconds for the calculation. If frame counts are used, convert them using the verified timebase. Do not compare raw frame counts from different frame rates as if they represented equal durations.

A three-point estimate is a diagnostic aid, not proof that drift is perfectly linear. Add intermediate checkpoints when the recording is long, contains restarts or shows non-linear behavior.

### Phase G — Decide and verify a correction

1. Record the observed condition and the evidence supporting the diagnosis.
2. Duplicate or version the synchronized structure before changing it.
3. For a fixed offset, document the amount and direction of any slip.
4. For drift, investigate source interpretation and recording behavior before choosing a correction. If a recording restart is involved, consider separate segments rather than stretching one continuous file.
5. If a rate or duration adjustment is justified, document the method, exact source/segment, before/after values and expected effect on motion, pitch and duration.
6. Preserve originals and retain the pre-correction project version.
7. Recheck the same start, middle and end anchors after correction, plus at least one additional event near any suspected discontinuity.
8. If the result remains uncertain, mark it **not verified** and escalate or request a better reference instead of hiding the discrepancy.

### Phase H — Establish the audio strategy

1. Listen to each available audio source independently.
2. Compare intelligibility, noise, distortion, clipping, channel identity, room tone and consistency.
3. Select the intended dialogue/master source based on evidence and the brief; do not assume the external recorder is automatically best.
4. Retain camera scratch audio for synchronization or reference if useful, then prevent unintended duplicate playback.
5. Check channel routing and listen for echo, comb filtering, phase problems, missing channels and abrupt ambience changes.
6. Preserve required isolated tracks or production audio according to the brief.
7. Record which source is used for dialogue, ambience and any other required element.

### Phase I — Build the editorial sequence

1. Identify the dramatic beats or information changes in the selected scene.
2. Make a short paper edit or angle plan before switching angles.
3. Start from the wide/master when it is needed to establish geography or preserve continuous action.
4. Select close-ups for meaningful performance, information or emotional emphasis.
5. Use reaction shots only when their chronology and source context support the implied response.
6. Preserve eyelines, screen direction, action continuity and the audience's understanding of who is speaking.
7. Keep the chosen dialogue/master audio continuous across picture changes unless the brief requires a motivated audio edit.
8. Review angle changes at normal speed with sound; do not rely only on a static frame or isolated waveform.
9. Create a 60–90 second review edit and save a new version with a clear identifier.

### Phase J — Validate and hand off

1. Recheck synchronization at the beginning, middle and end of every continuous source segment used.
2. Inspect dialogue and picture at each angle change.
3. Confirm that camera labels, audio routing and source references are consistent.
4. Confirm that the project opens with media online in the current environment.
5. If portability is claimed, copy the project and required dependencies to a separate test location and attempt a reopen there. Record the actual result; a manifest alone is not a portability test.
6. Export only when a written or clearly provisional review specification exists.
7. If an export is created, inspect the actual rendered file independently. A successful export dialog is not a full QC pass.
8. Complete the sync report, correction log, project manifest and limitation statement.

## 7. Worked example — fictional three-point drift diagnosis

The following data are simulated teaching values. They are not measurements from real footage.

**Assumptions:** Camera A and Camera B report the same verified 25 fps timebase. The recording lasts 24 minutes. The same clap is identifiable in both sources at each checkpoint. Positive offset means Camera B is later than Camera A.

| Checkpoint | Elapsed time | Relative offset | Equivalent time |
|---|---:|---:|---:|
| Start | 0 s | 0 frames | 0.000 s |
| Middle | 720 s | +2 frames | +0.080 s |
| End | 1,440 s | +6 frames | +0.240 s |

At 25 frames per second, one frame represents 0.04 seconds. The measured relative offset has changed by 0.24 seconds over 1,440 seconds.

Approximate drift rate:

- 0.24 ÷ 1,440 = 0.0001667 seconds per second.
- 0.0001667 × 1,000,000 ≈ **167 ppm**.

**Interpretation:** The data suggest progressive drift rather than a single fixed offset. The midpoint is important: it shows that the discrepancy is already changing before the end. The estimate does not establish the exact cause or prescribe a universal correction. The learner should inspect additional shared events, confirm the timebase and determine whether a restart or media interpretation issue exists.

**Separate fixed-offset example:** An external recorder is consistently 1 frame later than Camera A at all three checkpoints on the same 25 fps timebase. That is a constant 0.04-second offset within the stated measurement precision. A documented slip may be appropriate after verifying the reference and audio behavior.

**Editorial example:** The editor keeps the wide master for the opening geography, cuts to the speaking subject when the key information changes, holds the listener only when the reaction is chronologically supported, and returns to the master for the shared action. The dialogue master remains continuous. The angle plan explains each change; it does not use a new angle merely because one is available.

**Expected artifacts:** a source inventory, three-point measurement table, drift classification and calculation, audio-routing decision, 60–90 second edit or paper edit, validation record and handoff manifest.

## 8. Dry run — annotated decision walkthrough

1. **Inventory:** CAM-A-001, CAM-B-001 and AUD-REC-001 are listed with original filenames. Frame-rate and sample-rate values are marked as reported or verified.
2. **Anchor:** a slate/clap near the start is identified in both cameras and the recorder. The method and evidence location are recorded.
3. **Initial alignment:** the sources are aligned to the shared event. The project is saved as a new version.
4. **Middle check:** the same event is measured again. The offset is recorded using the declared sign convention.
5. **End check:** the final shared event is measured. The learner compares all three values and classifies the result.
6. **Correction gate:** if the offset is constant, a slip may be tested. If it changes, the learner investigates drift or discontinuity. No correction is applied solely to make the table look consistent.
7. **Editorial and handoff:** the learner chooses a master-audio source, builds the angle sequence, repeats the sync checks and records whether the project was actually reopened or exported.

For each step, retain the input, decision, evidence, expected result and actual result. If the exercise uses simulated values, label the entire walkthrough as simulated.

## 9. Guided practice

### Exercise A — Slate/clap alignment

Use two learner-created or authorized camera recordings and one audio recording of the same clap.

- Inventory all three sources.
- Identify the common event in each source.
- Record the initial alignment and measurement precision.
- Verify another shared event later in the recording.
- Submit the source table and a short explanation of the sync method's limitations.

**Instructor guidance:** Full credit requires matching the same physical event and recording evidence from each source. A guessed alignment or a timecode-only claim is insufficient.

### Exercise B — Offset, drift or discontinuity?

Classify each simulated dataset and state the next diagnostic action.

| Dataset | Start | Middle | End | Expected classification |
|---|---:|---:|---:|---|
| A | +3 frames | +3 frames | +3 frames | Fixed offset |
| B | 0 frames | +2 frames | +6 frames | Progressive drift |
| C | 0 frames | 0 frames | +8 frames after restart | Possible discontinuity; inspect segment boundary |
| D | +1 frame | +5 frames | +2 frames | Inconclusive or bad reference; add checkpoints |

**Instructor guidance:** The classification is based on the pattern, not a memorized threshold. Learners must state the timebase and investigate the event identity before recommending correction.

### Exercise C — Editorial angle selection

Create a 60-second angle plan from a short conversation. For every picture change, record:

- source and source range;
- dramatic or informational purpose;
- performance/eyeline/geography check;
- audio source during the cut;
- chronology or factual-integrity concern.

**Instructor guidance:** A continuous master shot may be preferable to unnecessary cutting. Angle count is not a quality measure.

## 10. Independent assignment — multicamera interview package

Prepare a synchronized interview or dialogue scene using at least two picture sources and one separate audio source. Aim for a 60–90 second edit.

Submit:

1. Rights/consent and source inventory.
2. Environment and media-property record.
3. Synchronization-method decision with limitations.
4. Start/middle/end offset table for each continuous source segment.
5. Fixed-offset/drift/discontinuity diagnosis and calculation where appropriate.
6. Correction and retest log, or a reasoned no-correction decision.
7. Audio-routing and master-source decision.
8. Angle-selection plan tied to beats, performance and geography.
9. Review edit or paper edit, labeled accurately.
10. QC report, project manifest and 300–500 word reflection.

**Constraint:** If only simulated data are available, label the submission simulated. It may earn reasoning credit but not executed-sync, edit, export or portability credit.

## 11. Troubleshooting and rollback

| Symptom | Likely causes | Diagnostic and safe recovery |
|---|---|---|
| All sources are displaced by a similar amount | Fixed offset or wrong anchor | Reconfirm the shared event, sign convention and source pair; test a documented slip in a new version |
| Sync is correct at the start but wrong at the end | Clock drift, frame/timebase mismatch or variable-frame-rate interpretation | Add checkpoints, inspect source properties and production records; do not rely on a global offset |
| Sync changes after a camera restart | New recording segment or discontinuity | Treat each file/segment independently and locate a new shared event |
| Waveform matching produces several possible alignments | Repeating music, ambience, echo or different microphone perspectives | Prefer a distinct slate/clap or verified visual event; record uncertainty |
| Audio sounds doubled or hollow | Multiple camera microphones or duplicate tracks are active | Solo each source, identify the intended master and verify routing |
| Picture changes break eyelines or screen direction | Angle labels or geography assumptions are wrong | Recheck the scene diagram and source roles; revise the angle plan |
| One source appears to change speed or cadence | Frame-rate interpretation, variable-frame-rate media or conversion | Inspect source metadata and test a working copy; preserve originals |
| Media goes offline after moving the project | Absolute paths or missing dependencies | Restore the documented folder structure, relink from the manifest and record the portability result |
| A correction improves one checkpoint but worsens another | Wrong diagnosis or non-linear timing change | Roll back to the pre-correction version, add measurements and seek a reliable reference |

**Rollback rule:** Never overwrite the source or the last known-good project. Preserve the pre-correction version, record the failed attempt and return to the last verified state before testing another method.

## 12. Validation and tests

Complete the table using actual evidence. The expected results are acceptance criteria, not claims that a test has already passed.

| Test | Method | Expected result | Actual result / evidence |
|---|---|---|---|
| Source identity | Compare manifest with media folder | Every used source maps to an original filename | |
| Rights and consent | Review authorization records | All used sources are permitted for the exercise | |
| Sync anchor | Inspect the shared event in each source | Same event is identified and aligned within stated precision | |
| Start/middle/end | Measure all checkpoints | Offset pattern is documented and classified | |
| Segment boundaries | Inspect restarts and file splits | Each continuous segment has a valid sync basis | |
| Audio routing | Solo and listen to intended channels | Dialogue source is clear; no unintended duplicate audio | |
| Editorial continuity | Watch the edit at normal speed | Angle changes preserve understandable geography and chronology | |
| Project reopen | Close and reopen the project in the same environment | Sources and sync structure remain available | |
| Portability | Reopen from a separate location, if claimed | Dependencies resolve or missing items are documented | |
| Render inspection | Play the actual review file, if exported | Full file and properties meet the stated review specification | |

Record each result as Pass, Fail, Not Applicable or Not Tested. A blank cell is not a pass.

## 13. Performance, security and portability

- Use proxies or optimized media only when required by the available hardware or source format. Record the relationship to originals and verify that the final project points to the intended media.
- Keep source originals and project versions separate from temporary render/cache folders.
- Do not delete camera scratch audio until synchronization and master-audio decisions are verified.
- Avoid uploading confidential or identifiable media to cloud services without explicit authorization.
- Limit project access to authorized collaborators; do not place passwords, private review links or tokens in the handoff.
- Record plugins, fonts, LUTs, external audio, proxies and other dependencies that may be needed to reopen the project.
- Do not claim a portable project until a separate-location reopen has been attempted and evidenced.

## 14. Submission and handoff

Submit the following in a clearly named package:

- source manifest and rights/consent status;
- environment/version record;
- synchronization method and measurement table;
- drift calculation and correction/retest log, if applicable;
- angle and audio decision notes;
- project file and required dependencies, where an application edit was executed;
- review file and its provisional or approved specification, where exported;
- QC and defect record;
- version/change log;
- limitation statement distinguishing executed, simulated, paper-only and not-tested work.

The recipient must be able to identify the exact project version, media dependencies, intended audio, synchronization method, known limitations and approval status.

## 15. Assessment rubric — 100 points

| Criterion | Points | Observable evidence |
|---|---:|---|
| Source inventory and rights | 10 | Stable IDs, original names, metadata source and authorization record |
| Sync-method selection | 15 | Method fits the available evidence; limitations are explicit |
| Three-point verification and drift reasoning | 20 | Start/middle/end checks, sign convention, timebase and correct classification/calculation |
| Correction safety and retest | 15 | Non-destructive versioning, justified correction or justified no-change decision, retest evidence |
| Audio strategy | 10 | Master-source choice, channel identity and duplicate-audio check |
| Editorial angle decisions | 15 | Beat/performance rationale, geography, eyelines and chronology |
| Handoff and QC | 15 | Reproducible records, project dependencies and honest validation status |
| **Total** | **100** | |

**Pass threshold:** 70/100, with all critical gates satisfied. A paper-only or simulated submission cannot earn points for an executed edit, actual media synchronization, export inspection or project portability.

**Critical failure conditions:** unauthorized media use; destructive alteration or loss of originals; fabricated synchronization measurements or execution evidence; knowingly false QC or technical claims; or an edit that materially misrepresents a factual event. Critical failures require remediation regardless of numeric score.

## 16. Lab quality checklist

- [ ] Environment, application and version recorded, or explicitly marked not applicable for a paper exercise.
- [ ] Source files, original filenames, rights and consent documented.
- [ ] Source originals preserved.
- [ ] Sync method and reference event identified.
- [ ] Timebase and offset sign convention stated.
- [ ] Start, middle and end measured for each continuous segment.
- [ ] Fixed offset, drift, discontinuity or inconclusive result classified with evidence.
- [ ] Any correction documented, versioned and retested.
- [ ] Intended audio source and channel routing verified.
- [ ] Editorial angle changes serve performance, story and geography.
- [ ] Actual tests are distinguished from simulated or not-tested items.
- [ ] Project dependencies, limitations and handoff status documented.
- [ ] Actual review export inspected if an export is claimed.

## 17. References and version notes

### Internal learning references

- [CT-02 Lesson 06 — Multicamera Editing and Synchronization](../lessons/lesson-06-multicamera-editing-and-synchronization.md)
- [CT-02 Textbook — Chapter 7: Multicamera Synchronization and Scene Management](../CT-02-FILM-CINEMATIC-EDITING-TEXTBOOK.md)
- [CT-02 Student Workbook — Section 9: Multicamera Sync Record](../CT-02-STUDENT-NOTES-WORKBOOK.md#9-multicamera-sync-record)
- [CT-02 Knowledge Assessment and Answer Guidance](../assessment-quiz-and-answer-key.md)
- [PCMDK369 Professional Lab Template](../../../../templates/professional-lab-template.md)
- [PCMDK369 Professional Academic Standard](../../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md)

### Version and compatibility notes

- Revision 2.0, 2026-11-24: expanded the original lab in place to the professional lab template; added a measurable brief, environment record, rights and privacy controls, project architecture, sync decision procedure, sign convention, drift calculation, worked example, annotated dry run, guided and independent practice, validation tests, rollback, portability, 100-point rubric and handoff requirements.
- The lab remains tool-independent. No NLE, operating system, multicamera sync feature, automatic waveform algorithm, time-stretch process or export setting is asserted as tested.
- Application menu names and behavior must be verified against the exact product, edition and version selected by the learner. Consult that product's current official documentation before publishing a software-specific walkthrough.
- All example source IDs, offsets, frame rates, elapsed times and results are simulated teaching data. No real media was synchronized, edited, rendered, exported or independently reviewed for this revision.
