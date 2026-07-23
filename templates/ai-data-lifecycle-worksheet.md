# AI data lifecycle worksheet for schools

> **Canonical guide:** https://honorlyai.com/ferpa-ai-schools
>
> Map each data category from collection through deletion. A diagram or contract that says "encrypted" does not answer who uses the data, for what purpose, or how long it exists.

## System context

- District: `[DISTRICT]`
- Product/vendor: `[PRODUCT/VENDOR]`
- Educational purpose: `[PURPOSE]`
- Users/ages/grades: `[SCOPE]`
- Integrations: `[SSO/SIS/LMS/OTHER]`
- Reviewer: `[NAME/ROLE]`
- Date/version: `[DATE/VERSION]`

## Lifecycle map

Complete one row for every meaningful data category.

| Data category | Source | Collection method | Approved purpose | Storage/location | Authorized access | Subprocessors | Active retention | Backup retention | Export | Deletion trigger | Deletion verification |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Student identifier |  |  |  |  |  |  |  |  |  |  |  |
| Roster/class data |  |  |  |  |  |  |  |  |  |  |  |
| Prompt/conversation |  |  |  |  |  |  |  |  |  |  |  |
| Model output |  |  |  |  |  |  |  |  |  |  |  |
| Uploaded file/image |  |  |  |  |  |  |  |  |  |  |  |
| Teacher instruction |  |  |  |  |  |  |  |  |  |  |  |
| Feedback/rating |  |  |  |  |  |  |  |  |  |  |  |
| Safety/integrity flag |  |  |  |  |  |  |  |  |  |  |  |
| Device/log data |  |  |  |  |  |  |  |  |  |  |  |
| Support record |  |  |  |  |  |  |  |  |  |  |  |
| Inference/profile |  |  |  |  |  |  |  |  |  |  |  |
| Other |  |  |  |  |  |  |  |  |  |  |  |

## Questions at collection

- Is each field necessary for the approved purpose?
- Can identifiers be reduced, separated, or replaced?
- Can the task use fictionalized, local-only, or non-student data?
- Is collection obvious to the user?
- Which fields are optional?
- Does the product collect more in telemetry or logs than in the visible form?
- Are prompts and outputs treated as data records, transient processing, or both?

## Questions during use

- Which district roles can view individual data?
- Which vendor personnel can view content, and under what controls?
- Is data used for model training, evaluation, safety review, analytics, or product improvement?
- Can data be combined across customers or services?
- Can students or educators correct inaccurate information?
- Are flags and summaries distinguishable from verified facts?
- Is access logged and reviewable?

## Questions at retention and exit

- What event starts the retention clock?
- Are backups, logs, safety records, and support tickets on different schedules?
- Can the district request targeted deletion?
- What must the district export before deletion?
- How are legal holds handled?
- How quickly are departing users deprovisioned?
- What happens at contract expiration, nonrenewal, or vendor failure?
- How does the vendor confirm deletion?
- Which copies may remain, for how long, and why?

## Data-flow diagram

Use this plain-text structure or replace it with a reviewed diagram:

```text
[District system/user]
        |
        v
[Collection/API/integration]
        |
        +--> [Primary service/storage]
        |          |
        |          +--> [Authorized district roles]
        |          +--> [Vendor support access]
        |          +--> [Model provider/subprocessor]
        |          +--> [Analytics/safety systems]
        |
        +--> [Backups/logs]
                   |
                   v
          [Retention/deletion process]
```

Annotate every arrow with the data category, purpose, control, and retention period.

## Approval summary

- Minimum approved data: `[INSERT]`
- Prohibited data: `[INSERT]`
- Model-training/product-improvement rule: `[INSERT]`
- Human-review rule: `[INSERT]`
- Retention schedule: `[INSERT]`
- Subprocessor condition: `[INSERT]`
- Exit plan: `[INSERT]`
- Owner and next review: `[INSERT]`

This worksheet supports data minimization and review. It is not legal advice or a complete data inventory by itself. Licensed under CC BY 4.0.
