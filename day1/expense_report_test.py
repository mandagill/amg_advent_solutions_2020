import unittest

from expense_report import ExpenseReport


class HelperFunctions():

    def get_test_data(self):
        """helper function to streamline test data input"""
        with open("/Users/amg/src/advent_of_code_2020/day1/input.txt") as f:
            entries = f.read()
        print(dir(entries))
        return entries


class ExpenseReportTest(unittest.TestCase):

    def test_six_item_list(self):

        small_input = """1721
          979
          366
          299
          675
          1456"""
        er = ExpenseReport(small_input)
        result = er.get_two_adding_to_2020()

        self.assertEqual(result, [1721, 299])

    def test_full_list(self):

        hf = HelperFunctions()
        entries = hf.get_test_data()
        er = ExpenseReport(entries=entries)
        array_to_add = er.get_two_adding_to_2020()

        result = array_to_add[0] + array_to_add[1]
        self.assertEqual(result, 2020)

    def test_product_returned(self):
        hf = HelperFunctions()
        entries = hf.get_test_data()

        er = ExpenseReport(entries=entries)
        result = er.find_product_of_entries()

        self.assertGreater(result, 2020)


if __name__ == '__main__':
    unittest.main()
