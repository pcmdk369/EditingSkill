# CT-03 Lesson 04 — Advanced Multi-Format Pacing and Version Control

- **Course:** CT-03 — Short-Form & Social Video Editing
- **Level:** Advanced
- **Estimated time:** 240–300 minutes, including adaptation, review and evidence packaging
- **Prerequisites:** Lessons 01–03; one approved short-form edit; source project and rights/asset records
- **Tools/environment:** Any editor supporting sequence duplication, transforms, markers and export; spreadsheet/plain-text log or issue tracker; storage with backup/version history. Record editor, version, OS and storage method.
- **Version/review date:** Academic revision 2.0 — 2026-11-19. Tool-neutral instruction; verify current destination specifications and editor behavior before production use.

## Learning outcomes

By the end of this lesson, learners can:
1. Design a deliverable matrix for a campaign with multiple aspect ratios, durations, destinations, languages and calls to action.
2. Distinguish a canonical approved master, editable project, review proxy, derivative sequence and final distribution export.
3. Build modular timelines and identify dependencies that should remain shared versus intentionally diverge.
4. Adapt narrative structure and pacing to different viewing contexts without distorting facts or removing necessary qualifiers.
5. Calculate and evaluate runtime budgets, information density, shot duration and CTA reading time.
6. Recompose each format shot by shot rather than applying blind resize presets.
7. Apply controlled version identifiers, naming conventions, change requests, approval states and release manifests.
8. Prevent stale graphics, inconsistent claims and accidental overwrites across a deliverable family.
9. Perform specification-led, independent QC on every derivative and record defect/retest evidence.
10. Package editable project dependencies and final outputs for a traceable professional handoff.

## Key definitions and terminology

| Term | Definition | Context/example |
|---|---|---|
| Deliverable matrix | Table of every required output and its unique requirements | 9:16 / 30 s / Thai / feed |
| Canonical master | Designated approved editorial source used as the reference for derivatives | Locked master sequence |
| Working master | Editable source timeline used to produce a family of outputs; not automatically client-approved | Protected project sequence |
| Derivative | A distinct adaptation created from a master for a specified purpose | 1:1 square cut |
| Conform | Aligning an edit or media package to a required technical specification or project state | Replacing proxies with originals |
| Modular timeline | Timeline organized into reusable sections or logical units | Hook, proof, offer, CTA |
| Dependency | Asset or setting required for a project to open or render correctly | Font, LUT, linked audio |
| Runtime budget | Planned allocation of time to story functions | 3 s hook, 12 s proof |
| Information density | Amount and complexity of information presented in a period | Three claims in two seconds |
| Beat | Meaningful story or action unit that changes viewer understanding | Problem revealed |
| Version identifier | Unique label distinguishing a saved state or deliverable | v003 |
| Revision | A change to an existing version in response to review or correction | Corrected legal qualifier |
| Release candidate | Candidate output submitted for final QC before approval | RC1 |
| Baseline | Frozen reference version against which changes are compared | Approved v1.0 |
| Change request | Traceable description of a proposed alteration and its authorization | CR-014: replace offer date |
| Change impact | Set of sequences, assets, exports and records affected by a change | Price update affects 3 languages |
| Manifest | Structured inventory of outputs and their properties | Filename, ratio, language, checksum |
| Provenance | Record of where an asset or claim originated and how it changed | Source clip and license record |
| Regression check | Retest of previously working areas after a change | Recheck captions after duration edit |
| Checksum | Computed value used to detect whether a file changed | SHA-256 digest |
| Immutable archive | Stored release copy protected from casual editing or replacement | Read-only approved package |
| Semantic versioning | Version scheme where major/minor/patch communicate change type | 2.1.0; use only if team defines it |
| Branch / derivative branch | Separate working line used to develop an adaptation without changing the protected source | Square-format sequence |

## Purpose and professional relevance

A campaign rarely ends with one export. A client may request vertical, square and landscape versions, shorter cutdowns, translated variants, alternate calls to action and revisions after review. Each output must preserve the approved message while adapting composition, pacing, reading time and technical properties to its intended context.

