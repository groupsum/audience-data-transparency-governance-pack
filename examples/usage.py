"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_audience_data_transparency import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:iab-data-transparency-disclosure-record-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-iab-data-transparency-disclosure-record-requirements.yaml"
