"""Helper library for logging the LLMs answers."""
# pylint: disable=inconsistent-quotes
import os
import json

def log_extraction(
        extraction_list: list[dict],
        output_name: str,
        log_path: str,
) -> None:
    """
    Logs the structured extraction output from the LLM.

    Parameters:
        extraction: list[dict] - The list of structured extraction outputs
        output_name: str - The name of the output file
        log_path: str - The path to the directory where logs should be saved

    Returns:
        None
    """
    # make json dict out of the extraction list
    extraction_json = {}

    for idx, extraction in enumerate(extraction_list):
        extraction_json[idx] = {
            "url": extraction.url,
            "pii_information_present": extraction.pii_information_present,
            "information": extraction.information,
        }

    if not os.path.isdir(log_path):
        os.mkdir(log_path)

    file_name = os.path.join(log_path, output_name)

    with open(file=file_name, mode="w", encoding="utf-8") as f:
        json.dump(extraction_json, f, indent=4)
