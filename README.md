# NBA Data Analysis Project Documentation

![NBA Logo](https://goodlogo.com/images/logos/national_basketball_association_nba_logo_2414.gif)

Goal was to try to find any relationship between a NBA player's salary and his points for Data Mining extra credit. Didn't finish.
###Web Scraping Process

 Used python in 'nbasalariestesting.py'. This goes to http://www.espn.com/nba/salaries/_/year/2016 and scrapes the player data according to inspect element/tags of that site. Then it loops through the rest of the 11 or 12 pages of data and does the same. It saves all of this to one csv file named 'nbasalaries.csv'. 

The csv file for the player's stats like rebounds/points/steals was already available in 'NBApoints.csv' so I just merged the two csv files together where the names match. This is done in 'merge.py' to make the final csv file with the players stats and salaries altogether is in 'nbasalariespoints.csv'
 
 
###Data Transformation Process
 
 - For `NBApoints.csv`, the Player name will include “\information” after the players actual name. To remove this, in Excel, we use the  find and replace feature, and in the “Find” area, we put “\*”, and in the replace, we put “ “. This will clean up the player name feature to be just the name.
 - Similarly, for `nbasalaries.csv`, we do the same process. In the “Find” area, we put “,*”, and in the replace, we put “ “. This will clean up the player name feature to be just the name.
