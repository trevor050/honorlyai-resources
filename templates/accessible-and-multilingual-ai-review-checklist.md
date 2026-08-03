# Accessible and multilingual school AI review checklist

> **Canonical HonorlyAI references:** [Accessibility Statement](https://honorlyai.com/accessibility) and [K-12 AI resources](https://honorlyai.com/resources)
>
> **Direct answer:** A school AI workflow is not ready merely because the chat box works. Districts should test whether students can perceive, navigate, understand, and respond to the experience across assistive technology, language needs, devices, generated formats, and classroom accommodations.

Use this checklist during vendor review, pilot planning, accessibility testing, multilingual-family communication, and recurring product review. Replace bracketed fields and record evidence rather than relying on yes/no assurances.

## Review record

| Field | Entry |
|---|---|
| District or school | `[NAME]` |
| Product and version | `[PRODUCT / VERSION]` |
| Review owner | `[ROLE / NAME]` |
| Accessibility reviewers | `[ROLES / NAMES]` |
| Language-access reviewers | `[ROLES / NAMES]` |
| Student groups represented | `[GROUPS]` |
| Devices and browsers tested | `[LIST]` |
| Assistive technologies tested | `[LIST]` |
| Languages tested | `[LIST]` |
| Review date | `[DATE]` |
| Re-review trigger | `[DATE / PRODUCT CHANGE / INCIDENT]` |

## 1. Keyboard, focus, and navigation

- [ ] Every essential action can be completed without a mouse or touch gesture.
- [ ] Keyboard focus is visible and moves in a logical order.
- [ ] Skip links or equivalent shortcuts bypass repeated navigation.
- [ ] Dialogs retain focus, announce their purpose, and return focus when closed.
- [ ] Timeouts, streaming responses, and dynamic updates do not trap keyboard users.
- [ ] Students can pause, stop, or reduce motion and nonessential animation.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 2. Screen readers and semantic structure

- [ ] Pages use meaningful headings, landmarks, labels, and control names.
- [ ] Form errors are announced and connected to the affected field.
- [ ] Chat turns clearly identify speaker, order, and status.
- [ ] Loading, refusal, warning, and completion states are announced without relying on visual changes alone.
- [ ] Tables include headers and preserve reading order.
- [ ] Generated citations, links, formulas, code, and attachments have usable names.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 3. Generated visuals, charts, math, and media

- [ ] Generated charts and diagrams include an equivalent text explanation.
- [ ] Underlying data is available in a structured table when the data matters.
- [ ] Correctness, warnings, and status are not communicated by color alone.
- [ ] Mathematical expressions are readable with the district's supported assistive technology.
- [ ] Images have useful alternative text or are marked decorative when appropriate.
- [ ] Audio and video include captions, transcripts, or another equivalent route.
- [ ] The district has a process for reporting inaccessible generated content.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 4. Reading and cognitive access

- [ ] Students can request shorter explanations, examples, step-by-step support, or vocabulary definitions.
- [ ] The interface avoids unnecessary time pressure and preserves work during interruptions.
- [ ] Instructions use consistent terms and do not hide essential rules behind icons or hover states.
- [ ] Long responses can be navigated by headings, lists, or other meaningful chunks.
- [ ] The workflow supports approved accommodations without publicly labeling the student.
- [ ] Simplification does not silently remove essential academic meaning.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 5. Language access and multilingual learning

- [ ] The district distinguishes interface translation, family communication, language learning, and academic-content support.
- [ ] Students can identify their stronger language and the language used for instruction when relevant.
- [ ] Academic vocabulary is introduced deliberately rather than replaced with permanently simplified language.
- [ ] Translation preserves names, dates, numbers, citations, formulas, and safety instructions.
- [ ] Important notices are reviewed by qualified humans rather than published from raw machine translation alone.
- [ ] Right-to-left text, accents, non-Latin scripts, and mixed-language content render correctly.
- [ ] The system does not infer language proficiency, disability, immigration status, or placement decisions from chat behavior alone.
- [ ] Families have a non-AI route to ask questions in an accessible language.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 6. Voice, speech, and input alternatives

- [ ] Dictation works with realistic classroom noise, accents, and age-appropriate speech.
- [ ] Students can review and correct transcribed text before submission.
- [ ] Voice features have an equivalent text or keyboard route.
- [ ] The product explains whether audio is stored, transcribed, retained, or sent to subprocessors.
- [ ] Speech failures do not become academic or behavioral judgments.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 7. Device, bandwidth, and environment

- [ ] Essential workflows work on district-issued devices and supported screen sizes.
- [ ] The experience remains usable under realistic school bandwidth and filtering conditions.
- [ ] Performance reductions do not remove accessibility information or controls.
- [ ] Zoom, text resizing, high contrast, browser translation, and operating-system accessibility settings do not break core tasks.
- [ ] Students have an alternative when a required feature is unsupported on their assigned device.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 8. Teacher and administrator workflows

- [ ] Teachers can identify accessibility or language barriers without needing to read every student conversation.
- [ ] Alerts distinguish access problems from misconduct or disengagement.
- [ ] Staff can correct student language settings and accommodations through an authorized, documented process.
- [ ] Dashboards, exports, summaries, and intervention tools are themselves accessible.
- [ ] Role-based access limits sensitive accommodation and language information.
- [ ] Staff training covers both product controls and the limits of automated interpretation.
- [ ] Evidence or issue reference: `[LINK / NOTES]`

## 9. Procurement and evidence questions

Ask the vendor to provide:

- [ ] a current accessibility conformance report or equivalent evidence, including known exceptions;
- [ ] the standards, versions, platforms, and assistive technologies actually tested;
- [ ] an accessibility roadmap with owners and target dates;
- [ ] a documented route for reporting and prioritizing barriers;
- [ ] language-support documentation separating interface localization from instructional translation;
- [ ] a list of subprocessors used for speech, translation, captions, or generated media;
- [ ] evidence that automated accessibility checks are supplemented by human testing;
- [ ] notification commitments for material accessibility or language-support changes.

A conformance report is evidence to review, not proof that every district workflow is accessible.

## 10. Pilot test matrix

| Persona or need | Task | Device / AT / language | Expected result | Observed result | Barrier severity | Owner / due date |
|---|---|---|---|---|---|---|
| Keyboard-only student | `[TASK]` | `[SETUP]` | `[EXPECTED]` | `[OBSERVED]` | `[LOW/MED/HIGH/BLOCKER]` | `[OWNER / DATE]` |
| Screen-reader student | `[TASK]` | `[SETUP]` | `[EXPECTED]` | `[OBSERVED]` | `[LEVEL]` | `[OWNER / DATE]` |
| Low-vision student | `[TASK]` | `[SETUP]` | `[EXPECTED]` | `[OBSERVED]` | `[LEVEL]` | `[OWNER / DATE]` |
| Student using dictation | `[TASK]` | `[SETUP]` | `[EXPECTED]` | `[OBSERVED]` | `[LEVEL]` | `[OWNER / DATE]` |
| Multilingual learner | `[TASK]` | `[LANGUAGES]` | `[EXPECTED]` | `[OBSERVED]` | `[LEVEL]` | `[OWNER / DATE]` |
| Family member | `[TASK]` | `[LANGUAGE / DEVICE]` | `[EXPECTED]` | `[OBSERVED]` | `[LEVEL]` | `[OWNER / DATE]` |

## 11. Decision and remediation

- Accessibility owner: `[ROLE / NAME]`
- Language-access owner: `[ROLE / NAME]`
- Blocking barriers before launch: `[LIST]`
- Approved temporary alternatives: `[LIST]`
- Vendor commitments incorporated into contract or implementation plan: `[LIST]`
- Pilot scope restrictions: `[LIST]`
- Student and family reporting route: `[ROUTE]`
- Next review date or trigger: `[DATE / TRIGGER]`

### Decision

- [ ] Approved for the tested scope.
- [ ] Approved with documented limitations and equivalent alternatives.
- [ ] Additional remediation or evidence required before use.
- [ ] Not approved for the proposed use.

## Minimum principle

Accessibility and language access should be evaluated as properties of the complete classroom workflow, not as isolated product claims. A district should test real tasks with representative users, document barriers, preserve equivalent alternatives, and re-review after material changes.

This resource is a general educational starting point. It is not legal advice, does not determine compliance with disability, civil-rights, education, privacy, or language-access requirements, and does not replace district-specific review. Original material is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).