A multi-format workflow is not “resize, export, repeat.” Different frame shapes change what can be seen at once. Different runtimes change how much evidence can be presented. Different languages alter line length and reading time. A price or offer change can affect every version, including a version already approved or queued for publication.

Version control is therefore a quality and risk-control discipline. It prevents an old price, outdated disclaimer, missing caption, unapproved music track or wrong CTA from appearing in one member of a campaign family. It also enables another editor to identify the correct source and reproduce the handoff.

## Theory and principles

### 1. Separate the source, master, derivative and export

These objects serve different purposes:

- **Source media** are original camera files, audio, graphics, licensed assets and supplied documents. Preserve them.
- **Working project** is the editable project file plus its dependencies. It may contain multiple sequences.
- **Working master** is the designated editorial reference sequence. It can be revised only through controlled change.
- **Approved master** is the version accepted by the authorized reviewer. Freeze and identify it.
- **Derivative sequence** is a distinct adaptation with its own timing, framing, language or graphic decisions.
- **Review export** is a candidate file for inspection; it is not approved merely because it rendered.
- **Release export** is the final file that passed the specified acceptance gates.

A project may use one sequence as the canonical master and duplicate sequences for adaptations. Another project may use nested sequences or a structured project file. The naming convention is less important than the ability to identify the authoritative source and trace every output back to it.

### 2. Plan the deliverable family before editing

Build a matrix before making derivatives. Typical dimensions include:

- destination and placement (feed, story, website, in-store display, client archive);
- aspect ratio and pixel dimensions;
- runtime and permitted duration range;
- frame rate and orientation;
- language, subtitle/caption convention and reading direction;
- CTA, price, offer period, legal qualifier and destination URL;
- audio requirements, loudness target and channel layout where specified;
- file container, codec, bitrate or quality setting;
- safe-composition and interface overlay checks;
- approval owner, deadline and status.

Never infer current platform limits from memory. Use a dated client/platform specification or verify current official destination guidance. If a requirement is unknown, mark it **TBC** and ask the owner; do not silently invent it.

### 3. Design pacing around comprehension and evidence

Pacing is not simply average shot length or cuts per minute. Evaluate:
- how quickly the viewer understands the situation;
- how long the action or product demonstration must remain visible;
- whether the next shot answers a question raised by the previous shot;
- how much text appears simultaneously;
- whether the viewer has time to read a claim and its qualifier;
- whether the CTA is understood before the video ends;
- whether pauses, reactions and transitions carry meaning.

A short cutdown should remove redundancy before it removes evidence. If a 15-second version cannot responsibly support all claims from a 45-second version, narrow the promise rather than compressing the same number of claims into unreadable speed.

### 4. Use a runtime budget as a planning tool, not a rigid formula

For a target duration (T), allocate time across story functions:
[
T = t_{	ext{hook}} + t_{	ext{context}} + t_{	ext{proof}} + t_{	ext{qualifier}} + t_{	ext{CTA}} + t_{	ext{transitions}}
]
Some functions can overlap, but the sum of actual timeline intervals must equal the sequence duration. A timing sheet helps reveal over-allocation before editing.

**Illustrative 30-second plan:** hook 3.0 s; context 4.0 s; demonstration 12.0 s; qualifier 3.0 s; CTA 5.0 s; transitions/holds 3.0 s. This is a teaching example, not a universal formula. A complex demonstration may need more proof time and a simpler opening.

### 5. Preserve claim integrity during compression

For every factual, commercial, safety or performance claim, record:
- exact approved wording;
- source of truth and owner;
- date or effective period;
- conditions, limitations and required qualifier;
- which formats/languages display it;
- who approved the final wording.

Do not shorten “up to 30% savings on selected products, until 30 June” into “30% off” if that changes the scope or certainty. Do not imply a product feature was demonstrated if the cut removes the demonstration. When the evidence does not fit the runtime, reduce the claim or request a different brief.

### 6. Modular timelines and dependency strategy

A useful timeline may be divided into modules such as hook, problem, proof, offer, qualifier, CTA and end card. Modules may be separate sequences, nested clips, markers, labeled tracks or documented sections. Choose a structure the team can understand and maintain.

