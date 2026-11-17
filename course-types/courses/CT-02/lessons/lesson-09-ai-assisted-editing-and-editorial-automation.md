# CT-02 Lesson 09 — AI-Assisted Editing and Editorial Automation

- Course: CT-02 — Film & Cinematic Editing
- Level: AI & Automation
- Estimated time: 6–8 hours
- Prerequisites: Lessons 01–08; ability to identify source media, timecode, editorial beats, continuity risks and delivery requirements
- Tools/environment: Optional transcription, media search, scene analysis, caption drafting, NLE scripting or workflow automation tools. A manual workflow is always an acceptable alternative.
- Software policy: Tool-independent. Record provider, product, model/tool version, date, settings and data-handling terms for any system used. No product availability, interface behavior or vendor privacy promise is assumed.
- Version/review date: 2.0 — 2026-11-17

## Learning outcomes

By the end of this lesson, learners can:

1. Decompose an editorial workflow into tasks that are suitable, unsuitable or conditionally suitable for automation, with reasons.
2. Define measurable acceptance criteria for an AI-assisted task before submitting media or text.
3. Complete a privacy, consent, rights, confidentiality and data-retention assessment before processing assets.
4. Design a small-sample test with a reference answer, error categories, review threshold and manual fallback.
5. Verify AI-generated transcripts, captions, translations, shot labels and edit suggestions against original media and context.
6. Preserve source IDs, source timecodes, tool/model/version, transformations, human corrections and approvals in a provenance record.
7. Distinguish deterministic automation from probabilistic model output and explain why confidence scores do not establish truth.
8. Produce a human-approved editorial result and a written limitations/risk report.

**Evidence standard:** Submit the task specification, risk assessment, test sample, reference data, error log, human review record, provenance ledger, final editorial decision and fallback plan. Simulated tests must be labeled simulated.

## Prerequisites and preparation

Learners should already understand:

- dramatic beats, audience point of view and performance context;
- screen geography, continuity, source timecode and synchronization;
- assembly, rough cut, fine cut, picture lock and finishing QC;
- rights, consent, confidentiality and the distinction between originals, proxies and exports.

Prepare a short, self-recorded or properly authorized clip. Avoid sensitive personal footage for initial exercises. If no AI tool is available or permitted, complete the same workflow manually and evaluate a hypothetical tool proposal using the decision framework below.

Before any external processing, identify the asset owner, people represented, contractual restrictions, intended purpose, data destination, retention/deletion controls, access permissions and whether the tool provider may retain or reuse submitted content. If these terms cannot be established, do not upload the media.

## Key definitions and terminology

| Term | Definition | Editorial context |
|---|---|---|
| Artificial intelligence (AI) | Broad class of computational systems performing tasks associated with human perception, prediction, language or decision-making | A category, not a guarantee of correctness |
| Machine learning (ML) | Methods that infer patterns from data to make predictions or generate outputs | May classify, rank, transcribe or detect |
| Generative AI | Systems that generate text, images, audio, video or other outputs from learned patterns and prompts | Useful for drafts; can invent plausible but false details |
| Speech-to-text (STT) | Automated conversion of speech audio into text | Transcript draft must be checked against audio |
| Speaker diarization | Estimation of which speaker is active at which time | Speaker labels can be wrong, especially with overlap |
| Scene/shot detection | Automated proposal of visual boundaries or shot changes | A cut detector does not understand story structure |
| Semantic search | Retrieval using descriptive meaning rather than only exact filenames | Search results are suggestions, not proof of relevance |
| Embedding | Numerical representation used to compare semantic similarity | Similarity is not factual equivalence |
| Proxy | Lower-resource media copy linked to original media | A proxy is not the camera original |
| Confidence score | A system-provided estimate of certainty under its own method | Not a calibrated guarantee unless validated for the task |
| Human-in-the-loop | Workflow where a person reviews and decides on consequential output | Human review must be meaningful, not a rubber stamp |
| Provenance | Record of asset origin, transformations, tools and decisions | Supports traceability and accountability |
| Deterministic automation | Same valid input and configuration produce the same defined operation | Examples: renaming from a fixed rule or copying a file |
| Probabilistic output | Output may vary or be uncertain even with similar inputs | Common in speech recognition and generative models |
| Hallucination | Plausible output unsupported by the supplied evidence | May insert names, dialogue or events that did not occur |
| Model drift | Change in output behavior over time due to model, data or configuration changes | Requires re-testing after updates |
| Prompt injection | Malicious or misleading content in an input that attempts to alter a model's behavior | Treat transcripts, captions and embedded text as untrusted data |
| Synthetic alteration | AI-generated or AI-modified media content | Must be disclosed and approved according to brief and policy |

