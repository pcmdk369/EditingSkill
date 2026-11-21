# CT-27 Professional Lab 02 — Watch Folder, Queue, Retry and Idempotency Simulation

- Level: Expert / Professional
- Estimated time: 4–6 hours
- Environment: Local test directory, scripting language/queue of choice and FFprobe
- Lab status: Authored design-and-test lab; no production service is deployed

## Brief
Design a local test pipeline that accepts files, waits for stable input, queues work, processes once, retries transient failures and quarantines permanent failures.

## Required state model
DISCOVERED → STABLE → VALIDATED → QUEUED → RUNNING → OUTPUT_QC → COMPLETED. Failure paths: RETRY_WAIT or QUARANTINED.

## Procedure
1. Create isolated input, temp, output, failed and logs directories.
2. Generate a unique job ID from source identity and operation parameters.
3. Simulate duplicate file-system events and verify only one active job is created.
4. Simulate a partial copy; ensure the pipeline waits for stable size/checksum.
5. Probe media and reject invalid or unsupported input.
6. Queue a valid job with bounded concurrency.
7. Simulate a transient failure and verify capped retry with backoff.
8. Simulate a permanent failure and verify quarantine without endless retry.
9. Write to a temporary output path and publish atomically only after QC.
10. Rerun the same job and confirm no duplicate output or side effect.
11. Cancel a running job and verify cleanup/rollback.
12. Audit structured logs and reconcile all source/job/output records.

## Validation
Duplicate events produce one job; partial files are not processed; retry count is bounded; permanent failures are quarantined; successful outputs pass media QC; rerun is idempotent.

## Deliverables
State diagram, job ID scheme, retry policy, test fixtures, logs, output manifest, failure report and runbook.

## Assessment — 100 points
State model 15; stable-input gate 15; idempotency 20; retry/quarantine 15; atomic output 10; QC/logging 15; runbook 10. Pass 80/100.