Keep shared elements centralized only when a change should propagate to all derivatives. Examples include an approved logo asset or a legal line that must be identical. Keep format-specific composition and pacing local to each derivative. A linked graphic can prevent inconsistent copy but can also unintentionally change all outputs; understand the dependency before using it.

### 7. Version states must be explicit

A practical state model is:
- **WIP** — active working version, not for approval or publication.
- **REVIEW** — submitted for review; feedback pending.
- **CHANGES-REQUESTED** — reviewer requested specific changes.
- **RC** — release candidate undergoing final QC.
- **APPROVED** — accepted by the named authority for the specified scope.
- **RELEASED** — delivered/published through an authorized process.
- **SUPERSEDED** — replaced by a later identified version.
- **WITHDRAWN** — intentionally invalidated; do not use.

An approval is scoped: approval of the 9:16 Thai version does not automatically approve the 1:1 English version. A change after approval creates a new version and may invalidate previous QC evidence.

### 8. File naming and version identifiers

Use a stable, sortable convention. Example:
`CLIENT_CAMPAIGN_DESTINATION_RATIO_LANGUAGE_DURATION_v###_STATE_YYYYMMDD.ext`

Example fictional filename:
`NORTHSTAR_SPRING_FEED_9x16_TH_30s_v004_REVIEW_20261119.mp4`

Rules:
- use one agreed separator and spelling convention;
- avoid ambiguous labels such as `final-final2`, `new` or `latest`;
- use zero-padded version numbers if sorting lexically;
- distinguish project files from exports;
- keep a human-readable change log even when the editor has project history;
- do not encode sensitive personal information in filenames;
- never rename a file without updating its manifest or handoff record.

### 9. Change management and impact analysis

Every change request should answer:
1. Who requested it, and are they authorized?
2. What exact content or time range changes?
3. Why is the change needed, and what is the source of truth?
4. Which formats, languages, graphics, captions, project sequences and exports are affected?
5. Does the change alter facts, rights, privacy, safety, accessibility or the approved brief?
6. Who must approve the revised result?
7. Which regression checks must be repeated?

A request such as “make it more exciting” is not sufficiently testable. Convert it into a specific hypothesis or ask for examples and acceptance criteria. A request such as “change the price to 499” needs a currency, effective date, authoritative source and approval.

### 10. Backups, synchronization and collaboration

Version history is not a backup. A backup is a separate recoverable copy; synchronization may replicate deletion or corruption. A project package may depend on media, fonts, LUTs, plugins, motion templates and linked graphics. Record dependencies and verify portability on a second location or test machine when the project requires it.

For teams:
- define one owner for the canonical master;
- avoid simultaneous edits to the same project unless the tool supports controlled collaboration;
- communicate when a baseline is frozen;
- record handoffs and outstanding changes;
- use access controls and retention rules;
- do not put confidential source files in public repositories;
- protect credentials and private client information.

## Tools, requirements and alternatives

**Editing environment:** any non-linear editor that can duplicate sequences, manage media, set transforms, use markers and export specified formats. Menu names vary by product and release.

**Version tracking:** a spreadsheet or CSV is sufficient for a small campaign. A project-management issue tracker helps teams assign requests and approvals. Git can track text-based project metadata, scripts, manifests and documentation; it is generally not a substitute for a media asset manager for large binary video projects.

**Integrity checking:** use a trusted checksum utility when transfer integrity is required. Record algorithm, file identity and result. A matching checksum indicates byte-level identity, not creative correctness or legal approval.

**Storage:** use a primary working location plus a separate backup appropriate to the client's retention and security policy. Do not claim that cloud sync alone is a complete backup.

**Accessibility alternatives:** where a visual timeline or dense spreadsheet is difficult to use, provide a plain-text change log, labeled headings, keyboard-accessible tables or an accessible CSV export.

**Version caveat:** exact export settings, collaboration behavior, autosave, project recovery, media relinking and proxy behavior depend on editor/version and configuration. Verify against the installed version's official documentation.

## Procedure

