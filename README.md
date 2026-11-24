# audience-data-transparency-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>audience-data-transparency-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for audience-data transparency, audience taxonomy, content taxonomy, segment provenance, and recency disclosures.</p>
<p align="center">
<a href="https://pypi.org/project/audience-data-transparency-governance-pack/"><img alt="pypi: audience-data-transparency-governance-pack" src="https://img.shields.io/pypi/v/audience-data-transparency-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.1.1.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.1.1.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/audience-data-transparency-governance-pack/"><img alt="Monthly PyPI downloads: audience-data-transparency-governance-pack" src="https://img.shields.io/pypi/dm/audience-data-transparency-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/README.md"><img alt="README hits: audience-data-transparency-governance-pack" src="https://hits.sh/github.com/groupsum/audience-data-transparency-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/audience-data-transparency-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for audience-data transparency, audience taxonomy, content taxonomy, segment provenance, and recency disclosures.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern audience data transparency and taxonomy, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Audience Data Transparency And Taxonomy.

### Features

**Included ADRs**

- [`adr:audience-data-transparency-disclosure-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1001-audience-data-transparency-disclosure-policy.yaml) — Audience Data Transparency Disclosure Policy
- [`adr:audience-segment-provenance-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1002-audience-segment-provenance-policy.yaml) — Audience Segment Provenance Policy
- [`adr:audience-segment-recency-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1003-audience-segment-recency-policy.yaml) — Audience Segment Recency Policy
- [`adr:iab-audience-taxonomy-classification-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1004-iab-audience-taxonomy-classification-policy.yaml) — IAB Audience Taxonomy Classification Policy
- [`adr:iab-content-taxonomy-contextual-classification-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1005-iab-content-taxonomy-contextual-classification-policy.yaml) — IAB Content Taxonomy Contextual Classification Policy
- [`adr:audience-data-provider-and-permitted-use-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1006-audience-data-provider-and-permitted-use-policy.yaml) — Audience Data Provider And Permitted Use Policy
- [`adr:data-clean-room-audience-output-transparency-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1007-data-clean-room-audience-output-transparency-policy.yaml) — Data Clean Room Audience Output Transparency Policy
- [`adr:audience-transparency-audit-evidence-policy`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/adr/ADR-1008-audience-transparency-audit-evidence-policy.yaml) — Audience Transparency Audit Evidence Policy

**Included SPECs**

- [`spc:iab-data-transparency-disclosure-record-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2001-iab-data-transparency-disclosure-record-requirements.yaml) — IAB Data Transparency Disclosure Record Requirements
- [`spc:audience-segment-source-and-provider-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2002-audience-segment-source-and-provider-requirements.yaml) — Audience Segment Source And Provider Requirements
- [`spc:audience-segment-provenance-lineage-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2003-audience-segment-provenance-lineage-requirements.yaml) — Audience Segment Provenance Lineage Requirements
- [`spc:audience-segment-recency-and-expiration-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2004-audience-segment-recency-and-expiration-requirements.yaml) — Audience Segment Recency And Expiration Requirements
- [`spc:iab-audience-taxonomy-id-and-version-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2005-iab-audience-taxonomy-id-and-version-requirements.yaml) — IAB Audience Taxonomy ID And Version Requirements
- [`spc:iab-audience-taxonomy-mapping-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2006-iab-audience-taxonomy-mapping-requirements.yaml) — IAB Audience Taxonomy Mapping Requirements
- [`spc:iab-content-taxonomy-id-and-version-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2007-iab-content-taxonomy-id-and-version-requirements.yaml) — IAB Content Taxonomy ID And Version Requirements
- [`spc:iab-content-taxonomy-contextual-mapping-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2008-iab-content-taxonomy-contextual-mapping-requirements.yaml) — IAB Content Taxonomy Contextual Mapping Requirements
- [`spc:audience-permitted-use-and-restriction-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2009-audience-permitted-use-and-restriction-requirements.yaml) — Audience Permitted Use And Restriction Requirements
- [`spc:data-clean-room-input-output-transparency-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2010-data-clean-room-input-output-transparency-requirements.yaml) — Data Clean Room Input Output Transparency Requirements
- [`spc:audience-data-export-disclosure-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2011-audience-data-export-disclosure-requirements.yaml) — Audience Data Export Disclosure Requirements
- [`spc:audience-transparency-audit-evidence-requirements`](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates/specs/SPEC-2012-audience-transparency-audit-evidence-requirements.yaml) — Audience Transparency Audit Evidence Requirements

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add audience-data-transparency-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install audience-data-transparency-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add audience-data-transparency-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_audience_data_transparency import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:audience-data-transparency"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:audience-data-transparency` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_audience_data_transparency import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:iab-data-transparency-disclosure-record-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-iab-data-transparency-disclosure-record-requirements.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `audience-data-transparency-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_audience_data_transparency
uv run ssot pack preflight . ssot_pack_audience_data_transparency --all
uv run ssot pack sync . ssot_pack_audience_data_transparency --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_audience_data_transparency` in SSOT Registry. Review reservation owner `extension-pack:audience-data-transparency-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

The pack owns the Audience Data Transparency And Taxonomy ADRs and SPECs listed under Features.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_audience_data_transparency` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/audience-data-transparency-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/audience-data-transparency-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/src/ssot_pack_audience_data_transparency/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/audience-data-transparency-governance-pack)
- [Issues](https://github.com/groupsum/audience-data-transparency-governance-pack/issues)
- [Repository](https://github.com/groupsum/audience-data-transparency-governance-pack)
- [pypi: audience-data-transparency-governance-pack](https://pypi.org/project/audience-data-transparency-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/audience-data-transparency-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:audience-data-transparency`. The pack's reservation owner is `extension-pack:audience-data-transparency-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [IAB Tech Lab Data Transparency Standard](https://iabtechlab.com/standards/data-transparency-standard/)
- [IAB Tech Lab Audience Taxonomy](https://iabtechlab.com/standards/audience-taxonomy/)
- [IAB Tech Lab Content Taxonomy](https://iabtechlab.com/standards/content-taxonomy/)
- [IAB Data Clean Rooms Guidance](https://iabtechlab.com/datacleanrooms/)
- [IAB Tech Lab measurement and data transparency materials](https://iabtechlab.com/standards/)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/audience-data-transparency-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
