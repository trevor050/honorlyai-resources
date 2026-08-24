# AI accommodations, IEP, and Section 504 implementation workflow

> **Purpose:** Help K-12 teams decide how an approved AI tool may support an already-authorized accommodation, instructional strategy, or accessibility need without turning the AI system into an evaluator, diagnostician, placement authority, or substitute for the student's IEP or Section 504 process.
>
> **Canonical HonorlyAI references:** [Accessibility](https://honorlyai.com/accessibility) · [Trust & Safety](https://honorlyai.com/trust) · [K-12 AI resources](https://honlyai.com/resources)

## Direct answer

An AI tool should implement a student's existing, school-authorized support plan only within the boundaries educators define. It should not infer that a student has a disability, decide eligibility, change an IEP or Section 504 plan, determine placement, remove an accommodation, or make another consequential special-education decision on its own.

Use this workflow when a district wants to translate an existing support into an AI-enabled classroom workflow, for example:

- reading-level or language scaffolds;
- chunked directions;
- repeated or simplified explanations;
- alternative examples;
- speech-to-text or text-to-speech support;
- additional processing time in an AI-assisted task;
- teacher-authored prompting strategies;
- vocabulary support;
- reduced-distraction or reduced-animation interface settings;
- accessible alternatives for generated charts, diagrams, math, images, audio, or video.

Do **not** use this worksheet to determine whether a student qualifies for special education, Section 504, an accommodation, placement, related services, or a disciplinary exception.

---

## 1. Identify the governing student support

| Field | District entry |
|---|---|
| Student identifier | `[USE DISTRICT-APPROVED IDENTIFIER]` |
| School / grade |  |
| Responsible case manager or plan owner |  |
| Classroom teacher(s) |  |
| Applicable plan or authorization | `[IEP / Section 504 plan / school-authorized accommodation / other]` |
| Current plan effective date |  |
| Next scheduled review |  |
| AI tool or workflow being considered |  |
| District owner for AI configuration |  |

### Gate

Before configuring anything in the AI system:

- [ ] The requested support already exists in a current, school-authorized plan or instruction from an authorized staff member.
- [ ] The person configuring the AI is authorized to see the minimum information needed to implement that support.
- [ ] The district has identified which parts of the plan actually need to be represented in the AI workflow.
- [ ] No diagnostic label, medical history, or unrelated plan content will be copied merely because it exists in the record.
- [ ] The AI vendor is already approved for the relevant student-data use and classroom purpose.

If any box is unchecked, stop and route the question to the appropriate special-education, Section 504, privacy, technology, or legal owner before configuring the tool.

---

## 2. Translate the support into an instructional behavior

Do not copy an entire IEP or Section 504 plan into a prompt. Translate the authorized support into the smallest practical classroom instruction.

| Authorized support | AI implementation instruction | Information the AI does **not** need |
|---|---|---|
| Example: directions provided in smaller steps | Present multi-step tasks in chunks of no more than `[N]` steps, pause for student confirmation, and restate when requested. | diagnosis, evaluation history, unrelated services |
|  |  |  |
|  |  |  |
|  |  |  |

### Better configuration pattern

Prefer:

> Break long instructions into short numbered steps. Ask the student to confirm the current step before introducing the next one.

Instead of:

> This student has `[DISABILITY]` and an IEP. Treat them differently because of their condition.

The first instruction describes the educational behavior the system should perform. The second unnecessarily exposes sensitive information and invites the model to improvise from a diagnostic label.

---

## 3. Define what the AI may and may not do

### The AI may

Check only what the district has approved:

- [ ] follow teacher-defined instructional strategies;
- [ ] change explanation format or pacing;
- [ ] provide examples or practice at an authorized level;
- [ ] use approved language-support strategies;
- [ ] provide accessible alternatives to generated content;
- [ ] support approved dictation, read-aloud, or alternative-input workflows;
- [ ] remind the student of an authorized strategy;
- [ ] surface a teacher-visible note that the configured support could not be delivered;
- [ ] other: `[DEFINE]`.

### The AI may not independently

- [ ] diagnose a disability or medical condition;
- [ ] decide that a student should be evaluated;
- [ ] determine IDEA or Section 504 eligibility;
- [ ] create, amend, interpret, or override an IEP or Section 504 plan;
- [ ] decide placement, services, goals, minutes, or accommodations;
- [ ] withdraw or reduce an accommodation based on perceived student performance;
- [ ] make disciplinary decisions or infer misconduct from disability-related behavior;
- [ ] make high-stakes judgments from speech recognition, writing style, response speed, chat behavior, or inferred affect;
- [ ] disclose the existence or contents of a student's plan to unauthorized users;
- [ ] present itself to a student or family as the authority on the student's legal rights or services.

Treat every item in this second list as a human-decision boundary, not merely a prompt preference.

---

## 4. Minimize student information

For each data element, ask whether the AI needs it to deliver the support.

| Data element | Needed? | Why? | Storage / retention location | Access roles |
|---|---:|---|---|---|
| Student name |  |  |  |  |
| Class / course |  |  |  |  |
| Authorized instructional strategy |  |  |  |  |
| Disability or diagnosis |  |  |  |  |
| IEP / 504 plan text |  |  |  |  |
| Evaluation results |  |  |  |  |
| Related-service information |  |  |  |  |
| Medical information |  |  |  |  |
| Teacher notes |  |  |  |  |
| Student AI conversations |  |  |  |  |

### Default rule

If the AI can deliver the support from an instructional instruction alone, do not provide a diagnosis, full plan, evaluation report, or medical information.

Cross-reference the [AI data lifecycle worksheet](ai-data-lifecycle-worksheet.md) and [school AI privacy review checklist](school-ai-privacy-review-checklist.md) before storing plan-derived information in a vendor system.

---

## 5. Test the actual student workflow

A configuration is not complete because the settings page saved successfully.

Test the student experience using realistic tasks.

### Access and usability

- [ ] Keyboard-only operation works through the complete AI interaction.
- [ ] Focus order and visible focus are usable.
- [ ] Screen-reader output identifies controls and generated content meaningfully.
- [ ] Zoom, text scaling, contrast, and district browser settings do not break the workflow.
- [ ] Dictation or speech recognition works well enough for the intended use, or an alternative exists.
- [ ] Generated equations, charts, diagrams, images, tables, audio, and video have usable alternatives where needed.
- [ ] The workflow works on the student's assigned device and network conditions.

### Instructional behavior

- [ ] The support appears when it should.
- [ ] The support does not appear in contexts where it would undermine the learning objective or assessment condition.
- [ ] The AI follows the teacher's boundary consistently across several prompt variations.
- [ ] The student can ask for clarification without losing the configured support.
- [ ] The AI does not reveal the reason the support exists unless disclosure is intentionally required.
- [ ] The AI does not overgeneralize one support into unrelated tasks.
- [ ] The AI does not turn a support into answer vending.

### Failure behavior

- [ ] Staff know what happens if the AI cannot deliver the support.
- [ ] A non-AI alternative is available when needed.
- [ ] The student is not penalized because the AI tool failed.
- [ ] Staff can report the failure quickly.
- [ ] The district can pause or disable the workflow without removing the student's underlying support obligation.

---

## 6. Separate accessibility testing from eligibility decisions

AI systems can produce signals that look deceptively diagnostic. A student may repeatedly request simpler language, use dictation, take longer to respond, misspell words, ask for repetition, switch languages, or struggle with generated visuals.

Those observations can be useful **instructional context**, but they are not an AI diagnosis or an automatic eligibility determination.

District rule:

> AI-generated observations, summaries, classifications, inferred traits, or behavioral patterns must not independently determine disability status, referral, eligibility, placement, services, accommodations, discipline, or other legally consequential student decisions.

If staff believe ordinary classroom evidence raises a concern that should enter a district's established referral or support process, they should use that human-owned process rather than asking the AI to make the determination.

---

## 7. Preserve teacher and case-manager control

Document who can change the configuration.

| Action | Authorized role(s) | Student/family notice needed? | Change logged? |
|---|---|---|---|
| Create support configuration |  |  |  |
| Edit support configuration |  |  |  |
| Disable AI delivery |  |  |  |
| Restore AI delivery |  |  |  |
| View plan-derived configuration |  |  |  |
| Review student AI activity |  |  |  |
| Export or delete data |  |  |  |

Recommended controls:

- [ ] Changes are attributable to a named staff account.
- [ ] Students cannot edit protected staff-authored support rules.
- [ ] AI-generated suggestions cannot silently rewrite the configuration.
- [ ] A teacher or case manager can review the plain-language instruction the AI receives.
- [ ] A human can override or disable the AI behavior immediately.
- [ ] The district retains a record of material configuration changes when that record is needed for accountability.

---

## 8. Check assessment conditions separately

An accommodation appropriate during instruction may not be permitted, or may operate differently, during a quiz, benchmark, state assessment, AP exam, certification test, or teacher-designed independent assessment.

Before AI use in an assessment:

- [ ] Identify the assessment owner and governing rules.
- [ ] Confirm whether generative AI is permitted at all.
- [ ] Confirm which accessibility tools remain authorized.
- [ ] Distinguish assistive functionality from content-generating functionality.
- [ ] Configure the tool so prohibited generative assistance cannot leak into the assessment workflow.
- [ ] Provide a non-AI method for delivering the authorized accommodation when required.

Never assume that because an accommodation is authorized, every AI feature is therefore authorized during every assessment.

---

## 9. Family and student communication

Explain the workflow in plain language when district policy or the student's circumstances call for it.

Suggested questions to answer:

- What support is the AI helping deliver?
- Who decided that support should be used?
- What information about the student is sent to the tool?
- Can the AI change the student's formal plan? **No.**
- Can a teacher review or change the AI configuration?
- What happens if the AI gets the support wrong?
- Is there a non-AI alternative?
- Who should the family contact with a question or correction?

Do not describe AI-enabled accommodations as a reason to reduce access to qualified educators, related services, assistive technology, or other supports required by the student's actual plan.

---

## 10. Review after real use

Review the configuration after `[NUMBER]` school days or `[NUMBER]` uses and whenever there is a material change.

Trigger review when:

- [ ] the IEP, Section 504 plan, or school-authorized support changes;
- [ ] the student changes class, teacher, grade, or school;
- [ ] the AI vendor changes a model, subprocessor, accessibility behavior, or relevant feature;
- [ ] staff observe that the support is inconsistently delivered;
- [ ] the student or family reports a barrier;
- [ ] generated content becomes inaccessible;
- [ ] the tool begins exposing information beyond the intended audience;
- [ ] the AI's behavior appears to influence a consequential decision;
- [ ] an incident or complaint identifies a new risk.

### Review record

| Date | Reviewer | Evidence reviewed | Change made | Follow-up date |
|---|---|---|---|---|
|  |  |  |  |  |

---

## 11. District sign-off

- [ ] The support originates from a valid school-authorized source.
- [ ] The AI configuration describes instructional behavior rather than unnecessary diagnostic information.
- [ ] The minimum necessary student information is used.
- [ ] Human-decision boundaries are documented.
- [ ] Accessibility was tested in the student's real workflow.
- [ ] A fallback exists if the AI cannot deliver the support.
- [ ] Assessment conditions were reviewed separately.
- [ ] Authorized staff can inspect, change, or disable the configuration.
- [ ] The district knows how to report and correct failures.
- [ ] The configuration has a review date and owner.

**Approved by:** `[NAME / ROLE]`  
**Date:** `[DATE]`  
**Next review:** `[DATE]`

---

## Official references for local review

District teams should verify current requirements with counsel and the relevant public agencies. Useful starting points include:

- U.S. Department of Education, Office for Civil Rights: [Section 504](https://www.ed.gov/laws-and-policy/individuals-disabilities/section-504)
- U.S. Department of Education, Office for Civil Rights: [Disability discrimination and FAPE](https://www.ed.gov/laws-and-policy/civil-rights-laws/disability-discrimination/disability-discrimination-key-issues/disability-discrimination-providing-free-appropriate-public-education-fape)
- U.S. Department of Education, Office for Civil Rights: *Avoiding the Discriminatory Use of Artificial Intelligence* (November 2024), available through the Department/ERIC
- U.S. Department of Education student privacy resources: [Privacy and data sharing](https://studentprivacy.ed.gov/privacy-and-data-sharing)

Federal guidance can change. This worksheet does not determine whether a district, vendor, configuration, or particular student plan complies with IDEA, Section 504, the ADA, FERPA, state law, or another requirement.

## HonorlyAI implementation boundary

HonorlyAI's public accessibility materials describe educators configuring school-authorized instructional strategies. HonorlyAI does not diagnose students, determine eligibility, replace an IEP or Section 504 plan, or independently make accommodation decisions. Districts should use the same boundary when evaluating any AI system used around disability-related supports.

---

This resource is a general educational starting point, **not legal advice**, a special-education determination, an accessibility certification, or a compliance certification. Local policy, student-specific plans, district procedures, contracts, privacy rules, assessment rules, and applicable law control.

Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Suggested attribution: *Adapted from the HonorlyAI K-12 AI Governance Toolkit.*