## Purpose and professional relevance

AI can reduce repetitive work in transcription, logging, search, rough selects, caption drafts, translation drafts, metadata extraction and repetitive file operations. It can also introduce errors that are difficult to notice because the output appears fluent and confident.

An editorial workflow contains several kinds of judgment:

- **Mechanical:** repeatable operations with explicit inputs and outputs.
- **Perceptual:** recognizing speech, objects, shot changes or visual conditions.
- **Interpretive:** understanding motivation, tone, irony, implication and cultural context.
- **Ethical:** deciding whether a representation is fair, authorized and non-misleading.
- **Creative:** selecting performance, point of view, pacing and story meaning.

Automation is usually safest when the task is narrow, reversible, measurable and easy to inspect. Interpretive, ethical and creative decisions require accountable human judgment. A system may help find candidate material, but it does not become the editor, director, participant or rights holder.

## Theory and decision principles

### 1. Choose the task before choosing the tool

Do not begin with “Which AI tool should I use?” Begin with “What specific problem needs solving?”

A useful task statement identifies:
- input asset and permitted scope;
- requested operation;
- output format;
- intended user of the output;
- measurable acceptance criterion;
- foreseeable harm if the output is wrong;
- human approval point;
- fallback method.

Example: “Generate a draft transcript with source time references for a 5-minute authorized interview; a human will verify every selected quote against the original audio before editing.” This is more testable than “Use AI to edit the interview.”

### 2. Suitability matrix

| Task | Typical suitability | Required human control |
|---|---|---|
| Batch file naming from a fixed pattern | High, if tested on copies | Inspect preview and sample output; preserve original names |
| Proxy generation or checksum creation | High when deterministic tools and settings are known | Verify output and source mapping |
| Speech transcription | Conditional | Check every quote, names, numbers, negation, speaker and timing |
| Subtitle timing draft | Conditional | Verify timing, reading order, line breaks, meaning and accessibility |
| Translation draft | Conditional/high risk | Qualified language review for meaning, idiom, names and sensitive context |
| Shot/scene boundary proposals | Conditional | Inspect source frames and correct false positives |
| Semantic footage search | Conditional | Verify result against actual source and context |
| Music or sound generation | Conditional | Confirm rights, originality, brief fit, disclosure and licensing terms |
| Performance selection | Low as an autonomous decision | Human compares complete performance and dramatic context |
| Story structure or final pacing | Low as an autonomous decision | Human editor/director decides and documents rationale |
| Documentary fact verification | Not delegated to a generative model | Check primary evidence and context independently |
| Synthetic face/voice or identity alteration | High risk | Explicit informed consent, legal/contract review and clear disclosure; refuse if unauthorized |

Suitability depends on asset sensitivity, system design, quality, provider terms, project obligations and consequences of error. This table is a decision aid, not a blanket approval.

### 3. Establish a reference before evaluating output

A test without a reference cannot reliably measure accuracy. For transcription, create a verified human reference transcript for a representative short sample. For file operations, define expected filenames and folder structure. For scene detection, manually mark expected boundaries. For semantic search, write a set of known relevant and irrelevant examples.

Measure errors that matter to the task. A transcript may have high overall word accuracy yet miss the word “not,” a person's name or a key number. Therefore, aggregate scores must not replace critical-error review.

### 4. Risk is more than accuracy

Assess at least these risk dimensions:

