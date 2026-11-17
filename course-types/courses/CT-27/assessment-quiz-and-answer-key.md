# CT-27 — Batch Editing & Media Automation Assessment

**Total:** 50 points | **Suggested time:** 45–60 minutes

## Part A — Multiple choice (10 × 2 = 20)
1. FFprobe is primarily used to: A. Inspect media B. Paint frames C. Record voice D. Animate titles
2. A container and codec are: A. Identical concepts B. Different concepts C. Both file names D. Both filters
3. A dry-run should: A. Modify source files B. Show planned operations without applying them C. Delete failures D. Publish outputs
4. Idempotency helps prevent: A. Duplicate side effects B. Metadata inspection C. File playback D. Color correction
5. A queue retry policy should: A. Retry forever B. Distinguish transient/permanent errors and cap retries C. Ignore logs D. Delete source
6. A manifest should map: A. Inputs to outputs and status B. Only file sizes C. Only user names D. Only codec brand
7. Exit code zero guarantees playable media. A. True B. False
8. Watch folders should verify: A. File is stable/complete B. File name only C. Folder color D. Screen brightness
9. Secrets should be: A. Hard-coded B. Managed outside source scripts C. Printed to logs D. Shared publicly
10. AI classification output should be: A. Treated as authoritative B. Validated and routed to human review when uncertain C. Published immediately D. Used as rights approval

## Part B — Short answer (5 × 3 = 15)
11. Distinguish codec and container.
12. Name three output validation checks.
13. What is an idempotent job?
14. Why should permanent failures be quarantined?
15. What belongs in a release runbook?

## Part C — Applied case (15)
16. A batch job reports success for 100 files, but 7 outputs contain no audio. Explain how to diagnose and prevent recurrence. (8)
17. A watch-folder receives duplicate events and begins transcoding a file before upload completes. Design a safe control flow. (7)

## Answer key
1 A; 2 B; 3 B; 4 A; 5 B; 6 A; 7 B; 8 A; 9 B; 10 B.
11. Codec encodes/decodes a stream; container packages one or more streams and metadata. (3)
12. Metadata, stream presence, duration, playback, checksum, manifest reconciliation. (3)
13. Repeating the same job does not create duplicate unintended side effects. (3)
14. It prevents repeated futile attempts and preserves evidence for diagnosis. (3)
15. Versions, configuration, inputs/outputs, monitoring, failure/retry, rollback and contact/escalation. (3)
16. Probe audio stream mapping, inspect commands and output streams, test sample, add validation that rejects missing audio, rerun affected jobs from source and log defect. (8)
17. Wait for file stability/checksum, assign idempotency key, lock/claim job, validate input, enqueue once, cap retries and atomically publish completion. (7)

## Performance bands
45–50 exemplary; 40–44 competent; 35–39 developing; below 35 remediation. Source overwrite or unbounded unsafe execution is a critical failure.
