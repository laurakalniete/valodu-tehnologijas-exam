import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("attiritie_dati.csv")
train_df, temp_df = train_test_split(
    df,
    test_size=0.30, #train 70%, temp 30%
    shuffle=True,
    stratify=df["gen"],  
    random_state=73
)

# atlikusos 30% sadala validation un testa datos
val_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    shuffle=True,
    stratify=temp_df["gen"],
    random_state=73
)

train_df.to_csv("train.csv", index=False)
val_df.to_csv("validation.csv", index=False)
test_df.to_csv("test.csv", index=False)

print("Train:", len(train_df))
print("Validation:", len(val_df))
print("Test:", len(test_df))

# print(train_df["gen"].value_counts())
# print(val_df["gen"].value_counts())
# print(test_df["gen"].value_counts())