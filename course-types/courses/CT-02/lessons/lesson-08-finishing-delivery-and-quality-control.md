# CT-02 Lesson 08 — Finishing, Delivery and Quality Control

- **Course:** CT-02 — Film & Cinematic Editing
- **Level:** Professional Practice
- **Estimated study time:** 6–8 hours, including a complete export inspection and handoff simulation
- **Prerequisites:** Lessons 01–07; an approved picture-lock version; basic understanding of frame rate, image dimensions, audio channels and project media management
- **Tools/environment:** Any NLE capable of producing the approved deliverables; an independent media inspector/player; optional audio loudness meter, caption validator and checksum utility
- **Software policy:** Tool-independent. Record the exact application, version, operating system, export preset and any external inspection utility used. Menu names and codec availability vary by product, edition, platform and version.
- **Lesson revision:** 2.0 — expanded academic lesson, 2026-11-17

---

## Learning outcomes

By the end of this lesson, the learner can:

1. Translate a written delivery brief into a version-controlled specification matrix without inventing missing technical requirements.
2. Prepare a finishing turnover from an approved picture lock and identify dependencies that must be conformed or relinked.
3. Distinguish a project timeline, mezzanine/master file, review copy and distribution derivative.
4. Select an export path that matches the approved specification and record the settings that materially affect the result.
5. Inspect the actual exported file independently for metadata, image, sound, captions, runtime, integrity and playback defects.
6. Classify defects by severity, document evidence and perform a controlled correction/retest cycle.
7. Package project files, media dependencies, rights records, captions, credits and delivery manifests for a professional handoff.
8. Apply accessibility, privacy, licensing, retention and approval requirements throughout finishing.

## Prerequisite check

Before beginning, confirm that the picture-lock version has a stable identifier, the authorized approver is known, and the project has a documented change-freeze rule. If the cut is not approved, do not label a file as final. You may prepare a clearly marked review export, but the approval state must remain visible.

Learners should be able to explain the difference between source media and a rendered export, identify the sequence frame rate, locate the audio configuration, and reopen a saved project. If these foundations are uncertain, revisit the earlier media-management and timeline lessons before continuing.

## Key definitions and terminology

| Term | Definition | Practical significance |
|---|---|---|
| Delivery specification | Written acceptance requirements for each deliverable | Prevents an editor from guessing what “high quality” means |
| Finishing | The controlled preparation of an approved edit for delivery | Includes conform, titles, color, sound, captions, export and QC |
| Turnover | Transfer of the approved edit and its dependencies to finishing or another department | Makes responsibility, version and missing elements explicit |
| Conform | Rebuilding or checking the final sequence against approved edit decisions and source media | Detects offline, wrong, mismatched or substituted media |
| Master | The approved high-quality deliverable designated as the source for later versions | Must be clearly distinguished from a review copy |
| Mezzanine file | A high-quality intermediate file used for downstream processing or exchange | Usually prioritizes fidelity and editability over small file size |
| Distribution derivative | A version encoded for a particular client, platform, channel or use | Must be derived from the approved master or approved project state |
| Container | The file wrapper that holds video, audio, captions or metadata streams | A container name alone does not identify the codec |
| Codec | The method used to encode or decode a media stream | Must be compatible with the receiving workflow |
| Loudness | Perceived audio level measured using a defined method | Target values must come from the delivery specification |
| True peak | An estimate of the reconstructed signal peak between digital samples | Can reveal inter-sample peaks not obvious from sample-peak readings |
| Sidecar caption | A separate subtitle/caption file delivered alongside media | Requires matching filename, language and timing |
| Burned-in caption | Text permanently rendered into the picture | Cannot be switched off and must be approved for that version |
| Checksum | A digest calculated from file contents to detect changes or transfer errors | Helps verify that a copy matches the supplied file |
| QC report | A record of tests, observations, defects, corrections and retest results | Provides evidence rather than an unsupported “looks good” statement |
| Archive package | The authorized set of project, media, metadata and delivery records retained for future use | Must follow the project retention and access policy |

## Purpose and professional relevance

Finishing is the point where creative approval becomes a controlled technical handoff. A timeline that plays correctly on the editor's workstation is not, by itself, proof that a deliverable is correct. The export may have the wrong dimensions, frame rate, audio layout, caption version, color transform, duration or filename. A transfer may also be incomplete, or a project may reopen with missing media.

