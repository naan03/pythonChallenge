import unittest

from task1.gen import CsvGenerator

class TestCsvGenerator(unittest.TestCase):

    def test_pass(self):
        #Manually check if the file exists
        rows = 10
        output_path = "outputs"
        g = CsvGenerator(rows=rows, output_path=output_path,
                         column_data=[("int_data", "integer"), ("string_data", "string")])
        g.generate_file()

    def test_not_specify_rows(self):
        #Manually check if the file is 50 lines
        output_path = "outputs"
        g = CsvGenerator(output_path=output_path,
                         column_data=[("int_data", "integer"), ("string_data", "string")])
        g.generate_file()

    def test_not_specify_output_path(self):
        #Manually check if the file exists
        rows = 10
        g = CsvGenerator(rows=rows,
                         column_data=[("int_data", "integer"), ("string_data", "string")])
        g.generate_file()

if __name__ == '__main__':
    unittest.main()
