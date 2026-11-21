# CT-03 Workbook Section 05 — Editorial Testing and Performance Log

**Purpose:** Design fair, privacy-conscious editorial tests; interpret evidence without overclaiming; diagnose editing-performance bottlenecks; and record reversible optimization and final-proof evidence.

**Use with:** [CT-03 Lesson 05 — Expert Editorial Testing and Performance Optimization](../lesson-05-expert-editorial-testing-and-performance-optimization.md).

> All sample data in this workbook are fictional. Mark every simulated value clearly. Do not record passwords, private messages, unnecessary personal identifiers or confidential analytics exports.

## 1. Editorial decision and hypothesis

- Campaign / project ID:
- Decision owner:
- Audience and viewing context:
- Intended comprehension or action:
- Current approved baseline version:
- Decision to be made:
- Why this decision matters:

**Hypothesis**

- If we change:
- We expect:
- Because:
- We will measure:
- Evidence that would weaken the hypothesis:
- What we will not claim from this test:

## 2. Test method selection

Choose and justify one primary method.

| Method | Selected? | Reason / limitation |
|---|---|---|
| Editorial peer review | | |
| Moderated comprehension test with consenting participants | | |
| Authorized platform experiment | | |
| Observational analytics comparison | | |
| Simulated dataset for practice only | | |

- Is allocation randomized by a supported method? Yes / No / Not applicable
- If not, why is the result not described as a controlled experiment?
- Who authorized access and collection?
- Participant consent/notice record location, if applicable:
- Data minimization and retention plan:

## 3. Variable and variant manifest

| Field | Control / Variant A | Variant B | Held constant / notes |
|---|---|---|---|
| Master project / version | | | |
| Sequence / output ID | | | |
| Opening shot | | | |
| Runtime | | | |
| Caption style and wording | | | |
| Offer / CTA | | | |
| Music / audio | | | |
| Audience / allocation | | | |
| Distribution surface / window | | | |
| Other differences | | | |

**Primary variable changed:**  
**Potential confounders:**  
**Rights/factual/accessibility parity checked by:**  
**Reviewer and date:**  

## 4. Metric dictionary

Complete one row for each metric before collecting or reviewing outcomes.

| Metric label | Provider/source | Exact definition | Numerator | Denominator / eligible event | Window | Checked on | Limitation |
|---|---|---|---|---|---|---|---|
| Primary | | | | | | | |
| Guardrail 1 | | | | | | | |
| Guardrail 2 | | | | | | | |
| Secondary | | | | | | | |

Do not copy a metric label from a dashboard without recording its provider definition. If the denominator or calculation is unavailable, mark it unknown and do not derive a rate.

## 5. Guardrails and stopping rule

| Guardrail | Acceptable condition | Stop / hold condition | Owner |
|---|---|---|---|
| Factual claim and qualifier | | | |
| Caption accuracy/accessibility | | | |
| Rights and consent | | | |
| Privacy and participant safety | | | |
| Negative comprehension / confusion | | | |
| Technical playback / delivery | | | |

- Start condition:
- Observation window:
- Minimum evidence condition and rationale:
- Stop condition:
- Who can authorize a change or release?
- What would make the test inconclusive?

## 6. Evidence collection log

| Date/time and time zone | Variant ID | Eligible count | Numerator | Denominator | Exclusions / missing data | External factors | Source reference |
|---|---|---:|---:|---:|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

**Data classification:** Real authorized data / Moderated qualitative notes / Simulated exercise data  
**If simulated, label:** SIMULATED — NOT AUDIENCE RESULTS  
**Reviewer:**  
**Access restrictions and retention date:**  

## 7. Analysis and interpretation

| Outcome | Variant A | Variant B | Difference | Guardrail result | Interpretation / uncertainty |
|---|---:|---:|---:|---|---|
| Primary | | | | | |
| Guardrail 1 | | | | | |
| Guardrail 2 | | | | | |

- Percentage-point difference (if comparing percentages):
- Relative change (only if denominator and base are valid):
- Sample limitations:
- Confounders:
- Missing/estimated data:
- Is the result descriptive, qualitative, experimental, observational, simulated or inconclusive?
- What conclusion is justified?
- What conclusion would be an overclaim?
- Recommended next test:

