# CT-02 Lab 04 — Picture Lock, Finishing Handoff and Quality Control

**Level:** Advanced → Professional Practice  
**Estimated time:** 2–4 hours  
**Software:** NLE plus media player capable of inspecting the rendered file; optional audio meter and file metadata inspector.  
**Output:** Approved short scene export, handoff package and completed QC report.  
**Revision:** 2.0 — 2026-11-25.  
**Status:** Authored; tool-independent; not executed or software-tested.

## Learning outcomes
The learner can prepare a fine cut for review, document picture lock, create a controlled finishing handoff, export to a stated specification and inspect the actual delivered file.

## Prerequisites and materials
- CT-02 Labs 01–03 or equivalent experience.
- A completed 1–3 minute scene.
- Written delivery specification. If none is supplied, the learner must create and label a clearly provisional specification rather than claiming it is an industry standard.
- Rights/consent records for all media.

## Concepts
**Picture lock** is formal approval of picture timing for downstream finishing. **Conform** reconnects or rebuilds the approved edit from intended sources. **Quality control (QC)** is a documented check that the delivered file meets creative, technical and contractual requirements.

## Procedure

### A. Prepare for picture lock
1. Save a new fine-cut version.
2. Review the full scene at normal speed.
3. Check story completeness, performance, continuity, screen direction and pacing.
4. Confirm titles, credits, subtitles and graphic placeholders are resolved or clearly marked.
5. Record all outstanding issues and their owners.
6. Obtain documented approval from the responsible reviewer or mark the sequence as learner-approved for the exercise.

### B. Freeze and document the approved edit
1. Duplicate or tag the approved sequence as `PICTURE_LOCK`.
2. Record sequence frame rate, frame size, duration, audio layout and version ID.
3. Export or save an edit decision/reference record if the NLE supports it.
4. Store the locked version as read-only or protect it using the production's version-control method.
5. Any later picture change must have a change request with timecode, reason, approval and downstream impact.

### C. Prepare the handoff
Include only authorized materials:
- approved picture-locked project or interchange file where supported;
- media inventory and relink instructions;
- source and proxy relationship notes;
- title/graphics assets;
- music and footage license records;
- version/change log;
- delivery specification;
- unresolved issue list, if any.

Do not assume the recipient has access to your local drives or cloud accounts.

### D. Export
1. Confirm the requested container, codec, frame size, frame rate, scan type, audio channels, sample rate and any loudness/peak requirement.
2. Verify color space and transfer characteristics against the brief and workflow.
3. Choose an export preset only after checking its actual settings.
4. Export to a new delivery folder; never overwrite the approved master without authorization.
5. Record export filename, software/version, date, duration and relevant settings.

### E. Inspect the actual delivered file
1. Confirm the file exists and its size is plausible.
2. Open it in a separate media player.
3. Watch the complete file from beginning to end.
4. Check first and last frames, black gaps, flash frames, missing shots, freeze frames and unintended overlays.
5. Listen to the complete audio, checking dialogue intelligibility, missing channels, clipping, sync, abrupt cuts and unintended silence.
6. Inspect titles, spelling, captions, credits and safe placement.
7. Compare file properties with the written delivery specification.
8. Record each result as Pass, Fail or Not Applicable.
9. Correct failures, re-export to a new version and repeat the full QC pass.

## Worked example
The delivery brief requests a 1920×1080 progressive file at a specified frame rate with stereo audio. The export preset is named “1080p master,” but its audio is mono. The preset name is not proof of compliance: inspect actual metadata, correct the channel mapping, export a new version and recheck the delivered file.

## QC checklist

| Check | Result (Pass/Fail/N/A) | Evidence/notes |
|---|---|---|
| Correct version and filename | | |
| Correct duration and frame rate | | |
| Correct frame size and scan type | | |
| Correct codec/container | | |
| Correct audio channel layout | | |
| Dialogue sync and intelligibility | | |
| No unintended black/frozen/flash frames | | |
| No missing media or offline graphics | | |
| Titles/captions/credits checked | | |
| Rights and consent records present | | |
| Complete file played from start to end | | |
| Handoff files and relink notes included | | |

