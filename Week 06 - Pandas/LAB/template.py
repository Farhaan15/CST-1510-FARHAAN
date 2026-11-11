"""
RECORD CHECK  -  my version
===========================

Name  : Farhaan Ahmed
Lane  :  AI 
Date  : 7-11-2026


"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD

df = pd.read_csv("ai_data.csv")


# ================================================================= PROCESS


df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK"))


# ================================================================== OUTPUT
print("--- Full DataFrame ---")
print(df)

print("\n--- Filtered Rows (Not OK) ---")
print(df[df["status"] != "OK"])

print("\n--- Status Counts ---")
print(df["status"].value_counts())

# save full DataFrame to a new CSV file
df.to_csv("ai_data_report.csv", index=False)

# create, show, and save the bar chart
df["status"].value_counts().plot(kind="bar")
plt.title("AI Dataset Status Counts")
plt.savefig("ai_status_counts.png")
plt.show()




# ==========================================================================

