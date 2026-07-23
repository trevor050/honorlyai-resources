# School AI privacy review checklist

> **Canonical guide:** https://honorlyai.com/school-ai-privacy-checklist
>
> **Purpose:** Help a K-12 district document what student and school information an AI service processes, why it is needed, who controls it, and what happens throughout the data lifecycle.
>
> This checklist supports review. It does not determine legal compliance.

## Review record

- District: `[DISTRICT NAME]`
- Product/vendor: `[PRODUCT AND LEGAL ENTITY]`
- Approved purpose: `[PURPOSE]`
- Users and age/grade range: `[USERS]`
- Data owner: `[DISTRICT ROLE]`
- Privacy reviewer: `[NAME/ROLE]`
- Agreement and version reviewed: `[DOCUMENT/VERSION/DATE]`
- Review date: `[DATE]`
- Next review: `[DATE OR TRIGGER]`

## 1. Define the context before reviewing terms

- [ ] The educational purpose is specific.
- [ ] The district has identified the intended users, ages, grades, subjects, and settings.
- [ ] The district has documented prohibited and deferred use cases.
- [ ] The district has determined which accounts, devices, networks, and integrations are involved.
- [ ] The district has identified applicable federal, state, local, contractual, and board-policy requirements.
- [ ] A less data-intensive alternative was considered.

## 2. Build a complete data inventory

For each category, mark whether it is collected, generated, inferred, received from an integration, or optional.

| Data category | Collected? | Source | Purpose | Required? | Examples |
|---|---|---|---|---|---|
| Student identifiers |  |  |  |  |  |
| School/grade/class/roster data |  |  |  |  |  |
| Prompts and conversation text |  |  |  |  |  |
| Model outputs |  |  |  |  |  |
| Uploaded files or images |  |  |  |  |  |
| Teacher instructions/settings |  |  |  |  |  |
| Feedback, ratings, or corrections |  |  |  |  |  |
| Device, browser, IP, or log data |  |  |  |  |  |
| Usage analytics |  |  |  |  |  |
| Safety or integrity flags |  |  |  |  |  |
| Inferences or profiles |  |  |  |  |  |
| Support communications |  |  |  |  |  |
| Other |  |  |  |  |  |

- [ ] The vendor confirms that the inventory covers production, support, analytics, safety, model, and backup systems.
- [ ] Optional fields and telemetry can be disabled where appropriate.
- [ ] The district knows what is stored versus processed transiently.
- [ ] Sensitive and high-risk data categories are explicitly addressed.

## 3. Purpose and secondary use

- [ ] Each data category has an approved purpose.
- [ ] The contract limits use to the district-authorized service.
- [ ] The vendor explains whether data is used for model training, fine-tuning, evaluation, product improvement, safety review, or human review.
- [ ] The vendor explains whether district data may influence services for other customers.
- [ ] Advertising, sale, cross-context behavioral advertising, unrelated profiling, and other commercial uses are addressed.
- [ ] New purposes require notice and district review.
- [ ] Deidentified or aggregated data terms define the method, risk controls, permitted use, and retention rather than relying on the label alone.

## 4. Legal pathway and district control

Do not treat a vendor's generic claim as the legal analysis.

- [ ] The district has identified the lawful basis or disclosure pathway for each data flow.
- [ ] The agreement reflects the approved educational purpose.
- [ ] District direction and control over use and maintenance are documented where required.
- [ ] Redisclosure and onward use are restricted.
- [ ] Parent or eligible-student rights workflows are supported where applicable.
- [ ] Notice and consent responsibilities are assigned.
- [ ] The district has reviewed age-specific requirements and whether school authorization is available for the exact use.
- [ ] Applicable state student privacy requirements have been reviewed.

Questions to resolve:

1. Which party is responsible for each notice, consent, access, correction, and deletion step?
2. Can the vendor act independently with the data, or only under district instruction?
3. What happens when a user leaves the district or a parent exercises an applicable right?
4. What records must the district preserve even after product deletion?

## 5. Access and human review

- [ ] Role-based access is documented.
- [ ] Teacher visibility is limited to legitimate educational responsibilities.
- [ ] District administrators can review privileged access.
- [ ] Vendor employee access is limited, logged, justified, and time-bound.
- [ ] Support access requires authentication and an auditable process.
- [ ] Human review of prompts or outputs is disclosed and constrained.
- [ ] The district knows whether contractors or subprocessors can access identifiable content.
- [ ] Access is removed promptly when roles change.

## 6. Subprocessors and data location

| Subprocessor | Function | Data involved | Location | Contract control | Change notice |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

- [ ] The current list is available before approval.
- [ ] Material additions or changes trigger advance notice.
- [ ] The district has a review, objection, or termination pathway.
- [ ] Security, confidentiality, deletion, and purpose restrictions flow down.
- [ ] International transfers and storage locations are disclosed.

## 7. Retention, deletion, and exit

| Data category | Active retention | Backup retention | Deletion trigger | Deletion method | Verification |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

- [ ] Retention periods are specific rather than "as long as necessary."
- [ ] Different retention rules for logs, safety events, support, backups, and legal holds are explained.
- [ ] District-initiated and user-initiated deletion workflows are documented.
- [ ] Data is exportable in a usable format before exit.
- [ ] Contract termination triggers return or deletion.
- [ ] The vendor provides deletion confirmation where appropriate.
- [ ] The district's own records obligations are not confused with vendor retention.

## 8. Security and incident response

- [ ] Security controls match the sensitivity and scope of data.
- [ ] Data is protected in transit and at rest.
- [ ] Secrets, keys, and privileged credentials are managed appropriately.
- [ ] Logging and monitoring cover unauthorized access and unusual data flows.
- [ ] Vulnerability management and independent assessment evidence are current and scoped.
- [ ] The incident-notification timeline, recipients, content, cooperation, and remediation duties are contractual.
- [ ] The vendor can identify affected users, data, systems, and time periods.
- [ ] The district has its own escalation and communication plan.

## 9. Transparency and accuracy

- [ ] Public privacy materials match negotiated terms.
- [ ] Student and family notices describe actual data flows and educator visibility.
- [ ] Product interfaces do not contradict district policy.
- [ ] Material changes to the model, product, data use, or subprocessors trigger review.
- [ ] The district has a route to correct inaccurate account, roster, flag, or profile information.
- [ ] Automated flags are not treated as factual findings without human review.

## 10. Decision

### Approved data and purpose

`[INSERT]`

### Conditions and mitigations

`[INSERT]`

### Unresolved questions

`[INSERT]`

### Prohibited data or uses

`[INSERT]`

### Review triggers

- contract renewal;
- new data category;
- new educational purpose;
- new age or grade group;
- model training or product-improvement change;
- new subprocessor;
- security/privacy incident;
- material product redesign;
- legal or regulatory update;
- `[LOCAL TRIGGER]`.

Licensed under CC BY 4.0. Consult district counsel and privacy leadership for district-specific legal analysis.
