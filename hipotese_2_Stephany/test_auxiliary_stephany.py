import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from auxiliary_stephany import get_first_15_most_frequency, get_hour


class TestDataProcessing(unittest.TestCase):
    @patch("pandas.DataFrame.to_csv")
    @patch("pandas.read_csv")
    def test_get_hour(self, mock_to_csv, mock_read_csv):
        """
        """

        #An exemple  
        mock_df= pd.DataFrame({
            'callDateTime': ['03/15/2024 17:32:00+00']
        })

        mock_read_csv.return_value = mock_df
        result_df = get_hour(mock_df)


        expected_data = pd.DataFrame({
            'callDateTime': ['03/15/2024 17:32:00+00'],
            'hour': ['17']
        })

        pd.testing.assert_frame_equal(result_df,expected_data)

if __name__ == '__main__':
    unittest.main()