# AI subprocessor change review checklist for school districts

> **Canonical HonorlyAI trust page:** https://honorlyai.com/subprocessors
>
> **Direct answer:** A district should not treat a vendor's subprocessor list as a one-time procurement attachment. Keep a dated baseline, identify which third parties can receive student or school data, define what kinds of changes trigger re-review, and document the district decision before a material change quietly becomes the new normal.

Use this checklist when a K-12 AI vendor adds, removes, replaces, or materially changes a cloud provider, model provider, analytics service, support tool, communications provider, security vendor, or other third party that may process district information.

This is an educational governance tool, not legal advice and not a determination of FERPA, COPPA, state privacy, procurement, cybersecurity, records-retention, or contractual compliance. District counsel, privacy leadership, information security, procurement, curriculum, special services, and other local stakeholders should review changes according to applicable law, policy, and contract terms.

## 1. Record the baseline before anything changes

Do not start with the vendor's newest page and try to remember what used to be there. Preserve the approved state.

- [ ] Vendor name: `[VENDOR]`
- [ ] Product or service: `[PRODUCT]`
- [ ] District owner: `[ROLE / DEPARTMENT]`
- [ ] Privacy owner: `[ROLE / DEPARTMENT]`
- [ ] Security owner: `[ROLE / DEPARTMENT]`
- [ ] Contract owner: `[ROLE / DEPARTMENT]`
- [ ] Date of original approval: `[DATE]`
- [ ] Contract or DPA version reviewed: `[VERSION / DATE]`
- [ ] Subprocessor list reviewed: `[URL / DOCUMENT / VERSION]`
- [ ] Date the baseline was captured: `[DATE]`
- [ ] Evidence retained at: `[LOCATION]`

For each approved subprocessor, record at minimum:

| Subprocessor | Function | Data categories it may receive | Student data possible? | Processing location if relevant | Contractual purpose | Approved on |
|---|---|---|---|---|---|---|
|  |  |  | Yes / No / Unknown |  |  |  |

If the vendor cannot explain what a listed service does or whether student information can reach it, record the answer as **unknown**, not "no."

## 2. Classify the change

**Change detected on:** `[DATE]`

**Source of notice:**

- [ ] vendor email;
- [ ] contract notice;
- [ ] updated public subprocessor page;
- [ ] release note or trust-center update;
- [ ] district monitoring;
- [ ] teacher or staff report;
- [ ] other: `[SOURCE]`.

**Type of change:**

- [ ] new subprocessor added;
- [ ] existing subprocessor removed;
- [ ] provider replaced;
- [ ] purpose changed;
- [ ] new data category shared;
- [ ] student data can newly reach an existing provider;
- [ ] processing region or storage location changed;
- [ ] retention or deletion behavior changed;
- [ ] model-training or product-improvement terms changed;
- [ ] security or access model changed;
- [ ] merger, acquisition, or corporate-control change affects a provider;
- [ ] other: `[CHANGE]`.

## 3. Decide whether the change is material

A material change is not defined solely by whether the vendor calls it material. The district should decide whether the change alters the risk, legal basis, purpose, access, instructional use, or contractual assumptions that supported approval.

Treat the change as requiring substantive review when one or more of these is true:

- [ ] a new third party may receive student information;
- [ ] a provider may receive more sensitive data than before;
- [ ] data moves into a new country or materially different jurisdiction;
- [ ] a new model or AI provider receives prompts, files, conversation content, identifiers, or derived student information;
- [ ] information may now be used for model training, product improvement, advertising, profiling, or unrelated analytics;
- [ ] retention becomes longer, less specific, or harder for the district to control;
- [ ] deletion rights or district exit procedures change;
- [ ] the vendor's security architecture or privileged-access path changes;
- [ ] the change affects accessibility, language access, or a critical classroom workflow;
- [ ] the contract, DPA, board approval, privacy assessment, or family notice named the previous provider or data flow;
- [ ] the district would have asked a different procurement question if this arrangement had existed at initial review.