- privacy and confidentiality;
- rights, licenses and participant consent;
- misrepresentation, defamation or factual distortion;
- cultural, language and accessibility bias;
- security and unauthorized access;
- provider retention, reuse and cross-border processing;
- provenance loss and inability to reproduce;
- cost, latency, service dependency and vendor change;
- downstream harm if a wrong output is published.

Higher-impact tasks require stronger controls, narrower permissions, more independent review and clearer approval. If risk cannot be reduced to an acceptable level, use a manual process or do not perform the task.

### 5. Keep originals and reversible states

Never let an AI tool overwrite camera originals, source audio, the only project file or an approved master. Work from authorized copies, proxies or exports. Keep generated material in a separate, labeled location. Record transformations and retain the source reference.

### 6. Human review must be substantive

A reviewer must have enough context, time, competence and access to the source to challenge the output. “Human approved” is not meaningful if the person only clicks accept or cannot hear the original audio. Define what the reviewer checks and what errors require rejection.

### 7. Provenance is not proof of truth

A provenance record can document which tools and edits were declared and may support tamper-evident history. It does not prove that the depicted event is true, that the source is complete, that the editor's interpretation is fair or that every transformation was captured. Treat provenance as one evidence layer, not a truth certificate.

## Tools, requirements and alternatives

| Category | Example use | Verification requirement | Manual/low-tech alternative |
|---|---|---|---|
| Transcription system | Draft dialogue transcript | Compare with verified audio; check critical words and speakers | Human transcript with time references |
| Captioning system | Draft subtitle file | Check text, timing, speaker identity, reading speed and format | Manual caption authoring |
| Scene detector | Suggest cut boundaries | Inspect frames around every proposed boundary | Frame-by-frame review or shot log |
| Semantic search | Find a described object/action | Open source clip and verify context | Filename, metadata and human logging |
| NLE scripting/macros | Repeat known timeline/file operations | Test on duplicate project and small fixture | Manual checklist |
| Batch automation | Rename, copy, checksum or organize files | Dry run, collision detection, log and rollback | Manual controlled file operations |
| Generative assistant | Draft notes, summaries or shot descriptions | Verify every factual claim against sources | Human-written notes |
| Provenance utility | Record declared creation/edit history | Validate the manifest and understand coverage limits | Signed change log and file manifest |

Do not assume a named feature exists in a particular application, edition, operating system or version. Before a software-specific procedure is published or used, verify official documentation for the exact release and run a non-destructive test with expected output. This lesson deliberately uses tool-independent steps.

## Reproducible procedure

### Phase A — Define the task and acceptance test

1. Write one task statement using the input, operation, output, purpose and human decision point.
2. Define the smallest useful scope, such as a 30–60 second sample or one scene.
3. Identify critical errors. For transcription these may include negation, names, numbers, speaker attribution and omitted speech.
4. Define measurable acceptance criteria before running the tool.
5. Define a stop condition, such as any unauthorized data transfer, repeated critical errors or inability to trace output to source.
6. Name the person responsible for final approval.

**Exit evidence:** task specification, error taxonomy, acceptance threshold and stop condition.

### Phase B — Complete rights, privacy and data review

1. Identify who owns or controls the source media.
2. Confirm releases, consent, license scope and contractual restrictions for the intended processing.
3. Determine whether the asset contains personal, confidential, privileged, biometric, location or commercially sensitive information.
4. Identify the tool provider, model/version, processing location if disclosed, retention policy, training/reuse terms, subprocessors and deletion controls.
5. Confirm whether external upload is explicitly authorized. A public link or a free account does not imply permission.
6. Limit access, duration, resolution and content to the minimum necessary.
7. Prefer an approved local/offline workflow for sensitive media where practical, while still checking local software security and access.
8. Record the decision: approved, approved with controls, manual-only or prohibited.
9. If terms are unclear or consent is missing, stop and use an authorized alternative.

**Exit evidence:** completed risk record and documented processing decision.

### Phase C — Prepare and test a representative sample

