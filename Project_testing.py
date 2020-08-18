# -*- coding: utf-8 -*-
"""
CS 5010
Project 1
Testing
Holden Bridge, hab5d; Nikhil Daga, nd9hq; Pengwei Hu, ph3bz
"""
## This file requires a .py file to work.
## Please download the .ipynb as .py file and put the resulting .py file in the same directory as this file.
## Because the functions we are testing have matplotlib output please close all
## resulting output generated from the testing file to see the final message for our unit tests.

# Import the necessary modules
import pandas as pd
import unittest
from Bridge_Daga_Hu_Project import *

# Initialize the testing class for our dataframe and create_df function
class Test_dataframe(unittest.TestCase):

    # Making sure our main data frame have the correct number of rows
    def test_if_nba_have_correct_rownum(self):

        # Testing if the data frame 'nba' have all 150 rows
        self.assertEqual(len(nba.index), 150)

    # Making sure our main data frame have the correct number of columns
    def test_if_nba_have_correct_colnum(self):

        # Testing if the data frame 'nba' have all 27 columns
        self.assertEqual(len(nba.columns), 27)

    # Making sure our main data frame does not have any missing data
    def test_if_nba_have_NAs(self):

        # Testing if the data frame 'nba' have 0 missing data
        self.assertEqual(nba.isna().sum().sum(),0)

    # Making sure create_df returns a data frame with correct number of rows
    def test_if_create_df_have_correct_rownum(self):

        # Select all the rows that belongs to 'Philadelphia 76ers'
        df = create_df('Philadelphia 76ers')
        # Testing if the resulting data frame have 5 rows
        self.assertEqual(len(df.index), 5)

    # Making sure create_df returns a data frame with correct number of columns
    def test_if_create_df_have_correct_colnum(self):

        # Select all the rows that belongs to 'Los Angeles Clippers'
        df = create_df('Los Angeles Clippers')
        # Testing if the resulting data frame have 27 columns
        self.assertEqual(len(df.columns), 27)

    # Making sure create_df returns a data frame with all the correct elements
    def test_manually_create_df_1(self):

        # Testing if create_df returns the same data frame as the manually subsetted one
        self.assertTrue(pd.DataFrame.equals(nba.iloc[[2,32,77,102,135]], create_df('New Orleans Pelicans')))

    # Making sure create_df returns a data frame with all the correct elements
    def test_manually_create_df_2(self):

        # Testing if create_df returns the same data frame as the manually subsetted one
        self.assertTrue(pd.DataFrame.equals(nba.iloc[[27,47,78,116,149]], create_df('New York Knicks')))

    # Making sure create_df returns a data frame with all the correct elements
    def test_create_df_1(self):

        # Subset the data frame using nba.loc to get the rows with 'Milwaukee Bucks'
        df = nba.loc[nba['Team'].isin(['Milwaukee Bucks','Milwaukee Bucks*'])]
        # Testing if create_df returns the same data frame as the above subset
        self.assertTrue(pd.DataFrame.equals(df, create_df('Milwaukee Bucks')))

    # Making sure create_df returns a data frame with all the correct elements
    def test_create_df_2(self):

        # Subset the data frame using nba.loc to get the rows with 'Golden State Warriors'
        df = nba.loc[nba['Team'].isin(['Golden State Warriors','Golden State Warriors*'])]
        # Testing if create_df returns the same data frame as the above subset
        self.assertTrue(pd.DataFrame.equals(df, create_df('Golden State Warriors')))

