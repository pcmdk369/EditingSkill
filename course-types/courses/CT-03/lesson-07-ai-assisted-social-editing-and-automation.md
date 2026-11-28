# CT-03 Lesson 07 — AI-Assisted Social Editing and Responsible Automation

- Course: CT-03 — Short-Form & Social Video Editing
- Level: AI & Automation
- Estimated time: 180 minutes
- Prerequisites: Lessons 01–06; working short-form project and asset manifest
- Tools/environment: Optional transcription, scene detection, editing or automation tools; record vendor, model/tool and version
- Version/review date: Tool-neutral; verify current service terms and platform policies

## Learning outcomes
Learners can select suitable AI-assisted tasks, assess generated outputs, design a human-reviewed workflow, and document provenance, consent, privacy and failure handling.

## Key definitions
| Term | Definition | Context |
|---|---|---|
| AI-assisted operation | A task where a model proposes or transforms media/content | Transcript draft |
| Automation | Rule-based or model-assisted execution of repeatable steps | Batch naming |
| Provenance | Record of where media came from and how it was changed | Asset manifest |
| Human-in-the-loop | Required human review/approval before consequential use | Caption approval |
| Model hallucination | Plausible but unsupported generated output | Invented transcript word |
| Consent | Informed permission for a defined use | Voice processing |
| Reversibility | Ability to undo or recover from an operation | Non-destructive draft |

## Purpose and theory
AI can accelerate transcription, scene search, rough selects, caption drafts, reframing suggestions and version generation. It can also introduce false words, inaccurate translations, continuity errors, fabricated context, privacy risks and licensing uncertainty. Automation should reduce repetitive effort without transferring creative or factual accountability to a model.

## Tool selection
Before using a service, confirm actual availability, supported formats, retention/training terms, processing location where relevant, commercial rights, cost and export limitations. Prefer local processing for sensitive media when feasible. Never upload private footage, unreleased campaigns or identifiable voice recordings to an external service without authorization.

## Procedure
1. Identify the task and define why automation is useful.
2. Classify input sensitivity and rights/consent status.
3. Check service terms, cost, privacy, data retention and permitted use.
4. Create a copy of the project and retain original media.
5. Use AI for a bounded draft task such as transcription or scene labels.
6. Record tool/provider, model/version, date and input asset identifiers.
7. Review every factual statement, name, number, caption, translation and suggested cut against source media.
8. Reject fabricated or context-distorting suggestions.
9. Require human approval for voice/face synthesis, factual claims and public-facing creative decisions.
10. Run automated output checks, then human QC.
11. Store prompts/settings only when safe and useful; avoid exposing personal or confidential data.
12. Document what was generated, manually corrected and approved.

## Worked example
A speech-to-text service produces a draft transcript for a 30-second interview. The editor checks every cue against the recording, corrects names and numbers, then synchronizes captions. The transcript is labeled machine-generated draft until reviewed. No synthetic voice is used.

## Dry run
An AI highlight tool selects a sentence that sounds dramatic but removes the interviewee's qualifying statement. Compare the full context and reject the clip. Record why the automated selection was misleading. The tool's confidence score does not replace contextual review.

## Guided practice
Use a non-sensitive, learner-created clip to compare manual transcription with an AI draft. Measure correction time and error types. Do not use real personal data or upload third-party footage without permission.

## Independent assignment
Design an AI-assisted workflow with a data-flow diagram, tool risk assessment, human approval gates, error taxonomy, provenance log and validated deliverable.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Wrong caption | ASR error | Listen to source | Correct and review all cues |
| Misleading highlight | Missing context | Inspect full source passage | Restore context or reject |
| Unauthorized upload | Intake omitted consent check | Audit data flow | Stop processing, follow incident policy |
| Synthetic voice unclear | Consent or disclosure absent | Check authorization and context | Do not publish; obtain approval or use original voice |
| Automation overwrites master | Destructive pipeline | Inspect output path | Restore backup and use separate output directory |

## Knowledge check
1. Why is AI output a draft rather than ground truth?
2. What should be checked before external media upload?
3. What is provenance?
4. Why is context review essential for highlight extraction?
5. Which tasks require human approval?

## Answer guidance
1. Models can produce plausible errors and lack full editorial context.
2. Rights, consent, privacy terms, retention, cost and permitted use.
3. Record of origin and transformations.
4. A short excerpt can reverse or distort meaning.
5. Factual claims, translations, voice/face synthesis, sensitive edits and final publication decisions.

## Assessment rubric — 30 points
Task selection 5; privacy/rights assessment 6; human review design 7; provenance 5; validation and fallback 7. Pass: 24/30; unauthorized processing is a critical failure.

## QC checklist
- [ ] Input assets are authorized.
- [ ] Provider terms and privacy reviewed.
- [ ] Tool/model/version recorded.
- [ ] AI output compared to source.
- [ ] Human approval gates completed.
- [ ] Provenance and corrections documented.
- [ ] Final output independently validated.

## Further study
Study responsible AI documentation, privacy-by-design, media provenance, transcription evaluation and platform synthetic-media policies.
