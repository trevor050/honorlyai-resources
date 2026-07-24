# District AI procurement question bank

> **Purpose:** A written-response and evidence request for K-12 districts evaluating an AI-enabled product or service.
>
> **Canonical guide:** https://honorlyai.com/evaluate-ai-vendors-for-schools
>
> **Related field notes:** [FERPA, COPPA, and state privacy laws: who reviews what when schools buy AI?](https://honorlyai.com/blog/ferpa-coppa-state-privacy-school-ai) and [The school AI procurement questions vendors hope you do not skip](https://honorlyai.com/blog/school-ai-procurement-questions)
>
> **Status:** Editable template. This is not legal advice, procurement approval, a security assessment, or a compliance certification.

## Procurement record

- District: `[DISTRICT NAME]`
- Vendor legal name: `[LEGAL NAME]`
- Product and edition: `[PRODUCT / TIER / VERSION]`
- Proposed educational purpose: `[PURPOSE]`
- Users and grade range: `[USERS]`
- Review owner: `[NAME / ROLE]`
- Response due date: `[DATE]`
- Contract term considered: `[TERM]`
- Vendor response version: `[DATE / VERSION]`

## Vendor response instructions

For each answer:

1. state whether the answer applies to the exact product, edition, configuration, and contract under review;
2. identify any feature that is optional, unavailable, in beta, or limited by tier;
3. attach or link the supporting document;
4. identify the person responsible for the answer;
5. mark any answer that is expected to change during the proposed term.

A marketing page or generic statement such as “FERPA compliant,” “COPPA compliant,” “secure,” or “AI-powered” is not a complete response.

## 1. Educational purpose and product boundary

1. What specific K-12 educational or operational problems is the product designed to address?
2. Which uses are discouraged, unsupported, or prohibited?
3. Which capabilities are powered by generative AI, predictive models, rules, retrieval, or third-party services?
4. What changes by student age, grade, subject, role, assignment, language, or district setting?
5. Which consequential decisions can the product recommend or automate?
6. Which decisions must remain with a teacher, administrator, counselor, special-services professional, or other human?
7. What evidence supports the proposed learning or workload claims?
8. What limitations, negative findings, or populations not studied should the district understand?

**Evidence requested:** product architecture overview, supported-use statement, excluded-use statement, study summaries, known-limitations documentation.

## 2. Accounts, identity, and access

1. Can all users authenticate through district-managed accounts?
2. Which single sign-on, rostering, and lifecycle-management methods are supported?
3. Provide the complete role and permission matrix.
4. Can the district limit access by school, grade, course, class, assignment, feature, and date?
5. Which vendor employees or contractors can access district content, and under what approval and logging controls?
6. Can the district review privileged access and administrative changes?
7. How quickly can users be provisioned, suspended, and deleted?
8. How are shared devices, substitute teachers, transferred students, and departed staff handled?

**Evidence requested:** role matrix, authentication documentation, audit-log example, support-access procedure, offboarding procedure.

## 3. Complete data flow

For every data category, describe collection, purpose, recipient, storage, access, retention, deletion, and export.

Include:

- names, identifiers, and roster data;
- prompts, messages, files, assignments, and teacher instructions;
- AI responses, feedback, scores, summaries, flags, classifications, and recommendations;
- device, network, usage, and diagnostic data;
- support tickets and human-review records;
- embeddings, profiles, analytics, aggregate data, and other derived information.

Questions:

1. Which data is required, optional, inferred, or generated?
2. Which systems and subprocessors receive each category?
3. In which countries or regions is data stored or processed?
4. Are prompts, outputs, or files used for model training, fine-tuning, evaluation, safety review, product improvement, or human quality review?
5. Which uses can the district disable contractually and technically?
6. Does deletion cover primary storage, backups, logs, derived data, and model-related datasets?
7. Can the district verify deletion and obtain a destruction certification?
8. What data remains after contract termination, and why?

**Evidence requested:** current data-flow diagram, subprocessor list, retention schedule, deletion procedure, model-training and product-improvement statement.

## 4. FERPA, COPPA, state law, and records support

1. How does the product support a district acting under the Family Educational Rights and Privacy Act school-official exception when applicable?
2. What controls support district direction and control over the use and maintenance of education records?
3. For users under 13, what notice and consent pathways does the vendor support under the Children's Online Privacy Protection Act?
4. Does the vendor use children's information for advertising, unrelated commercial purposes, profiling, or sale?
5. Which state student-privacy terms or addenda are available?
6. How does the vendor support access, correction, export, record hold, deletion, and parent or eligible-student requests where applicable?
7. How are legal demands, subpoenas, and government requests handled and communicated?
8. Which product records may become district education or public records?

**District note:** applicability and legal sufficiency are district determinations made with counsel. Vendor responses provide evidence; they do not certify the district's use.

## 5. Model providers and product change

1. Identify every model provider used by the product and the purpose of each model.
2. Can the vendor change the model provider, model version, system instructions, moderation, web access, memory, or data use during the contract?
3. Which changes trigger advance notice, district approval, re-review, or an opt-out?
4. Can the district remain on a stable configuration during a school term?
5. How are releases tested against age, subject, language, safety, privacy, and teacher-control requirements?
6. What incident or change history is available for the product?
7. Can the district disable new AI features by default until reviewed?

**Evidence requested:** model and feature inventory, change-notice policy, release-testing summary, material-change contract language.

## 6. Classroom controls and teacher visibility

1. Can teachers define permitted assistance per assignment?
2. Can the system favor questions, explanations, examples, and hints before final answers?
3. What student activity is visible to teachers and administrators?
4. Can users see why a response was refused, redirected, summarized, or flagged?
5. Are aggregate patterns available before individual transcript review?
6. What justifies individual drill-down, and is sensitive access logged?
7. Can teachers correct, dismiss, or annotate inaccurate alerts and summaries?
8. Can the district export evidence needed for fair academic or safety review?

**Evidence requested:** live demonstration using district-written scenarios, screenshots of relevant teacher and administrator workflows, alert logic and limitation documentation.

## 7. Safety, reliability, and human escalation

1. How does the product address harmful, age-inappropriate, biased, or unsafe requests and outputs?
2. What happens when a student discloses self-harm, abuse, threats, or other urgent concerns?
3. What does the product tell the student, and who is notified?
4. How are hallucinations, unsupported claims, source errors, and uncertainty communicated?
5. How does the vendor test prompt injection, data leakage, jailbreaks, and misuse?
6. What are the false-positive and false-negative limitations of alerts or classifiers?
7. How can users report a problem, and what response times apply?
8. What uptime, latency, recovery, and support commitments apply?

## 8. Security evidence

Request evidence appropriate to the proposed risk and data:

- independent assessment or audit scope and date;
- penetration-testing and remediation process;
- encryption and key-management summary;
- vulnerability disclosure and patching process;
- logging, monitoring, backup, and disaster recovery;
- incident-notification timeline and required notice content;
- software-development and change-control practices;
- cyber-insurance and subcontractor requirements where appropriate.

Document which evidence was reviewed, by whom, and any remaining conditions.

## 9. Accessibility, language, and equity

1. Provide current accessibility conformance documentation for the exact product version.
2. Describe testing with keyboard navigation, screen readers, zoom, contrast, captions, alternative input, and assistive technology.
3. Which languages are supported, and how is quality evaluated?
4. What reading-level or communication controls exist?
5. What equivalent alternative is available when a student cannot or should not use the AI workflow?
6. What known subgroup performance differences or accessibility limitations exist?
7. How are barriers reported, prioritized, and remediated?

## 10. Contract, cost, support, and exit

1. Identify all license, usage, model, storage, support, integration, and overage costs.
2. What implementation and training are included?
3. Who owns district content, configuration, and exported records?
4. Which promises will be incorporated into the signed agreement or data-protection addendum?
5. Can the district suspend a feature or terminate for privacy, security, accessibility, instructional, legal, or material-change concerns?
6. What export format and transition support are available?
7. What is deleted at termination, on what schedule, and how is deletion verified?
8. What service continues during a transition or dispute?

## District scoring summary

| Domain | Pass | Conditional | Fail | Evidence / conditions |
|---|---:|---:|---:|---|
| Educational purpose |  |  |  |  |
| Identity and access |  |  |  |  |
| Data and privacy |  |  |  |  |
| Legal and records support |  |  |  |  |
| Model and change control |  |  |  |  |
| Teacher control |  |  |  |  |
| Safety and reliability |  |  |  |  |
| Security |  |  |  |  |
| Accessibility and equity |  |  |  |  |
| Contract, support, and exit |  |  |  |  |

## Decision

- Decision: `[DECLINE / REQUEST INFORMATION / LIMITED PILOT / APPROVE WITH CONDITIONS / APPROVE]`
- Approved scope: `[INSERT]`
- Required contract changes: `[INSERT]`
- Required configuration: `[INSERT]`
- Prohibited or deferred uses: `[INSERT]`
- Open risks and owners: `[INSERT]`
- Next review date or trigger: `[INSERT]`

Licensed under CC BY 4.0. Suggested attribution is available in the repository [README](../README.md). This template is general educational material and not legal advice, procurement approval, a security assessment, or a compliance certification.
