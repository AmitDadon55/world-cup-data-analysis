import pandas as pd

df = pd.read_csv("results.csv")

df["winner"] = df.apply(
    lambda row: row["home_team"]
    if row["home_score"] > row["away_score"]
    else row["away_team"]
    if row["away_score"] > row["home_score"]
    else "Draw",
    axis=1
)

print(df[["home_team", "away_team", "home_score",
          "away_score", "winner"]].head(10))
wins = df[df["winner"] != "Draw"]["winner"].value_counts()

print(wins.head(20))
games_home = df["home_team"].value_counts()
games_away = df["away_team"].value_counts()

games_played = games_home.add(games_away, fill_value=0)

wins = df[df["winner"] != "Draw"]["winner"].value_counts()

stats = pd.DataFrame({
    "games_played": games_played,
    "wins": wins
}).fillna(0)

stats["win_rate"] = stats["wins"] / stats["games_played"]

print(
    stats.sort_values("win_rate", ascending=False)
         .head(20)
)

stats_sorted = stats.sort_values(
    "win_rate",
    ascending=False
)

stats_sorted.to_csv("team_stats.csv")
# רק נבחרות עם לפחות 300 משחקים
stats_300 = stats[stats["games_played"] >= 300]

# מיון לפי אחוז ניצחונות
stats_300 = stats_300.sort_values(
    "win_rate",
    ascending=False
)

# שמירה לאקסל
stats_300.to_excel(
    "team_stats_300_plus.xlsx",
    index=True
)

print("Excel file created successfully!")