## Troubleshooting
| Failure | Likely cause | Response |
|---|---|---|
| Export has wrong dimensions | Sequence or export scaling | Compare sequence and export settings with brief |
| Audio channel mismatch | Incorrect routing or preset | Inspect track routing and rendered metadata |
| Missing titles/media | Unavailable assets or broken links | Relink authorized assets and export a new version |
| Picture differs from approved cut | Wrong sequence/version exported | Reconfirm version ID and export from locked sequence |
| File plays only partly | Incomplete render or storage issue | Check render completion and available storage; render a new version |

## Submission evidence
- Picture-lock approval record or learner approval statement.
- Version/change log.
- Delivery specification.
- Handoff folder inventory.
- Final export.
- Completed QC checklist with evidence.
- Reflection describing one defect found during QC and how it was corrected.

## Assessment — 30 points
- Picture-lock discipline: 6
- Handoff completeness: 6
- Export specification accuracy: 6
- Full-file QC and evidence: 8
- Rights/version documentation: 4

**Pass:** 21/30. Any uncorrected rights violation, missing source preservation or knowingly misrepresented technical compliance is a critical failure.

## Quality gate
The exported file—not merely the timeline—has been fully reviewed; actual file properties match the brief; the approved sequence is identifiable; handoff assets are traceable; rights and version records are present.


---

## Revision 2.0 — Professional lab expansion

**Revision date:** 2026-11-25  
**Lab status:** Authored; tool-independent; not executed or software-tested.  
**Environment rule:** Record the exact operating system, NLE edition/version, media-player version and any inspection-tool version used by the learner. No application-specific menu names, buttons, codec defaults or command flags are prescribed here because no exact application/version combination has been tested for this revision.  
**Evidence rule:** The worked example and dry run below are fictional. A paper-only submission may demonstrate planning and reasoning, but cannot receive credit for an executed export, full playback, metadata inspection, transfer or restore test.

### 1. Professional brief

You are the finishing editor receiving an approved short narrative scene from editorial. Prepare a traceable handoff, verify the approved picture state, complete specification-led finishing checks, export a delivery candidate and determine whether the actual rendered file is acceptable.

The production supplies a written delivery specification. It may be a client document, broadcaster/platform specification, festival requirement or an instructor-created exercise brief. The specification is authoritative for this exercise. Do not substitute a preset name, habit or assumed industry convention for a missing requirement.

**Acceptance criteria**

1. The exact approved sequence and version are identifiable.
2. Every post-lock change has an authorized change record and downstream impact assessment.
3. Source media, graphics, captions, audio and rights records are traceable.
4. The conform is compared with the approved reference and discrepancies are resolved or formally accepted.
5. Export settings are mapped to the written specification before rendering.
6. The actual delivered file—not only the timeline or export dialog—is inspected.
7. Required picture, sound, graphics, caption, accessibility and metadata checks have recorded results.
8. Defects are corrected in a new version and the corrected file is retested.
9. The handoff identifies dependencies, restrictions, version, recipient and unresolved limitations.

**Out of scope:** This lab does not establish legal compliance, guarantee acceptance by a particular platform, prescribe universal loudness or codec values, or certify a specific NLE. Contractual and distribution requirements must be checked against the current authoritative brief.

### 2. Learning and implementation objectives

By the end of the lab, the learner can:

- Convert a written delivery brief into a field-by-field specification matrix with a verification method for every requirement.
- Identify the exact picture-lock version, approval authority, sequence timebase and duration.
- Create a controlled change request and identify at least four downstream consequences of a post-lock picture change.
- Reconcile the locked edit against intended source media and document conform discrepancies.
- Separate editorial, picture, audio, graphics/captions, accessibility, technical and delivery QC passes.
- Inspect a rendered file independently and record metadata and full-duration playback evidence.
- Classify defects by impact, assign an owner, correct them non-destructively and record regression tests.
- Produce a handoff manifest that distinguishes present, missing, restricted, simulated and unverified items.

**Success threshold:** At least 80/100 on the revision 2.0 rubric, with all critical rights, source-preservation, version-identity and evidence-integrity gates passed.

### 3. Prerequisites and setup

**Required knowledge**

- CT-02 Lessons 07 and 08, or equivalent knowledge of fine-cut approval, picture lock, finishing and QC.
- CT-02 Labs 01–03 or equivalent scene, continuity and multicamera preparation.
- Basic understanding of frame rate/timebase, image dimensions, audio channels, containers, codecs and project dependencies.
- Ability to distinguish an editorial approval from technical delivery acceptance.

