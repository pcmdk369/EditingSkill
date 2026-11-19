# CT-03 Lesson 05 — Expert Editorial Testing and Performance Optimization

- **Course:** CT-03 — Short-Form & Social Video Editing
- **Level:** Expert
- **Estimated time:** 240–300 minutes, including test design, diagnosis, practical review and evidence packaging
- **Prerequisites:** Lessons 01–04; a documented brief, approved master, at least one derivative and a version manifest
- **Tools/environment:** Any editor with a repeatable preview workflow; media metadata inspector; system performance monitor; spreadsheet or structured review log; authorized analytics or moderated test method. Record application/version, OS, hardware, storage and test date.
- **Version/review date:** Academic revision 2.0 — 2026-11-19. Core method is tool-neutral; analytics definitions and application controls are platform/version-dependent and must be verified before use.

## Learning outcomes

By the end of this lesson, learners can:
1. Turn an editorial question into a falsifiable hypothesis with one primary variable, measurable outcome and predeclared guardrails.
2. Distinguish creative preference testing, moderated comprehension testing, platform experiments and observational analytics.
3. Define metric names, denominators, eligibility rules, collection windows and limitations before comparing variants.
4. Identify confounders, selection bias, survivorship bias, sample limitations and changes in platform metric definitions.
5. Interpret descriptive results without claiming causation or universal audience behavior from weak evidence.
6. Protect participant privacy and comply with consent, platform terms, client authority and data-minimization requirements.
7. Establish a reproducible performance baseline for an editing project and isolate likely decode, effects, storage, memory or export bottlenecks.
8. Choose proportionate optimizations such as proxies, preview settings, cache, media organization or effect simplification without degrading source integrity.
9. Preserve a rollback path and verify that the final export uses approved source quality and settings.
10. Produce a recommendation report that separates observed evidence, interpretation, uncertainty and the next test.

## Key definitions and terminology

| Term | Definition | Context/example |
|---|---|---|
| Hypothesis | A testable prediction about an edit decision and an observable outcome | “A demonstration-first opening improves correct feature recall” |
| Independent variable | The factor deliberately changed between conditions | Opening shot |
| Dependent outcome | The measured response that may change | Correct recall in a moderated test |
| Control / baseline | The reference condition used for comparison | Approved opening A |
| Confounder | An uncontrolled factor that may influence the result | Different audience or posting window |
| Random assignment | Assigning eligible participants to conditions by chance | Reduces systematic allocation bias |
| Sample | The observations included in a test | Eligible starts or consenting participants |
| Sample frame | The population from which observations are drawn | Followers who received the test |
| Selection bias | A systematic difference in who enters or remains in a sample | Only highly engaged viewers respond |
| Survivorship bias | Drawing conclusions only from cases that remain visible | Studying comments while ignoring silent exits |
| Metric definition | The exact event, denominator, window and calculation behind a number | Platform-defined 3-second view |
| Denominator | The population/count used as the base for a rate | Eligible impressions or starts, as defined |
| Percentage point | The arithmetic difference between two percentages | 65% − 60% = 5 percentage points |
| Practical significance | Whether a difference matters for the real decision | A small lift may not justify extra production cost |
| Statistical uncertainty | The range of plausible variation around an estimate | A small sample can produce unstable rates |
| Guardrail metric | A measure that must not deteriorate beyond an agreed limit | Caption complaints or misleading-claim reports |
| Observation window | The predeclared period during which data are collected | Same 48-hour window if the platform/test supports it |
| Instrumentation | The method used to collect and label observations | Authorized platform experiment report |
| Proxy media | Lower-resource copies linked to original media for editing | Offline/online workflow |
| Optimized media | Application-generated media intended to improve decode or playback | Editor-specific optimized files |
| Render cache | Stored intermediate processing used to reduce repeated computation | May improve preview, not guarantee final export speed |
| Bottleneck | The resource or operation currently limiting throughput | Decode, effect, memory, storage or encoder |
| Decode | Converting compressed source frames into usable image data | Long-GOP source footage |
| Encode | Compressing rendered frames/audio into an output stream | Final H.264/H.265 export |
| Throughput | Amount of work completed per unit time | Frames processed per second |
| Latency | Delay before an operation or response completes | Time from play command to responsive preview |
| Dropped frame | A frame not displayed or processed at the expected time | Preview stutter |
| Baseline measurement | Recorded performance before a change | Same timeline segment, settings and device |
| Reproducibility | Ability to repeat a test under documented conditions | Same source, segment, version and procedure |
| Regression test | A retest to ensure an optimization did not break another requirement | Recheck captions and export after changing sequence settings |

