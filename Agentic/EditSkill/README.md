# Agentic / EditSkill

Portable, modular agent instructions for editing and creative-production tasks.

## Entry point
Start with [SKILL.md](SKILL.md). It classifies the request, defines safety and execution rules, and routes the agent to specialist modules.

## Modules
- [Video Editing](./video-editing/SKILL.md)
- [Audio Editing](./audio-editing/SKILL.md)
- [Image Editing](./image-editing/SKILL.md)
- [Photo Editing](./photo-editing/SKILL.md)
- [Graphic Design](./graphic-design/SKILL.md)
- [Animation](./animation/SKILL.md)
- [Motion Graphics](./motion-graphics/SKILL.md)
- [3D Editing](./3d-editing/SKILL.md)
- [Visual Effects](./vfx/SKILL.md)
- [Subtitles and Captions](./subtitles/SKILL.md)
- [Color Grading](./color-grading/SKILL.md)
- [AI Editing](./ai-editing/SKILL.md)
- [Editing Automation](./automation/SKILL.md)
- [Software Tools](./software-tools/SKILL.md)
- [Production Workflows](./workflows/SKILL.md)
- [Quality Control](./quality-control/SKILL.md)
- [Shared references](./references/README.md)

## Relationship to the main curriculum
This directory is an agent execution layer, not a replacement for the main EditingSkill curriculum. Use the root `SKILL.md`, `course-types/`, `curriculum/`, `departments/`, `software/`, `workflows/`, `quality-control/` and `safety-and-licensing/` as existing sources of truth.

## Usage
1. Load this directory's `SKILL.md`.
2. Select one or more specialist modules.
3. Inspect user assets and constraints.
4. Plan and execute only with available tools and appropriate authorization.
5. Validate actual outputs and report evidence.

All instructions are tool-independent Markdown. Application-specific procedures must state their tested software version and platform.