**Required inputs**

- A completed 1–3 minute scene or a clearly labeled paper-only scenario.
- A written delivery specification with explicit values or tolerances.
- The approved reference export or another agreed reference for comparison.
- The editable project and a source/media inventory.
- Rights, consent, music, font, stock, graphics and participant records as applicable.

**Tools and alternatives**

| Tool or resource | Purpose | Alternative / limitation |
|---|---|---|
| NLE | Reopen the approved sequence, conform and export | A paper edit plan can demonstrate reasoning but not execution |
| Independent media player | Review the rendered artifact | A second independent playback path is preferable; a timeline preview is not equivalent |
| File-property or metadata inspector | Compare actual file properties with the brief | A trusted platform report may help; record the method and version |
| Audio meter or analyzer | Measure specified audio properties | Listening is essential but cannot replace a required objective measurement |
| Caption validator or text editor | Inspect caption timing, syntax and language | Manual review is useful but does not establish format conformance by itself |
| Checksum utility | Compare file identity after copying | A checksum does not prove creative quality, codec compliance or successful playback |
| Storage with controlled access | Preserve project and delivery evidence | Use an approved local or managed destination with a documented backup |

Record versions for every application or utility actually used. If a tool is unavailable, mark its test Not Run; do not infer a pass.

### 4. Inputs and asset rights

Create an inventory before opening or moving media.

| Input class | Required record | Hold condition |
|---|---|---|
| Picture sources | Source ID, owner, format, frame rate/timebase, duration, proxy/original relationship | Unknown source identity or unauthorized use |
| Approved sequence | Sequence ID, version, approval authority/date, timebase, duration | No identifiable approved version |
| Audio | Dialogue, production sound, effects, music, channel layout and rights | Missing license, consent or channel provenance |
| Graphics and fonts | File/version, creator, license, linked dependencies | Unlicensed or unavailable dependency |
| Captions/subtitles | Language, format, source transcript, version and timing basis | Unverified language, timing or permitted use |
| LUTs/plugins/templates | Name, version, license, location and compatibility | Missing or unauthorized dependency |
| Delivery specification | Issuer, revision/date, territory/platform, required fields and tolerances | Contradictory or incomplete requirements |
| Personal/confidential data | Data category, purpose, access and retention restriction | Unapproved disclosure or cloud processing |

Preserve camera originals and prior approved project versions. Never remove source files merely because a proxy or export exists. Do not upload confidential or personal media to an external service unless the owner has authorized that processing and the service's current terms and controls have been reviewed.

### 5. Architecture and project structure

Use a structure that separates the approved project, working outputs, final candidates and evidence. Adapt names to the studio's naming policy without losing the same distinctions.

| Folder | Contents |
|---|---|
| 00_brief-and-spec | Approved brief, specification revision, acceptance matrix |
| 01_picture-lock | Locked sequence reference, approval, lock/change log |
| 02_project | Editable project and required interchange files |
| 03_media-inventory | Source list, proxy/original mapping, relink notes |
| 04_finishing-assets | Authorized graphics, fonts, LUTs, audio and captions |
| 05_exports/review | Clearly labeled review candidates; never confuse with master |
| 05_exports/master | Approved delivery candidates with unique version IDs |
| 06_qc | Metadata reports, playback records, defect log and retest evidence |
| 07_handoff | Manifest, rights summary, recipient instructions and transfer receipt |
| 08_archive | Approved archive copy and retention/restore record |

**Naming principle:** Every export must carry a unique project/sequence identifier, version, date or controlled revision, and variant/language where relevant. A filename is a label, not proof of the file's contents. Verify the file itself.

**Data flow**

Brief and source inventory → approved picture-lock reference → conform/finishing → export candidate → independent inspection → defect correction and new candidate → approval → authorized handoff/archive.

Do not copy an unapproved review export into the master folder and rename it as final.

### 6. Implementation procedure

#### Phase A — Normalize the specification

1. Identify the specification issuer, revision, date, delivery purpose and recipient.
2. Extract every required field: container, video codec, dimensions, frame rate as an exact rate where specified, scan mode, duration/tolerance, color properties, audio codec/sample rate/channel layout, loudness or peak limits if specified, caption format/language, naming, file-size limits and transfer method.
3. For each field, record the exact requirement, allowed tolerance, verification method and responsible person.
4. Separate mandatory values from recommendations and optional preferences.
5. Raise contradictions or missing fields before export. Record the response and the specification revision that resolves them.
6. If no external specification exists, create a provisional exercise specification and label it as such. Do not call it a platform or industry standard.