## Purpose and professional relevance

Expert editing requires two complementary forms of evaluation:

- **Editorial testing** asks whether a creative decision helps the intended audience understand, feel or act in the intended way.
- **Technical performance testing** asks whether the project can be reviewed, edited, rendered and delivered reliably within the available resources.

These questions must not be confused. A clip that receives more views is not automatically more truthful, accessible or useful. A timeline that plays smoothly at low preview quality is not automatically ready for final export. A fast render is not a success if the output is soft, cropped incorrectly, out of sync or missing a qualifier.

A professional test is designed before results are seen. It identifies the decision, comparison, measurement, constraints and stopping rule. A professional optimization is measured before and after, changes one relevant factor at a time where practical, and preserves a way to reverse the change.

## Theory and principles

### 1. Choose the correct testing method

| Method | What it can answer | Main limitation |
|---|---|---|
| Editorial peer review | Whether trained reviewers find a cut clear, coherent and accurate | Reviewer judgment may not represent the intended audience |
| Moderated comprehension test | What consenting participants understand, notice or misinterpret | Small qualitative samples do not estimate population-wide behavior |
| Controlled platform experiment | How variants perform under the platform's supported allocation and measurement design | Platform eligibility, definitions and distribution controls may be limited |
| Observational analytics | What happened under actual distribution conditions | Audience, timing, placement and external events may differ |
| Technical benchmark | How a defined project operation performs under recorded conditions | Results may not transfer to other hardware, codecs or projects |

Do not describe an observational comparison as a randomized experiment. If the platform does not offer a supported experiment, do not imitate randomization with methods that violate its terms or expose participants to unwanted duplicate content. Use a moderated test or report the comparison as observational.

### 2. Define the editorial question before the metric

Start with the decision, not the dashboard. Examples:
- Can viewers identify the demonstrated feature?
- Does the opening establish the subject without implying an unsupported result?
- Are captions understood at normal mobile viewing size?
- Does the CTA remain visible long enough to read?
- Does a shorter cut preserve the necessary evidence and qualifier?

A metric is useful only if it is a reasonable indicator of the question. A click does not prove comprehension. A completed view does not prove the claim is true. A high comment count may reflect confusion or controversy rather than success.

### 3. Predeclare variables, controls and guardrails

Change one primary creative variable at a time when practical. Keep the message, offer, runtime, audience, caption treatment and distribution conditions stable unless one of those is the variable being studied. Record unavoidable differences.

Set guardrails before testing. Examples include:
- no unsupported or exaggerated claim;
- no omission of a necessary qualifier;
- no reduction in caption accuracy or accessibility;
- no use of unlicensed music or imagery;
- no increase in privacy or safety risk;
- no material increase in negative comprehension findings.

A variant that improves a viewing metric but violates a guardrail is not an acceptable winner.

### 4. Interpret metrics cautiously

Metric names and calculations are provider-specific and can change. For every metric, record:
- provider and product surface;
- exact displayed name and definition;
- numerator and denominator, if supplied;
- eligible event/population;
- collection window and reporting delay;
- whether data are estimated, filtered or modeled;
- date the definition was checked.

A percentage difference should be described precisely. If Variant A is 60% and Variant B is 65%, B is 5 percentage points higher, or approximately 8.3% higher relative to A. These are different statements. Neither establishes that the opening caused the difference.

