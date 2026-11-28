# CT-25 Lesson 05 — AI Video Pipeline Evaluation and Batch Automation

- Course: CT-25 — AI-Assisted Video Editing
- Level: Expert
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-25 lessons and authorized source media
- Tools/environment: AI video provider/editor plus conventional NLE; record provider/model/version, OS and source format
- Version/review date: Tool-neutral; provider terms and platform policies must be checked at production time

## Learning outcomes
Design a repeatable AI-assisted video pipeline with versioned inputs, deterministic exports, error handling and human review.

## Key definitions
- **ASR:** Automatic speech recognition.
- **Scene detection:** Automated identification of shot/scene boundaries.
- **Smart reframing:** Automated crop/subject tracking for a new aspect ratio.
- **Highlight extraction:** Model-suggested moments from longer media.
- **Generative video:** Model-created or extended moving-image content.
- **Provenance:** Record of source and transformations.
- **Human approval gate:** Required review before consequential use.
- **Model drift:** Output changes due to model/version updates.

## Purpose and theory
Batch AI workflows can create large volumes of clips, transcripts and versions. Track input hashes/IDs, model version, settings, output and reviewer. Handle failures, retries and partial outputs safely. Do not overwrite approved masters or assume model output is deterministic.

## Tools, requirements and alternatives
Use only providers whose terms, data handling and commercial use are acceptable. Preserve original media and project files. Verify exact model/version and destination requirements. Use manual editing as fallback for factual, identity-sensitive or context-heavy tasks.

## Procedure
1. Define pipeline stages and acceptance criteria. 2. Create source/output manifest. 3. Test representative sample. 4. Record provider/model/version and parameters. 5. Run batch on copies. 6. Validate output count, duration, aspect ratio and audio. 7. Route exceptions to human review. 8. Store logs and rollback paths.

## Worked example
A 20-clip social package is transcribed and reframed in batches, with manual review for clips containing multiple speakers or product demonstrations.

## Dry run
Provider model updates mid-batch. Stop, record version boundary and re-run affected jobs consistently.

## Guided practice
Design a batch workflow for 10 clips with failure handling and review queue.

## Independent assignment
Apply the workflow to a second non-sensitive source. Submit original, AI draft, reviewed final, provenance and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit pipeline diagram, manifest, sample outputs, exception log and QA results. | AI video workflow issue | Compare source, provider terms and final output | Reject or correct and document |

## Knowledge check
1. Why are AI highlights only suggestions?
2. What should be checked in a smart crop?
3. Why is generated video unsuitable as unlabelled factual evidence?
4. What belongs in a batch provenance manifest?
5. When is explicit face/voice consent required?

## Answer guidance
1. They may omit context or misrepresent chronology.
2. Subject/object visibility, action, captions and composition throughout motion.
3. It may depict events that did not occur.
4. Source ID, model/version, settings, output, errors and reviewer.
5. Before identity-based synthesis or use of a real person's likeness/voice.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Task selection and risk assessment | 4 | Brief/provider review |
| AI output evaluation | 4 | Draft/final comparison |
| Editorial accuracy/context | 4 | Source verification |
| Provenance/consent/disclosure | 4 | Logs and approvals |
| Technical QC/handoff | 4 | Final playback and manifest |

Pass: 16/20. Unauthorized identity synthesis, factual misrepresentation or privacy breach requires remediation.

## Quality-control checklist
- [ ] Source rights and consent verified.
- [ ] Provider terms/privacy reviewed.
- [ ] Original media preserved.
- [ ] AI suggestions compared with full context.
- [ ] Identity and factual accuracy reviewed.
- [ ] Generated segments documented/disclosed as required.
- [ ] Final export and archive validated.

## Further study
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- Check current provider terms and platform synthetic-media policies.
- Selected NLE's official documentation.

## Version and change notes
Tool-neutral. Provider models and platform rules change; verify current terms and policy. AI output requires human review.
