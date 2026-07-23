# Zenodo publication guide

This document contains the approved metadata and release checklist for publishing version 1.0.0 of the **HonorlyAI K-12 AI Governance Toolkit** on Zenodo.

## Recommended deposit method

Use a **manual Zenodo upload** for version 1.0.0 rather than Zenodo's automatic GitHub-release integration.

The repository is hosted on GitHub, but its primary content is an educational governance toolkit, not software. A manual upload allows the Zenodo record to use the most accurate resource type instead of being automatically treated as a software release.

## Files to upload

Create a GitHub release tagged `v1.0.0`, then download the release source archive as a ZIP file.

Upload one file to Zenodo:

- `honorlyai-k12-ai-governance-toolkit-v1.0.0.zip`

The ZIP should contain the complete repository at the `v1.0.0` release, including the README, license, citation file, implementation guide, governance documents, and all templates.

## Zenodo metadata

### DOI

- **Does this upload already have a DOI?** No
- Let Zenodo assign a DOI when the record is published.
- Reserve the DOI in advance only if it needs to appear inside a generated PDF before publication.

### Resource type

Choose the closest available option in this order:

1. **Other: Educational resource**
2. **Publication: Technical note**
3. **Publication: Report**
4. **Other**

Do not classify this release as software or a dataset.

### Title

**HonorlyAI K-12 AI Governance Toolkit**

### Publication date

**2026-07-23**

### Creators

Add the creators in this order:

1. **Kevin Rand**
2. **Trevor Rosato**

Use verified ORCID identifiers if available. Do not invent identifiers or affiliations.

### Publisher

**HonorlyAI LLC**

### Version

**1.0.0**

### Language

**English**

### License

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

### Description / abstract

The HonorlyAI K-12 AI Governance Toolkit is a collection of free, editable resources designed to help school districts, educators, technology leaders, families, and students evaluate and implement artificial intelligence responsibly.

The toolkit includes practical templates and checklists covering AI vendor evaluation, student acceptable-use policies, classroom AI-use levels, parent and family communication, district pilot planning, student privacy review, teacher classroom guidelines, academic integrity, incident response, and AI data lifecycle management.

The materials are designed to support local decision-making while preserving teacher oversight, student privacy, academic integrity, accessibility, and district control. They are general educational resources and are not legal advice, a compliance certification, or a substitute for district-specific legal, privacy, curriculum, accessibility, and community review.

All original materials are licensed under the Creative Commons Attribution 4.0 International License and may be copied, adapted, and redistributed with appropriate attribution.

### Keywords

Add each keyword separately:

- K-12 AI governance
- artificial intelligence in education
- school district AI policy
- classroom AI
- teacher-controlled AI
- responsible AI
- education technology
- student privacy
- academic integrity
- AI vendor evaluation
- school district procurement
- AI acceptable-use policy
- family communication
- AI pilot planning

### Contributors

Add **HonorlyAI LLC** as an organizational contributor or rights holder if Zenodo provides an appropriate role. Do not add the company as a creator if Kevin Rand and Trevor Rosato remain the named creators.

### Related works and identifiers

Add these related identifiers:

1. `https://github.com/trevor050/honorlyai-resources`
   - Relation: **Is identical to** or **Is version of**
   - Resource type: Other

2. `https://honorlyai.com/resources`
   - Relation: **Is documented by** or **Is supplemented by**
   - Resource type: Other

3. `https://honorlyai.com/blog/teacher-controlled-ai-for-k12`
   - Relation: **Is supplemented by**
   - Resource type: Publication or Other

### References

- HonorlyAI. K-12 AI resources. https://honorlyai.com/resources
- HonorlyAI. The future of K-12 AI is teacher-controlled. https://honorlyai.com/blog/teacher-controlled-ai-for-k12
- HonorlyAI K-12 AI Governance Toolkit source repository. https://github.com/trevor050/honorlyai-resources

### Visibility and access

- Metadata visibility: Public
- File visibility: Public
- Embargo: None
- Access right: Open

## Pre-publication checklist

Before creating the GitHub release and Zenodo record:

- [ ] Confirm all bracketed placeholders are intentional examples or are clearly identified.
- [ ] Confirm no private district, student, client, employee, or pilot information is present.
- [ ] Confirm all links work.
- [ ] Confirm every file is covered by the repository license or clearly identifies a different license.
- [ ] Confirm legal and compliance language does not claim certification or guaranteed compliance.
- [ ] Confirm `CITATION.cff` validates.
- [ ] Confirm the release date and version match across `CITATION.cff`, GitHub, and Zenodo.
- [ ] Create the GitHub tag and release `v1.0.0`.
- [ ] Download and rename the source ZIP to `honorlyai-k12-ai-governance-toolkit-v1.0.0.zip`.
- [ ] Preview the Zenodo record before publishing.

## After publication

Once Zenodo assigns the DOI:

1. Add the version DOI to `CITATION.cff` using a `doi` field.
2. Add the DOI badge and citation block to `README.md`.
3. Add the DOI to the HonorlyAI resources page.
4. Add the Zenodo record URL to the GitHub repository description or README.
5. Create a small follow-up pull request containing those DOI updates.

Suggested citation format after publication:

> Rand, K., & Rosato, T. (2026). *HonorlyAI K-12 AI Governance Toolkit* (Version 1.0.0). HonorlyAI LLC. Zenodo. https://doi.org/[DOI]

## Future versions

Use semantic versioning:

- Patch releases, such as `1.0.1`, for minor corrections.
- Minor releases, such as `1.1.0`, for new resources or substantial additions.
- Major releases, such as `2.0.0`, for major structural or policy-framework changes.

Create a new Zenodo version for meaningful file changes rather than replacing the original archived release.