Do not set a universal minimum sample size or significance threshold without a defensible design. Consider allocation method, expected effect, variability, statistical power, practical cost and the risk of repeatedly checking results and stopping when a favorable number appears. If the design is too weak, label the result inconclusive.

### 5. Separate performance dimensions

A slow project can fail in different places:

- **Source decode:** compressed media is expensive to decode or is poorly supported by the hardware.
- **Effects/compositing:** noise reduction, stabilization, tracking, blur, layered graphics or color operations add processing.
- **Memory:** large frames, many layers or background applications create pressure.
- **Storage:** media/cache reads and writes are delayed or the drive is nearly full.
- **Timeline complexity:** many tracks, nested sequences, high-resolution media or mixed frame rates increase work.
- **Export/encode:** the final output uses a demanding codec, effect stack or quality setting.
- **Thermal/power limits:** a device reduces performance under heat or power constraints.

The symptom is not the diagnosis. Record what operation is slow and when it occurs: ingest, scrubbing, real-time playback, effect preview, background cache, export or file transfer.

### 6. Optimize in a reversible order

Use a controlled sequence:
1. Reproduce the issue and record a baseline.
2. Inspect media properties, project settings and resource use.
3. Isolate the most likely bottleneck.
4. Apply one low-risk change on a copy or reversible setting.
5. Repeat the same test and compare the result.
6. Check image/audio quality and project portability.
7. Keep or revert the change based on evidence.
8. Recheck final export using the intended originals and specification.

Possible changes include closing unnecessary applications, improving media organization, using supported proxy/optimized media, reducing preview resolution, using render cache, temporarily disabling a heavy effect for review, or selecting a more suitable intermediate codec. These are options, not universal prescriptions. Hardware, editor version, source codec and project design determine whether they help.

### 7. Proxy, optimized media and cache are not interchangeable

- A **proxy** is a lower-resource representation linked to an original. It is intended to make editorial work easier while preserving a path to the original.
- **Optimized media** is generated by an editor or workflow to improve access or processing. Its exact behavior varies by application.
- A **render cache** stores processed results so the editor may not need to calculate the same effect repeatedly.

Record which mechanism is active. Confirm whether the export process uses originals, optimized files or proxies and whether that behavior is configurable in the selected editor. Never assume a proxy is automatically replaced at export.

### 8. Protect evidence, privacy and editorial integrity

Use learner-created, licensed or explicitly authorized media. For participant tests, explain purpose, what will be recorded, who can access it, retention and withdrawal options where applicable. Collect the minimum data needed; do not collect private messages, account credentials, sensitive personal data or unnecessary identifiers. Follow client agreements, platform terms and applicable law.

Do not manipulate analytics screenshots, omit failed tests or select only favorable time windows. Retain negative and inconclusive findings. Do not optimize for engagement by adding deceptive hooks, artificial urgency, misinformation, harassment or inaccessible visual effects.

## Tools, requirements and alternatives

**Editorial test record:** a spreadsheet, plain-text table or issue tracker is sufficient. Record test IDs, variant IDs, source project version, variable, control, metric definition, sample, observation window and decision.

**Audience evidence:** use an authorized platform analytics surface only if access and collection are permitted. Otherwise use a moderated test with consenting participants, a peer review or a clearly labeled simulated dataset. Do not scrape private accounts or bypass platform controls.

**Performance evidence:** use the editor's playback indicators, operating-system resource monitor and a trusted media metadata inspector. Exact labels and available measurements vary. Record hardware model, CPU/GPU/RAM, storage type and free space where relevant, OS, editor version, project settings, source codec/resolution/frame rate and test segment.

**Alternatives:** if no performance monitor is available, record repeatable elapsed times and visible dropped-frame behavior under the same conditions. If no analytics access is authorized, use qualitative comprehension tests or simulated data to practice calculations. Do not present simulated values as audience results.

**Version policy:** do not copy menu paths from a different editor release. Check the installed version's official documentation for proxy attachment, optimized media, cache, playback quality, render source selection and export behavior.

