import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from auxiliary import load_data, save_top_descriptions, remove_lines

class TestDataProcessing(unittest.TestCase):
    """
    Unit tests for data processing functions.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="recordId\tdistrict\tdescription\n1\tA\tOther\n2\tB\tAssault")
    def test_load_data(self, mock_file):
        """
        Test the load_data function to ensure it correctly loads data
        from a CSV file and returns the expected columns without null values.
        
        This test simulates reading from a CSV file using mock data and verifies:
        1. The DataFrame contains the expected columns ('recordId', 'district', 'description').
        2. There are no missing (null) values in the returned DataFrame.
        """

        filepath = "dummy_path.csv"  # Dummy file path used for testing
        df = load_data(filepath) 

        # Verify the expected columns are present in the DataFrame
        expected_columns = ['recordId', 'district', 'description']
        self.assertEqual(list(df.columns), expected_columns)

        # Ensure the DataFrame has no null values
        self.assertFalse(df.isnull().values.any())


    @patch("pandas.DataFrame.to_csv")
    def test_save_top_descriptions(self, mock_to_csv):
        """
        Test the save_top_descriptions function to verify it correctly
        extracts the top descriptions and saves them to a CSV file.
        
        This test:
        1. Creates a sample DataFrame with mock descriptions.
        2. Calls the save_top_descriptions function.
        3. Verifies that the to_csv method was called exactly once.
        4. Checks if the returned DataFrame contains the correct counts for each description.
        """
        # Sample data with descriptions and their counts
        data = {
            'description': ['DISORDERLY'] * 20 + ['911/NO VOICE'] * 10 + ['COMMON ASSAULT'] * 5
        }
        df = pd.DataFrame(data) 

        # Call the function to save descriptions and return the result DataFrame
        result_df = save_top_descriptions(df)

        # Verify that to_csv was called once to save the output
        mock_to_csv.assert_called_once()

        # Expected counts for each description
        expected_counts = {
            'DISORDERLY': 20,
            '911/NO VOICE': 10,
            'COMMON ASSAULT': 5,
        }

        # Check if the counts in the result match the expected counts
        for description, count in expected_counts.items():
            actual_count = result_df.loc[result_df['Description'] == description, 'Count'].values[0]
            self.assertEqual(actual_count, count)


    @patch("pandas.read_csv")
    @patch("pandas.DataFrame.to_csv")
    def test_remove_lines(self, mock_to_csv, mock_read_csv):
        """
        Test the remove_lines function to ensure rows containing unwanted words 
        in the 'district' column are removed and the cleaned data is saved to a new file.
        """
        # Mock DataFrame for testing
        mock_df = pd.DataFrame({
            'district': ['EVT1', 'TRU', 'NE', 'SS', 'CW', 'ND'],
            'call_count': [100, 150, 200, 250, 300, 350]
        })

        # Returns the simulated DataFrame
        mock_read_csv.return_value = mock_df

        # Call the funct remove_lines
        result_df = remove_lines("dummy_path.csv")

        # Reset the index of the resulting DataFrame
        result_df = result_df.reset_index(drop=True)

        # Expected data after removing lines with 'EVT1', 'TRU', 'SS', 'CW'
        expected_df = pd.DataFrame({
            'district': ['NE', 'ND'],
            'call_count': [200, 350]
        })

        # Checks if the DataFrame returned by remove_lines is the same as expected
        pd.testing.assert_frame_equal(result_df, expected_df)

        # Checks if the to_csv method was called once with the correct file name
        mock_to_csv.assert_called_once_with('Cleaned_Call_Distribution.csv', index=False)


if __name__ == '__main__':
    unittest.main()