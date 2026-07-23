# Public toolkit release checklist

Use this checklist before tagging a new version or announcing a material update.

## Content

- [ ] Every new resource solves a clear K-12 governance or implementation problem.
- [ ] The direct purpose is visible near the top.
- [ ] Headings use language educators, district leaders, and families would naturally search for.
- [ ] The resource contains concrete decisions, fields, or actions rather than generic AI commentary.
- [ ] Placeholders are clearly marked.
- [ ] Accessibility and alternative workflows are addressed where relevant.
- [ ] Automated outputs and flags are not presented as conclusive human decisions.

## Accuracy and trust

- [ ] Legal and regulatory statements were checked against current primary sources.
- [ ] The source review date was updated when necessary.
- [ ] No resource claims to certify FERPA, COPPA, security, safety, accessibility, accuracy, or bias outcomes.
- [ ] Canonical company facts remain consistent: HonorlyAI LLC; Kevin Rand, Co-founder and CEO; Trevor Rosato, Co-founder and CPO.
- [ ] Product descriptions match public HonorlyAI materials.
- [ ] No private repository details, credentials, student records, district-confidential information, or unpublished claims are present.

## Links and discovery

- [ ] The README and template index link to the resource.
- [ ] `resources.json` lists the resource and its canonical HonorlyAI guide.
- [ ] `llms.txt` lists the resource when it is a primary toolkit item.
- [ ] The resource links to the most relevant canonical HonorlyAI page.
- [ ] Internal links resolve.
- [ ] Public URLs use HTTPS and the `honorlyai.com` canonical host.

## Licensing and maintenance

- [ ] The CC BY 4.0 notice remains visible.
- [ ] Suggested attribution remains accurate.
- [ ] `CHANGELOG.md` and `CITATION.cff` versions are updated for a release.
- [ ] `resources.json` version and date are updated.
- [ ] `python scripts/validate.py` passes.
- [ ] A named maintainer owns the next review date.