## Procedure

### Phase A — Frame the editorial test
1. State the decision that must be made in one sentence.
2. Identify the audience and the intended comprehension or action.
3. Write a directional hypothesis with a reason and evidence basis.
4. Select one primary variable and define what remains constant.
5. Select one primary outcome that genuinely relates to the decision.
6. Define guardrails, eligibility rules, observation window and stopping rule before collecting results.
7. Choose a suitable method: peer review, moderated test, authorized platform experiment or observational analytics.
8. Record the source master, variant IDs, version numbers and rights/consent basis.

### Phase B — Prepare and protect test data
9. Create variants from a protected master; do not overwrite approved source sequences.
10. Confirm both variants are truthful, complete and equally compliant with required qualifiers, captions and rights.
11. Record exact differences using a comparison sheet or change log.
12. Confirm test access and collection are authorized. Minimize personal data.
13. Check the metric definition and date against the selected provider's current documentation.
14. If a fair comparison cannot be achieved, state the limitation and choose a safer method.

### Phase C — Collect and interpret evidence
15. Collect observations within the predeclared window; do not stop early solely because a favorable number appears.
16. Record counts, denominators, exclusions, dates, allocation method and external events.
17. Calculate simple rates only from the documented numerator and denominator.
18. Distinguish percentage points from relative percentage change.
19. Review guardrails, qualitative feedback and accessibility/factual issues alongside engagement metrics.
20. State whether the evidence is descriptive, qualitative, experimental, inconclusive or invalid.
21. Make a limited recommendation and identify what further evidence would change it.

### Phase D — Establish a technical baseline
22. Save a copy/checkpoint of the project and identify the exact sequence and time range.
23. Record the editor/version, OS, hardware, storage and project settings.
24. Inspect source media codec, resolution, frame rate, variable-frame-rate status where known, audio streams and file location.
25. Define a repeatable operation: e.g., play the same 30-second section, scrub to the same frame or export the same short range.
26. Record baseline playback behavior, elapsed time, dropped-frame indicator or resource use where available.
27. Identify whether the slowdown occurs during source decode, effects, playback, export or transfer.

### Phase E — Isolate and optimize
28. Change one likely cause at a time on a duplicate or through a reversible setting.
29. Re-run the same operation and record the result.
30. Test proxy/optimized media only after confirming how the editor links it to originals.
31. Test cache behavior separately from final export speed.
32. Check image quality, motion, text, captions, audio sync and project relinking after each meaningful change.
33. Keep, modify or revert the change and record why.
34. Avoid deleting cache, originals or intermediate files unless their role, recovery path and authorization are clear.

### Phase F — Final verification and reporting
35. Restore the intended final-quality source path and verify export-source behavior.
36. Export a short proof using the approved delivery settings.
37. Inspect the proof for sharpness, scaling, motion, frame cadence, color, audio, sync and caption integrity.
38. Render the full output only after the proof passes and authorization exists.
39. Play the final export completely and compare metadata against the delivery specification.
40. Produce a report separating observed data, interpretation, uncertainty, optimization, rollback and outstanding approval.

## Worked example

**Brief/input:** A fictional reusable-bottle campaign has an approved 20-second master. The team wants to know whether a problem-first or demonstration-first opening makes the locking feature easier to understand. The team also reports slow playback on a workstation.

**Editorial test plan:**
- Variant A opens with the product and then demonstrates the lock.
- Variant B opens with the problem context and then demonstrates the same lock.
- Only the first two-second opening changes; the demonstration, CTA, runtime, captions and qualified product wording remain the same.
- The team selects a moderated comprehension test with consenting volunteers because no authorized randomized platform experiment is available.
- Primary outcome: whether participants can correctly describe what the lock does after one viewing.
- Guardrails: no variant may imply a waterproof or safety claim not present in the approved brief; captions remain accurate; no unnecessary participant identifiers are collected.

**Simulated teaching data (not real audience analytics):**

