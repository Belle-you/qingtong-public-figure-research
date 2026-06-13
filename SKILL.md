---
name: qingtong-public-figure-research
description: Research a public figure using lawful, publicly available, verifiable sources and produce a neutral, cited due-diligence report with a timeline, evidence ledger, source-confidence ratings, contradiction checks, and clearly bounded risk signals. Use when a user asks to investigate, background-check, fact-check, compare, or monitor a celebrity, influencer, executive, creator, politician, or other public figure before following, hiring, partnering, sponsoring, or endorsing them.
---

# Qingtong Public Figure Research

Build an evidence-first public-figure report that helps the user make their own decision. Treat every negative claim as unverified until supported by reliable sources.

## Non-Negotiable Boundaries

- Research only public figures and matters relevant to their public role.
- Do not investigate minors, private individuals, home addresses, family members, private relationships, leaked data, or other non-public personal information.
- Do not infer protected traits, medical conditions, sexuality, guilt, intent, or personality disorders.
- Do not present allegations, rumors, social-media posts, or AI analysis as established fact.
- Do not use a numerical "values match probability." Explain observed evidence and let the user decide.
- Do not recommend harassment, contact campaigns, doxxing, or punitive action.
- Prefer omission over repeating a sensational claim that lacks public-interest relevance.

If the request crosses these boundaries, narrow it to lawful public-interest research and explain the limitation briefly.

## Workflow

### 1. Define the Decision

Identify:

- The exact person and disambiguating details.
- The user's decision context: follow, hire, collaborate, sponsor, compare, or monitor.
- Relevant time range, jurisdictions, and risk categories.
- The user's explicit deal-breakers, if any.

Ask only for details that materially change the research. Otherwise, proceed with clearly stated assumptions.

### 2. Plan Sources Before Searching

Read [references/source-and-risk-rubric.md](references/source-and-risk-rubric.md).

Build a source plan that prioritizes:

1. Primary records and the person's own full-context statements.
2. Reputable reporting with named evidence.
3. Specialist databases and established trade publications.
4. Other public sources used only as leads.

Browse the web for current information. Record publication date, event date, URL, source tier, and what the source directly supports.

### 3. Build an Evidence Ledger

Store important findings as JSON using the schema in the rubric. Keep claims atomic: one record should support one checkable proposition.

For each claim:

- Separate fact, allegation, opinion, and inference.
- Preserve the original context and date.
- Search for corrections, denials, court outcomes, retractions, and later developments.
- Seek at least two independent reliable sources for consequential negative claims unless a definitive primary record exists.
- Mark unresolved conflicts instead of choosing the more dramatic version.

Run:

```bash
python scripts/validate_evidence.py evidence.json
```

Fix all errors before drafting the report.

### 4. Assess Risk Without Declaring Guilt

Classify only evidence relevant to the user's decision. Use the rubric's categories:

- Legal and regulatory
- Professional conduct
- Public statements and values
- Commercial and consumer
- Reliability and consistency
- Information integrity

Assign each signal a confidence level and status. Describe severity separately from confidence. A severe allegation with weak evidence remains low confidence.

Use careful language:

- Prefer: "A lawsuit filed on DATE alleges X; no judgment was found."
- Avoid: "The person committed X."

### 5. Draft the Report

Read [references/report-template.md](references/report-template.md) and follow its structure.

The report must:

- Lead with scope, identity, date, and limitations.
- Give a concise decision-oriented summary.
- Present a dated timeline.
- Distinguish verified facts, credible allegations, disputed claims, and unresolved gaps.
- Cite every material claim with direct links.
- Include positive and exculpatory evidence when found.
- State what was searched but not found.
- End with questions or verification steps, not a verdict about the person's worth.

### 6. Final Quality Gate

Before delivering, verify:

- Every material claim has a citation.
- Every consequential negative claim has sufficient support and precise status language.
- Sources are independent where claimed.
- Event dates are not confused with publication dates.
- No private-person or minor information slipped into the report.
- The summary matches the evidence ledger.
- Limitations and unresolved conflicts are visible.

When evidence is too thin, say so plainly and produce a limited findings report.

## Common Requests

- "调查这位博主是否适合品牌合作。"
- "帮我核验某位公众人物最近争议的事实依据。"
- "比较两位创作者的公开商业与职业风险。"
- "根据我的底线，整理这个人的公开记录，但不要替我下结论。"

## Resources

- `references/source-and-risk-rubric.md`: source hierarchy, confidence rules, risk taxonomy, and evidence schema.
- `references/report-template.md`: required structure and wording patterns for final reports.
- `scripts/validate_evidence.py`: dependency-free validator for the evidence ledger.