1. Duplicate or export a small, authorized sample; preserve the original.
2. Record source ID, source in/out, frame rate or audio sample rate where relevant, language and known recording conditions.
3. Create a verified reference answer or expected result.
4. Run the selected tool with recorded settings.
5. Save raw output unchanged before making corrections.
6. Compare output with the reference and classify errors: omission, substitution, insertion, timing, speaker, language, context, identity or formatting.
7. Count critical errors separately from minor errors.
8. Evaluate whether the acceptance threshold is met. If not, adjust settings or reject the tool for this task.
9. Repeat the test after material changes to provider, model, prompt, settings or input conditions.

**Exit evidence:** sample, reference, raw output, error log, decision and tested configuration.

### Phase D — Process the authorized scope

1. Confirm the sample test passed and the processing decision remains valid.
2. Process only the approved media and purpose.
3. Keep source IDs and time references attached to every result.
4. Store raw output separately from human-corrected output.
5. Record interruptions, failed files, low-confidence regions and unavailable results.
6. Do not treat a generated summary as a source transcript or a generated shot label as a verified event.
7. Do not permit automated operations to overwrite originals or approved sequences.
8. If the system generates synthetic picture, voice, performance or music, stop for the specific consent, rights, disclosure and approval checks before use.

### Phase E — Human verification and editorial decision

1. Open the original source, not only the AI output.
2. Verify every excerpt intended for publication or use in a final edit.
3. Check full question/answer context, negation, names, numbers, speaker identity, emotional tone and pauses.
4. Inspect suggested shot boundaries and semantic search results in the original footage.
5. Correct errors while preserving the raw output and recording the correction.
6. Ask a second qualified reviewer for high-impact factual, translation, identity or sensitive-content decisions.
7. Decide whether to accept, revise or reject each suggestion.
8. Make final story, performance, pacing and representation choices as the authorized human editor/director.
9. Review the final timeline for sync, continuity, rights and unintended synthetic changes.

### Phase F — Provenance, disclosure and fallback

1. Record source asset IDs and the exact ranges processed.
2. Record tool/provider, model or application version, date, settings, prompts or automation rules where appropriate, and output location.
3. Record raw output hash or file identity when practical.
4. Record human corrections, reviewer, approval and unresolved uncertainty.
5. Record whether generated content is included in the final deliverable and what disclosure the brief, law, platform or client requires.
6. Keep a manual fallback that can complete the critical workflow if the tool fails or becomes unavailable.
7. Archive only authorized data and apply the project's retention/deletion policy.
8. Re-run relevant QC after any automated change to the timeline or media.

## Worked example — Interview quote selection

**Brief:** An editor must find a short answer in a 12-minute authorized interview. The intended quote concerns whether a project was approved. The interview includes room noise and overlapping speech.

**Task specification:** Produce a draft transcript with time references to locate candidate answers. No automated transcript may be used as final dialogue without listening to the source.

**Sample test:** A 60-second segment is transcribed. The verified reference shows the speaker said, “We did not approve the second version.” The draft transcript omits “not.”

**Diagnosis:** This is a critical semantic error even if the rest of the transcript is accurate. A search for “approve” could return the passage but reverse its meaning.

**Recovery:** Correct the transcript against the audio, mark the tool output as rejected for that phrase, and search the complete question and answer. Listen before and after the selected range. Preserve the original audio and the raw transcript. Record the correction, reviewer and source time references.

**Editorial decision:** The editor chooses whether the quote belongs in the story only after considering the complete answer and surrounding context. The transcript is a navigation aid, not the authority.

**Expected result:** a traceable candidate quote with verified words, source time references, context and a documented human decision.

## Dry run / annotated walkthrough

Use a 60-second self-recorded clip containing two speakers, one proper name, one number, a pause and a sentence containing “not.” Do not use sensitive content.