| Measure | Variant A | Variant B |
|---|---:|---:|
| Consenting participants | 20 | 20 |
| Correct feature explanation | 13/20 (65%) | 15/20 (75%) |
| Participants who noticed the qualifier | 18/20 (90%) | 17/20 (85%) |
| Participants who reported confusion | 2/20 (10%) | 3/20 (15%) |

**Interpretation:** B has 10 percentage points more correct feature explanations in this small simulated sample, but slightly fewer participants noticed the qualifier and more reported confusion. The result does not establish population-wide superiority. The next step is to inspect the confusion notes and test a revised B opening without reducing qualifier visibility. The team should not select B based on one metric alone.

**Technical diagnosis:** The same timeline segment plays smoothly with heavy effects disabled but drops frames when stabilization and noise reduction are active. The editor/version, source codec, device resources and test segment are recorded. The learner tests one effect at a time on a duplicate sequence, then tests a proxy workflow. The final proof is checked with original media selected according to the editor's documented export behavior.

**Expected output:** a test plan, two traceable variants, a clearly labeled evidence log, a cautious recommendation, a performance baseline/change log, a verified proof and a report of remaining limitations. All people counts and outcomes above are fictional instructional data.

## Dry run / annotated walkthrough

**Scenario:** A 30-second vertical edit stutters during preview and the team has two opening variants with different completion figures.

1. **Do not combine the questions.** Create one editorial test record and one technical performance record. A faster preview does not explain a completion-rate difference.
2. **Check the editorial comparison.** The variants differ in both opening shot and caption size. This is two variables, so the result cannot isolate the effect of the opening. Mark the test confounded.
3. **Check the denominator.** The dashboard label is “views,” but the team has not recorded the provider's definition or whether it includes repeat plays. Do not calculate a completion rate from an unknown base.
4. **Check the performance symptom.** Stutter occurs only in a section with stabilization and layered graphics. Record the exact time range and reproduce it.
5. **Isolate.** Disable stabilization on a duplicate, repeat the same playback test and record the result. Re-enable it, then test the graphics separately. Do not change both at once.
6. **Try a reversible workflow.** If supported, attach proxies or optimized media to copies and verify the source-to-proxy mapping. Record whether playback changes.
7. **Check final-quality behavior.** Restore the intended original media path. Render a short proof and compare sharpness, motion and overlays. Do not assume the proxy switch is correct.
8. **Disposition.** Reject the creative test as inconclusive and redesign it with one variable. Keep the optimization only if the project remains portable and the final proof passes.

## Guided practice

### Exercise 1 — Write a testable hypothesis
Use a fictional 20-second edit. Compare two openings that preserve the same claim and demonstration.

**Hints:** State the audience, one variable, one primary outcome, one guardrail and the reason the outcome is relevant.

**Success criteria:** another learner can identify exactly what changes, what stays constant and what result would weaken the hypothesis.

### Exercise 2 — Metric interpretation
Use the simulated table in the worked example. Calculate the percentage-point difference in correct explanations and the difference in qualifier awareness.

**Hints:** Subtract the percentages. Do not call the result statistically significant or causal.

**Success criteria:** calculations are correct and the conclusion mentions sample size and guardrails.

### Exercise 3 — Confounder audit
A team compares two posts published on different days, with different captions and different audiences.

**Hints:** List each changed condition and decide whether the result is experimental or observational.

**Success criteria:** learner identifies at least three confounders and proposes a safer next test.

### Exercise 4 — Performance isolation
A timeline stutters during a section with a high-resolution source and multiple effects.

**Hints:** Record a baseline, isolate one effect, test source decode and storage, then test a reversible proxy/cache option. Keep the same segment and playback conditions.

**Success criteria:** the learner distinguishes symptom from cause and documents a rollback.

### Exercise 5 — Export-source verification
A proxy-based project plays smoothly. Prepare the final-export proof checklist.

**Hints:** Verify source selection, relinking, dimensions, frame rate, scaling, motion, audio sync, captions and metadata.

