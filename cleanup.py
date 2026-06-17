import pandas as pd
import re

df = pd.read_csv("bodies.csv")

df["body"] = df["body"].astype(str)

# ārā metamie - [removed], [deleted], "...I am a bot...", [gif]
bad_pattern = r"\[removed\]|\[deleted\]|I am a bot|\[gif\]"

# patur rindas, kurās neparādās bad_pattern
df = df[~df["body"].str.contains(
    bad_pattern,
    case=False,
    regex=True,
    na=False
)]

# noņem linkus
df["body"] = df["body"].str.replace(
    r"https?://\S+|www\.\S+",
    "",
    regex=True
)

# noņem extra atstarpes
df["body"] = df["body"].str.replace(r"\s+", " ", regex=True).str.strip()

# noņem tukšās rindas
df = df[df["body"] != ""]

df.to_csv("attiritie_dati.csv", index=False)
# print()