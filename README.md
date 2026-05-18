<div align="center">

# audience-data-transparency-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/audience-data-transparency-governance-pack.svg)](https://pypi.org/project/audience-data-transparency-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/audience-data-transparency-governance-pack.svg)](https://pypi.org/project/audience-data-transparency-governance-pack/)
[![License](https://img.shields.io/pypi/l/audience-data-transparency-governance-pack.svg)](https://pypi.org/project/audience-data-transparency-governance-pack/)
[![Publish](https://github.com/groupsum/audience-data-transparency-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/audience-data-transparency-governance-pack/actions/workflows/publish.yml)

</div>

Installable SSOT governance pack for audience-data transparency, audience taxonomy, content taxonomy, segment provenance, and recency disclosures.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `audience-data-transparency-governance-pack` is an installable SSOT governance pack for Audience Data Transparency And Taxonomy. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern audience data transparency and taxonomy, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`audience-data-transparency-governance-pack`](https://pypi.org/project/audience-data-transparency-governance-pack/)
- GitHub package repository: [`groupsum/audience-data-transparency-governance-pack`](https://github.com/groupsum/audience-data-transparency-governance-pack)
- Import package: `ssot_pack_audience_data_transparency`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:audience-data-transparency`
- PyPI package: `audience-data-transparency-governance-pack`
- Import package: `ssot_pack_audience_data_transparency`
- GitHub repository: [groupsum/audience-data-transparency-governance-pack](https://github.com/groupsum/audience-data-transparency-governance-pack)
- Reservation owner: `extension-pack:audience-data-transparency-governance-pack`

## Domain Focus

Audience Data Transparency And Taxonomy

## Authority Sources

- [IAB Tech Lab Data Transparency Standard](https://iabtechlab.com/standards/data-transparency-standard/)
- [IAB Tech Lab Audience Taxonomy](https://iabtechlab.com/standards/audience-taxonomy/)
- [IAB Tech Lab Content Taxonomy](https://iabtechlab.com/standards/content-taxonomy/)
- [IAB Data Clean Rooms Guidance](https://iabtechlab.com/datacleanrooms/)
- [IAB Tech Lab measurement and data transparency materials](https://iabtechlab.com/standards/)

## Included ADRs

- [`adr:audience-data-transparency-disclosure-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1001-audience-data-transparency-disclosure-policy.yaml) - Audience Data Transparency Disclosure Policy
- [`adr:audience-segment-provenance-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1002-audience-segment-provenance-policy.yaml) - Audience Segment Provenance Policy
- [`adr:audience-segment-recency-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1003-audience-segment-recency-policy.yaml) - Audience Segment Recency Policy
- [`adr:iab-audience-taxonomy-classification-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1004-iab-audience-taxonomy-classification-policy.yaml) - IAB Audience Taxonomy Classification Policy
- [`adr:iab-content-taxonomy-contextual-classification-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1005-iab-content-taxonomy-contextual-classification-policy.yaml) - IAB Content Taxonomy Contextual Classification Policy
- [`adr:audience-data-provider-and-permitted-use-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1006-audience-data-provider-and-permitted-use-policy.yaml) - Audience Data Provider And Permitted Use Policy
- [`adr:data-clean-room-audience-output-transparency-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1007-data-clean-room-audience-output-transparency-policy.yaml) - Data Clean Room Audience Output Transparency Policy
- [`adr:audience-transparency-audit-evidence-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1008-audience-transparency-audit-evidence-policy.yaml) - Audience Transparency Audit Evidence Policy

## Included SPECs

- [`spc:iab-data-transparency-disclosure-record-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2001-iab-data-transparency-disclosure-record-requirements.yaml) - IAB Data Transparency Disclosure Record Requirements
- [`spc:audience-segment-source-and-provider-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2002-audience-segment-source-and-provider-requirements.yaml) - Audience Segment Source And Provider Requirements
- [`spc:audience-segment-provenance-lineage-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2003-audience-segment-provenance-lineage-requirements.yaml) - Audience Segment Provenance Lineage Requirements
- [`spc:audience-segment-recency-and-expiration-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2004-audience-segment-recency-and-expiration-requirements.yaml) - Audience Segment Recency And Expiration Requirements
- [`spc:iab-audience-taxonomy-id-and-version-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2005-iab-audience-taxonomy-id-and-version-requirements.yaml) - IAB Audience Taxonomy ID And Version Requirements
- [`spc:iab-audience-taxonomy-mapping-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2006-iab-audience-taxonomy-mapping-requirements.yaml) - IAB Audience Taxonomy Mapping Requirements
- [`spc:iab-content-taxonomy-id-and-version-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2007-iab-content-taxonomy-id-and-version-requirements.yaml) - IAB Content Taxonomy ID And Version Requirements
- [`spc:iab-content-taxonomy-contextual-mapping-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2008-iab-content-taxonomy-contextual-mapping-requirements.yaml) - IAB Content Taxonomy Contextual Mapping Requirements
- [`spc:audience-permitted-use-and-restriction-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2009-audience-permitted-use-and-restriction-requirements.yaml) - Audience Permitted Use And Restriction Requirements
- [`spc:data-clean-room-input-output-transparency-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2010-data-clean-room-input-output-transparency-requirements.yaml) - Data Clean Room Input Output Transparency Requirements
- [`spc:audience-data-export-disclosure-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2011-audience-data-export-disclosure-requirements.yaml) - Audience Data Export Disclosure Requirements
- [`spc:audience-transparency-audit-evidence-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2012-audience-transparency-audit-evidence-requirements.yaml) - Audience Transparency Audit Evidence Requirements

## Install With uv

```bash
uv add audience-data-transparency-governance-pack
uv add ssot-registry audience-data-transparency-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install audience-data-transparency-governance-pack
uvx --from ssot-registry ssot pack sync . audience-data-transparency-governance-pack
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

- GitHub package repository: [groupsum/audience-data-transparency-governance-pack](https://github.com/groupsum/audience-data-transparency-governance-pack)
- PyPI package: [audience-data-transparency-governance-pack](https://pypi.org/project/audience-data-transparency-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
