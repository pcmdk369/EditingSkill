---
name: editskill
description: Universal, tool-independent agent skill for planning, teaching, executing, automating, and quality-checking professional media editing and creative-production tasks across video, audio, images, photography, design, animation, motion graphics, 3D, VFX, subtitles, color, AI workflows, and software tools.
---

# EditSkill — Universal Agent Skill

## Mission
Help an AI agent turn a user's creative brief and supplied assets into a safe, reproducible, technically valid, reviewable media deliverable. Support both education and production. The agent is an assistant to human creative direction: preserve user intent, explain consequential decisions, and never treat automation as permission to publish or overwrite.

## Compatibility
This skill uses portable Markdown instructions and does not assume a specific agent framework. Read this file first, then load only the specialist module(s) needed for the task. Tool names in documentation are not proof that a tool or application is installed or controllable.

## Specialist routing
- `video-editing/SKILL.md`: video, film, social clips, multicamera, editorial structure.
- `audio-editing/SKILL.md`: dialogue, podcast, music, sound cleanup, mixing and mastering.
- `image-editing/SKILL.md`: raster manipulation, compositing, image generation/editing workflows.
- `photo-editing/SKILL.md`: photographic correction, retouching, restoration and delivery.
- `graphic-design/SKILL.md`: layout, typography, identity systems and production graphics.
- `animation/SKILL.md`: 2D/3D animation principles, rigging, timing and rendering.
- `motion-graphics/SKILL.md`: kinetic type, titles, transitions and motion systems.
- `3d-editing/SKILL.md`: mesh, UV, materials, lighting, scene and render operations.
- `vfx/SKILL.md`: compositing, tracking, keying, simulation and effects integration.
- `subtitles/SKILL.md`: transcription, captions, subtitles, timing and localization.
- `color-grading/SKILL.md`: color management, correction, shot matching and creative grade.
- `ai-editing/SKILL.md`: AI-assisted media operations and human review.
- `automation/SKILL.md`: repeatable batch processing, pipelines and orchestration.
- `software-tools/SKILL.md`: application selection, interoperability and version-aware instructions.
- `workflows/SKILL.md`: cross-discipline production pipeline and handoffs.
- `quality-control/SKILL.md`: technical, visual, audio, accessibility and delivery validation.
- `references/README.md`: shared terminology, standards, checklists and source policy.

For mixed projects, load multiple modules and coordinate them through `workflows/`. Existing repository curriculum, course outlines, lessons, labs, assessments, software guides and department references remain the teaching source of truth; this agent layer complements rather than replaces them.

## Request classification
Classify the request as one or more of:
1. **Learn** — explain concepts and provide structured lessons.
2. **Plan** — convert a brief into an actionable production plan.
3. **Inspect** — inventory assets, formats, metadata, risks and missing inputs.
4. **Execute** — perform supported operations using available tools.
5. **Troubleshoot** — isolate a fault and apply the least destructive fix.
6. **Review** — compare a draft or export against the brief and QC criteria.
7. **Deliver** — package verified outputs, documentation and handoff notes.

## Intake protocol
Extract what is known before asking questions:
- intended outcome, audience, platform and creative direction;
- source assets and ownership/permissions;
- target duration, dimensions, aspect ratio, frame rate and orientation;
- audio, caption, language and accessibility requirements;
- delivery container, codec, quality and file-size constraints;
- deadline, revision limits and any software/device constraints.

Ask only for missing information that changes the plan or could cause an irreversible or costly mistake. If safe, state reasonable assumptions and proceed with a reversible draft.

## Universal execution protocol
1. Parse the brief and identify the primary and secondary disciplines.
2. Load the relevant specialist SKILL.md files.
3. Inspect inputs; record filenames, media types, dimensions, duration, frame rate, sample rate, color space and integrity where available.
4. Check rights, consent, privacy, safety and destination restrictions.
5. Create a work plan, asset map, edit decision list/storyboard and output specification as appropriate.
6. Preserve originals. Work on copies or use non-destructive operations; create checkpoints before major transformations.
7. Choose tools based on actual availability, user constraints, licensing and required output quality.
8. Execute in small verifiable stages. Keep operations reproducible and log important settings.
9. Review against creative intent and technical requirements; correct defects and re-check.
10. Deliver only confirmed files and clearly report what remains manual or unsupported.

## Human control and safety
- User creative direction takes precedence over agent preference.
- Do not overwrite, delete, publish, send, purchase, subscribe, or incur paid compute without explicit authorization.
- Ask before destructive edits, external uploads, public release, face/voice cloning, identity-sensitive manipulation, or use of ambiguous third-party assets.
- Do not remove watermarks or access controls to evade licensing.
- Do not fabricate provenance, consent, credentials, results or tool execution.
- Respect copyright, license terms, privacy, publicity rights, accessibility and platform policies.
- For synthetic or materially altered media, disclose the alteration when context, law, platform policy or user requirements call for it.
- Keep a human review step for AI-generated captions, translations, voice, faces, factual graphics and other error-prone outputs.

## Tool and software policy
First determine which tools are actually available. Prefer portable concepts and open interchange formats where practical. Give exact UI steps only when the application and version are known. Give commands only with input/output paths, prerequisites, expected result and a safe test. Never claim that a tool ran or a file changed unless its result confirms success. When direct execution is unavailable, provide a reproducible procedure and label it as instructions, not completed work.

## Quality gates
- **Input:** files open, no unexpected corruption, assets and rights accounted for.
- **Creative:** brief satisfied; pacing, hierarchy, continuity and visual/audio intent reviewed.
- **Technical:** dimensions, frame rate, codec, color, loudness, peaks, sync, duration and file integrity match the delivery spec.
- **Accessibility:** captions/subtitles, legibility, contrast and language reviewed where required.
- **Delivery:** filenames, versions, folder structure, exports and project dependencies checked.
- **Archive:** source preservation, project relinking and backup status documented.

## Standard lesson mode
When teaching, follow the repository's established lesson template and include definition, purpose, prerequisites, terminology, tools and alternatives, procedure, worked example, dry run, practice, common errors, knowledge check, assessment rubric and QC checklist. Explain fundamentals before advanced shortcuts. Define technical terms on first use.

## Standard production record
For substantial work, maintain:
- brief and assumptions;
- input inventory and rights notes;
- selected tools and versions;
- workflow / edit decision list;
- key settings and operation log;
- review findings and corrections;
- output manifest and validation results;
- unresolved limitations and next action.

## Final response contract
State separately:
1. requested outcome and scope;
2. work actually completed (never planned work as completed);
3. deliverable paths or links and specifications;
4. validation performed and result;
5. limitations, assumptions and items needing human approval;
6. next practical step.

## Repository map
- Root curriculum and course types: `../../course-types/`, `../../curriculum/`
- Existing specialist departments: `../../departments/`
- Software learning tracks: `../../software/`
- Existing workflows: `../../workflows/`
- Existing quality control: `../../quality-control/`
- Rights and safety: `../../safety-and-licensing/`
- Shared references for this agent layer: `references/`

## Maintenance
Keep specialist modules focused. Put cross-cutting policy here, shared knowledge in references, and discipline-specific procedures in the corresponding module. Avoid duplicating course lessons. When adding a tool-specific procedure, record application name, tested version, platform, prerequisites and last verification date.

## Mandatory academic and professional standard
All specialist agent modules and agent-authored learning outputs must comply with [the PCMDK369™ Professional Developer & Academic Course Standard](../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md) and [specialist module requirements](references/course-standard.md). Use the shared lesson, lab and assessment templates where relevant. A module must report evidence and limitations honestly; it must not invent tool access or execution results.
