# CT-27 Capstone — Reproducible Batch Transcode and Quality Pipeline

- Level: Master / Professional Practice
- Estimated time: 12–18 hours
- Status: Brief authored; execution and independent review not evidenced

## Brief
Design a batch media pipeline for an authorized test library. It must inventory inputs, validate media, process to a written specification, record logs, retry transient failures safely, quarantine permanent failures and produce an auditable manifest.

## Required deliverables
- architecture diagram and threat/risk notes;
- source inventory and target specification;
- versioned script/configuration;
- dry-run output;
- batch logs and error handling;
- output metadata and playback validation;
- manifest with source/output mapping and status;
- retry/quarantine test evidence;
- runbook, rollback and archive procedure;
- 500–800 word reflection.

## Mandatory gates
Originals remain unchanged. No secret credentials in source code or logs. No external upload without authorization. No output is marked successful without media-level validation.

## Rubric — 100 points
Architecture 10; safe file operations 15; media probing/specification 15; processing correctness 15; retries/observability 15; output validation 15; security/rights 5; reproducibility/handoff 10. Pass 80/100. Source overwrite or unsafe secret handling is a critical failure.

## Review protocol
Run on a clean test directory, compare expected and actual file counts, inspect logs, probe outputs, play representative/full outputs as required, simulate a failure and confirm rollback/quarantine. This brief alone does not establish execution.