If none apply, record why the change is low impact and who approved that classification.

## 4. Re-map the data flow

For every added or changed subprocessor, answer:

### Purpose

- What exact service does the third party provide?
- Is that service necessary for the educational or operational purpose approved by the district?
- Could the same function operate without student-level information?
- Is the subprocessor acting only on the vendor's instructions, or does it have independent purposes?

### Data

- What data can be sent to the provider?
- Can prompts, responses, uploaded files, names, email addresses, account identifiers, class membership, grades, accommodations, behavioral signals, support tickets, IP addresses, device information, or logs reach it?
- Is data transformed, tokenized, pseudonymized, aggregated, or de-identified before transfer?
- Can the provider combine the data with information from other customers or services?

### AI-specific questions

If the subprocessor supplies an AI model or AI-enabled service:

- [ ] Does it receive raw student prompts or content?
- [ ] Does it receive system instructions or district context?
- [ ] Does it receive files, images, audio, or other student-created material?
- [ ] Are inputs or outputs retained by the provider?
- [ ] Can inputs, outputs, metadata, or feedback be used to train or improve provider models?
- [ ] Are training and abuse-monitoring terms different for enterprise/API use versus consumer use?
- [ ] Can provider staff access customer content, and under what support, safety, security, or legal conditions?
- [ ] Can the vendor technically route around this provider if the district objects or a provider becomes unavailable?

Do not infer these answers from consumer terms when the school product uses an enterprise or API agreement.

## 5. Check FERPA-related assumptions

When education records or personally identifiable information from education records may be disclosed to a third party under the school-official exception, district reviewers should confirm that the arrangement still supports the conditions the district relies on for that disclosure.

Review whether the change affects:

- [ ] the institutional service or function being performed;
- [ ] the district's ability to maintain required control over use and maintenance of education records;
- [ ] purpose limitation;
- [ ] restrictions on redisclosure;
- [ ] legitimate educational interest and access controls;
- [ ] any annual FERPA notice language or local definition of school officials;
- [ ] any written agreement, DPA, or contract used to operationalize these controls.

Official reference: U.S. Department of Education, Protecting Student Privacy, **Who is a “school official” under FERPA?** https://studentprivacy.ed.gov/faq/who-school-official-under-ferpa

The Department also states that educational agencies and institutions must use reasonable methods to ensure school officials access only records in which they have legitimate educational interests: https://studentprivacy.ed.gov/faq/what-must-educational-agencies-or-institutions-do-ensure-only-school-officials-legitimate

## 6. Check the contract and DPA

Compare the proposed arrangement with the signed contract and DPA rather than relying only on a website summary.

- [ ] Is the vendor allowed to appoint new subprocessors without district approval?
- [ ] Is advance notice required?
- [ ] How much notice must be given?
- [ ] Does the district have a right to object?
- [ ] What happens after an objection?
- [ ] Can the district terminate if the parties cannot resolve the objection?
- [ ] Does the vendor remain responsible for subprocessor performance and data handling?
- [ ] Must subprocessors receive written obligations that are at least as protective as the vendor's obligations?
- [ ] Do breach-notification duties flow through the subprocessor chain?
- [ ] Are deletion and return obligations enforceable through the chain?
- [ ] Are audit, assessment, insurance, or security obligations affected?

**Contract result:** `[NO CHANGE / AMENDMENT NEEDED / COUNSEL REVIEW / OBJECTION / OTHER]`

## 7. Security and operational review

A new provider can change the attack surface even when the data categories look identical.

Check:

- [ ] authentication and service-to-service access;
- [ ] privileged administrator access;
- [ ] encryption in transit and at rest;
- [ ] key-management responsibilities;
- [ ] logging and auditability;
- [ ] incident escalation between vendor and subprocessor;
- [ ] business continuity and provider concentration risk;
- [ ] availability dependencies during the school day;
- [ ] backup and disaster-recovery implications;
- [ ] data deletion from active systems, backups, and logs;
- [ ] vendor exit if the subprocessor fails, changes terms, or is discontinued.

