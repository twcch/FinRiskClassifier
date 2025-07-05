import os
import shutil
from pathlib import Path

import pandas as pd
import simfin as sf

SIMFIN_TOKEN = os.getenv('SIMFIN_KEY')
sf.set_api_key(SIMFIN_TOKEN)
data_dir = 'data/temp/'
sf.set_data_dir(data_dir)


def fetch_us_companies() -> pd.DataFrame:
    sf.load_companies()
    data = pd.read_csv(Path(data_dir) / 'us-companies.csv', sep=';')
    return data


def save_us_companies(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / 'us_companies.csv', index=False)


def fetch_us_income_statement() -> pd.DataFrame:
    sf.load_income(variant='quarterly')
    data = pd.read_csv(Path(data_dir) / 'us-income-quarterly.csv', sep=';')
    return data


def save_us_income_statement(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / 'us_income_statement.csv', index=False)


def fetch_us_balance_sheet() -> pd.DataFrame:
    sf.load_balance(variant='quarterly')
    data = pd.read_csv(Path(data_dir) / 'us-balance-quarterly.csv', sep=';')
    return data


def save_us_balance_sheet(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / 'us_balance_sheet.csv', index=False)


def fetch_us_share_prices() -> pd.DataFrame:
    sf.load_shareprices(variant='daily')
    data = pd.read_csv(Path(data_dir) / 'us-shareprices-daily.csv', sep=';')
    return data


def save_us_share_prices(path: Path, df: pd.DataFrame) -> pd.DataFrame:
    df.to_csv(path / 'us_share_prices.csv', index=False)


def delete_temp_dir() -> None:
    target_path = Path('data/temp')

    if target_path.exists() and target_path.is_dir():
        shutil.rmtree(target_path)
