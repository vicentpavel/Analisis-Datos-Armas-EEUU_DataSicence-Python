import unittest
import pandas as pd
import data_processing as dp

class TestDataProcessing(unittest.TestCase):

    def test_read_csv(self):
        filepath = '/mnt/data/nics-firearm-background-checks.csv'
        df = dp.read_csv(filepath)
        self.assertGreater(len(df), 0)
        self.assertIn('month', df.columns)
        self.assertIn('state', df.columns)

    def test_clean_csv(self):
        data = {'month': ['2021-01'], 'state': ['AL'], 'permit': [100], 'handgun': [200], 'long_gun': [300], 'other': [50]}
        df = pd.DataFrame(data)
        cleaned_df = dp.clean_csv(df)
        self.assertEqual(set(cleaned_df.columns), {'month', 'state', 'permit', 'handgun', 'long_gun'})

    def test_rename_col(self):
        data = {'month': ['2021-01'], 'state': ['AL'], 'permit': [100], 'handgun': [200], 'longgun': [300]}
        df = pd.DataFrame(data)
        renamed_df = dp.rename_col(df)
        self.assertIn('long_gun', renamed_df.columns)
        self.assertNotIn('longgun', renamed_df.columns)

    def test_breakdown_date(self):
        data = {'month': ['2020-2'], 'state': ['AL'], 'permit': [100], 'handgun': [200], 'long_gun': [300]}
        df = pd.DataFrame(data)
        updated_df = dp.breakdown_date(df)
        self.assertIn('year', updated_df.columns)
        self.assertIn('month', updated_df.columns)
        self.assertEqual(updated_df.at[0, 'year'], 2020)
        self.assertEqual(updated_df.at[0, 'month'], 2)

    def test_erase_month(self):
        data = {'month': ['2020-2'], 'year': [2020], 'state': ['AL'], 'permit': [100], 'handgun': [200], 'long_gun': [300]}
        df = pd.DataFrame(data)
        updated_df = dp.erase_month(df)
        self.assertNotIn('month', updated_df.columns)
        self.assertIn('year', updated_df.columns)

    def test_groupby_state_and_year(self):
        data = {'year': [2020, 2020], 'state': ['AL', 'AL'], 'permit': [100, 150], 'handgun': [200, 300], 'long_gun': [300, 400]}
        df = pd.DataFrame(data)
        grouped_df = dp.groupby_state_and_year(df)
        self.assertIn('year', grouped_df.columns)
        self.assertIn('state', grouped_df.columns)
        self.assertEqual(grouped_df.at[0, 'permit'], 250)
        self.assertEqual(grouped_df.at[0, 'handgun'], 500)
        self.assertEqual(grouped_df.at[0, 'long_gun'], 700)

    def test_print_biggest_handguns(self):
        data = {'year': [2020, 2021], 'state': ['AL', 'CA'], 'handgun': [200, 300]}
        df = pd.DataFrame(data)
        dp.print_biggest_handguns(df)

    def test_print_biggest_longguns(self):
        data = {'year': [2020, 2021], 'state': ['AL', 'CA'], 'long_gun': [300, 400]}
        df = pd.DataFrame(data)
        dp.print_biggest_longguns(df)

    def test_time_evolution(self):
        data = {'year': [2020, 2021], 'state': ['AL', 'CA'], 'permit': [100, 150], 'handgun': [200, 300], 'long_gun': [300, 400]}
        df = pd.DataFrame(data)
        dp.time_evolution(df)  # Verifica que la función se ejecuta sin errores

    def test_groupby_state(self):
        data = {'year': [2020, 2021], 'state': ['AL', 'CA'], 'permit': [100, 150], 'handgun': [200, 300], 'long_gun': [300, 400]}
        df = pd.DataFrame(data)
        grouped_df = dp.groupby_state(df)
        self.assertIn('state', grouped_df.columns)
        self.assertEqual(len(grouped_df), 2)

   