### Phase A — Intake and specification freeze
1. Read the approved brief and list every required output.
2. Create a deliverable matrix with one row per format/language/runtime combination.
3. Record source media, rights, releases, music/stock licenses and factual claim sources.
4. Identify the authorized approver for editorial, factual, legal and brand elements.
5. Mark unknown requirements as TBC and resolve them before final export.
6. Assign a campaign ID and a version/naming convention.
7. Save a dated baseline of the brief and acceptance criteria.

### Phase B — Protect the master
8. Open the approved project and verify media links and sequence settings.
9. Save a protected copy or create a clearly named master sequence.
10. Record project filename, sequence name, runtime, frame rate, dimensions, audio configuration and current version.
11. Confirm the master is not overwritten by an export preset or batch process.
12. Duplicate the master into a derivative sequence for each target format.
13. Give every derivative a unique ID that maps to the deliverable matrix.

### Phase C — Adapt story and composition
14. Write the one-sentence message and essential proof for each derivative.
15. Create a beat map for each target runtime.
16. Identify material that can be removed without changing the claim or story.
17. Identify material that must remain: demonstration, safety warning, limitation, source context, attribution or CTA.
18. Reframe every shot for the target aspect ratio; do not assume one crop fits all shots.
19. Reposition graphics, logos, subtitles and CTA elements for the target viewing area.
20. Check movement, gaze, product details, screen text and other essential context.
21. Review language length and text timing separately for every localization.
22. Compare the derivative with the approved master for factual meaning and tone.

### Phase D — Pace and review
23. Review at normal playback speed, not only while scrubbing.
24. Measure the time available to understand each demonstration and read each key text element.
25. Remove redundant pauses only after checking their narrative function.
26. Ensure cuts do not create false cause/effect, misleading chronology or unsupported product claims.
27. Check opening, transitions, audio continuity and ending at the actual target runtime.
28. Ask a reviewer unfamiliar with the edit to summarize the message and identify the CTA.
29. Record feedback as discrete change requests, not vague untracked notes.

### Phase E — Change control and release candidate
30. Triage each request as accepted, rejected, deferred or clarification required.
31. Verify source-of-truth details for factual changes.
32. Complete an impact analysis across all affected derivatives and languages.
33. Save a new version before implementing approved changes.
34. Update the change log and record who authorized the change.
35. Re-export affected versions only; do not silently reuse stale exports.
36. Label the candidate RC and freeze the exact files submitted for QC.

### Phase F — QC, approval and handoff
37. Validate each file against its own specification and the manifest.
38. Play every candidate export completely; inspect captions, overlays, audio and ending.
39. Compare shared facts and brand elements across the full deliverable family.
40. Log defects with severity, timecode, version and retest result.
41. Resolve critical defects and obtain explicit disposition for major deviations.
42. Record approval by version, format, language and date.
43. Create final filenames and a release manifest.
44. Package editable project, dependencies, exports, rights records, change log and version notes.
45. Verify the package opens or is otherwise usable by the intended recipient; document anything that cannot be included.
46. Archive the approved release separately from active working files.

## Worked example

**Brief/input:** Fictional campaign for a reusable insulated bottle. The approved 45-second master explains a leak-resistant lid, demonstrates the locking mechanism and includes a qualified claim: “Keeps drinks cold for up to 12 hours under the stated test conditions.” The client requests:
- 30-second vertical English feed edit;
- 15-second vertical Thai story edit;
- 20-second square English product-page edit.

**Decision process:**
1. Preserve the 45-second approved master as baseline `MASTER_v003_APPROVED`.
2. Build three rows in the deliverable matrix. Each row has its own runtime, aspect ratio, language, CTA and export specification.
3. For the 30-second vertical edit, retain the problem, full locking demonstration, qualified temperature claim and CTA. Crop the hand and lid together; do not crop to the speaker's face alone.
4. For the 15-second Thai story edit, choose one clear demonstration and a shorter approved CTA. Do not imply that the full 12-hour test is shown. Translate the qualifier accurately and allow enough display time.
5. For the 20-second square product-page edit, keep product and hand movement centered in the square composition; include a longer close-up if the page audience needs feature inspection.
6. A late request changes the CTA URL. Create CR-007, verify the destination URL with the campaign owner, update all three derivatives and their end cards, then recheck QR/URL readability and spelling.
7. A price update is requested without a currency or effective date. Mark it blocked pending clarification; do not invent a price.
8. Export review candidates, inspect each complete file, and compare the claim, qualifier and CTA against the approved source.
9. Approve only the versions that passed. Record approval separately for each language/format.