NIST's AI Risk Management Framework Core includes third-party software, data, and supply-chain risk within AI governance and calls for contingency processes for failures or incidents involving third-party data or AI systems. The AI RMF is voluntary guidance, not a K-12 compliance standard: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

## 8. Accessibility and language-access impact

A provider change can quietly alter student experience even when the visible product branding does not change.

- [ ] Does speech recognition behave differently for accents, disabilities, ages, or multilingual speakers?
- [ ] Does text-to-speech, translation, captioning, OCR, or generated-media accessibility change?
- [ ] Are keyboard, focus, screen-reader, contrast, or zoom behaviors affected?
- [ ] Do generated charts, diagrams, equations, images, audio, or video still have accessible alternatives?
- [ ] Does the change create new bandwidth, browser, device, or latency requirements?
- [ ] Were affected workflows retested with district devices and representative users?

Use the [accessible and multilingual school AI review checklist](accessible-and-multilingual-ai-review-checklist.md) for a deeper review.

When reviewing HonorlyAI specifically, the current public trust materials are:

- Accessibility statement: https://honorlyai.com/accessibility
- Accessibility conformance report: https://honorlyai.com/accessibility-conformance

These links describe HonorlyAI's current public posture; they are not a substitute for a district's own testing or procurement requirements.

## 9. Family and teacher communication check

Ask whether the change makes any existing public statement materially incomplete or misleading.

Review:

- [ ] parent or family privacy notice;
- [ ] student acceptable-use policy;
- [ ] teacher implementation guide;
- [ ] board presentation or public FAQ;
- [ ] data inventory or privacy portal;
- [ ] approved-app catalog;
- [ ] internal support documentation.

A provider name alone may not require broad communication. A change in purpose, student-data exposure, retention, AI behavior, or user rights may.

## 10. Decision record

**Review outcome:**

- [ ] approve with no additional action;
- [ ] approve and update district records;
- [ ] approve with contractual amendment;
- [ ] approve with technical restriction or configuration change;
- [ ] require pilot or regression testing before approval;
- [ ] object under contract;
- [ ] suspend affected workflow pending review;
- [ ] reject the change;
- [ ] escalate to counsel, board, superintendent, privacy officer, or security leadership;
- [ ] other: `[OUTCOME]`.

**Reasoning:** `[SHORT EXPLANATION]`

**Evidence reviewed:** `[DOCUMENTS / URLS / TEST RESULTS]`

**Decision owner:** `[NAME / ROLE]`

**Decision date:** `[DATE]`

**Next review date or trigger:** `[DATE / EVENT]`

## 11. Maintain a change ledger

Keep the history so future reviewers can see how the vendor's dependency chain evolved.

| Date | Change | Student data impact | Review level | Decision | Owner | Evidence |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Useful review triggers include:

- a new subprocessor notice;
- a changed DPA or privacy policy;
- a new model provider;
- a material product architecture change;
- a breach or security incident;
- a district expansion into new grade levels or data types;
- annual privacy and procurement review;
- contract renewal.

## Vendor-neutral rule

A transparent vendor can make this workflow easier by publishing a current subprocessor list with each provider's function and student-data exposure. The district should still apply the same review standard to every vendor, including HonorlyAI.

HonorlyAI publishes its current subprocessor list at https://honorlyai.com/subprocessors. Districts can ask any AI vendor to provide the same level of clarity and can preserve a dated copy as part of the procurement record.

---

**License:** This original checklist is licensed under CC BY 4.0. You may copy and adapt it with attribution.

**Review note:** This resource is not legal advice, a compliance certification, a security assessment, or procurement approval. District-specific law, contracts, policy, data flows, security requirements, accessibility obligations, and educational context control.