# Initialize the testing class for plot_division function
class Test_plot_divison(unittest.TestCase):

    # Making sure Southeast division wins over time plots correctly
    def test_plot_Southeast(self):

        # Setup the input data frames
        magic = create_df("Orlando Magic")
        heat = create_df("Miami Heat")
        wizards = create_df("Washington Wizards")
        hornets = create_df("Charlotte Hornets")
        hawks = create_df("Atlanta Hawks")

        # Setup the input team names and labels
        southeast_div = [magic, heat, wizards, hornets, hawks]
        southeast_names = ["Orlando Magic", "Miami Heat", "Washington Wizards", \
                           "Charlotte Hornets", "Atlanta Hawks", "Southeast"]
        southeast_colList = ['skyblue', 'fuchsia', 'royalblue', 'mediumturquoise', 'red']

        # Test if the plot_division function finished all 5 iterations
        self.assertEqual(plot_divison(southeast_div, southeast_names, southeast_colList),5)

    # Making sure Atlantic division wins over time plots correctly
    def test_plot_Atlantic(self):

        # Setup the input data frames
        raptors = create_df("Toronto Raptors")
        celtics = create_df("Boston Celtics")
        sixers = create_df("Philadelphia 76ers")
        nets = create_df("Brooklyn Nets")
        knicks = create_df("New York Knicks")

        # Setup the input team names and labels
        atlantic_div = [raptors, celtics, sixers, nets, knicks]
        atlantic_names = ["Toronto Raptors", "Boston Celtics", "Philadelphia 76ers", "Brooklyn Nets", "New York Knicks", "Atlantic"]
        atlantic_colList = ['red', 'limegreen', 'blue', 'black', 'orange']

        # Test if the plot_division function finished all 5 iterations
        self.assertEqual(plot_divison(atlantic_div, atlantic_names, atlantic_colList),5)

    # Making sure Central division wins over time plots correctly
    def test_plot_Central(self):

        # Setup the input data frames
        bucks = create_df("Milwaukee Bucks")
        pacers = create_df("Indiana Pacers")
        bulls = create_df("Chicago Bulls")
        pistons = create_df("Detroit Pistons")
        cavs = create_df("Cleveland Cavaliers")

        # Setup the input team names and labels
        central_div = [bucks, pacers, bulls, pistons, cavs]
        central_divnames = ["Milwaukee Bucks", "Indiana Pacers", "Chicago Bulls", "Detroit Pistons", "Cleveland Cavaliers", "Central"]
        central_colList = ['darkgreen', 'gold', 'red', 'royalblue', 'maroon']

        # Test if the plot_division function finished all 5 iterations
        self.assertEqual(plot_divison(central_div, central_names, central_colList),5)

    # Making sure Northwest division wins over time plots correctly
    def test_plot_Northwest(self):

        # Setup the input data frames
        nuggets = create_df("Denver Nuggets")
        jazz = create_df("Utah Jazz")
        thunder = create_df("Oklahoma City Thunder")
        blazers = create_df("Portland Trail Blazers")
        twolves = create_df("Minnesota Timberwolves")

        # Setup the input team names and labels
        northwest_div = [nuggets, jazz, thunder, blazers, twolves]
        northwest_names = ["Denver Nuggets", "Utah Jazz", "Oklahoma City Thunder", "Portland Trail Blazers", "Minnesota Timberwolves", "Northwest"]
        northwest_colList = ['gold', 'navy', 'orange', 'red', 'limegreen']

        # Test if the plot_division function finished all 5 iterations
        self.assertEqual(plot_divison(northwest_div, northwest_names, northwest_colList),5)

    # Making sure Pacific division wins over time plots correctly
    def test_plot_Pacific(self):

        # Setup the input data frames
        lakers = create_df("Los Angeles Lakers")
        clippers = create_df("Los Angeles Clippers")
        kings = create_df("Sacramento Kings")
        suns = create_df("Phoenix Suns")
        warriors = create_df("Golden State Warriors")

        # Setup the input team names and labels
        pacific_div = [lakers, clippers, kings, suns, warriors]
        pacific_names = ["Los Angeles Lakers", "Los Angeles Clippers", "Sacramento Kings", "Phoenix Suns", "Golden State Warriors", "Pacific"]
        pacific_colList = ['blueviolet', 'red', 'gray', 'orange', 'blue']

        # Test if the plot_division function finished all 5 iterations
        self.assertEqual(plot_divison(pacific_div, pacific_names, pacific_colList),5)

    # Making sure Southwest division wins over time plots correctly
    def test_plot_Southwest(self):

        # Setup the input data frames
        rockets = create_df("Houston Rockets")
        mavs = create_df("Dallas Mavericks")
        grizz = create_df("Memphis Grizzlies")
        spurs = create_df("San Antonio Spurs")
        pelicans = create_df("New Orleans Pelicans")

        # Setup the input team names and labels
        southwest_div = [rockets, mavs, grizz, spurs, pelicans]
        southwest_names = ["Houston Rockets", "Dallas Mavericks", "Memphis Grizzlies", "San Antonio Spurs", "New Orleans Pelicans", "Southwest"]
        southwest_colList = ['red', 'dodgerblue', 'navy', 'gray', 'burlywood']

        # Test if the plot_division function finished all 5 iterations
        self.assertEqual(plot_divison(southwest_div, southwest_names, southwest_colList),5)

