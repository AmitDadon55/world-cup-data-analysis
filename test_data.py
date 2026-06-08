import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("results.csv")

df["winner"] = df.apply(
    lambda row: row["home_team"]
    if row["home_score"] > row["away_score"]
    else row["away_team"]
    if row["away_score"] > row["home_score"]
    else "Draw",
    axis=1
)

games_home = df["home_team"].value_counts()
games_away = df["away_team"].value_counts()

games_played = games_home.add(games_away, fill_value=0)

wins = df[df["winner"] != "Draw"]["winner"].value_counts()

stats = pd.DataFrame({
    "games_played": games_played,
    "wins": wins
}).fillna(0)

stats["win_rate"] = (stats["wins"] / stats["games_played"]).round(3)

stats_300 = stats[stats["games_played"] >= 300]

stats_300 = stats_300.sort_values(
    "win_rate",
    ascending=False
)

os.makedirs("output", exist_ok=True)

stats_300.to_excel(
    "output/team_stats_300_plus.xlsx",
    index=True
)

top15 = stats_300.head(15)

plt.figure(figsize=(12, 6))
plt.bar(top15.index, top15["win_rate"])

plt.title("Top 15 National Teams by Win Rate (300+ Games)")
plt.xlabel("National Team")
plt.ylabel("Win Rate")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("output/top15_win_rate.png")

plt.show()

print("Excel file created: output/team_stats_300_plus.xlsx")
print("Graph created: output/top15_win_rate.png")