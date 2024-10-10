import unittest
import pandas as pd
from unittest.mock import patch, mock_open
import sys
import os
sys.path.append(os.path.abspath('..'))
from src.hipotese_3_Eliane.calls_eliane import load_data, categorize_activity, call_counter
from src.hipotese_3_Eliane.calls_eliane import distribution_in_percentage, save_data, process_and_save_data


class TestDataProcessing(unittest.TestCase):
    """
    Unit tests for data processing functions.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="recordId\tdistrict\tdescription\n1\tA\tOther\n2\tB\tAssault")
    def test_load_data(self, mock_file):
        """
        Test the load_data function to ensure it correctly loads data
        from a CSV file and returns the expected columns without null values.
        """
        
        filepath = "dummy_path.csv"  # Dummy file path used for testing
        df = load_data(filepath)

        # Verify the expected columns are present in the DataFrame
        expected_columns = ['recordId', 'district', 'description']
        self.assertEqual(list(df.columns), expected_columns)

        # Ensure the DataFrame has no null values
        self.assertFalse(df.isnull().values.any())

    def test_categorize_activity(self):
        """
        Test the categorize_activity function to correctly categorize the activities.
        
        This test:
        1. Creates a sample list of descriptions.
        2. Calls the categorize_activity function for each description.
        3. Verifies that each description is categorized correctly.
        """
        # Sample descriptions and their expected categories
        descriptions = [
            ('disorderly', 'Against Public Welfare'),
            ('911/NO Voice', 'Against Unknown'),
            ('AudiBLE AlarM', 'Uncategorized High Frequency Descriptions'),
            ('HIt AnD RUn', 'Against Person'),
            ('VehiCLE DIstuRB', 'Against Public Property'),
            ('PANHANDLER', 'Low Frequency Descriptions')
        ]

        for description, expected_category in descriptions:
            category = categorize_activity(description)
            self.assertEqual(category, expected_category)

    def setUp(self):
        """
        This method creates a sample DataFrame with columns 'district' and 'description'.

        DataFrame structure:
        
        ==========  ================================================
        district    description
        ==========  ================================================
        D1          HIT AND RUN           # Against Person
        D1          COMMON ASSAULT        # Against Person
        D2          NARCOTICS             # Against Public Welfare
        D2          LOUD MUSIC            # Against Public Welfare
        D1          AUTO THEFT            # Against Public Property
        ==========  ================================================

        The test data will be used for testing the call_counter and distribution_in_percentage functions.
        """

        self.data = pd.DataFrame({
            'district': ['D1', 'D1', 'D2', 'D2', 'D1'],
            'description': [
                'HIT AND RUN',        # Against Person
                'COMMON ASSAULT',     # Against Person
                'NARCOTICS',          # Against Public Welfare
                'LOUD MUSIC',         # Against Public Welfare
                'AUTO THEFT'          # Against Public Property
            ]
        })

    def test_call_counter(self):
        """
        Test the call_counter function to count the number of calls per category in each district.

        This test checks the following:
        1. Counts the number of calls for each category in the provided test data.
        2. That the counts are as expected:
        
                        | district | category                | call_count |
                        |----------|-------------------------|------------|
                        | D1       | Against Person          | 2          |
                        | D1       | Against Public Property | 1          |
                        | D2       | Against Public Welfare  | 2          |

        It also verifies that the function handles empty DataFrames.
        """

        result = call_counter(self.data)
        self.assertTrue((result['call_count'] == [2, 1, 2]).all())
        empty_df = pd.DataFrame(columns=['district', 'description'])
        result = call_counter(empty_df)
        self.assertTrue(result.empty)

    def test_distribution_in_percentage(self):
        """
        Test the distribution_in_percentage function to ensure percentages sum to 100% per district.

        This test checks the percentage distribution of calls for each category within districts based on the call counts.

        Expected Percentages:
            {
                'D1': {
                    'Against Person': 66.67,
                    'Against Public Property': 33.33,
                },
                'D2': {
                    'Against Public Welfare': 100.0,
                }
            }
        """

        result = call_counter(self.data)
        percentage_result = distribution_in_percentage(result)

        # Checks whether the sum of the percentages is 100%
        grouped = percentage_result.groupby('district')['percentage'].sum().reset_index()
        for i, row in grouped.iterrows():
            self.assertAlmostEqual(row['percentage'], 100.0, places=1)

        expected_percentages = {
            'D1': {
                'Against Person': 66.66666666666666,
                'Against Public Property': 33.33333333333333,
            },
            'D2': {
                'Against Public Welfare': 100.0,
            }
        }

        for j, row in percentage_result.iterrows():
            district = row['district']
            category = row['category']
            expected = expected_percentages[district][category]
            self.assertAlmostEqual(row['percentage'], expected, places=1)

        empty_df = pd.DataFrame(columns=['district', 'category', 'call_count'])
        result = distribution_in_percentage(empty_df)
        self.assertTrue(result.empty)

    @patch('pandas.DataFrame.to_csv')
    def test_save_data(self, mock_to_csv):
        """
        Test the save_data function to ensure it correctly saves the DataFrame 
        to a CSV file.
        
        This test:
        1. Creates a sample DataFrame.
        2. Calls the save_data function to save it.
        3. Verifies that pandas to_csv was called with the correct parameters.
        """
        #  DataFrame to save
        df = pd.DataFrame({
            'Category': ['Against Person', 'Against Public Property'],
            'Count': [10, 20]
        })

        save_data(df, 'output.csv')
        mock_to_csv.assert_called_once_with('output.csv', index=False)

    @patch('calls_by_category.save_data')
    @patch('calls_by_category.distribution_in_percentage')
    @patch('calls_by_category.call_counter')
    @patch('calls_by_category.load_data')
    def test_process_and_save_data(self, mock_load_data, mock_call_counter, mock_distribution_in_percentage, mock_save_data):
        """
        Test the process_and_save_data function to ensure it processes the data 
        and saves it correctly.

        This test:
        1. Mocks load_data to return a sample DataFrame.
        2. Mocks call_counter and distribution_in_percentage to return expected outputs.
        3. Verifies that the correct functions are called in the right order 
        with the correct parameters.
        """

        mock_load_data.return_value = pd.DataFrame({
            'description': ['HIT AND RUN', 'COMMON ASSAULT','NARCOTICS'],     
            'district': ['D1', 'D1', 'D2']
        })

        mock_call_counter.return_value = pd.DataFrame({
            'Category': ['Against Person', 'Against Public Property'],
            'Count': [2, 1]
        })

        mock_distribution_in_percentage.return_value = pd.DataFrame({
            'Category': ['Against Person', 'Against Public Property'],
            'Percentage': [66.67, 33.33]
        })

        process_and_save_data('input.csv', 'output.csv')

        mock_load_data.assert_called_once_with('input.csv')
        mock_call_counter.assert_called_once()
        mock_distribution_in_percentage.assert_called_once_with(mock_call_counter.return_value)
        mock_save_data.assert_called_once_with(mock_distribution_in_percentage.return_value, 'output.csv')


    # The following cases deal with possible errors.

    @patch("pandas.read_csv")
    def test_load_data_with_empty_file(self, mock_read_csv):
        """
        Test load_data with an empty file.
        """

        mock_read_csv.return_value = pd.DataFrame(columns=['recordId', 'district', 'description'])
        df = load_data("empty_file.csv")
        self.assertTrue(df.empty)

    def test_call_counter_empty_dataframe(self):
        """
        Test call_counter with an empty DataFrame.
        """

        empty_df = pd.DataFrame(columns=['district', 'description'])
        result = call_counter(empty_df)
        self.assertTrue(result.empty) 

    def test_distribution_in_percentage_empty_dataframe(self):
        """
        Test distribution_in_percentage with an empty DataFrame.
        """

        empty_df = pd.DataFrame(columns=['district', 'category', 'call_count'])
        result = distribution_in_percentage(empty_df)
        self.assertTrue(result.empty) 

    def test_distribution_in_percentage_no_calls(self):
        """
        Test distribution_in_percentage when all call counts are zero.
        """

        df = pd.DataFrame({
            'district': ['D1', 'D1', 'D2'],
            'category': ['Against Person', 'Against Public Property', 'Against Public Welfare'],
            'call_count': [0, 0, 0]
        })
        result = distribution_in_percentage(df)
        self.assertTrue(result['percentage'].isnull().all()) 


    @patch('calls_by_category.load_data')
    def test_process_and_save_data_load_error(self, mock_load_data):
        """
        Test process_and_save_data when load_data raises an error.
        """

        mock_load_data.side_effect = FileNotFoundError("File not found.")
        output_filepath = "output.csv"

        with self.assertRaises(FileNotFoundError):
            process_and_save_data("dummy_path.csv", output_filepath)


if __name__ == '__main__':
    unittest.main()