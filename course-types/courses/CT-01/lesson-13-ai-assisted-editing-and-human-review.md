# CT-01 — AI & Automation: AI-Assisted Editing, Automation and Human Review

**Course:** Video Editing  
**Pathway stage:** AI & Automation

## Learning outcomes
Use AI to accelerate transcription, logging, search and rough-cut preparation; distinguish suggestions from verified facts; design safe automation; protect consent and privacy; validate generated or transformed content.

## Prerequisites
Lessons 01–12; familiarity with project folders and versioning.

## Key definitions
- AI-assisted editing: use of machine-learning tools to support parts of the editorial workflow.
- Speech-to-text (ASR): automatic conversion of speech into text.
- Speaker diarization: automated estimation of who spoke when.
- Semantic search: finding media based on described meaning rather than only filename.
- Generative AI: models that produce new text, images, audio or video from prompts or other inputs.
- Human-in-the-loop: workflow where a person reviews or approves model outputs.
- Provenance: record of where media came from and how it was changed.
- Hallucination: plausible-sounding but unsupported model output.
- Automation: repeatable execution of defined operations with limited manual intervention.

## Why it matters
AI can reduce repetitive work, but it can mishear speech, misidentify speakers, invent context, alter faces/voices or produce technically invalid media. Human review and traceable source links are essential.

## Theory
Use AI first for assistive, reversible tasks: transcription drafts, rough logging, shot descriptions, search terms, caption drafts and version checklists. Treat outputs as hypotheses. Verify quotes against source audio and check timecodes against the media.

Do not upload confidential or personal media to a service unless the project owner has approved the service, data handling and retention terms. Obtain informed consent for voice cloning, face manipulation or synthetic likeness. Do not impersonate people or create deceptive evidence. Clearly disclose synthetic or materially altered media when required by law, platform rules or the audience context.

## Tools and alternatives
NLE transcription/search tools, local transcription models, authorized cloud services, spreadsheets and scripts. A manual transcript and shot log remain valid alternatives. Tool availability, model behavior and privacy terms change; check current documentation and settings before use.

## Procedure
1. Identify a repetitive task and define measurable success criteria.
2. Confirm rights, consent, confidentiality and data-transfer approval.
3. Preserve the original media and create a working copy.
4. Select an AI tool whose supported input, output and privacy controls meet the project requirements.
5. Generate a transcript or media log with source identifiers and time references where supported.
6. Review every important quote, name, speaker attribution and caption against the original.
7. Ask AI for candidate selects or edit suggestions, not final editorial truth.
8. Rebuild the suggested edit using verified source timecodes.
9. Keep AI-generated assets separate and label their provenance.
10. Run technical QC on every generated or transformed asset.
11. Record tool/model, date, settings, human corrections and unresolved limitations.
12. Obtain required approvals before publishing.

## Worked example
An interview transcript labels a speaker as “Maya,” but the audio is unclear. Do not publish the name based on diarization alone. Check the slate, approved interview notes or ask the authorized producer. Correct the transcript and record the human verification.

## Dry run
Run transcription on a short self-recorded clip. Create a table with timestamp, model transcript, verified transcript and correction reason. Count word errors and missed speaker changes to assess whether the tool is useful for this recording type.

## Guided exercise
Generate a transcript and candidate selects from a rights-cleared interview. Verify ten quotes against the source and log every correction.

## Independent assignment
Design an AI-assisted workflow for a 3-minute interview. Submit a process map, privacy/consent check, original-to-output traceability, human review log, corrected transcript and final edit.

## Common errors and recovery
- AI invents a quote: verify against original media; remove unsupported text.
- Wrong speaker label: confirm identity through an authorized source; correct or mark unknown.
- Timecodes drift: compare against source frame/timebase and regenerate or manually correct.
- Sensitive footage uploaded without approval: stop processing, follow the service's deletion/reporting process and notify the project owner.
- Synthetic voice lacks consent: do not use it; obtain explicit authorization or use a non-imitative alternative.
- Automated edit removes context: restore source context and re-evaluate editorial fairness.

## Knowledge check
1. Why is AI transcription a draft?
2. What is provenance?
3. What does human-in-the-loop mean?
4. Name two risks of cloud processing.
5. What must be checked before voice cloning or face manipulation?

## Answer key
1. Recognition can mishear words, names, timing and speakers.
2. Record of source origin and transformations.
3. A person reviews and approves model outputs.
4. Confidentiality/privacy exposure and retention or jurisdiction concerns.
5. Informed consent, rights, lawful purpose and required disclosure.

## Assessment rubric — 30 points
Workflow suitability 5; privacy/rights safeguards 7; transcript/quote verification 6; traceability 5; human editorial judgment 4; technical QC 3. Pass 24/30.

## Quality-control checklist
- [ ] Original media preserved.
- [ ] Data transfer approved.
- [ ] Consent and rights checked.
- [ ] Names, quotes and timecodes verified.
- [ ] AI assets labeled and traceable.
- [ ] Human reviewer approved final content.
- [ ] Required disclosure completed.

## Further study
Study model evaluation, local inference, data retention, copyright, synthetic media disclosure and reproducible prompt/version logs.