Professional delivery therefore has two distinct objects to verify:

- **The editable project:** its sequence, linked media, graphics, fonts, effects, settings and dependencies.
- **The rendered deliverable:** the actual file that the recipient will play, ingest, publish or archive.

Both may require checks, but they answer different questions. A project can be well organized while its export is defective. An export can play correctly while the project is not portable. A complete handoff proves both only when the relevant evidence is present.

The governing principle is specification-first finishing. There is no single universal export preset, loudness target, codec, color space or subtitle format suitable for every broadcaster, festival, client, archive and social platform. The receiving party's current written requirements take precedence.

## Theory and decision principles

### 1. Separate creative approval from technical compliance

Picture lock is an editorial approval state, not a guarantee that every finishing task is complete. The locked cut can still require color conform, sound mix, titles, captions, legal review, end credits and output preparation. Those operations must not silently alter the approved editorial structure.

If a finishing issue requires a picture change, record the issue, identify its impact, request authorization from the designated approver and create a new version. Never conceal an editorial change inside a technical export correction.

### 2. Build a specification matrix before exporting

A useful matrix records each deliverable separately. At minimum, capture:

| Field | Questions to answer |
|---|---|
| Deliverable purpose | Master, review, web, broadcast, festival, archive or another use? |
| Picture | Raster dimensions, aspect ratio, frame rate, scan type and orientation? |
| Encoding | Container, video codec, profile, bit depth and bitrate or quality rule? |
| Color | Color primaries, transfer characteristics, matrix, range and required transform? |
| Audio | Sample rate, bit depth where applicable, channel layout, loudness and peak limits? |
| Captions | Required languages, format, sidecar or burned-in, timing and accessibility rules? |
| Runtime | Exact or permitted duration range, including leader, slate and end credits? |
| Naming | Project, title, version, language, date and extension convention? |
| Destination | Approved transfer method, folder, recipient and access permissions? |
| Acceptance | Who approves, what tests are mandatory and what evidence must be returned? |

If a field is missing, mark it **not supplied** and ask the authorized stakeholder or record it as an unresolved dependency. Do not substitute a guessed value. If a client says “4K,” clarify the actual raster, frame rate, codec and color requirements rather than treating the word as a complete specification.

### 3. Understand the delivery chain

A typical controlled chain is:

1. Approved editorial sequence and change record.
2. Finishing turnover and dependency check.
3. Conform, graphics, color and sound preparation.
4. Master or mezzanine export.
5. Independent master inspection.
6. Derivative creation from the approved source.
7. Independent derivative inspection.
8. Packaging, transfer and integrity verification.
9. Recipient acceptance and authorized archive.

A failure at one stage should not be hidden by a later stage. For example, a derivative should not be generated from an unapproved review file simply because it is available.

### 4. Use independent inspection

The export dialog reports intended settings. It does not prove the rendered file contains the intended settings or plays correctly. Use an independent media inspector or a second playback path where practical. Inspect the entire runtime, not only the opening frame or a short sample.

A metadata inspection can verify dimensions, duration, frame rate, stream layout and codec identification. Playback inspection can reveal visual glitches, missing frames, black flashes, audio pops, sync errors, caption defects and abrupt endings. A checksum can verify file identity after transfer, but it cannot prove creative or technical correctness.

### 5. Keep objective tests separate from subjective notes

Objective tests include dimensions, frame rate, stream presence, runtime, checksum match and successful decode. Subjective or context-dependent review includes pacing, performance, emotional tone, color preference and whether a mix suits the creative brief. Both matter, but they should not be reported as the same kind of evidence.

## Tools, requirements and alternatives

| Tool category | Purpose | Alternatives and limitations |
|---|---|---|
| NLE | Conform, final picture/audio preparation and export | Any editor that supports the approved source and output requirements; feature names vary |
| Media inspector | Read container, stream and metadata properties | A trusted command-line probe or independent inspection application; verify the tool version |
| Independent player | Full playback review | Use a second player or workstation when feasible; one player may share the same decoding assumptions as the editor |
| Audio meter | Measure the specified loudness and peak properties | Use a meter that implements the method required by the recipient; do not infer compliance from listening alone |
| Caption validator | Check file structure, timing and encoding | Manual review remains necessary for meaning, speaker identity and reading comfort |
| Checksum utility | Compare file identity after copying | Use a trusted SHA-256-capable utility where required; a checksum is not a substitute for backup or playback |
| Transfer system | Deliver files to the authorized recipient | Use an approved secure service or managed storage location with access controls and expiry where appropriate |

