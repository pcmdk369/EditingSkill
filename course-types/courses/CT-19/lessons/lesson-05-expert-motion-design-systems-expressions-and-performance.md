# CT-19 Lesson 05 — Motion Design Systems, Expressions and Performance

- Course: CT-19 — Motion Graphics & Kinetic Typography
- Level: Expert
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-19 lessons and authorized design assets
- Tools/environment: Motion graphics/compositing application; record OS/app/version, canvas and frame rate
- Version/review date: Tool-neutral; verify delivery and accessibility requirements

## Learning outcomes
Create reusable animation components, expressions and render-efficient workflows with clear dependencies and fallback behavior.

## Key definitions
- **Motion graphics:** Animated design elements used to communicate information or identity.
- **Kinetic typography:** Text animated to support meaning and hierarchy.
- **Easing:** Acceleration/deceleration behavior between keyframes.
- **Mask:** Shape or channel controlling visibility.
- **Motion token:** Reusable timing, spacing or easing rule.
- **Expression:** Procedural rule driving a property.
- **Data visualization:** Graphic representation of data.
- **Alpha channel:** Transparency information.

## Purpose and theory
Motion systems standardize easing, durations, spacing and reusable controls. Expressions can drive properties procedurally but may break across versions or missing fonts/plugins. Optimize previews and renders by measuring bottlenecks; keep manual fallback where automation is fragile.

## Tools, requirements and alternatives
Use a current motion graphics application with keyframes, masks, text and export. Record app/version, fonts/plugins and output settings. Use licensed assets and verify data sources.

## Procedure
1. Define motion tokens and easing curves. 2. Build reusable components. 3. Use expressions only for repeated logic. 4. Document inputs and dependencies. 5. Test at multiple durations/aspect ratios. 6. Measure render performance. 7. Provide fallback/manual controls. 8. Version and archive templates.

## Worked example
A lower-third template exposes name, role, duration and accent color as editable controls.

## Dry run
Expression fails on another machine due to missing font/plugin. Document dependencies and provide fallback assets.

## Guided practice
Build a reusable lower-third/title system with editable controls.

## Independent assignment
Create a second motion piece with a different aspect ratio or audience. Submit project, exports, source data/assets, dependency and QC notes.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit template, dependency list, performance notes and sample renders. | Motion design issue | Inspect timeline, source and delivery preview | Correct and re-render a proof |

## Knowledge check
1. Why should static layout be approved before animation?
2. What makes kinetic typography readable?
3. How can a data animation mislead?
4. What are motion tokens used for?
5. What should be checked in an alpha overlay delivery?

## Answer guidance
1. Motion cannot fix unclear hierarchy or message.
2. Timing, contrast, line breaks and sufficient reading time.
3. Changing scales or labels can exaggerate/obscure values.
4. Consistent reusable motion rules.
5. Alpha interpretation, edges, dimensions, frame rate and dependencies.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Design/message hierarchy | 4 | Style frame |
| Timing and motion craft | 5 | Timeline/preview |
| Typography/data accuracy | 4 | Proofread source |
| Reusability and format adaptation | 3 | Components/templates |
| Technical export and handoff | 4 | QC and manifest |

Pass: 16/20. Inaccurate factual data or unlicensed assets require remediation.

## Quality-control checklist
- [ ] Message and static hierarchy are clear.
- [ ] Text remains readable at normal speed.
- [ ] Data and labels are accurate.
- [ ] Motion is consistent and accessible.
- [ ] Fonts/plugins/assets are licensed and documented.
- [ ] Alpha/render settings match brief.
- [ ] Editable project and manifest are complete.

## Further study
- [W3C — WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)
- Selected motion application's official expression and export documentation.

## Version and change notes
Tool-neutral. Expression behavior, fonts and alpha handling vary by application/version; verify in the target environment.