**Success criteria:** the proof is checked against the delivery specification and is not assumed correct from the timeline preview.

## Independent assignment

Produce an expert editorial-testing and performance-optimization dossier for a learner-created or properly licensed short-form campaign.

**Required deliverables:**
1. One-sentence editorial decision statement and directional hypothesis.
2. Test-method rationale: peer review, moderated test, authorized platform experiment or observational analysis.
3. Variant manifest identifying the protected master, exact changed variable and all controlled conditions.
4. Metric dictionary with provider definition/date, numerator, denominator, eligibility, collection window and limitations; if no real data is authorized, use clearly labeled simulated data.
5. Guardrail and stop-rule record covering truthfulness, accessibility, rights and privacy.
6. Evidence table with sample size, exclusions, external factors and uncertainty.
7. A recommendation that separates observation from interpretation and avoids unsupported causal claims.
8. Technical environment record and reproducible performance baseline.
9. Bottleneck-isolation log with at least two controlled diagnostic steps and rollback notes.
10. Proxy/optimized-media/cache decision record, if used.
11. Final proof/QC report showing the intended original-source and export behavior.
12. Reflection describing one inconclusive finding, one rejected optimization or one risk avoided.

**Constraints:** do not use private analytics, scrape accounts, buy engagement or expose participant data. Obtain consent for participant testing and use only the minimum data required. Do not publish a variant or incur paid distribution without authorization. Never invent performance measurements or present simulated data as real results.

**Submission evidence:** variant IDs, test plan, worksheet, data source or simulation label, project/version manifest, baseline and retest records, proof export or a clearly labeled not-rendered report, QC evidence and reviewer feedback.

## Common errors and recovery

| Symptom | Likely cause | Diagnosis | Safe recovery |
|---|---|---|---|
| “Winner” declared after one metric | Metric tunnel vision | Review guardrails and comprehension evidence | Reassess against the actual decision and report trade-offs |
| Test variants differ in several ways | Poor variable control | Compare manifests and timelines | Mark result confounded; rebuild a one-variable test |
| Different audiences or time windows | Allocation/distribution confounder | Inspect test design and platform report | Use a supported experiment or label the result observational |
| Rate cannot be reproduced | Denominator or definition missing | Inspect provider documentation and raw counts | Record exact definition/date or omit the rate |
| Small sample treated as universal | Overgeneralization | Review sample frame and uncertainty | Narrow the conclusion and recommend further testing |
| Early stop favors a temporary spike | Repeated unplanned checking | Compare with the predeclared stop rule | Report exploratory status; repeat with a declared plan |
| Preview improves but export does not | Cache/proxy effect misunderstood | Compare preview and render operations separately | Diagnose export path and encoder independently |
| Final export is soft | Proxy or low-quality source used | Inspect relink/source selection and proof | Restore original source path and render a new proof |
| Optimization introduces artifacts | Settings changed without quality review | Compare reference frames/audio | Revert or test another variable |
| Hardware result cannot be repeated | Environment not recorded | Compare device, power, temperature and background load | Re-establish baseline under documented conditions |
| Cache consumes storage | Unbounded cache growth | Inspect cache location and size | Use editor-supported cache management after backup/authorization |
| Analytics contain personal data | Excessive collection or sharing | Audit fields, exports and access | Stop collection, restrict access and follow the responsible privacy process |

## Knowledge check

1. What is the difference between an editorial hypothesis and a performance benchmark?
2. Define an independent variable and a dependent outcome.
3. Give three examples of confounders in a short-form content comparison.
4. Why must a metric's denominator and provider definition be recorded?
5. Explain the difference between a percentage-point change and a relative percentage change.
6. Why is a completion metric not proof of truthfulness or accessibility?
7. When should a result be labeled observational rather than experimental?
8. What is a guardrail, and why is it declared before the test?
9. Name four possible technical bottleneck categories.
10. How does a proxy differ from a render cache?
11. Why must a technical baseline use the same segment and conditions?
12. What is the risk of repeatedly checking results and stopping when one looks favorable?
13. Why should an optimization be applied one variable at a time where practical?
14. What must be checked before final export from a proxy-based project?
15. What privacy controls apply to participant testing or analytics?
16. When is “inconclusive” the most accurate result?