**Calculation reminder:** 65% − 60% = 5 percentage points. Relative to 60%, the increase is about 8.3%. Do not confuse these quantities.

## 8. Technical environment and baseline

**Project / sequence:**  
**Source media IDs:**  
**Editor and exact version:**  
**Operating system/version:**  
**Device / CPU / GPU / RAM:**  
**Storage location/type and available space:**  
**Project dimensions / frame rate:**  
**Source codec / resolution / frame rate:**  
**Effects, plugins and linked dependencies:**  
**Power/thermal/background conditions, if relevant:**  
**Test segment/timecode:**  
**Operation tested:** Playback / Scrub / Effect preview / Cache / Export / Transfer  

| Baseline observation | Value / description | Measurement method | Date / evidence |
|---|---|---|---|
| Playback/drop-frame behavior | | | |
| Scrub responsiveness | | | |
| Preview/render elapsed time | | | |
| Export elapsed time (if tested) | | | |
| CPU/GPU/memory/storage observation | | | |

If no reliable measurement is available, record the observation and method rather than inventing a number.

## 9. Bottleneck diagnosis and controlled changes

| Change ID | Suspected bottleneck | One change applied | Same test repeated? | Result | Quality/portability impact | Keep / revert |
|---|---|---|---|---|---|---|
| OPT-001 | | | | | | |
| OPT-002 | | | | | | |
| OPT-003 | | | | | | |

**Diagnosis notes**
- Evidence that supports the suspected bottleneck:
- Other causes considered:
- Why the selected change is proportionate:
- Rollback method:
- Who authorized any destructive, paid or externally hosted operation:

## 10. Proxy, optimized media and cache record

| Mechanism | Enabled? | Source-to-proxy mapping verified? | Storage location | Export behavior verified? | Quality / portability notes |
|---|---|---|---|---|---|
| Proxy media | | | | | |
| Optimized media | | | | | |
| Render cache | | | | | |

- Which media representation is intended for final export?
- How was that behavior verified in the selected application/version?
- Were original media preserved?
- Can the project be reopened on another approved location/device?
- What cleanup is safe, and what must not be deleted?

## 11. Final proof and regression QC

**Exact proof filename/version:**  
**Export source path / mode:**  
**Specification revision:**  
**Reviewer / date:**  

| Check | Expected condition | Actual result / evidence | Pass / fail / not tested |
|---|---|---|---|
| Original media relink/source selection | | | |
| Dimensions / aspect ratio / frame rate | | | |
| Resolution and scaling | | | |
| Motion / cadence / dropped frames | | | |
| Color and effects | | | |
| Audio sync / intelligibility | | | |
| Captions / spelling / cue timing | | | |
| Qualifier / CTA / factual accuracy | | | |
| Full playback | | | |
| Project portability / dependencies | | | |
| Manifest and filename match | | | |

Do not mark an untested item as passed. Record why it was not tested and who must resolve it.

## 12. Recommendation and decision record

- Observed evidence:
- Interpretation:
- Uncertainty / limitations:
- Guardrail failures or trade-offs:
- Recommendation:
- Rejected alternative and reason:
- Further test required:
- Decision owner / approval / date:
- Release status: Hold / Revise / Approved for specified scope / Not authorized

## 13. Reflection and submission checklist

- [ ] Decision and hypothesis are stated.
- [ ] Method is accurately labeled.
- [ ] Variant IDs and exact differences are traceable.
- [ ] Metric definitions and denominators are documented.
- [ ] Guardrails and stop rule were set before reviewing results.
- [ ] Privacy, rights, consent and accessibility are addressed.
- [ ] Evidence is clearly labeled as real, qualitative or simulated.
- [ ] Limitations and inconclusive results are retained.
- [ ] Technical environment and baseline are recorded.
- [ ] Bottleneck diagnosis uses repeatable conditions.
- [ ] Changes are reversible and rollback is documented.
- [ ] Proxy/optimized-media/cache behavior is verified or marked not tested.
- [ ] Final proof is identified and checked against its own specification.
- [ ] Recommendation separates observation from interpretation.

**Learner:**  
**Reviewer:**  
**Date:**  
**Result:** Not submitted / In progress / Resubmit / Pass  
**Evidence location:**  

