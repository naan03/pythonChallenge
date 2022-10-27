import numbers
import os
import numpy as np
import random
import string
import pandas as pd
import time
import argparse
import json
from json_minify import json_minify


class Generator:
    """File generator.
    Attributes:
        rows: The number of lines in the file to be generated.
        output_path: Output path if the file.
        column_data: a list of tuples containing name, type definitions for the row.
                     The type of the argument can be `integer` or `string`.
                     E.g column_data = [(column_name, column_type),...]
    """

    def __init__(self, rows, output_path, column_data):
        if isinstance(rows, numbers.Number):
            self.rows = rows
        else:
            raise ValueError("The rows of data file must be a number!")

        if output_path is None:
            self.output_path = os.getcwd()
        else:
            self.output_path = output_path

        if column_data is None:
            raise ValueError("Data cannot be Null!")
        elif isinstance(column_data, list):
            istuple = True
            for data in column_data:
                if not isinstance(data, tuple):
                    istuple = False
            if istuple:
                self.column_data = column_data
            else:
                raise TypeError(
                    "The argument should be a list of tuples containing name, type definitions for the row! "
                    "E.g column_data = [(column_name, column_type),...]"
                )
        else:
            raise TypeError(
                "The argument should be a list of tuples containing name, type definitions for the row! "
                "E.g column_data = [(column_name, column_type),...]"
            )

    def generate_file(self):
        pass


class CsvGenerator(Generator):
    """A CSV file generator.
        Generate a CSV file with the specified number of lines."""

    def __init__(self, rows=50, output_path=None, column_data=None):
        super().__init__(rows, output_path, column_data)

    def generate_file(self):
        """Generate a CSV file.
        """
        column_data = self.column_data
        column_names = [elem[0] for elem in column_data]
        column_types = [elem[1] for elem in column_data]

        datas = []
        for type in column_types:
            if type.lower() == "integer":
                data = np.random.randint(100000, size=self.rows)
            elif type.lower() == "string":
                data = []
                for i in range(self.rows):
                    str = "".join(random.sample(string.ascii_letters, 10))
                    data.append(str)
            else:
                raise TypeError(f"The tpye {type} is unsupported data tpye!")
            datas.append(data)
        datas = [[r[col] for r in datas] for col in range(len(datas[0]))]
        dataframe = pd.DataFrame(datas, columns=column_names)

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        filename = (time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())) + ".csv"
        dataframe.to_csv(os.path.join(self.output_path, filename), index=False)


if __name__ == "__main__":
    # Parse Inputs
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-o", "--outputs_path", default="../outputs", help="path of results file"
    )
    ap.add_argument("-r", "--rows_of_file", default=10, help="rows of data file")
    ap.add_argument(
        "-c",
        "--conf",
        default="../config.json",
        help="path to the input configuration file",
    )
    args = vars(ap.parse_args())

    output_path = args["outputs_path"]
    rows = args["rows_of_file"]
    conf_file = os.path.normpath(args["conf"])

    try:
        conf = json.loads(json_minify(open(conf_file).read()))
    except:
        raise Exception(f"Unable to load configuration file {conf_file}")
    column_data = conf["column_data"].split(",")
    column_data = [(item.split(":")[0], item.split(":")[1]) for item in column_data]

    g = CsvGenerator(rows=rows, output_path=output_path, column_data=column_data)
    g.generate_file()