## Answer key / instructor guidance

1. An editorial hypothesis predicts an audience/creative outcome; a performance benchmark measures a defined technical operation under recorded conditions.
2. The independent variable is deliberately changed; the dependent outcome is measured.
3. Different audience, posting time, caption, runtime, offer, placement, distribution method or external event.
4. Providers may define events, exclusions and denominators differently or change them; without the definition, the rate is not reproducible or comparable.
5. From 60% to 65% is +5 percentage points; relative to 60%, it is an increase of about 8.3%.
6. The metric describes behavior, not factual accuracy, comprehension, accessibility or user benefit.
7. When variants were not allocated through a controlled supported design or important conditions differ.
8. A predeclared condition that must remain acceptable; it prevents a favorable primary metric from hiding harm or quality loss.
9. Source decode, effects/compositing, memory, storage I/O, timeline complexity, export/encode, thermal or power limits.
10. A proxy is an alternate media representation linked to an original; render cache stores processed intermediate results.
11. Otherwise, changes in media, effects, time range or system state may explain the difference rather than the optimization.
12. Repeated checking and optional stopping can make random fluctuations look like a stable effect and bias the decision.
13. It helps isolate which change caused the observed performance difference and supports rollback.
14. Original-media relinking/source selection, export behavior, dimensions, frame rate, scaling, quality, audio, captions and full playback.
15. Obtain appropriate consent/authority, minimize data, restrict access, document purpose/retention and comply with applicable law and platform/client terms.
16. When sample, design, metric definition or data quality cannot support a defensible choice, or evidence conflicts across outcomes/guardrails.

## Assessment rubric

| Criterion | Points | Evidence |
|---|---:|---|
| Decision statement and hypothesis | 10 | Clear question, rationale and measurable outcome |
| Test method and variable control | 15 | Appropriate design; controls/confounders documented |
| Metric dictionary and data integrity | 10 | Definitions, denominators, window and source traceable |
| Interpretation and uncertainty | 15 | Correct calculations; no unsupported causal/general claim |
| Guardrails, rights and privacy | 10 | Consent/authority, minimization and quality gates |
| Technical baseline and diagnosis | 15 | Reproducible conditions; bottleneck reasoning |
| Optimization and rollback | 10 | Controlled, reversible change and retest |
| Final proof and QC | 10 | Intended source quality and output specification verified |
| Report and reflection | 5 | Observations, limitations and next step clearly separated |
| **Total** | **100** | |

**Pass threshold:** 80/100. Mandatory gates: no fabricated data; no unauthorized/private data collection; no unsupported claim; original source preserved; no unverified export marked passed. Failure of a mandatory gate requires remediation regardless of the numeric score.

## Quality-control checklist

- [ ] Editorial decision and hypothesis are explicit.
- [ ] Method is correctly labeled as experimental, observational, moderated or simulated.
- [ ] Only the intended variable differs, or confounders are disclosed.
- [ ] Metric definition, provider, denominator and date are recorded.
- [ ] Sample frame, size, window and exclusions are documented.
- [ ] Calculations distinguish percentage points from relative change.
- [ ] Guardrails and stopping rules were set before collection.
- [ ] Interpretation includes uncertainty and avoids causal overclaim.
- [ ] Rights, consent, privacy and data minimization are addressed.
- [ ] Technical environment and exact test segment are recorded.
- [ ] Baseline and optimization use repeatable conditions.
- [ ] Changes are reversible and source media are preserved.
- [ ] Proxy/optimized-media mapping and export behavior are checked.
- [ ] Final proof uses the intended source quality and passes full playback.
- [ ] Known limitations, rejected changes and next test are reported.

## Capstone integration and requirements

