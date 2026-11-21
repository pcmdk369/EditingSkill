# CT-25 Lesson 02 — AI Transcription, Scene Detection and Searchable Media

- Course: CT-25 — AI-Assisted Video Editing
- Level: Beginner / Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-25 lessons and authorized source media
- Tools/environment: AI video provider/editor plus conventional NLE; record provider/model/version, OS and source format
- Version/review date: Tool-neutral; provider terms and platform policies must be checked at production time

## Learning outcomes
Use AI transcription and scene analysis to organize footage, then correct metadata and preserve source timecode.

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
ASR and scene detection can speed logging, but can mishear names/numbers, miss cuts and misclassify scenes. Timecode must refer to the exact source version. Search labels should describe observable content, not infer sensitive traits or intent.

## Tools, requirements and alternatives
Use only providers whose terms, data handling and commercial use are acceptable. Preserve original media and project files. Verify exact model/version and destination requirements. Use manual editing as fallback for factual, identity-sensitive or context-heavy tasks.

## Procedure
1. Confirm source version and timecode basis. 2. Review transcription provider terms. 3. Generate draft transcript and scene markers. 4. Compare speech against source. 5. Correct names, numbers and speakers. 6. Inspect scene boundaries. 7. Tag content with neutral observable labels. 8. Export searchable log and provenance.

## Worked example
AI marks a scene as “person angry.” Replace with neutral description such as “speaker raises voice” unless emotion label is necessary and supported.

## Dry run
Transcript omits a negation. Correct against audio and audit similar high-risk terms.

## Guided practice
Create a transcript and scene log for a five-minute non-sensitive clip.

## Independent assignment
Apply the workflow to a second non-sensitive source. Submit original, AI draft, reviewed final, provenance and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit source, draft, corrected transcript, scene log and tool record. | AI video workflow issue | Compare source, provider terms and final output | Reject or correct and document |

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