#### Phase B — Establish the lock state

1. Save a new working version without changing the previously approved version.
2. Confirm the sequence identifier, edit version, frame rate/timebase, dimensions, audio layout and runtime.
3. Review the full scene at normal speed for story, performance, continuity, pacing, titles and unresolved placeholders.
4. Record all open issues with severity, owner and disposition.
5. Obtain approval from the person authorized by the brief. In a self-directed exercise, record “learner approval for exercise” rather than inventing a client or director sign-off.
6. Mark the exact approved version as the finishing reference. Protect it using the available project/version-control method.
7. Record the lock date, approver, version ID and reference location.

Picture lock is a controlled approval state, not a claim that no future change can occur. A later change requires authorization, a new version and impact review.

#### Phase C — Control post-lock changes

For each requested change, record:

- request ID, requester and date;
- exact sequence/version and timecode or frame range;
- reason and intended result;
- source/graphic/audio/caption changes;
- approval authority and decision;
- effects on conform, sound mix, music, VFX, color, captions, credits, runtime, derivatives and delivery date;
- regression checks required after the change.

Do not silently change the locked sequence. If approval is unavailable, hold the change and preserve the approved version.

#### Phase D — Conform and turnover

1. Open a working copy of the approved project or the agreed interchange.
2. Reconcile source IDs, reel/clip names, original/proxy mapping and media paths against the inventory.
3. Confirm the project timebase and sequence settings against the approved reference.
4. Check edit points, handles, speed changes, reframing, transitions, effects and nested sequences.
5. Inspect offline media, missing fonts, graphics, LUTs, plugins and linked audio.
6. Compare the conform with the approved reference at the beginning, middle, end and every known high-risk edit or effect.
7. Record each discrepancy; do not repair a creative difference without authorization.
8. Resolve, escalate or formally accept each discrepancy before mastering.

#### Phase E — Complete independent finishing passes

Use separate passes so that one type of inspection does not conceal another.

| Pass | Inspect | Evidence |
|---|---|---|
| Editorial | Correct version, shot order, gaps, duplicate frames/shots, runtime and approved changes | Version and edit review log |
| Picture | Focus, exposure, color continuity, scaling, crop, aspect ratio, graphics and image artifacts | Picture QC record and timecodes |
| Audio | Dialogue intelligibility, sync, channel mapping, clipping/distortion, unwanted silence, transitions and required measurements | Listening record plus meter/report where required |
| Titles/graphics | Spelling, names, dates, logos, safe placement, animation and correct version | Graphics checklist |
| Captions/subtitles | Language, accuracy, speaker identification where required, timing, reading order, formatting and safe placement | Caption review/validation record |
| Accessibility | Required caption, subtitle, audio-description or other accessible deliverables from the brief | Accessibility requirements matrix |
| Rights/privacy | Music, footage, fonts, stock, participant permissions, personal data and disclosure restrictions | Rights and consent register |
| Technical | Actual dimensions, rate, codec/container, duration, audio streams, color metadata and file integrity | Metadata report and specification matrix |
| Delivery | Naming, folder structure, manifest, permissions, transfer and recipient instructions | Handoff and transfer record |

A subjective listening or viewing pass does not replace a specified measurement. A metadata report does not prove that a file plays correctly.

#### Phase F — Prepare and perform export

1. Confirm that the export source is the approved/authorized sequence version.
2. Map each export setting to a requirement in the specification matrix.
3. Inspect actual settings rather than trusting a preset label.
4. Confirm output location, filename, available storage and non-overwrite behavior.
5. Export a new candidate with a unique version identity.
6. Record application/version, export date/time, sequence ID, output name, relevant settings and any warnings.
7. Wait for the application to report completion and confirm the output exists. An apparently closed dialog is not sufficient evidence.
8. Preserve the candidate; do not replace the prior approved delivery file.

#### Phase G — Inspect the actual rendered artifact

