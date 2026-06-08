# ⚽ FIFA World Cup Data Analysis

## Project Overview

This project analyzes over 49,000 international football matches to evaluate the historical performance of national teams.

Using Python and Pandas, the project calculates:

- Total matches played
- Total wins
- Historical win rates
- Team rankings based on performance
- Visualization of the top-performing national teams

---

## Dataset

International Football Results Dataset

Dataset contains:

- 49,445 international matches
- Matches dating back to 1872
- 9 variables per match

Main features:

| Feature | Description |
|----------|-------------|
| date | Match date |
| home_team | Home team |
| away_team | Away team |
| home_score | Goals scored by home team |
| away_score | Goals scored by away team |
| tournament | Competition type |
| city | Match city |
| country | Match country |
| neutral | Neutral venue indicator |

---

## Data Processing

The project performs the following steps:

### Winner Calculation

A new feature called `winner` is generated:

- Home team if home score > away score
- Away team if away score > home score
- Draw otherwise

### Team Statistics

For each national team:

- Total games played
- Total wins
- Win rate

### Filtering

Only teams with at least **300 matches played** are included in the final ranking to avoid statistical bias.

---

## Results

The project generates:

### Excel Report

`team_stats_300_plus.xlsx`

Contains:

- Team name
- Matches played
- Wins
- Win rate

### Visualization

`top15_win_rate.png`

Shows the 15 national teams with the highest historical win rate among teams with at least 300 matches played.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Git
- GitHub

---

## Project Structure

```text
World_Cup/
│
├── results.csv
├── world_cup_analysis.py
│
├── output/
│   ├── team_stats_300_plus.xlsx
│   └── top15_win_rate.png
│
└── README.md
```

---

## Future Improvements

Planned next steps:

- FIFA ranking integration
- World Cup winner prediction model
- Team strength scoring system
- Top-5 European leagues player analysis
- Machine Learning based tournament simulation

---

## Author

Amit Dadon

Industrial Engineering & Management Student

Ben-Gurion University of the Negev