| Stage | Input/state | Action | Check / expected evidence |
|---|---|---|---|
| 1. Prepare | Original recording | Create a working copy and note source ID | Original remains unchanged |
| 2. Reference | Audio | Manually transcribe exact words and approximate time references | Reference is checked by listening |
| 3. Test | 60-second copy | Generate a draft transcript using an approved method | Tool/model/settings recorded |
| 4. Compare | Reference + draft | Mark omissions, substitutions, insertions, speaker and timing errors | Error log with counts and severity |
| 5. Correct | Raw draft | Create corrected transcript as a separate version | Every correction traceable |
| 6. Review | Original audio + corrected transcript | Listen to each intended excerpt in context | No unverified quote accepted |
| 7. Decide | Verified candidates | Select or reject the excerpt | Human rationale recorded |
| 8. Archive | Source, raw, corrected, log | Save only authorized records | Retention and access noted |

**Dry-run questions:** Did the system preserve “not”? Did it assign the proper name and number correctly? Did it split overlapping speakers? Did it shift time references? If no reference transcript exists, do not claim a word-accuracy percentage.

## Guided practice

### Exercise A — Task suitability (30 minutes)

Choose three editorial tasks: one mechanical, one perceptual and one creative. For each, write the input, operation, output, error impact, acceptance test, human decision point and manual fallback. Explain why the tool should or should not be used.

**Success criteria:** all three tasks have measurable tests; creative authority remains with the editor/director; no sensitive data is processed without permission.

### Exercise B — Transcript verification (60 minutes)

Use a 2–3 minute authorized clip or your own recording.

1. Create a verified reference transcript for a 30–60 second sample.
2. Generate a draft transcript only if a permitted tool is available.
3. Compare and classify errors.
4. Correct all content intended for use.
5. Record critical errors separately.
6. Select one excerpt and verify the full surrounding context.

**Success criteria:** every used word is checked against source audio; raw and corrected transcripts are separate; source time references are retained.

### Exercise C — Automation safety test (45 minutes)

Design a batch operation such as filename normalization or checksum generation. Use a duplicate test folder with at least six dummy files, including two names that could collide.

1. Write the expected output before execution.
2. Create a dry-run report.
3. Check collisions and missing inputs.
4. Execute only on the test copy if the tool is available.
5. Compare actual output with expected output.
6. Demonstrate rollback or a manual recovery path.

**Success criteria:** originals remain untouched; collisions are detected; the output can be independently checked.

### Exercise D — Provenance ledger (30 minutes)

Complete a ledger for one AI-assisted or simulated task. Include asset IDs, ranges, purpose, tool/version, date, settings, raw output, corrections, reviewer, decision, disclosure and retention status.

**Success criteria:** another editor can trace every suggestion to its source and understand what the system did not verify.

## Independent assignment — Human-controlled editorial automation plan

Design an AI-assisted workflow for a 3–5 minute scene or interview. You may implement a narrow, authorized task or submit a fully specified manual simulation.

### Required deliverables

1. Task statement and process map.
2. Suitability decision with reasons.
3. Rights, consent, privacy and provider-term risk assessment.
4. Sample test plan and reference answer.
5. Raw output and categorized error log, or a clearly labeled simulation.
6. Human correction/review record.
7. Provenance ledger and version record.
8. Final editorial decision with rationale.
9. Manual fallback and failure/rollback plan.
10. Disclosure statement or reason disclosure is not applicable.
11. Reflection (500–800 words) describing benefits, limitations, errors and decisions not delegated.

### Submission rules

- Do not upload private or third-party footage without authorization.
- Do not use a synthetic voice, likeness, performance or music without the necessary rights and informed consent.
- Do not claim a model is accurate based on one short test.
- Do not report a simulated test as executed.
- Do not equate a confidence score, watermark or provenance manifest with truth.
- If no suitable tool is available, complete the risk and design work without uploading assets.

## Common errors, diagnosis and recovery

| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Transcript changes the meaning | Omitted negation, overlap or noise | Listen to original around the time reference | Correct manually and reject affected output |
| Speaker labels are wrong | Similar voices or overlapping dialogue | Compare voice, camera and context | Relabel only after source review |
| Names and numbers are inaccurate | Unfamiliar vocabulary or model bias | Check spelling against authorized reference | Correct and flag high-impact fields |
| Search returns irrelevant clips | Prompt/query too broad or embeddings lack context | Inspect source clips and refine criteria | Use narrower query and manual logging |
| Scene detector misses cuts | Flash, dissolve, camera movement or low contrast | Inspect source frames around boundaries | Correct boundaries manually |
| Automation renames wrong files | Collision or ambiguous pattern | Compare dry-run and manifest | Stop, restore from copy and revise rule |
| Model behavior changes | Provider/model/settings changed | Compare version and test records | Re-run validation before production use |
| Sensitive material was uploaded | Permission review omitted | Stop processing and follow incident policy | Notify authorized owner; request deletion where possible; document incident |
| Generated summary invents facts | Model fills gaps with plausible text | Trace each claim to source | Remove unsupported claims; use verified notes |
| Provenance is incomplete | Some transformations were not recorded | Compare source, logs and export history | Document known gaps; never claim complete history |

## Knowledge check

1. Why should a task be defined before selecting an AI tool?
2. Name four factors to check before uploading source footage.
3. Why is a reference answer required for meaningful accuracy evaluation?
4. Give three examples of critical transcription errors.
5. Explain the difference between deterministic automation and probabilistic output.
6. Why is a confidence score not proof that a transcript is correct?
7. What is the difference between raw model output and a human-corrected transcript?
8. Why must every edit suggestion retain source IDs and time references?
9. Which editorial decisions should remain under authorized human control?
10. What should happen when provider retention or reuse terms cannot be established?
11. Does a valid provenance manifest prove that a video depicts a true event?
12. Name five fields in a useful provenance ledger.
13. When should a sample test be repeated?
14. Why is a manual fallback part of a professional automation plan?

## Answer key and instructor guidance

1. A narrow task and measurable output prevent tool-led experimentation from expanding beyond the brief and make evaluation possible.
2. Ownership/rights, participant consent, confidentiality, provider retention/reuse, processing location, access and deletion terms are valid answers.
3. Without a reference, the learner cannot distinguish correct output from plausible output or calculate meaningful error rates.
4. Missing “not,” incorrect name, wrong number, wrong speaker, omitted phrase or shifted time reference.
5. Deterministic automation performs a defined operation consistently for valid inputs; probabilistic systems can vary and require evaluation.
6. It is a system-specific estimate and may not be calibrated to the task or critical error type.
7. Raw output is preserved as generated; corrected output contains traceable human changes.
8. Traceability lets the editor retrieve source material, verify context and reproduce or reject a suggestion.
9. Story meaning, performance, pacing, factual representation, ethical decisions and final approval.
10. Do not upload; seek approved terms or use a permitted local/manual alternative.
11. No. Provenance can support origin and change history but does not establish factual truth or completeness.
12. Asset ID, range/timecode, purpose, tool/model/version, date/settings, raw output, correction, reviewer, approval, disclosure or retention.
13. After material changes to model/provider, settings, prompts, input conditions or task scope.
14. It protects continuity of work, prevents lock-in and ensures critical work can be completed if the system fails.
 
**Instructor guidance:** Require reasoning tied to the scenario. A learner who reports simulated execution as real, ignores consent, or delegates final factual/creative approval fails the professional-process gate regardless of score.

## Assessment rubric (100 points)

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Task definition and suitability | 15 | Narrow purpose, inputs, output, measurable criteria and justified task choice |
| Rights, privacy and risk assessment | 20 | Ownership, consent, confidentiality, provider terms, minimization and stop condition |
| Test design and reproducibility | 15 | Representative sample, reference answer, recorded configuration and repeatable procedure |
| Output verification and error analysis | 20 | Source-based checks, critical-error handling, corrections and limitations |
| Provenance and human approval | 15 | Traceable source IDs, transformations, reviewer, decision and disclosure |
| Fallback and professional reflection | 15 | Safe manual alternative, rollback, failure handling and reasoned evaluation |
| **Total** | **100** | |

