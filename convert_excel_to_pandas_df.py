import time
import pandas as pd
import python_calamine
from typing import IO, Iterator


def iter_excel_calamine(file: IO[bytes]) -> Iterator[dict[str, object]]:
    workbook = python_calamine.CalamineWorkbook.from_filelike(file)  # type: ignore[arg-type]
    rows = iter(workbook.get_sheet_by_index(0).to_python())
    headers = list(map(str, next(rows)))
    for row in rows:
        yield dict(zip(headers, row))


def excel_calamine_to_dataframe(file: IO[bytes]) -> pd.DataFrame:
    data = list(iter_excel_calamine(file))
    return pd.DataFrame(data)


def fetch_excel_df(source_file_path):
    try:
        start_time = time.time()
        with open(source_file_path, "rb") as file:
            df = excel_calamine_to_dataframe(file)
            end_time = time.time()
            print("Time taken to fetch the excel file is {} seconds".format(end_time - start_time))
            return df
    except Exception as e:
        print(e)
        return None
