import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pathlib import Path
from core.data import *


RAW_DATA_PATH = Path("data/raw/")


def main():
    companies_df = fetch_us_companies()
    save_us_companies(RAW_DATA_PATH, companies_df)

    income_statement_df = fetch_us_income_statement()
    save_us_income_statement(RAW_DATA_PATH, income_statement_df)

    balance_sheet_df = fetch_us_balance_sheet()
    save_us_balance_sheet(RAW_DATA_PATH, balance_sheet_df)

    share_prices_df = fetch_us_share_prices()
    save_us_share_prices(RAW_DATA_PATH, share_prices_df)

    delete_temp_dir()

if __name__ == "__main__":
    main()
