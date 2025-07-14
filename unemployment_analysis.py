import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Unemployment in India.csv")

print("\n Dataset Preview:")
print(df.head())

print("\n Columns:")
print(df.columns)

df.columns = ["States", "Date", "Frequency", "Estimated Unemployment Rate",
              "Estimated Employed", "Estimated Labour Participation Rate", "Region"]

df["Date"] = pd.to_datetime(df["Date"],dayfirst=True)

unemp_statewise = df.groupby("States")["Estimated Unemployment Rate"].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=unemp_statewise.values, y=unemp_statewise.index, palette="Reds_r")
plt.title("Average Unemployment Rate by State (India)")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("States")
plt.tight_layout()
plt.show(block=False)
plt.pause(5)
plt.close()

plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Estimated Unemployment Rate", data=df, hue="Region")
plt.title("Unemployment Rate Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend(title="Region")
plt.tight_layout()
plt.show()