Examples of independent utilities include MediaInfo for media metadata, FFmpeg tools for probing or decoding, and a standards-compatible subtitle validator. Availability and command syntax depend on installed versions and operating systems. This lesson does not claim that any utility has been executed.

## Reproducible finishing procedure

### Phase A — Accept and freeze the turnover

1. Record the project title, course/capstone identifier, sequence name, sequence version and picture-lock approval reference.
2. Confirm the approver and the date/time of approval. If approval is verbal, request a written record before final delivery.
3. Record whether the edit is frozen. List permitted finishing changes and the person authorized to approve an editorial change.
4. Save a protected checkpoint of the approved sequence. Do not overwrite the only approved project copy.
5. Collect the turnover package: edit decision list or equivalent, source manifest, graphics, VFX, music and sound notes, caption files, credits, rights records and known issue list.
6. Compare the turnover against the source inventory. Mark every missing, offline, substituted or unverified dependency.

**Exit condition:** the approved sequence is identifiable, the delivery brief is available, and unresolved dependencies are listed with owners.

### Phase B — Build the delivery matrix

1. Create one row for each required output: master, review copy, web version, language version, caption file or archive copy.
2. Copy technical values from the recipient's current written specification.
3. Record the source of each requirement, such as a client document title, platform specification revision or authorized email.
4. Mark unknown values as unresolved. Do not silently fill gaps with a familiar preset.
5. Confirm runtime conventions, slate/leader requirements, end-credit handling, audio layout and subtitle naming.
6. Obtain clarification for conflicting requirements before export.
7. Save the matrix with a version identifier and approval status.

**Exit condition:** every deliverable has a traceable specification or an explicitly recorded unresolved item.

### Phase C — Conform and prepare the sequence

1. Open the approved project copy and verify the expected sequence identifier and frame rate.
2. Relink media only against the approved source manifest. Do not replace offline media with a visually similar file without authorization.
3. Review the sequence from beginning to end for offline media, placeholder graphics, temporary titles, disabled tracks, missing effects and unintended gaps.
4. Confirm that the picture conforms to the approved edit decisions. Compare against a reference export or review file if supplied.
5. Check that titles, logos, end credits and legal text match the approved copy and asset versions.
6. Confirm that color management and output transforms are understood. Do not apply a second transform to footage that is already transformed.
7. Confirm the audio mix, channel mapping, fades, synchronization and required stems or splits.
8. Verify that the correct caption version is associated with the cut. Check language, speaker labels, punctuation and timing.
9. Record all changes made during finishing and identify which were approved technical changes versus editorial changes.

**Exit condition:** the sequence is complete, dependencies are resolved or documented, and the finishing state is reproducible.

### Phase D — Prepare export settings

1. Select the deliverable row in the matrix; do not begin with a generic preset.
2. Match the raster, frame rate, scan type, aspect ratio and orientation exactly to the approved specification.
3. Select a container and codec supported by the recipient. Confirm profile, bit depth, chroma sampling and bitrate/quality requirements where specified.
4. Confirm color primaries, transfer characteristics, matrix, range and metadata behavior required for the destination.
5. Confirm audio sample rate, channel layout, channel order, loudness method and peak limit from the written specification.
6. Confirm whether captions are sidecar files, burned-in, embedded or separately delivered.
7. Set file naming and destination paths before starting the export.
8. Record the export preset name and any overridden settings. A preset name alone is not a complete record.
9. If the NLE offers hardware and software encoding options, use the path approved or supported for the target. Do not assume two encoding paths produce identical results.
10. Export to a controlled staging folder, not directly to the final delivery location.

**Exit condition:** the settings have been checked against the delivery matrix and the staging export is clearly labeled as awaiting QC.

### Phase E — Inspect the actual rendered file

Perform these checks on the exported file, not only on the NLE timeline.

**Metadata and integrity**

1. Confirm that the file exists, has a plausible non-zero size and opens in an independent inspector.
2. Verify container, video codec, dimensions, frame rate, duration, scan type, color metadata, audio stream count, sample rate and channel layout.
3. Compare each measured property with the corresponding delivery-matrix field.
4. Confirm that the file decodes without errors using a trusted independent path where available.
5. Record the file size and calculate a checksum if required by the transfer or archive procedure.

