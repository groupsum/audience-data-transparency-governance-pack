# ssot-pack-audience-data-transparency

Installable SSOT governance pack for audience-data transparency, audience taxonomy, content taxonomy, segment provenance, and recency disclosures.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:audience-data-transparency`
- Priority: `P3.3`
- PyPI package: `ssot-pack-audience-data-transparency`
- Import package: `ssot_pack_audience_data_transparency`
- GitHub repository: `groupsum/audience-data-transparency-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-audience-data-transparency`

## Domain Focus

Audience Data Transparency And Taxonomy

## Authority Sources

- IAB Tech Lab Data Transparency Standard
- IAB Tech Lab Audience Taxonomy
- IAB Tech Lab Content Taxonomy
- IAB Data Clean Rooms Guidance
- IAB Tech Lab measurement and data transparency materials

## Included ADRs

- `adr:audience-data-transparency-disclosure-policy` - Audience Data Transparency Disclosure Policy
- `adr:audience-segment-provenance-policy` - Audience Segment Provenance Policy
- `adr:audience-segment-recency-policy` - Audience Segment Recency Policy
- `adr:iab-audience-taxonomy-classification-policy` - IAB Audience Taxonomy Classification Policy
- `adr:iab-content-taxonomy-contextual-classification-policy` - IAB Content Taxonomy Contextual Classification Policy
- `adr:audience-data-provider-and-permitted-use-policy` - Audience Data Provider And Permitted Use Policy
- `adr:data-clean-room-audience-output-transparency-policy` - Data Clean Room Audience Output Transparency Policy
- `adr:audience-transparency-audit-evidence-policy` - Audience Transparency Audit Evidence Policy

## Included SPECs

- `spc:iab-data-transparency-contract` - IAB Data Transparency Contract
- `spc:iab-audience-taxonomy-contract` - IAB Audience Taxonomy Contract
- `spc:iab-content-taxonomy-contract` - IAB Content Taxonomy Contract
- `spc:segment-provenance-recency-contract` - Segment Provenance Recency Contract

## Install With uv

```bash
uv add ssot-pack-audience-data-transparency
uv add ssot-registry ssot-pack-audience-data-transparency
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-audience-data-transparency
uvx --from ssot-registry ssot pack sync . ssot-pack-audience-data-transparency
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_audience_data_transparency import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/audience-data-transparency-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-audience-data-transparency/
- SSOT Registry: https://pypi.org/project/ssot-registry/