1. Verify the file exists and its size is plausible for the expected content.
2. Inspect actual container and stream properties against the specification.
3. Open the file in a separate playback application or independent review path.
4. Watch the complete file from first frame to last frame.
5. Check black gaps, flash frames, freezes, missing shots, unintended overlays, scaling/crop errors and first/last frame integrity.
6. Listen to the complete audio and inspect each required channel; check sync, intelligibility, clipping, missing or duplicated channels, abrupt edits and unintended silence.
7. Review captions, titles, credits, spelling, language, timing and placement against the final picture.
8. Confirm the actual runtime, dimensions, frame rate, codec/container, audio layout and other required metadata.
9. Record Pass, Fail, Not Run or Not Applicable with evidence. Explain every Not Applicable result.
10. If playback or inspection is interrupted, record the incomplete range. Do not mark full-file QC as passed.

#### Phase H — Classify defects, correct and retest

Use impact and the written acceptance criteria, not personal preference alone.

- **Critical:** rights/consent breach, wrong or untraceable master, corrupted/unreadable delivery, destructive source loss, materially false claim or a defect that makes the deliverable unusable or unsafe. Hold delivery.
- **Major:** failure of a required specification, missing/incorrect audio channel, material sync error, missing required caption/language, wrong runtime/version, missing essential shot or substantial picture defect. Correct and rerun affected plus regression checks before acceptance.
- **Minor:** limited defect that does not prevent the intended use but still violates a stated requirement or quality expectation. Record owner and disposition; obtain approval for any accepted exception.
- **Observation:** non-blocking suggestion or preference that is not a requirement. Keep it separate from a failed test.

For every defect record an ID, severity, version, time/frame or file property, requirement, observed result, likely cause, owner, correction, retest result and approval/exception. Export corrections to a new version. Recheck all affected requirements and nearby content; then repeat full playback when picture/audio content has changed or when the acceptance plan requires it.

#### Phase I — Package, transfer and archive

1. Create a manifest listing each deliverable, version, file name, size, role, rights/restrictions and location.
2. Include project/interchange files, required media or relink instructions, graphics, fonts, LUTs, audio, captions, licenses, change log, delivery specification and QC report as authorized.
3. State dependencies that cannot be transferred, such as licensed plugins or restricted source media.
4. If a checksum is used, record algorithm, tool/version, file identity and when it was calculated. A matching checksum indicates bit-for-bit identity for the checked copy; it does not prove that the content is correct or compliant.
5. Verify the transfer receipt and recipient access through an approved method.
6. If project portability or restore is claimed, reopen a separate copy in the intended environment and record the actual result. A folder copy or a written plan is not a restore test.
7. Apply the owner's retention and deletion instructions. Do not invent a retention period.
8. Close the delivery only when required evidence and approvals are present.

### 7. Worked example — fictional stereo delivery mismatch

**Brief/input:** A fictional client requests a 2-minute-30-second, 1920 × 1080 progressive master at a specified frame rate, with two-channel stereo audio and one English caption sidecar. The exact codec, audio format, caption format and tolerances are copied from the fictional brief into the matrix.

**Decision process:**

1. The editor records the approved sequence as SCENE-A v006 and obtains learner-exercise approval for that version.
2. The conform review finds all listed sources online and the approved edit points aligned with the reference.
3. The export candidate is named SCENE-A_v006_master_candidate01. The preset name includes “1080 Master,” but the actual metadata inspection reports one audio channel.
4. The matrix requires two-channel stereo. The candidate therefore fails the audio-layout test even though the image dimensions match.
5. The editor inspects the authorized project routing, corrects the channel mapping in a new working version and exports candidate02. The earlier candidate is retained as failed evidence, not overwritten.
6. The second candidate's metadata reports the required two-channel layout. The editor listens to both channels and checks dialogue sync and intelligibility.
7. The entire candidate is played from beginning to end. Captions are checked against the final picture, and the final filename/version is reconciled with the manifest.
8. The delivery is marked ready only after every required test has evidence and no blocking defect remains.

**Expected output:** A completed specification matrix, identifiable lock record, conform report, two export-attempt records, defect/retest entry, full-file QC report, caption record and handoff manifest. This is a simulated decision trace, not a rendered file or measured test.

### 8. Dry run / annotated walkthrough

Use the following fictional event sequence to rehearse the decision process without opening an NLE:

