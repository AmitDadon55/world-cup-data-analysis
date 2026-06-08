import os
import pandas as pd
import matplotlib.pyplot as plt

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

stats["win_rate"] = stats["wins"] / stats["games_played"]

home_goals = df.groupby("home_team")["home_score"].sum()
away_goals = df.groupby("away_team")["away_score"].sum()
goals_scored = home_goals.add(away_goals, fill_value=0)

stats["goals_scored"] = goals_scored

stats["avg_goals_per_match"] = (
    stats["goals_scored"] / stats["games_played"]
)

stats_300 = stats[stats["games_played"] >= 300].copy()

stats_300 = stats_300.sort_values(
    "avg_goals_per_match",
    ascending=False
)

os.makedirs("output", exist_ok=True)

stats_300.to_excel(
    "output/team_stats_300_plus.xlsx",
    index=True
)

top15 = stats_300.head(15)

plt.figure(figsize=(12,6))

plt.scatter(
    top15.index,
    top15["avg_goals_per_match"]
)

plt.title("Top 15 National Teams by Average Goals Per Match")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(stats_300.head(20).to_string())
print("Excel file created: output/team_stats_300_plus.xlsx")
print("Graph created: output/top15_avg_goals.png")
plt.savefig("output/top15_avg_goals_horizontal.png")