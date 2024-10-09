import unittest
import pandas as pd
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath('..'))
import src.hipotese_2_Stephany.auxiliary_stephany as ax


class TestDataProcessing(unittest.TestCase):
    """
    Unit tests for data processing functions.
    """

    @patch("pandas.read_csv")
    def test_get_hour(self, mock_read_csv):
        """
        Test the get_hour function to ensure it correctly creates a new Dataframe column called `hour`,
        based on the 'callDateTime' column.
        
        This test simulates reading data from a CSV file using mock data and verifies:
        1. if the new DataFrame contains the 'hour' column whith the hour information extracted from the `callDateTime` column.
        2. If the extracted hours are formatted as two-digit strings.
        The input data simulates datetime strings in the format 'MM/DD/YYYY HH:MM:SS+00'.
        """
        #A simulate DataFrame
        mock_df= pd.DataFrame({
            'callDateTime': ['03/15/2024 17:32:00+00', '12/11/2021 00:02:00+00']
        })

        mock_read_csv.return_value = mock_df
        result_df = ax.get_hour(mock_df)

        expected_data = pd.DataFrame({
            'callDateTime': ['03/15/2024 17:32:00+00', '12/11/2021 00:02:00+00'],
            'hour': ['17', '00']
        })

        pd.testing.assert_frame_equal(result_df,expected_data)

    def test_get_hour2(self):
        """
        Test the get_hour function's reaction to a None input.

        This test ensures that the function raises a TypeError when None is passed as input,
        as the function expects a valid pandas DataFrame.
        """
        with self.assertRaises(TypeError):
            ax.get_hour(None)

    @patch("pandas.read_csv")
    def test_get_first_15_most_frequency(self, mock_read_csv):
        """
        Test the get_first_15_most_frequency function to ensure it retrieves the top 15 most frequent `description` rows
        from the DataFrame.
        
        This test simulates reading data from a CSV file using mock data and verifies:
        1. if the new DataFrame contains no more than 15 distinct `description` rows based on their frequency.

        As the function filters the corresponding rows, it is necessary to reset the index to be able
        to compare with the expected result.
        """
        mock_df= pd.DataFrame({
            'callDateTime': ['2021/01/04 16:33:00+00','2021/01/04 17:34:00+00','2021/01/04 17:40:00+00','2021/01/04 17:45:00+00',\
                             '2021/01/05 13:11:00+00','2021/01/05 16:45:00+00','2021/01/05 16:47:00+00','2021/01/05 17:16:00+00',\
                             '2021/01/05 17:28:00+00','2021/01/06 10:49:00+00','2021/01/06 16:34:00+00','2021/01/07 12:25:00+00',\
                             '2021/01/07 16:33:00+00','2021/01/07 17:07:00+00','2021/01/08 16:39:00+00','2021/01/08 18:55:00+00',\
                             '2021/01/11 11:39:00+00','2021/01/11 11:57:00+00','2021/01/11 12:52:00+00','2021/01/11 14:20:00+00',\
                             '2021/01/05 13:11:00+00','2021/01/05 16:45:00+00','2021/01/05 16:47:00+00','2021/01/05 17:16:00+00',\
                             '2021/01/05 17:28:00+00','2021/01/06 10:49:00+00','2021/01/06 16:34:00+00','2021/01/07 12:25:00+00',\
                             '2021/01/07 16:33:00+00','2021/01/07 17:07:00+00','2021/01/08 16:39:00+00','2021/01/08 18:55:00+00'],
            'description': ['HIT AND RUN','SIGNAL FLASHING','OTHER','NARCOTICS','DESTRUCT PROP','TO ASSIST','AUTO ACCIDENT',\
                            'LARCENY F/AUTO','LARCENY','LOUD MUSIC','SUPV COMPLAINT','SIGNAL FLASHING','VANDELIZED','FALSE PRETENSE',\
                            'WELL CHECK','WELL CHECK','YELLING FOR HELP', 'YELLING HELP', 'YORK','SECURITY CHECK', 'WELL CHECK',\
                            'TRFIC CONTROL','YELLING FOR HELP', 'YELLING HELP', 'SIGNAL FLASHING','REPO', 'YORK','REPO',\
                            'YELLING FOR HELP', 'YELLING HELP', 'YORK','UNKOWN']
        })
        amy= mock_df.groupby('description').size()
        mock_read_csv.return_value = mock_df
        result_df = ax.get_first_15_most_frequency(mock_df,amy)


        expected_data = pd.DataFrame({
            'callDateTime': ['2021/01/04 16:33:00+00','2021/01/04 17:34:00+00','2021/01/05 13:11:00+00','2021/01/05 16:47:00+00',\
                             '2021/01/05 17:16:00+00','2021/01/05 17:28:00+00','2021/01/06 10:49:00+00','2021/01/06 16:34:00+00',\
                             '2021/01/07 12:25:00+00','2021/01/07 17:07:00+00','2021/01/08 16:39:00+00','2021/01/08 18:55:00+00',\
                             '2021/01/11 11:39:00+00','2021/01/11 11:57:00+00','2021/01/11 12:52:00+00','2021/01/11 14:20:00+00',\
                             '2021/01/05 13:11:00+00','2021/01/05 16:47:00+00','2021/01/05 17:16:00+00','2021/01/05 17:28:00+00',\
                             '2021/01/06 10:49:00+00','2021/01/06 16:34:00+00','2021/01/07 12:25:00+00','2021/01/07 16:33:00+00',\
                             '2021/01/07 17:07:00+00','2021/01/08 16:39:00+00'],
            'description': ['HIT AND RUN','SIGNAL FLASHING','DESTRUCT PROP','AUTO ACCIDENT','LARCENY F/AUTO','LARCENY',\
                            'LOUD MUSIC','SUPV COMPLAINT','SIGNAL FLASHING','FALSE PRETENSE','WELL CHECK','WELL CHECK',\
                            'YELLING FOR HELP', 'YELLING HELP', 'YORK','SECURITY CHECK', 'WELL CHECK','YELLING FOR HELP',\
                            'YELLING HELP', 'SIGNAL FLASHING','REPO', 'YORK','REPO','YELLING FOR HELP', 'YELLING HELP', 'YORK']
        })

        pd.testing.assert_frame_equal(result_df.reset_index(drop=True),expected_data.reset_index(drop=True))

    @patch("pandas.read_csv")
    def test_get_first_15_most_frequency2(self, mock_read_csv):
        """
        Test the reaction of the get_first_15_most_frequency function when it receives an input with less than 15 dates.
        
        This test ensures that the function still returns the most frequent occurrences even 
        when there are less than 15 different descriptions.

        As the function filters the corresponding rows, it is necessary to reset the index to be able
        to compare with the expected result.
        """
        mock_df= pd.DataFrame({
            'callDateTime': ['2021/01/04 16:33:00+00'],
            'description': ['HIT AND RUN']
        })
        amy= mock_df.groupby('description').size()
        mock_read_csv.return_value = mock_df
        result_df = ax.get_first_15_most_frequency(mock_df,amy)


        expected_data = pd.DataFrame({
            'callDateTime': ['2021/01/04 16:33:00+00'],
            'description': ['HIT AND RUN']
        })

        pd.testing.assert_frame_equal(result_df.reset_index(drop=True),expected_data.reset_index(drop=True))

    def test_get_first_15_most_frequency3(self):
        """
        Test the get_first_15_most_frequency function's reaction to a None input.

        This test ensures that the function raises a TypeError when None is passed as input,
        as the function expects a valid pandas DataFrame.
        """
        
        with self.assertRaises(TypeError):
            ax.get_first_15_most_frequency(None)

if __name__ == '__main__':
    unittest.main()