**Expected output:** three distinct, traceable adaptations; an unchanged protected master; a complete change log; a manifest with exact filenames/specifications; QC and approval records. All campaign details above are fictional teaching data.

## Dry run / annotated walkthrough

Use this simulated change request:
- Baseline: `BOTTLE_MASTER_v003_APPROVED`
- Deliverables: `V30_9x16_EN`, `V15_9x16_TH`, `V20_1x1_EN`
- Request CR-007: “Change CTA from /spring to /summer.”
- Request CR-008: “Make the product colder and say 24 hours.”

**Trace:**
1. CR-007 has a specific proposed URL but still needs owner confirmation that the destination is live and approved.
2. If approved, impact analysis lists all three end cards, captions if the URL is spoken, QR codes, thumbnails and exports.
3. Create new versions for the affected derivatives; do not alter the approved baseline.
4. CR-008 changes a product-performance claim. It requires evidence and authorized approval. Without substantiation, reject or hold it.
5. A visual ice effect cannot be used to imply a tested performance claim. It may be a creative treatment only if it does not mislead.
6. Re-export affected files and compare all shared claims across the three outputs.
7. QC records each file's exact version and confirms no old URL remains.
8. The release manifest identifies which outputs are approved and which remain blocked.

## Guided practice

### Exercise 1 — Deliverable matrix
Create a matrix for one approved 30-second video requiring vertical 15 s, vertical 30 s, square 20 s and landscape 30 s outputs in two languages.

**Hints:** Use one row per unique combination. Record runtime, dimensions, language, captions, CTA, approver and status.

**Success criteria:** no combination is missing; every unknown is marked TBC; each version can be uniquely identified.

### Exercise 2 — Runtime budget
Prepare a 20-second story budget with hook, context, proof, qualifier and CTA.

**Hints:** Make the proof observable. Allocate enough time for the qualifier and CTA. If the total exceeds 20 seconds, simplify the promise rather than speeding every shot.

**Success criteria:** interval total equals 20 seconds; essential evidence and qualifiers remain.

### Exercise 3 — Adaptation map
Choose five shots from a landscape master and record the vertical crop, essential visual information, graphic movement and fallback if the crop fails.

**Success criteria:** every shot has a reasoned framing decision and an alternate plan.

### Exercise 4 — Change impact
A verified offer end date changes. Identify every place the date appears and the records that must be updated.

**Success criteria:** impact list includes all aspect ratios, languages, captions, end cards, metadata/description where supplied, thumbnails and queued exports.

### Exercise 5 — Handoff reconstruction
Give another learner only the manifest, change log and package tree. Ask them to identify the approved master, current release and superseded versions.

**Success criteria:** learner can identify authoritative files without guessing or opening every candidate.

## Independent assignment

Create a campaign family from one approved 30–60 second source edit.

**Required deliverables:**
1. One protected master and at least three adaptations with different aspect ratios or runtimes.
2. A deliverable matrix and per-output acceptance specification.
3. A beat map/runtime budget for each adaptation.
4. Shot-by-shot reframing and graphic/caption adaptation notes.
5. A version naming convention and version manifest.
6. At least three sample change requests, including one factual change that is held pending evidence.
7. A change-impact analysis showing which versions require rework.
8. A QC report for every export, with at least one deliberately seeded non-destructive test defect and documented retest.
9. A rights/source/approval record and handoff package tree.
10. A reflection explaining one creative trade-off and one risk avoided.

**Constraints:** use media you own, have permission to use or that is explicitly licensed for the exercise. Do not use a real person's image, voice, personal information or commercial claim without the required permission and evidence. Do not publish the outputs unless separately authorized.

