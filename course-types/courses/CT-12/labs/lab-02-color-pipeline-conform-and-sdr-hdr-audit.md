# CT-12 Professional Lab 02 — Color Pipeline Conform and SDR/HDR Delivery Audit

- Course: CT-12 — Color Correction & Color Grading
- Level: Expert / Professional
- Estimated time: 4–6 hours
- Environment: Color-managed grading application, calibrated/reference display where available, waveform/vectorscope and metadata tools
- Lab status: Authored procedure; no display calibration, HDR mastering or device validation is claimed

## 1. Scenario
A mixed-camera project contains log footage, standard display-referred clips and a requested SDR master. A second HDR deliverable may be requested later. Build a documented color pipeline that prevents accidental double transforms and keeps the SDR and HDR deliverables distinct.

## 2. Learning objectives
- inventory camera/source color characteristics;
- define a color-management pipeline and output transform;
- use scopes alongside visual monitoring;
- distinguish creative look from technical correction;
- create separate output paths for different delivery targets;
- validate metadata and playback on intended review systems.

## 3. Inputs and prerequisites
Use authorized footage with known or documented source settings where possible. Record camera, codec, bit depth, transfer characteristics, gamut, frame rate and any supplied LUTs. If source metadata is unknown, mark it unknown rather than guessing.

## 4. Pipeline record
Document:
- source color space/gamma or camera log profile;
- input transform method and LUT/version;
- working color space and timeline settings;
- display/monitor assumptions and calibration status;
- creative look node/order;
- output transform and target color space;
- export codec, bit depth, metadata and destination;
- review device and known limitations.

## 5. Procedure
1. Back up the project and create a technical test sequence.
2. Inventory source clips and group by camera/profile.
3. Confirm sequence/timeline color settings before applying transforms.
4. Choose one managed transform strategy; avoid stacking an input LUT and automatic transform unintentionally.
5. Normalize exposure and white balance using scopes and reference frames.
6. Match shots before applying the creative look.
7. Build the look on a separate node/group so it can be bypassed and compared.
8. Check skin/object hue, saturation, highlight roll-off and shadow detail.
9. Render a short SDR test using the specified output transform.
10. Inspect scopes, metadata and playback on the intended SDR review path.
11. If HDR is required, define a separate HDR target and mastering/display assumptions; do not simply relabel the SDR file.
12. Render a separate HDR proof and verify transfer/gamut metadata and tone mapping using qualified equipment/workflow.
13. Compare both outputs for intended creative continuity and destination suitability.
14. Record any unverified display or metadata limitations in the handoff.

## 6. Scope interpretation
- Waveform: signal level and exposure distribution.
- RGB parade: channel balance and color casts.
- Vectorscope: hue/saturation distribution.
- Histogram: broad tonal distribution; not a substitute for video scopes.
- False color: exposure aid whose mapping depends on configuration.

Scopes provide measurement, not automatic creative correctness. Confirm the tool's scale and legal/full-range interpretation before relying on numeric thresholds.

## 7. Validation matrix
| Test | Method | Pass condition |
|---|---|---|
| Source inventory | Inspect metadata and camera notes | Profiles recorded or marked unknown |
| Transform chain | Inspect project nodes/settings | No unintended double transform |
| Shot match | Compare references/scopes | No unexplained exposure/color jumps |
| SDR output | Inspect metadata and playback | Matches specified target |
| HDR output | Separate proof and metadata check | Matches approved HDR spec |
| Display assumption | Record monitor/device status | No unsupported accuracy claim |
| Conform | Reopen project and relink media | No missing dependencies |
| Handoff | Audit pipeline sheet | Another operator can reproduce |

## 8. Troubleshooting
- Double contrast/saturation: check input LUT and color-management transform overlap.
- Washed-out export: inspect range tags, output transform and player interpretation.
- Clipped highlights: review source headroom and tone mapping; do not invent detail.
- Different devices disagree: verify profiles, metadata and display state before changing grade.
- HDR looks wrong in SDR player: confirm correct tone mapping and review path rather than grading blindly.

## 9. Deliverables
Source inventory, pipeline diagram/settings sheet, matched scene, creative look, SDR export, optional separate HDR proof, metadata reports, QC notes and handoff manifest.

## 10. Assessment — 100 points
Source/pipeline diagnosis 20; transform management 20; correction and shot matching 15; look separation 10; SDR/HDR target handling 15; technical QC 10; reproducible handoff 10. Pass 80/100. Mislabeling output color space or claiming unverified mastering is a critical failure.

## 11. Completion checklist
- [ ] Source color characteristics recorded.
- [ ] Timeline and working space documented.
- [ ] Transform chain checked for duplication.
- [ ] Correction and creative look separated.
- [ ] Scopes interpreted with correct scale/range.
- [ ] SDR output inspected against target.
- [ ] HDR handled as a distinct workflow if required.
- [ ] Metadata, review limitations and handoff recorded.
