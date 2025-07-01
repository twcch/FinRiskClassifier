import os
import pandas as pd
import simfin as sf
import shutil
from simfin.names import *
from pathlib import Path


SIMFIN_TOKEN = os.getenv("SIMFIN_KEY")
sf.set_api_key(SIMFIN_TOKEN)
sf.set_data_dir("data/temp/")


def fetch_us_companies() -> pd.DataFrame:
    return sf.load_companies()


def save_us_companies(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / "us_companies.csv", index=False)


def fetch_us_income_statement() -> pd.DataFrame:
    return sf.load_income(variant="quarterly")


def save_us_income_statement(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / "us_income_statement.csv", index=False)


def fetch_us_balance_sheet() -> pd.DataFrame:
    return sf.load_balance(variant="quarterly")


def save_us_balance_sheet(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / "us_balance_sheet.csv", index=False)


def fetch_us_share_prices() -> pd.DataFrame:
    return sf.load_shareprices(variant="daily")


def save_us_share_prices(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / "us_share_prices.csv", index=False)


def delete_temp_dir() -> None:
    target_path = Path("data/temp")

    if target_path.exists() and target_path.is_dir():
        shutil.rmtree(target_path)
