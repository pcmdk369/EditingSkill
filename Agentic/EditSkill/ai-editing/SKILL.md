---
name: editskill-ai-editing
description: Specialist agent instructions for ai editing within the universal EditSkill architecture.
---

# AI Editing — EditSkill Specialist Module

## Scope
Use AI for assistive generation, cleanup, segmentation, tracking, transcription, translation, enhancement and media organization.

## Core principles
Treat model output as a draft; verify factual, linguistic and visual accuracy; disclose synthetic changes when appropriate; protect private source assets.

## Task procedure
Choose a task-specific model/tool; confirm data handling and rights; run a small test; compare against source; correct manually; document model and settings.

## Quality-control requirements
Human-review faces, voices, text, translation, temporal consistency, artifacts, provenance and rights; never assume model confidence equals correctness.

## Required task record
For substantial work, record the brief, assumptions, source assets, rights/consent notes, selected software and version, key settings, steps performed, output paths, validation evidence and unresolved issues.

## Boundaries
- Load `../SKILL.md` for universal execution, safety and reporting rules.
- Consult the matching course in `../../../../course-types/courses/` and existing repository references before inventing a new teaching sequence.
- Do not claim execution or successful export without tool confirmation.
- Preserve originals and request authorization before destructive, paid or externally published actions.
- If required tooling is unavailable, provide reproducible user-executable steps and clearly label them as instructions.

## Handoff
State inputs consumed, operations completed, output specification, QC result, known limitations and the next required human decision.

## PCMDK369™ academic and professional module compliance
This specialist module is governed by the [repository-wide Professional Developer & Academic Course Standard](../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md) and [agent module requirements](../references/course-standard.md). For teaching requests, use the shared academic lesson structure and provide measurable outcomes, prerequisites, definitions, theory, verified tools/alternatives, reproducible steps, worked examples, practice, troubleshooting, assessment evidence and QC. For implementation requests, document the brief, environment/version, inputs and rights, architecture, safe procedure, expected outputs, validation tests, recovery and handoff. Include discipline-specific risks and quality criteria; preserve human approval for consequential or external actions. Report actual evidence and limitations without inventing tool execution or test results.


## Responsible AI workflow and evaluation gates

### Task suitability
Use AI for bounded assistive tasks such as transcript drafts, scene labels, object/shot search, rough selects, cleanup suggestions and format adaptation. Do not delegate factual truth, consent, rights clearance, identity verification or final editorial approval to a model.

### Pre-processing gate
- Confirm source ownership/permission and participant consent.
- Classify confidentiality and personal data.
- Review provider retention, training, access, processing location, commercial terms and deletion controls.
- Record model/provider/version, date, settings and input identifiers.
- Prefer local processing for sensitive media when feasible and authorized.

### Evaluation method
Create a small representative test set with known expected outcomes. Measure error types: omissions, false detections, hallucinated words, identity/attribution errors, temporal flicker, geometry drift, text corruption and context loss. Include negative examples and uncertain cases.

### Human review matrix
| Output | Required review |
|---|---|
| Transcript/translation | Full source comparison and fluent reviewer |
| Highlight/select | Full context and factual integrity |
| Face/voice operation | Explicit rights/consent and identity safety |
| Generative extension | Frame-by-frame continuity and disclosure |
| Product/image change | Compare with authoritative product/source facts |
| QC classification | Confirm false positives and false negatives |

### Provenance record
Store source asset ID, tool/model/version, task/prompt or settings where safe, generated draft ID, manual corrections, reviewer, approval and final output ID. Do not store sensitive prompts or raw personal data unnecessarily.

### Release gate
Block release for unauthorized uploads, deceptive impersonation, fabricated evidence, materially misleading product details, unreviewed factual text or unresolved rights. Provide a human-created alternative when AI is unsuitable.
