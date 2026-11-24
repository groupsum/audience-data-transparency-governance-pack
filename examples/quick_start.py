"""Inspect the installed pack identity."""

from ssot_pack_audience_data_transparency import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:audience-data-transparency"
print(metadata["origin"]["id"])
