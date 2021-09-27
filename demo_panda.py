import os, pandas
from pandas.core.frame import DataFrame


def read_data_file(path: str) -> DataFrame:
    if not os.path.exists(path):
        return None
    data_file = open(path, 'rb')
    if ".csv" in path:
        data = pandas.read_csv(data_file)
    elif ".xlsx" in path:
        data = pandas.read_excel(data_file, sheet_name='excel_file')
    elif ".json" in path:
        data = pandas.read_json(data_file)
    else:
        return None
    print(data)
    return data

def main():
    data = read_data_file("./statics/excel_file.csv")
    print("--- Your data file ---")
    print(f"Data types:\n{data.dtypes}\n")
    print(f"File's info:\n{data.info()}\n")
    print(f"{data.count()}\n")
    print(f"Columns:\n{data.columns}\n")
    print(f"{data.to_json()}\n")
    print(f"{data.to_html()}\n")
    print(f"{data.to_dict()}\n")

    temp_df = data[["clientid"]].copy()
    print(temp_df)
    temp_df["clientid"] = temp_df["clientid"].apply(lambda x: x ** 2)
    print(temp_df)
    data["clientid"] = temp_df["clientid"]

    # Write an Excel file with the updated values
    data.to_excel("./demo_excel.xlsx")

if __name__ == "__main__":
    main()