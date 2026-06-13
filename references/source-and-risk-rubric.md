# Source And Risk Rubric

## Source Tiers

| Tier | Typical sources | Use |
|---|---|---|
| A | Court or regulator records, official filings, full original recordings, verified first-party statements | Establish what the record or speaker directly says |
| B | Reputable newsrooms, established investigative outlets, recognized trade publications with named evidence | Corroborate and contextualize |
| C | Specialist databases, credible local reporting, transcripts, archived public pages | Support narrower claims or provide leads |
| D | Anonymous posts, fan pages, reposts, edited clips, forums, unsourced aggregators | Leads only; never establish a consequential claim |

Treat a source as independent only when it did not merely repeat another source.

## Claim Status

- `verified`: Directly established by strong primary evidence or multiple independent reliable sources.
- `credible-allegation`: A clearly attributed allegation supported by meaningful evidence but not adjudicated or conclusively established.
- `disputed`: Materially conflicting reliable accounts exist.
- `unverified`: Insufficient reliable support; do not repeat prominently.
- `cleared-or-corrected`: A claim was materially disproven, dismissed, retracted, or corrected.

## Confidence

- `high`: Definitive primary record or multiple independent Tier A/B sources.
- `medium`: One strong source plus meaningful corroboration, with no major unresolved contradiction.
- `low`: Limited, indirect, incomplete, or conflicting support.

Confidence describes evidence strength, not severity.

## Risk Categories

- `legal-regulatory`: Publicly documented litigation, enforcement, sanctions, or regulatory compliance issues.
- `professional-conduct`: Workplace, collaboration, attribution, plagiarism, or professional standards.
- `public-statements-values`: Relevant public statements or conduct, preserved in context.
- `commercial-consumer`: Advertising, sponsorship, product, investment, or consumer-protection issues.
- `reliability-consistency`: Material, repeated contradictions relevant to a decision.
- `information-integrity`: Fabricated credentials, manipulated evidence, coordinated misinformation, or material factual misrepresentation.
- `positive-evidence`: Documented corrective actions, consistent positive conduct, transparent disclosures, or credible exculpatory evidence.

## Evidence Ledger Schema

Save the ledger as a JSON array. Keep `claim` atomic and neutral.

```json
[
  {
    "id": "E001",
    "claim": "Neutral, checkable proposition",
    "claim_type": "fact",
    "status": "verified",
    "confidence": "high",
    "risk_category": "professional-conduct",
    "event_date": "2025-01-15",
    "source_title": "Source title",
    "source_url": "https://example.com/source",
    "source_publisher": "Publisher",
    "source_tier": "A",
    "published_date": "2025-01-16",
    "direct_support": "What this source directly establishes",
    "counterevidence": "Relevant denial, correction, outcome, or contrary evidence",
    "notes": "Optional context and limitations"
  }
]
```

Allowed `claim_type` values: `fact`, `allegation`, `opinion`, `inference`.

For an allegation, identify who made it and do not use `verified` merely because the allegation was published. A source can verify that an allegation was made without verifying its substance.

## Decision Rules

1. Do not elevate Tier D material beyond `unverified`.
2. Do not mark an allegation `verified` without evidence that establishes its substance.
3. Look for the latest procedural outcome of lawsuits and investigations.
4. Include corrections, apologies, remediation, dismissals, and exculpatory evidence.
5. Separate "not found" from "did not happen."
6. Use exact dates and jurisdictions when they matter.