**Picture review**

1. Watch the entire file at normal speed on a suitable display.
2. Inspect the first and last frames, transitions, title cards, credits and any frame where a defect was previously reported.
3. Look for black flashes, frozen frames, duplicated frames, unintended scaling, crop changes, missing graphics, edge artifacts, banding, clipping and color-transform errors.
4. Check that titles remain legible at the intended viewing size and do not collide with required safe areas.
5. Compare representative shots with the approved reference where one exists. Do not treat an uncalibrated display as proof of color-critical compliance.

**Audio review**

1. Listen to the entire program with appropriate monitoring.
2. Check for missing channels, swapped channels, silence, clicks, pops, abrupt cuts, distortion, unwanted noise and synchronization drift.
3. Measure loudness and true peak using the method specified by the recipient.
4. Verify that dialogue, music and effects remain intelligible and balanced according to the approved creative brief.
5. Confirm that any required split tracks or stems are present, named and synchronized.

**Caption and accessibility review**

1. Open every sidecar caption file in a validator or compatible editor.
2. Confirm file encoding, cue order, time format and absence of malformed or overlapping cues where prohibited by the target format.
3. Watch the video while reading the captions. Check spelling, speaker identity, punctuation, line breaks, timing and meaningful sound cues.
4. Confirm that caption text does not cover essential action or required graphics.
5. Review burned-in captions at the final display size and verify that the correct language version was exported.
6. Check contrast and reading time. Avoid relying only on automatic caption confidence or spell-check.

**Exit condition:** all required checks are recorded as pass, fail or not applicable with a reason. Any unresolved critical defect blocks delivery.

### Phase F — Correct, re-export and retest

1. Create a defect record with a unique ID, severity, file version, timecode or frame reference, expected result, observed result and evidence.
2. Identify the source of the defect: editorial sequence, source media, graphics, audio, captions, export settings, encoder or transfer.
3. Apply the least destructive correction in a new working version.
4. Obtain approval if the correction changes editorial meaning, performance, runtime, credits or other approved content.
5. Re-export using a new version identifier. Never replace a previously approved delivery silently.
6. Repeat the affected checks and any regression checks that could be affected by the change.
7. Close a defect only when the retest evidence is recorded. If a defect is accepted as a known exception, record the authorized approver and the reason.

### Phase G — Package and deliver

1. Create a delivery folder containing only authorized deliverables and required handoff documents.
2. Include a manifest listing filename, purpose, version, language, dimensions, frame rate, codec/container, duration, file size and checksum where required.
3. Include project files and dependencies only when the contract and recipient require them.
4. Include captions, transcripts, credits, rights/consent records, release notes and the QC report as appropriate.
5. Include software, plugin, font and media dependency notes where the recipient needs them to reopen the project.
6. Remove temporary proxies, cache files and private review copies only under the authorized cleanup and retention policy.
7. Transfer through the approved destination and access list. Avoid public links for confidential or personal media.
8. Verify that the recipient's copy matches the supplied checksum when the process supports it.
9. Request or record recipient acceptance. Do not describe a file as accepted merely because a transfer completed.

### Phase H — Archive and close

1. Confirm which project assets and deliverables are authorized for retention.
2. Record archive owner, location, access controls, retention period and deletion trigger.
3. Preserve the approved project, required source media, final master, delivery derivatives, manifests, QC reports and approval/change records according to policy.
4. Test the archive by reopening the project or restoring a sample package from the archive location when required.
5. Record the restore test result and any missing dependency.
6. Close the project only after handoff and archive status are clear.

## Worked example — fictional narrative short

**Brief:** A fictional 3-minute-12-second narrative short called *Harbor Lantern* has an approved picture lock. The client requests a high-quality master, a web review copy and English captions. The exercise specification supplied by the fictional client states:

| Item | Exercise requirement |
|---|---|
| Master | MOV container with ProRes 422 HQ video |
| Picture | 1920 × 1080 progressive, 25 frames per second |
| Audio | 48 kHz, stereo, with the supplied exercise loudness and peak limits |
| Web review | MP4 container with H.264 video and AAC stereo audio |
| Captions | English SRT sidecar with matching runtime |
| Naming | HarborLantern_MASTER_v1, HarborLantern_REVIEW_v1 and HarborLantern_EN_v1 |
| Approval | Producer signs the final QC report before delivery |

