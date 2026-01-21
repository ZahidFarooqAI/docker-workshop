import sys
import pandas as pd
print("argumnets",sys.argv)
month=int(sys.argv[1])
df = pd.DataFrame({"day": [1, 2], "number_passenger": [3, 4]})
df["month"]=month
df.to_parquet(f"output_{month}.parquet")
print(df.head())
print(f"hello pipeline.py,month={month}")
print("2+2=4") 