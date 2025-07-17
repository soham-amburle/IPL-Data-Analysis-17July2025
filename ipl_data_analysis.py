import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Load the matches dataset
ipl = pd.read_csv('matches.csv')

# Print the first few rows of the dataset
print(ipl.head())

# Print the shape of the dataset (rows, columns)
print(ipl.shape)

# Count how many times each player won "Player of the Match"
print(ipl['player_of_match'].value_counts())

# Get the top 10 player of the match counts
print(list(ipl['player_of_match'].value_counts()[0:10]))

# Get the names of the top 10 players
print(list(ipl['player_of_match'].value_counts()[0:10].keys()))

# Bar chart for top 10 players of the match
plt.figure(figsize=(5,5))
plt.bar(
    list(ipl['player_of_match'].value_counts()[0:10].keys()),
    list(ipl['player_of_match'].value_counts()[0:10]),
    color='g'
)
plt.show()

# Count types of results (e.g., normal, tie)
print(ipl['result'].value_counts())

# List of teams that won the toss
print(list(ipl['toss_winner'].value_counts().keys()))

# Filter matches where teams won by runs (i.e., batting first)
batting_first = ipl[ipl['win_by_runs'] != 0]
print(batting_first.head())

# Horizontal histogram of win by runs
plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'], color='r', orientation='horizontal')
plt.show()

# Vertical histogram of win by runs
plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'], color='b', orientation='vertical')
plt.title('Distribution of runs')
plt.xlabel('Number of runs')
plt.show()

# Top 5 teams that won matches batting first
print(list(batting_first['winner'].value_counts()[0:5].keys()))

# Bar chart for top 3 teams batting first
plt.figure(figsize=(7,7))
plt.bar(
    list(batting_first['winner'].value_counts()[0:3].keys()),
    list(batting_first['winner'].value_counts()[0:3]),
    color=["blue", "yellow", "orange"]
)
plt.title('Top 3')
plt.show()

# Pie chart for top 3 teams batting first
plt.figure(figsize=(7,7))
plt.pie(
    list(batting_first['winner'].value_counts()[0:3]),
    labels=list(batting_first['winner'].value_counts()[0:3].keys()),
    autopct='%0.1f%%'
)
plt.show()

# Pie chart for all teams batting first
plt.figure(figsize=(7,7))
plt.pie(
    list(batting_first['winner'].value_counts()),
    labels=list(batting_first['winner'].value_counts().keys()),
    autopct='%0.1f%%'
)
plt.show()

# Redefine batting_first again (redundant but harmless)
batting_first = ipl[ipl['win_by_runs'] != 0]
print(batting_first.head())

# Filter matches where teams won by wickets (i.e., batting second)
batting_second = ipl[ipl['win_by_wickets'] != 0]
print(batting_second.head())

# Histogram for number of wickets won when batting second
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'], bins=50)
plt.xlabel('Number of wickers')
plt.ylabel('Number of runs')
plt.show()

# Top 10 teams that won chasing
print(list(batting_second['winner'].value_counts()[0:10].keys()))

# Bar chart for top 3 teams batting second
plt.figure(figsize=(7,7))
plt.bar(
    list(batting_second['winner'].value_counts()[0:3].keys()),
    list(batting_second['winner'].value_counts()[0:3]),
    color=['purple', 'blue', 'red']
)
plt.show()

# Pie chart for all teams batting second
plt.figure(figsize=(7,7))
plt.pie(
    list(batting_second['winner'].value_counts()),
    labels=list(batting_second['winner'].value_counts().keys()),
    autopct='%0.1f%%',
    # colors can be added manually if needed
)
plt.show()

# List of seasons (not necessarily in chronological order)
print(list(ipl['season'].value_counts().keys()))

# Top 5 cities where matches were played
print(ipl['city'].value_counts()[0:5])

# Number of matches where toss winner also won the match
print(np.sum(ipl['toss_winner'] == ipl['winner']))

# Total number of matches in the dataset
print(len(ipl))

# Shape of the dataset (again, redundant but okay)
print(ipl.shape)

# Print all unique cities in the dataset
print(ipl['city'].unique())

# List of unique seasons
print(list(ipl['season'].unique()))

# Filter matches won by Sunrisers Hyderabad
SunHyd = ipl[ipl['winner'] == 'Sunrisers Hyderabad']
print(SunHyd.head())

# Shape of Sunrisers Hyderabad wins
print(SunHyd.shape)

# Count total SRH vs RCB matches
print(np.sum(
    (ipl['team1'] == 'Sunrisers Hyderabad') & (ipl['team2'] == 'Royal Challengers Bangalore') |
    (ipl['team1'] == 'Royal Challengers Bangalore') & (ipl['team2'] == 'Sunrisers Hyderabad')
))

# Count matches where player of match was Yuvraj Singh or CA Lynn
print(np.sum(
    (ipl['player_of_match'] == 'Yuvraj Singh') |
    (ipl['player_of_match'] == 'CA Lynn')
))

# Count matches in 2017 where SRH won both toss and match
print(np.sum(
    (ipl['season'] == 2017) &
    (ipl['toss_winner'] == 'Sunrisers Hyderabad') &
    (ipl['winner'] == 'Sunrisers Hyderabad')
))

# Filter matches where SRH won both toss and match
Srh_wins = ipl[
    (ipl['toss_winner'] == 'Sunrisers Hyderabad') &
    (ipl['winner'] == 'Sunrisers Hyderabad')
]
print(Srh_wins)

# List of seasons where SRH won both toss and match
print(Srh_wins['season'].unique())

# Count of unique such seasons
print(len(Srh_wins['season'].unique()))