| Event | Observation | Correct decision |
|---|---|---|
| D01 | Reviewer approves sequence v006 | Record exact authority, date and version |
| D02 | A request arrives to replace a reaction shot after lock | Create a change request; do not edit v006 silently |
| D03 | Approval is granted for a new version | Duplicate to v007 and assess sound, captions, runtime and derivatives |
| D04 | Conform comparison reveals one missing licensed font | Hold export; locate an authorized dependency or replace only with approval |
| D05 | Candidate01 has the wrong audio channel count | Fail the candidate; correct routing and export a new candidate |
| D06 | Candidate02 metadata matches but the last 12 seconds were not played | QC remains incomplete; finish the playback |
| D07 | Full playback finds a misspelled credit | Record defect, correct in a new version and repeat graphics plus full-file checks |
| D08 | Corrected candidate passes all required tests | Record evidence, approval and manifest identity |

**Branching rule:** If the source license, approval authority, exact specification or file identity is unknown, stop at that gate and request evidence. Do not infer approval from silence or infer compliance from a filename.

### 9. Guided practice

**Exercise A — Specification traceability (20–30 minutes)**  
Use the fictional worked brief. Create one row per requirement with value, tolerance, source document, verification method and pass/fail evidence.  
*Hint:* If a field has no verification method, the matrix is not ready.  
*Success criterion:* Every mandatory field is traceable to a brief clause and a test.

**Exercise B — Lock and change control (20–30 minutes)**  
Given a locked 90-second sequence, document a requested 3-second reaction-shot replacement. Identify at least four affected items and the required approval.  
*Hint:* Consider sound, music, captions, runtime, color, graphics and alternate versions.  
*Success criterion:* The approved version remains recoverable and the proposed change has an owner and impact list.

**Exercise C — Defect triage and retest (30–40 minutes)**  
Classify the stereo mismatch, a misspelled credit, a stale filename and an incomplete playback. Create a defect register and state which checks must be repeated.  
*Success criterion:* No failed or unrun test is recorded as passed; corrected outputs receive a new identity.

### 10. Independent assignment

Prepare a finishing package for a learner-created or authorized 2–4 minute scene.

**Deliverables**

1. Approved delivery specification or clearly labeled provisional exercise specification.
2. Picture-lock record and version/change log.
3. Source, rights and dependency inventory.
4. Conform comparison and finishing turnover checklist.
5. Separate picture, sound, graphics/caption, accessibility, technical and delivery QC records.
6. Export-attempt log and actual metadata inspection where executed.
7. Full-duration playback evidence where executed.
8. Defect register with severity, correction and retest.
9. Handoff manifest, recipient/access restrictions and transfer record.
10. 500–800 word reflection describing one defect, its impact, correction and evidence.

**Submission labels:** Use Executed, Paper-only, Simulated, Not Run or Not Verified for each evidence item. Do not create fictional screenshots, metadata, approvals, file paths, checksums or transfer receipts.

### 11. Validation and tests

| Test ID | Method | Expected result | Actual result/evidence |
|---|---|---|---|
| T01 Specification | Compare matrix with the issued brief | Every mandatory field and tolerance is represented | Learner records |
| T02 Lock identity | Match sequence/version to approval | Exact approved version is identifiable | Learner records |
| T03 Change control | Inspect post-lock requests | Every change has authority and impact disposition | Learner records |
| T04 Conform | Compare source IDs, edit points and dependencies | No unexplained mismatch or offline required asset | Learner records |
| T05 Export properties | Inspect the actual file | Required metadata matches the matrix | Learner records |
| T06 Picture playback | Play the entire file | No unresolved picture defect | Learner records |
| T07 Audio playback | Listen to required channels and check specified measurements | Layout, sync and required audio criteria pass | Learner records |
| T08 Captions/graphics | Compare final picture and sidecars | Correct language, text, timing and version | Learner records |
| T09 Rights/privacy | Review source and disclosure records | Authorized use and handling are documented | Learner records |
| T10 Handoff | Reconcile manifest, files and recipient instructions | Package is traceable and access is appropriate | Learner records |
| T11 Portability/restore | Reopen a separate copy if claimed | Dependencies resolve and project behaves as expected | Learner records |
| T12 Regression | Repeat affected checks after correction | Corrected version passes; prior version is retained | Learner records |

The Actual result/evidence column is intentionally blank in this authored lab. It must be completed only after a learner performs the test.

### 12. Troubleshooting and rollback