**Submission evidence:** project/sequence screenshots or equivalent records, exported files or a clearly labeled simulated export report, matrix, logs, QC checklist and version history. If actual rendering is not possible, submit the full reproducible plan and label the output as not rendered.

## Common errors and recovery

| Symptom | Likely cause | Diagnosis | Safe recovery |
|---|---|---|---|
| One format has an old price or URL | Change applied to only one derivative | Search all project sequences and exports; compare manifest | Update affected derivatives from verified source; issue new versions and retest |
| Master changes unexpectedly | Derivative shares linked elements or same sequence | Compare baseline and project history | Restore baseline copy; isolate derivative dependencies |
| 15-second cut feels rushed | All original claims retained | Map proof and reading time | Reduce claim scope or select one proof point |
| Vertical crop hides the mechanism | Face-first or center-only crop | Inspect each shot at target size | Reframe around action; choose alternate shot or layout |
| Localized version ends later | Text expansion or slower narration | Compare language cue and timeline durations | Re-time, simplify with translator approval or revise runtime |
| Wrong export is delivered | Ambiguous filenames or stale manifest | Compare version IDs, metadata and checksum | Quarantine ambiguous files; rebuild manifest and resend correct release |
| Reviewer comments are lost | Feedback stored only in chat | Audit change log against messages | Transcribe actionable notes, confirm interpretation and disposition |
| Duplicate versions conflict | No single canonical owner | Inspect approvals and timestamps | Pause release; appoint owner and establish baseline |
| Project opens with missing assets | Dependencies not packaged | Open package in clean location | Relink authorized media; update dependency manifest |
| QC passed before final change | Change invalidated previous tests | Compare tested checksum/version with current candidate | Repeat all impacted checks on exact release candidate |

## Knowledge check

1. Explain the difference between a working master, approved master, derivative and release export.
2. Why is a deliverable matrix created before editing?
3. Name four reasons a shorter version may need a different story structure.
4. Why should a factual qualifier not be removed simply to meet a runtime?
5. What is the difference between a version label and an approval?
6. Which fields make a change request actionable?
7. Why is version history not the same as a backup?
8. When is it appropriate to share a graphic or nested sequence across derivatives?
9. How should a late factual claim change be handled?
10. What does a matching checksum prove, and what does it not prove?
11. Why must each localized version receive its own timing review?
12. What is a regression check?
13. When should a release candidate be frozen?
14. What evidence belongs in a professional handoff?

## Answer key / instructor guidance

1. The working master is the editable reference; the approved master is authorized for a defined scope; a derivative is a format-specific adaptation; a release export is the exact final file that passed QC and approval.
2. It reveals all unique outputs and requirements, preventing omissions and conflicting assumptions.
3. Different aspect ratio, runtime, audience context, proof needs, language length, CTA or platform placement.
4. Removing a qualifier can change the truth or scope of a claim and mislead viewers.
5. A version label identifies a file state; approval records an authorized decision about a specific version and scope.
6. Request ID, requester/authority, exact change, rationale/source, affected versions, due date, approval owner and status.
7. Version history may share the same storage failure or replicate deletion; a backup is a separate recoverable copy.
8. When the element is intentionally identical across formats and linked-update behavior is understood; format-specific placement should remain independent.
9. Hold the change, verify authoritative evidence and approval, analyze impact, create new versions, then rerun affected QC.
10. A matching checksum indicates byte-level identity to the compared reference; it does not prove correctness, rights, approval or playback quality.
11. Translation changes text length, line breaks, reading speed and sometimes meaning; timing must be checked in the target language.
12. A retest of previously working or affected areas after a change to detect regressions.
13. After approved changes are implemented and before final QC, so the tested file remains identifiable and unchanged during review.
14. Approved brief/specification, master and derivative identity, editable project/dependencies, exports, manifest, rights/source records, change/approval log, QC report, known limitations and archive location.

## Assessment rubric

