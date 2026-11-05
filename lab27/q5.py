"""Read in the file diabetes.csv, and after obtaining the pandas dataframe, do the following:
(i) Print all the column names
(ii) Print the first 10 rows
(iii) Print the mean of the BloodPressure column values
(iv) Print the first 4 rows of columns 3,4,5
(v) Add another column ’NormalizedBP’ using (max-min) normalization to the dataframe
as: BP[i] -min(BP) / (max(BP) - min(BP)).

(vi) Write a function categorize_age(age) that returns ”Youth”, ”Adult” or ”Se-
nior” based on the age brackets (1-18, 19-50, ¿50). Create a new column in the

dataframe with this function called age category."""
#1
import pandas as pd
df=pd.read_csv("diabetes.csv")
print(df.columns)

#2
import pandas as pd
df=pd.read_csv("diabetes.csv")
print(df.head(10))

#3
import pandas as pd
df = pd.read_csv("diabetes.csv")
print(df["BloodPressure"].mean())

#4
import pandas as pd
df = pd.read_csv("diabetes.csv")
print(df.iloc[:4, 3:6])

#5
import pandas as pd
df = pd.read_csv("diabetes.csv")
bp = df["BloodPressure"]
df["NormalizedBP"] = (bp - bp.min()) / (bp.max() - bp.min())
print(df[["BloodPressure", "NormalizedBP"]].head())

#6
import pandas as pd

df = pd.read_csv("diabetes.csv")

def categorize_age(age):
    if age <= 18:
        return "Youth"
    elif age <= 50:
        return "Adult"
    else:
        return "Senior"

df["age_category"] = df["Age"].apply(categorize_age)
print(df[["Age", "age_category"]].head(10))