| Symptom | Likely cause | Diagnosis | Safe recovery |
|---|---|---|---|
| Export looks correct but has wrong channels | Routing or export mapping | Inspect stream metadata and listen to each channel | Correct routing in a new version and re-export |
| Picture differs from approved reference | Wrong sequence, stale export or conform mismatch | Compare lock ID, edit points and file identity | Return to the approved version; reconform and document |
| Captions are out of sync | Picture changed after caption timing | Compare sidecar against final locked picture | Retiming by authorized workflow; validate again |
| Project opens with offline media | Missing dependencies or path changes | Reconcile inventory and relink notes | Relink authorized sources; preserve original paths and log changes |
| File is unexpectedly short | Interrupted export, wrong range or stale candidate | Compare duration and playback endpoints | Export a new candidate and inspect the whole file |
| Color appearance changes between players | Different color-management behavior or metadata | Compare reference, metadata and controlled playback path | Escalate the discrepancy; do not silently alter approved grade |
| Checksum differs after transfer | Incomplete or altered copy | Recalculate using the same recorded algorithm and verify source identity | Re-transfer through an approved route; preserve both records |
| Restore cannot find media | Manifest omitted dependency or path is invalid | Compare actual package with manifest | Restore from a verified source copy and update the manifest |
| Approval is unclear | Wrong authority or ambiguous note | Check the approval matrix and exact version | Hold delivery until an authorized decision is recorded |

**Rollback rule:** Never repair by overwriting the only approved sequence or master. Return to the last known approved version, create a new working version, document the correction and rerun affected tests. If a failed file has already been transferred, notify the authorized recipient and follow the documented replacement/recall process.

### 13. Performance, security and portability

- Use proxies or lower-resolution review media only when their relationship to originals is documented and the final conform returns to the intended source quality.
- Check storage capacity before export; preserve failed candidates only as long as required by the production's evidence/retention policy.
- Limit access to confidential footage, unreleased cuts, participant data and client specifications to authorized people.
- Do not upload media or captions to cloud AI, transcription or review services without the necessary owner authorization and privacy/terms review.
- Transfer only files the recipient is entitled to receive. Separate restricted source media from deliverables where necessary.
- Record fonts, plugins, LUTs, codecs, project versions and linked assets that affect portability.
- Test portability on a separate copy; do not treat the original workstation's successful open as proof that another system can reopen the project.
- A checksum verifies identity of the checked bytes only. It does not replace visual/audio QC, rights review or playback.
- Retain approvals, manifests and QC evidence according to the project owner's documented policy; no universal retention duration is assumed.

### 14. Submission and handoff

The handoff must state:

- project, scene, sequence and approved version;
- delivery specification revision and any approved exception;
- actual delivered file names and variants;
- project/interchange files and dependency/relink instructions;
- rights, consent, disclosure restrictions;
- captions, graphics, audio and other included assets;
- QC result, open defects and accepted limitations;
- transfer date, recipient, access method and receipt;
- checksum details if used;
- portability/restore status, including Not Run where applicable;
- editor/reviewer names or role identifiers and approval date;
- archive location and retention instruction supplied by the owner.

Do not include credentials, private access tokens or unnecessary personal data in the package.

### 15. Assessment rubric — revision 2.0

The original 30-point checkpoint rubric above is preserved as a short-form exercise. For the full revision 2.0 lab, use this separate 100-point rubric; do not add the two scores together.

| Criterion | Points | Observable evidence |
|---|---:|---|
| Specification and rights traceability | 15 | Complete matrix, source/rights inventory and resolved ambiguities |
| Picture-lock and change governance | 15 | Exact lock identity, approval authority and impact-controlled changes |
| Conform and dependency integrity | 15 | Source reconciliation, edit-point comparison and dependency record |
| Finishing-pass completeness | 15 | Separate picture, sound, graphics/caption, accessibility and rights passes |
| Export specification and artifact identity | 10 | Settings mapped to brief, unique output identity and actual metadata inspection |
| Full-file QC | 15 | Complete playback/listening evidence and documented pass/fail results |
| Defect correction and regression | 10 | Severity, owner, new version and retest evidence |
| Handoff and portability | 5 | Manifest, restrictions, transfer and honest restore status |
| **Total** | **100** | |

**Pass:** 80/100, with no critical failure. Unauthorized source use, destructive overwrite, untraceable master identity, fabricated approval/metadata/QC evidence or knowingly false compliance claims are mandatory remediation regardless of numeric score.

### 16. Lab quality checklist