These values are fictional exercise inputs, not universal delivery recommendations. The learner must use them only because the fictional brief explicitly supplies them.

**Decision process**

1. Create three delivery-matrix rows rather than trying to force one export to satisfy every purpose.
2. Confirm that the approved timeline is 25 fps and 1920 × 1080 progressive.
3. Verify the audio mix and supplied exercise limits before rendering.
4. Export the master and inspect it independently.
5. Create the web review copy from the approved master or approved sequence using the separate review specification.
6. Inspect the review copy for runtime, sync, readability and playback.
7. validate the SRT structure, then watch the full review copy while following the captions.
8. Record checksums and package the three outputs with the QC report and manifest.

**Expected result:** a clearly named, versioned package with three distinct deliverables, a completed matrix, independent inspection evidence and an approval record. A successful export dialog alone does not meet the assignment.

## Annotated dry run — diagnose before delivery

A learner receives a candidate master and finds the following:

| Observation | Evidence | Classification | Next action |
|---|---|---|---|
| File reports 24 fps but matrix requires 25 fps | Independent metadata inspection | Major | Check sequence/export settings and confirm intended cadence before re-export |
| Last caption ends 2 seconds before the final spoken line | Full playback against SRT | Major | Correct timing, validate again and replay affected section |
| Right audio channel is silent | Channel meter and independent listening | Major | Trace channel routing and re-export; inspect both channels |
| One-frame black flash after a dissolve | Frame-by-frame inspection | Major | Inspect transition/media handles and retest the complete transition |
| Filename lacks version suffix | Manifest comparison | Minor or major according to handoff rules | Rename under the approved convention and update manifest |

The learner must not “fix” the frame rate by merely changing a metadata label if the source cadence and frame conversion are not understood. The correct action depends on the approved specification and intended motion treatment.

## Guided practice

Use a fictional, self-authored 30–60 second scene or a rights-cleared practice sequence. Do not download or reuse commercial film footage, commercial music or unlicensed graphics.

### Exercise 1 — Specification extraction

Create a delivery matrix for one master and one review copy. Include every field in the matrix above. Intentionally leave two fields unknown and show how you would request clarification. **Evidence:** completed matrix and clarification note.

### Exercise 2 — Export verification

Export a test file from an available editor. Record the app/version and compare the actual metadata against the intended settings. **Evidence:** export record and independent inspection report. If the application is unavailable, submit a tool-independent test plan and label it as unexecuted.

### Exercise 3 — Full playback QC

Review the complete test export. Record at least five time-referenced observations, including one audio check, one caption or accessibility check and one end-of-file check. **Evidence:** defect log with pass/fail status.

### Exercise 4 — Controlled correction

Choose one non-critical defect, correct it in a new version and document the retest. **Evidence:** before/after record, new filename and closed defect entry.

### Exercise 5 — Handoff rehearsal

Create a manifest and package the project or a documented project substitute, export, captions, rights record and QC report. Reopen the package from a different folder if project portability is part of the brief. **Evidence:** handoff checklist and restore result.

## Independent practical assignment

**Assignment:** Finish and deliver a 2–4 minute original narrative scene using only original, public-domain or explicitly licensed practice material.

Submit:

1. Approved-cut identifier and approval/change record.
2. Delivery specification matrix with source of each requirement.
3. Finishing turnover checklist and media-dependency report.
4. Export settings record for every deliverable.
5. Final master and at least one specified derivative, or a documented export plan if no rendering environment is available.
6. Independent metadata report and full-playback QC report.
7. Caption file and caption review record where dialogue or accessibility requirements apply.
8. Rights, consent, credits and privacy record.
9. Delivery manifest with versions, file sizes and checksums where required.
10. Handoff and archive/restore note.
11. A 300–500 word reflection explaining two consequential finishing decisions, one limitation and one defect corrected.

Do not submit copyrighted film clips, commercial music, unlicensed fonts or third-party assets without documented permission. If a required asset is unavailable, replace it with original work or a clearly identified rights-safe placeholder.

## Common mistakes and troubleshooting

