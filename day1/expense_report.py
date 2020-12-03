from os import environ


class ExpenseReport:

    def __init__(self, entries):
        self.entries = entries

    def convert_entries_to_arrays(self):
        expense_list = []
        print(type(self.entries))
        iterable_entries = self.entries.split("\n")
        for line in iterable_entries:
            # print(f"this is the line's type: {type(line)}")

            cleaned = line.strip()
            # print(f"this is the line int-ified: {int(cleaned)}")
            expense_list.append(int(cleaned))
        return expense_list

    def get_two_adding_to_2020(self):

        array_a = self.convert_entries_to_arrays()
        array_b = array_a.copy()

        for line_item_a in array_a:
            entry_a = int(line_item_a)
            index_b = 0
            for line_item_b in array_b:
                entry_b = int(line_item_b)
                print(f"entry a: {entry_a} and entry b: {entry_b}")
                if (entry_a + entry_b) == 2020:
                    print(f"""
                    these are the two entries you want: {entry_a} and {entry_b}
                    """)
                    return [entry_a, entry_b]
            index_b += 1

    def find_product_of_entries(self):
        array_to_multiply = self.get_two_adding_to_2020()
        return array_to_multiply[0] * array_to_multiply[1]


if __name__ == "__main__":
    with open(environ['INPUT_PATH']) as f:
        entries = f.read
    report = ExpenseReport(entries)
    report.find_product_of_entries()