- [ ] Environment and exact versions recorded for tools actually used.
- [ ] Inputs, rights, consent and restrictions documented.
- [ ] Delivery specification has an issuer/revision and a test for every required field.
- [ ] Approved picture-lock version and approval authority are traceable.
- [ ] Post-lock changes are controlled and downstream impacts reviewed.
- [ ] Conform and source dependencies are reconciled.
- [ ] Picture, sound, graphics/captions, accessibility and rights passes are recorded separately.
- [ ] Actual export properties are checked against the specification.
- [ ] Complete rendered-file playback is recorded, or explicitly marked Not Run.
- [ ] Defects have severity, owner, correction and retest evidence.
- [ ] Failed and prior approved versions are preserved without destructive overwrite.
- [ ] Manifest, handoff restrictions and recipient instructions are complete.
- [ ] Checksum/transfer/restore claims are supported by actual evidence.
- [ ] Simulated, paper-only and unverified work is labeled honestly.

### 17. Knowledge check and answer guidance

1. Why is a preset name insufficient evidence of export compliance?
2. What information must identify a picture-locked sequence?
3. Name four downstream items that may be affected by a post-lock picture change.
4. Why are conform review and final-file QC separate activities?
5. What is the difference between a metadata check and full playback?
6. When should a failed export be replaced with a new version rather than overwritten?
7. What does a matching checksum establish, and what does it not establish?
8. Why must a paper-only submission not receive playback-QC credit?

**Answer guidance**

1. Preset labels do not prove the actual settings or rendered streams; inspect the artifact.
2. Project/scene, sequence ID, version, timebase, duration, approval authority/date and reference location.
3. Examples include sound mix, music, VFX, color, captions/subtitles, titles/credits, runtime, derivatives and delivery date.
4. Conform verifies the approved edit is connected to intended sources/dependencies; final-file QC verifies the rendered artifact and delivery specification.
5. Metadata reports file properties; playback checks actual decoded picture/audio behavior across the full duration.
6. When a correction changes content/settings or a new candidate is needed for traceability; preserve the failed and prior approved files.
7. It establishes bit-for-bit identity for the checked copies under the recorded algorithm; it does not establish correct content, rights, playback or specification compliance.
8. No rendered artifact was inspected; a plan or simulated record cannot prove execution.

### 18. References and version notes

**Repository references**

- [CT-02 Lesson 07 — Assembly, Rough Cut, Fine Cut and Picture Lock](../lessons/lesson-07-assembly-rough-cut-fine-cut-picture-lock.md)
- [CT-02 Lesson 08 — Finishing, Delivery and Quality Control](../lessons/lesson-08-finishing-delivery-and-quality-control.md)
- [CT-02 Textbook Chapter 10 — Picture Lock, Finishing and Quality Control](../CT-02-FILM-CINEMATIC-EDITING-TEXTBOOK.md#chapter-10-picture-lock-finishing-and-quality-control)
- [CT-02 Student Workbook Section 25 — Picture Lock, Finishing and Quality-Control Evidence](../CT-02-STUDENT-NOTES-WORKBOOK.md#25-picture-lock-finishing-and-quality-control-evidence)
- [PCMDK369 Professional Lab Template](../../../../templates/professional-lab-template.md)
- [PCMDK369 Professional Academic Standard](../../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md)

The written delivery brief, contract and current platform/broadcaster requirements are the primary project-specific authorities. Verify current external requirements at the time of delivery; this lab does not reproduce or freeze a third party's specification.

**Version notes**

- Revision 2.0, 2026-11-25: added professional brief, measurable implementation objectives, environment and rights controls, project architecture, lock/change governance, conform workflow, separate finishing passes, artifact-level validation, defect severity and retest, worked example, dry run, guided/independent practice, validation matrix, security/portability, handoff, expanded 100-point rubric and answer guidance.
- The original Lab 04 procedure, worked example, 30-point checkpoint rubric and QC checklist are retained above.
- Procedures are tool-independent. No DaVinci Resolve, Premiere Pro, Final Cut Pro, CapCut, FFmpeg, media-player, metadata-inspector, caption-validator or checksum-utility UI/command behavior is asserted or tested in this revision.
- No application, encoder, meter, caption validator, storage/transfer service, export, playback, checksum or restore operation was executed by the authoring process. Learners must record actual results; the lab is authored, not tested.