| Symptom | Likely cause | Diagnostic step | Recovery |
|---|---|---|---|
| Export has wrong frame rate | Wrong sequence, preset override or unintended conversion | Compare sequence and actual file metadata | Correct the source/export path; choose a documented conversion only if required |
| File plays in the NLE but not the recipient's player | Unsupported codec/profile, incomplete file or decoder difference | Inspect metadata and test with a second supported player | Re-export to the recipient's verified specification |
| Picture looks washed out or too contrasty | Incorrect color metadata, transform or display interpretation | Inspect color properties and compare in a known display pipeline | Correct the transform/metadata according to the approved color workflow |
| Audio sounds clipped | Peak overload, processing or channel summing | Inspect meters and listen to the rendered file | Correct gain/processing and remeasure against the required target |
| Audio channels are reversed or missing | Incorrect mapping or export routing | Inspect channel layout and audition channels separately | Correct routing and repeat full audio QC |
| Captions drift over time | Wrong frame-rate assumption, timing basis or edit version | Compare cue times against the final runtime and dialogue | Retiming must use the final approved cut and target format |
| Captions are unreadable | Excessive text, poor contrast or unsafe placement | Review at actual display size | Re-segment, adjust styling/position and obtain approval |
| Project opens with offline media | Dependencies were not collected or paths changed | Reopen from the packaged location | Relink from the approved manifest and repeat the portability test |
| Checksum differs after transfer | Incomplete transfer, file changed or wrong file selected | Recalculate both sides and compare names/sizes | Re-transfer from the verified source; investigate repeated mismatches |
| A “final” file contains an unapproved edit | Version and approval state were not controlled | Compare change log and approval record | Quarantine the file, restore the approved state and issue a corrected version |

## Knowledge check with answer key

1. **Why is the export dialog insufficient evidence of delivery compliance?**  
   Because it records intended settings, not proof of the actual file's metadata, playback, captions, audio or transfer integrity.

2. **What is the difference between a container and a codec?**  
   A container holds streams and related data; a codec encodes or decodes an individual media stream. A container name alone does not identify the video or audio codec.

3. **What should an editor do when the brief says only “high quality”?**  
   Request or document the missing acceptance requirements. Do not invent dimensions, codec, bitrate, color or audio targets.

4. **Why should the actual exported file be watched from beginning to end?**  
   Defects may occur anywhere in the runtime, and timeline playback does not prove the export is correct.

5. **Does a checksum prove that a film looks and sounds correct?**  
   No. It verifies file identity against another digest; it does not assess creative or technical quality.

6. **When is a picture change during finishing an editorial change?**  
   Whenever it changes approved content, timing, performance, meaning, credits or other locked editorial decisions. It requires the agreed approval process.

7. **Why are master and review exports separate delivery rows?**  
   They may have different purposes, codecs, quality, security, watermarking, naming and approval states.

8. **What is the purpose of a defect severity scale?**  
   It helps prioritize correction and prevents a critical rights, corruption or content defect from being treated like a minor naming issue.

9. **Why must captions be checked against the final cut?**  
   The edit may change cue timing, wording, speaker turns or runtime; a previously correct subtitle file may no longer match.

10. **What does a successful project portability test demonstrate?**  
    That the required project and dependencies can be reopened from the packaged location or tested environment. It does not prove every future system will be compatible.

11. **Should an editor use a familiar loudness target when the delivery specification is silent?**  
    No. The target and measurement method must be supplied or approved by the receiving party.

12. **When may temporary or personal source media be deleted?**  
    Only under the authorized retention and deletion policy, contract and applicable requirements; an editor must not make an independent retention decision without authority.

13. **What evidence closes a corrected defect?**  
    A new version identifier, the correction record and a successful retest of the affected output plus any relevant regression checks.

14. **Why is recipient acceptance separate from successful file transfer?**  
    Transfer proves that data was sent or copied; acceptance confirms that the authorized recipient has reviewed or acknowledged the deliverable according to the agreed process.

## Assessment rubric — 100 points

