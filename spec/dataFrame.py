import pandas as pd
from pathlib import Path

## https://www.heywhale.com/mw/project/5ba9a2801e126e003c86c332

excel_dir = Path('/Users/zqy/codes/python/tmp')

excel_files = excel_dir.glob('*.xlsx')

df = pd.DataFrame()

for xls in excel_files:
    data = pd.read_excel(xls)
    df = df.append(data)

    excel_reader = pd.ExcelFile(xls)
    print(excel_reader.sheet_names)

df.to_excel(excel_dir / "output.xlsx")