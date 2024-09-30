import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from calls_by_category import load_data, categorize_activity, call_counter, distribution_in_percentage, save_data, process_and_save_data

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

if __name__ == '__main__':
    unittest.main()