**Pass threshold:** 80/100. Unauthorized sensitive upload, fabricated test results, unapproved synthetic identity alteration or false claims of human verification are critical failures regardless of score.

**Remediation:** Repeat the privacy/risk gate first for any critical failure. Otherwise improve the lowest-scoring section, rerun the sample test where possible and submit corrected provenance and review evidence.

## Quality-control checklist

### Task and test
- [ ] Task is narrow, relevant and measurable.
- [ ] Acceptance criteria and critical errors are defined before processing.
- [ ] Reference data is verified and representative.
- [ ] Provider/model/tool version and settings are recorded.
- [ ] Output errors are categorized and critical errors separately reported.

### Rights, privacy and security
- [ ] Asset ownership, license and consent are confirmed.
- [ ] Confidentiality and personal data are assessed.
- [ ] Provider retention, reuse and deletion terms are checked.
- [ ] Data minimization and access controls are applied.
- [ ] Unclear or unauthorized processing is stopped.

### Editorial and provenance
- [ ] Originals remain unchanged.
- [ ] Raw output and corrected output are separate.
- [ ] Source IDs and time references remain attached.
- [ ] Every used transcript/translation/selection is checked against source.
- [ ] Human editor/director makes final creative and factual decisions.
- [ ] Synthetic changes and disclosure requirements are addressed.
- [ ] Provenance gaps and uncertainty are reported.

### Delivery and maintenance
- [ ] Manual fallback and rollback exist.
- [ ] Model/provider changes trigger re-testing.
- [ ] Final timeline is checked for sync, continuity and rights.
- [ ] Retention and deletion follow project authorization.
- [ ] Simulation and actual execution are clearly distinguished.

## Further study and references

### Primary course resources
- [CT-02 Academic Textbook — Chapter 11: AI-Assisted Film Editing and Automation](../CT-02-FILM-CINEMATIC-EDITING-TEXTBOOK.md)
- [CT-02 Student Notes & Practical Workbook](../CT-02-STUDENT-NOTES-WORKBOOK.md)
- [Lesson 03 — Shot Coverage, Performance and Editorial Choice](lesson-03-coverage-and-performance.md)
- [Lesson 07 — Assembly, Rough Cut, Fine Cut and Picture Lock](lesson-07-assembly-rough-cut-fine-cut-picture-lock.md)
- [Lesson 08 — Finishing, Delivery and Quality Control](lesson-08-finishing-delivery-and-quality-control.md)
- [PCMDK369 Professional Academic Standard](../../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md)

### External references
- Autio, C. et al. (2024). [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)](https://doi.org/10.6028/NIST.AI.600-1). National Institute of Standards and Technology. A risk-management resource, not a film-editing product endorsement.
- National Institute of Standards and Technology. [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Framework and resources for managing AI risks.
- Coalition for Content Provenance and Authenticity. [C2PA Specifications](https://spec.c2pa.org/). Technical specifications and guidance for media provenance. Provenance is not a truth judgment.
- Coalition for Content Provenance and Authenticity. [Content Credentials Technical Specification, version 2.5](https://spec.c2pa.org/specifications/specifications/2.5/specs/C2PA_Specification.html). Consult the current specification and implementation guidance; adoption and feature support vary.

External frameworks support risk and provenance concepts. They do not replace the project's contracts, privacy policy, rights review or human editorial approval.

## Version and change notes

- **2.0 — 2026-11-17:** Expanded the working draft into a full academic lesson with measurable outcomes, prerequisites, terminology, suitability theory, risk assessment, tool alternatives, six-phase procedure, worked transcript example, annotated dry run, four guided exercises, independent workflow assignment, troubleshooting, 14 answer-guided knowledge checks, 100-point rubric, QC gates and authoritative references.
- Tool-independent by design. No AI provider, model, NLE feature, upload, transcript, media render or automated edit was executed for this lesson.
- Software/provider terms, model behavior and data policies change. Recheck the exact version and current terms before every real production use.
- **Next review:** independent AI-risk, privacy, editorial and accessibility review; practical test using authorized non-sensitive footage and a documented tool/version.