Apply this lesson in the [CT-03 Three-Format Social Campaign Capstone](capstone/README.md). The capstone must demonstrate not only three technically valid adaptations but also one evidence-led editorial decision and a reproducible performance review.

**Required capstone evidence linked to this lesson:**
1. Select one meaningful editorial decision affecting at least one output, such as opening structure, demonstration order, caption presentation or CTA timing.
2. Submit a test plan that identifies the decision, hypothesis, method, primary outcome, controlled conditions, guardrails and stopping rule.
3. Include two traceable variants where safe and practical. If a controlled comparison is not authorized or feasible, use a moderated comprehension review or structured peer review and state the limitation. Do not publish duplicate variants merely to create a test.
4. Include a metric dictionary and evidence log. Use authorized real data only; otherwise use a clearly labeled moderated/qualitative record or simulated exercise data. Never present simulated values as audience results.
5. Record a technical baseline on the learner's actual editing environment, then document one reversible optimization and retest, or justify with evidence why no optimization is required.
6. Recheck all three final exports after any optimization that could affect rendering, source selection, captions, audio or metadata.
7. Include the recommendation, uncertainty, rejected alternatives, rights/consent/privacy notes and final proof evidence in the handoff.

**Capstone acceptance gate:** no fabricated data, unauthorized analytics collection, unsupported causal claim, unlicensed asset, unapproved public test or unverified final export. A learner without authorized platform analytics can still demonstrate the learning outcomes through a consenting moderated test or documented peer review; the evidence type must be explicit.

## Further study and references

- NIST/SEMATECH — *e-Handbook of Statistical Methods*, including experimental design and measurement principles: https://www.itl.nist.gov/div898/handbook/
- FFmpeg — official documentation for media inspection and processing; verify the installed build and supported options: https://ffmpeg.org/documentation.html
- Adobe Help Center — Premiere Pro user guide; consult the installed release's proxy, playback, cache and export documentation: https://helpx.adobe.com/premiere-pro/user-guide.html
- Blackmagic Design — DaVinci Resolve training and official documentation: https://www.blackmagicdesign.com/products/davinciresolve/training
- Selected platform's current official analytics/experimentation documentation — record the exact page, metric definition and review date used in the learner's project.
- Related CT-03 lessons: [Lesson 01 — Audience, Platform and Format Design](lesson-01-audience-platform-and-format-design.md); [Lesson 02 — Hooks, Story Compression and Retention](lesson-02-hooks-story-compression-and-retention.md); [Lesson 03 — Vertical Reframing, Captions and Safe Composition](lesson-03-vertical-reframing-captions-and-safe-composition.md); [Lesson 04 — Advanced Multi-Format Pacing and Version Control](lesson-04-advanced-multi-format-pacing-and-version-control.md).
- Related practice: [Workbook Section 05 — Editorial Testing and Performance Log](workbook/section-05-editorial-testing-and-performance-log.md); [Lab 01 — Vertical Social Edit and Export](labs/lab-01-vertical-social-edit-and-export.md); [Lab 02 — Multi-Format Versioning and Batch Delivery](labs/lab-02-multi-format-versioning-and-batch-delivery.md).

## Version and change notes

- Revision 2.0 — 2026-11-19: expanded the initial draft into a complete expert lesson with experimental-method distinctions, metric definitions and denominators, confounder/uncertainty analysis, guardrails, privacy, technical bottleneck diagnosis, reversible optimization, proxy/cache distinctions, worked and dry-run examples, five guided exercises, independent assignment, capstone integration, troubleshooting, 16 answer-guided checks, 100-point rubric and mandatory QC gates.
- All campaign metrics and participant counts in the worked example are fictional instructional data; no real audience analytics or participant test was collected.
- No editing application, analytics provider, benchmark utility, proxy workflow, cache or export was executed in this authoring session.
- Metric definitions, platform experimentation rules, editor controls, codecs and hardware behavior are version-dependent. Verify the authoritative current documentation and record the actual environment before practical use.
- Independent academic, editorial, statistical, accessibility, rights/privacy and technical review remains outstanding.
