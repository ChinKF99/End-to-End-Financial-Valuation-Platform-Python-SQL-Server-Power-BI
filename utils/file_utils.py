"""
==========================================================================================
file_utils.py

Utility functions for file management (Mainly for deleting old downloaded bronze files).
==========================================================================================
"""

from pathlib import Path
import shutil

from config.logging_config import setup_logger

logger = setup_logger(Path(__file__).stem)


def clean_download_folders(project_root: Path):
    """
    Remove all downloaded files from the Bronze folders.

    Keeps the folder structure.
    """

    bronze_root = project_root / "data" / "bronze"

    folders = [
        "company_profile",
        "income_statement",
        "balance_sheet",
        "cash_flow",
        "ratiosttm",
    ]

    for folder in folders:

        folder_path = bronze_root / folder

        if not folder_path.exists():
            continue

        for item in folder_path.iterdir():

            if item.is_file():

                item.unlink()

            elif item.is_dir():

                shutil.rmtree(item)

        logger.info(f"Cleaned {folder}")