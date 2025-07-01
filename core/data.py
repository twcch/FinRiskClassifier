import os
import pandas as pd
import simfin as sf
import shutil
from simfin.names import *
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/")

SIMFIN_TOKEN = os.getenv("SIMFIN_KEY")
sf.set_api_key(SIMFIN_TOKEN)
sf.set_data_dir("data/temp/")


def fetch_us_companies() -> pd.DataFrame:
    return sf.load_companies()


def save_us_companies(df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(RAW_DATA_PATH / "us_companies.csv", index=False)


def fetch_us_income_statement() -> pd.DataFrame:
    return sf.load_income(variant="quarterly")


def save_us_income_statement(df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(RAW_DATA_PATH / "us_income_statement.csv", index=False)


def fetch_us_balance_sheet() -> pd.DataFrame:
    return sf.load_balance(variant="quarterly")


def save_us_balance_sheet(df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(RAW_DATA_PATH / "us_balance_sheet.csv", index=False)


def fetch_us_share_prices() -> pd.DataFrame:
    return sf.load_shareprices(variant="daily")


def save_us_share_prices(df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(RAW_DATA_PATH / "us_share_prices.csv", index=False)


def remove_path_and_contents() -> None:
    target_path = Path("data/temp")

    if target_path.exists() and target_path.is_dir():
        shutil.rmtree(target_path)


def main():
    companies_df = fetch_us_companies()
    save_us_companies(companies_df)

    income_statement_df = fetch_us_income_statement()
    save_us_income_statement(income_statement_df)

    balance_sheet_df = fetch_us_balance_sheet()
    save_us_balance_sheet(balance_sheet_df)

    share_prices_df = fetch_us_share_prices()
    save_us_share_prices(share_prices_df)
    
    remove_path_and_contents()


if __name__ == "__main__":
    main()