<text> </text>
| Criterion | Points | Evidence |
|---|---:|---|
| Deliverable matrix and specification accuracy | 10 | Every output uniquely defined; unknowns explicit |
| Master protection and project architecture | 10 | Baseline identified; derivatives isolated; dependencies documented |
| Narrative adaptation and claim integrity | 15 | Message/evidence preserved; no misleading compression |
| Runtime budget and pacing decisions | 10 | Timing is reasoned; comprehension and CTA time considered |
| Format-specific composition | 10 | Shot-by-shot reframing and graphic/caption review |
| Version naming and manifest | 10 | Files traceable; status and identifiers consistent |
| Change control and impact analysis | 10 | Requests authorized, scoped and dispositioned |
| QC and regression evidence | 10 | Every candidate checked; defects/retests linked to exact version |
| Rights, privacy and approval records | 5 | Sources and permissions traceable |
| Handoff and reflection | 10 | Package is reconstructable; trade-offs and risks explained |
| **Total** | **100** | |

**Pass threshold:** 80/100. Mandatory gates: source/master not overwritten; no unsupported factual claim; no unlicensed asset; no critical defect; all release files trace to a specification and approval. A mandatory-gate failure prevents a pass regardless of numeric score.

## Quality-control checklist

- [ ] Every requested output has a matrix row and acceptance specification.
- [ ] The protected master is identified and unchanged.
- [ ] Every derivative has a distinct sequence/version identity.
- [ ] Story beats, evidence, qualifiers and CTA are appropriate to runtime.
- [ ] No cut creates misleading chronology, causality or claim scope.
- [ ] Reframing, graphics and captions are reviewed shot by shot and language by language.
- [ ] All factual values, dates, URLs and claims use approved sources.
- [ ] Version names, project sequence names, change log and manifest agree.
- [ ] The exact candidate export is identified and played in full.
- [ ] Technical metadata matches the relevant specification.
- [ ] Critical/major defects are resolved or formally dispositioned by an authorized owner.
- [ ] Regression checks cover all impacted versions and shared elements.
- [ ] Approval is recorded separately for each required scope.
- [ ] Project dependencies, rights records and handoff documentation are included.
- [ ] Archive copy is separated from active working files and is recoverable under the agreed process.

## Further study and references

- Adobe Help Center — official documentation for the specific Premiere Pro version in use: https://helpx.adobe.com/premiere-pro/user-guide.html
- Blackmagic Design — DaVinci Resolve official training and documentation: https://www.blackmagicdesign.com/products/davinciresolve/training
- Git documentation — version-control concepts and distributed history (use for text-based project records and scripts, not as a substitute for media asset management): https://git-scm.com/doc
- NIST — Secure Software Development Framework (SP 800-218), useful supplementary reading for controlled change, traceability and release discipline: https://csrc.nist.gov/pubs/sp/800/218/final
- Related CT-03 lessons: [Lesson 01 — Audience, Platform and Format Design](lesson-01-audience-platform-and-format-design.md); [Lesson 02 — Hooks, Story Compression and Retention](lesson-02-hooks-story-compression-and-retention.md); [Lesson 03 — Vertical Reframing, Captions and Safe Composition](lesson-03-vertical-reframing-captions-and-safe-composition.md).
- Related practice: [Lab 02 — Multi-Format Versioning and Batch Delivery](labs/lab-02-multi-format-versioning-and-batch-delivery.md); [Workbook Section 04 — Multi-Format Version Control](workbook/section-04-multi-format-version-control.md).

## Version and change notes

- Revision 2.0 — 2026-11-19: expanded the initial lesson into a full advanced academic lesson with deliverable planning, runtime/pacing theory, claim integrity, modular timeline design, version states, change impact, worked and dry-run examples, five guided exercises, independent assignment, troubleshooting, 14 answer-guided checks, 100-point rubric, mandatory gates and QC.
- Examples are fictional instructional data. No specific editor, platform or cloud service was executed or validated for this lesson.
- Platform requirements, editor features, codecs, export settings, licensing terms and client acceptance rules are version- and contract-dependent; verify the current authoritative source before use.
- Do not mark this lesson technically validated until an independent reviewer reproduces the relevant workflow and records the exact software/device versions and evidence.