| Criterion | Points | Evidence |
|---|---:|---|
| Specification matrix and traceability | 15 | Requirements have sources; unknowns are not guessed |
| Turnover, conform and change control | 15 | Approved version, dependencies and changes are documented |
| Export settings and version record | 10 | Settings match the written specification and are reproducible |
| Independent metadata and playback QC | 20 | Actual file is inspected; results and time references are recorded |
| Audio, caption and accessibility checks | 10 | Relevant tests are completed and defects dispositioned |
| Rights, privacy, credits and consent | 10 | Asset use and handling are documented and authorized |
| Delivery manifest, transfer and archive | 15 | Package is organized, integrity is checked and restore status is clear |
| Reflection and professional reporting | 5 | Decisions, limitations and next actions are explained |
| **Total** | **100** | |

**Pass rule:** 80/100 or higher, with no unresolved critical defect and a complete delivery manifest. A score cannot compensate for an unauthorized release, missing essential deliverable, corrupt master or unresolved rights/consent breach.

## Capstone integration requirements

For the CT-02 narrative-scene capstone, Lesson 08 evidence is part of the final submission. The capstone package must identify the approved cut, master and review derivatives, export specification, QC findings, corrected defects, caption/credit requirements, rights record, handoff manifest and archive/restore status. The learner must distinguish a rendered file from a project file and must not claim a software render or restore test unless it was actually performed.

## Quality-control checklists

### Before export
- [ ] Picture-lock version and approver are recorded.
- [ ] Delivery specification is written and unresolved fields are visible.
- [ ] Media, graphics, titles, color, audio and captions match the approved cut.
- [ ] Project dependencies and source rights are accounted for.
- [ ] Export destination and version naming are approved.

### After export
- [ ] Actual metadata matches the correct delivery-matrix row.
- [ ] File decodes and plays from beginning to end.
- [ ] Picture, sound, synchronization, titles and credits pass review.
- [ ] Captions and accessibility requirements pass review where applicable.
- [ ] Defects are recorded, corrected and retested.
- [ ] File size, checksum and transfer status are recorded where required.

### Before handoff and archive
- [ ] Manifest matches the files in the delivery folder.
- [ ] Correct versions and languages are present.
- [ ] Access is limited to authorized recipients.
- [ ] Rights, consent, credits and approvals accompany the package as required.
- [ ] Project portability and archive restore status are recorded.
- [ ] Retention and deletion responsibilities are documented.

## Accessibility, rights, privacy and professional practice

- Captions must be accurate, synchronized, readable and appropriate to the intended language and audience. Do not treat auto-generated captions as approved without human review.
- Avoid flashing or rapidly alternating visual patterns that may create risk. Respect the project's accessibility specification and applicable guidance.
- Verify font, music, footage, still-image, logo, voice and performer permissions for the actual use and distribution territory. A training placeholder is not a license.
- Keep private source media, unreleased performances, contact details and client review links in approved storage with appropriate access controls.
- Do not upload confidential or personal media to a third-party inspection or AI service without authorization and a review of its data-handling terms.
- Do not remove watermarks, access restrictions or metadata to evade a license or hide provenance.
- Retain only the material authorized by the contract and retention policy. Record who owns the archive and who can request deletion.
- The QC report must separate measured facts, subjective observations, assumptions and unresolved issues. It must not imply legal certification or recipient approval that has not been obtained.

## Version notes and limitations

- Revision 2.0 is a tool-independent academic expansion dated 2026-11-17.
- No specific NLE, encoder, operating system, loudness meter, caption validator or transfer service was executed for this lesson.
- Codec availability, export controls, color-management behavior, metadata writing and caption support vary by application version and platform. Verify the exact installed version and current official documentation before writing menu-specific steps.
- Delivery specifications, loudness targets, legal duties and retention rules vary by recipient, contract and jurisdiction. This lesson teaches a verification workflow and is not legal advice or a universal delivery specification.

## References and further study

- FFmpeg documentation — format, codec and media inspection concepts: https://ffmpeg.org/documentation.html
- MediaInfo — independent media metadata inspection: https://mediaarea.net/en/MediaInfo
- W3C WebVTT — timed text track format specification: https://www.w3.org/TR/webvtt1/
- European Broadcasting Union, EBU R 128 — loudness normalization recommendation; consult the current publication and the recipient's specification rather than assuming its target applies to every project: https://tech.ebu.ch/publications/r128
- Blackmagic Design support and current DaVinci Resolve documentation: https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion
- Adobe Premiere Pro user guide and version-specific export documentation: https://helpx.adobe.com/premiere-pro/user-guide.html

External references supplement this authored lesson. They do not replace the receiving party's current delivery specification or independent inspection of the actual file.