# Initialize the testing class for bestToWorst and bestToWorstYear functions
class Test_bestToWorst(unittest.TestCase):

    # Making sure bestToWorst function returns the correct value for win rate
    def test_bestToWorst_for_winrate(self):

        # Setup data frame and compute average win rate grouped by team
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['W'].groupby(data['Team']).mean()/82

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorst('WL%'))

    # Making sure bestToWorst function returns the correct value for 2point percentage
    def test_bestToWorst_for_2point_percentage(self):

        # Setup data frame and compute average 2points percentage grouped by team
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['2P%'].groupby(data['Team']).mean()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorst('2P%'))

    # Making sure bestToWorst function returns the correct value for free throw percentage
    def test_bestToWorst_for_free_throw_percentage(self):

        # Setup data frame and compute average free throw percentage grouped by team
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['FT%'].groupby(data['Team']).mean()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorst('FT%'))

    # Making sure bestToWorst function returns the correct value for 3point percentage
    def test_bestToWorst_for_3point_percentage(self):

        # Setup data frame and compute average 3points percentage grouped by team
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['3P%'].groupby(data['Team']).mean()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorst('3P%'))

    # Making sure bestToWorst function returns the correct value for field goal percentage
    def test_bestToWorst_for_field_goal_percentage(self):

        # Setup data frame and compute average field goal percentage grouped by team
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['FG%'].groupby(data['Team']).mean()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorst('FG%'))

    # Making sure bestToWorst function returns the correct value for total points
    def test_bestToWorst_for_total_points(self):

        # Setup data frame and compute total points grouped by team
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['PTS'].groupby(data['Team']).sum()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorst('PTS'))

    # Making sure bestToWorst function returns the correct value for total Assist
    def test_bestToWorst_for_Assist(self):

        # Setup data frame and compute total Assist grouped by team
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['AST'].groupby(data['Team']).sum()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorst('AST'))

    # Making sure bestToWorstYear function returns the correct value for 2point percentage
    def test_bestToWorstYear_2point_percentage(self):

        # Setup data frame and compute average 2point percentage grouped by year
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['2P%'].groupby(data['Year']).mean()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorstYear('2P%'))

    # Making sure bestToWorstYear function returns the correct value for 3point percentage
    def test_bestToWorstYear_3point_percentage(self):

        # Setup data frame and compute average 3points percentage grouped by year
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['3P%'].groupby(data['Year']).mean()

        # Test is the bestToWorstYear returns the correct value
        self.assertEqual(min(bois), bestToWorstYear('3P%'))

    # Making sure bestToWorst function returns the correct value for total points
    def test_bestToWorstYear_total_points(self):

        # Setup data frame and compute total points grouped by year
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['PTS'].groupby(data['Year']).sum()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorstYear('PTS'))

    # Making sure bestToWorstYear function returns the correct value for total Assist
    def test_bestToWorstYear_Assist(self):

        # Setup data frame and compute total Assist grouped by year
        data=nba
        data['Team'] = data['Team'].str.replace(r'*', '')
        bois=data['AST'].groupby(data['Year']).sum()

        # Test is the bestToWorst returns the correct value
        self.assertEqual(min(bois), bestToWorstYear('AST'))


if __name__ == '__main__':
    unittest.main()
