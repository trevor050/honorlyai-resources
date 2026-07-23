# K-12 AI incident response plan

> **Purpose:** A coordinated response template for unexpected AI behavior, unauthorized access, inappropriate disclosure, unsafe output, material policy violations, and vendor changes.
>
> **Related HonorlyAI resources:** https://honorlyai.com/resources

## Plan record

- District: `[DISTRICT]`
- Plan owner: `[ROLE]`
- Approved by: `[AUTHORITY]`
- Effective date: `[DATE]`
- Version: `[VERSION]`
- Emergency contact: `[CONTACT]`
- Privacy/security reporting route: `[URL/PHONE/EMAIL]`
- Next exercise/review: `[DATE]`

## 1. Incident categories

An AI incident may involve:

- unauthorized account or data access;
- exposure of student, educator, family, or district information;
- prompts, outputs, or files visible to the wrong user;
- unsafe, threatening, sexual, hateful, manipulative, or self-harm-related output;
- harmful bias or discriminatory treatment;
- inaccurate output used in a high-impact decision;
- bypass of teacher, district, or product safeguards;
- credential exposure or malicious prompt content;
- material vendor change to data use, model behavior, subprocessors, or terms;
- extended outage or reliability failure affecting instruction;
- suspected violation of district policy;
- another event requiring coordinated review.

## 2. Severity levels

### Severity 1: Critical

Immediate threat to safety; confirmed or likely broad unauthorized access; active exploitation; significant disclosure; or an AI-supported high-impact decision causing immediate harm.

Target action: immediate escalation and containment.

### Severity 2: High

Limited unauthorized access or disclosure; repeated unsafe behavior; material control failure; significant policy bypass; or vendor change that invalidates approval assumptions.

Target action: same-day triage and containment plan.

### Severity 3: Moderate

Isolated inappropriate output, incorrect flag, access issue, or policy concern with limited impact and no evidence of ongoing exposure.

Target action: prompt review, correction, and monitoring.

### Severity 4: Low

Routine defect, unclear wording, minor support issue, or low-impact error that does not involve sensitive data, safety, or unauthorized access.

Target action: normal support and improvement process.

Local response times: `[INSERT]`

## 3. Immediate actions

The first responder should:

1. protect immediate student and staff safety;
2. stop the affected interaction or workflow when safe;
3. avoid spreading harmful output or personal information;
4. preserve the minimum evidence necessary, including date, time, account, affected feature, and screenshots only when authorized;
5. report through the designated route;
6. avoid public accusations or conclusions before review;
7. not conduct unauthorized testing or access another person's account.

## 4. Triage record

- Incident ID: `[ID]`
- Date/time discovered: `[TIMESTAMP/TIME ZONE]`
- Reporter/contact: `[NAME/ROLE]`
- Product/model/version: `[INSERT]`
- Affected users/schools: `[INSERT]`
- Data potentially involved: `[INSERT]`
- Safety concern: `[YES/NO/UNKNOWN]`
- Ongoing exposure: `[YES/NO/UNKNOWN]`
- Severity: `[1/2/3/4]`
- Incident commander: `[NAME/ROLE]`
- Vendor ticket/contact: `[INSERT]`

## 5. Containment options

Depending on the event:

- disable a feature, integration, model, class, account, or district access;
- revoke sessions or credentials;
- change permissions;
- preserve logs;
- block an unsafe workflow;
- move instruction to an approved alternative;
- pause the pilot;
- request vendor isolation or deletion;
- notify relevant district leaders and counsel;
- activate safety, crisis, or student-support procedures.

Record who authorized containment and what instructional alternative is available.

## 6. Investigation questions

- What happened, and what remains uncertain?
- Which user, role, school, class, and product version were involved?
- Was the behavior caused by configuration, model output, user action, integration, vendor change, or unauthorized access?
- What data was accessed, generated, disclosed, changed, or retained?
- Who could view or retrieve it?
- When did exposure begin and end?
- Did an automated flag or system summary misstate the event?
- Were assignment directions and training clear?
- Did accessibility or language needs affect the interaction?
- Which contract, policy, legal, insurance, or notification duties require review?
- Is the issue reproducible without accessing real student data?

## 7. Communication

Assign owners for:

- affected students and families;
- educators and school leadership;
- district privacy, security, legal, communications, and executive teams;
- vendor and subprocessor coordination;
- board, regulator, insurer, law enforcement, or other notices when applicable;
- public statements.

Communications should separate confirmed facts, current risk, protective steps, available support, and open questions. Do not use vague reassurance or speculate about intent.

## 8. Recovery

Before restoring the workflow:

- [ ] Root cause or containment is sufficient.
- [ ] Access and configuration are verified.
- [ ] Required notices and support are underway.
- [ ] Data correction, return, export, or deletion has been addressed.
- [ ] Teachers and support staff know the revised procedure.
- [ ] An accessible alternative is available.
- [ ] The vendor has documented remediation and remaining risk.
- [ ] The district decision-maker has approved restoration.

## 9. Post-incident review

Within `[TIME]`, document:

- timeline;
- affected people, data, and systems;
- decisions and owners;
- root cause and contributing conditions;
- vendor performance;
- policy, training, product, contract, or support changes;
- evidence that remediation works;
- whether the pilot or approval should continue;
- next review date.

Do not publish private incident details in this public repository.

This template is not legal advice, an emergency plan, or a substitute for existing safety, cybersecurity, breach, records, and crisis procedures. Licensed under CC BY 4.0.
