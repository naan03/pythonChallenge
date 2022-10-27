from flask import Flask, jsonify, abort, request
import json
import os
import time
import pandas as pd
from json_minify import json_minify
from concurrent.futures import ThreadPoolExecutor

# from db import DbConnection
# from models import DataFile
executor = ThreadPoolExecutor(10)
app = Flask(__name__)


def write2csv(iter):
    datachuck, output_file = [iter[0]], iter[1]
    print(f"datachuck = {datachuck}")
    print(f"output_file = {output_file}")
    column_names = ["datacol1"]

    header = False
    if not os.path.exists(output_file):
        header = True

    try:
        dataframe = pd.DataFrame(datachuck, columns=column_names)
        dataframe.to_csv(
            output_file, index=False, mode="a", header=header, encoding="utf-8",
        )
    except Exception as e:
        print(e)

    print("delay task done")


# @app.route('/file/<filename>', methods=['GET'])
# def get_file(filename):
#     try:
#         session = DbConnection.get_db_connection()
#         file = DataFile.get_by_filename(session,filename)
#     except Exception as e:
#         print(e)
#
#     if file is not None:
#         file_data = file.file_data
#         return jsonify({'tasks': file_data})
#     else:
#         abort(404)

filedata = [
    {"id": 1, "string1": "Cheese", "string2": "Pizza"},
    {"id": 2, "string1": "Apple", "string2": "Banana"},
]


@app.route("/file", methods=["GET"])
def get_file():
    return jsonify({"file data": filedata})


@app.route("/file", methods=["POST"])
def create_file():
    #
    file_data = request.args.get("file_data")

    try:
        conf = json.loads(json_minify(open("../config.json").read()))
    except:
        raise Exception(f"Unable to load configuration file.")
    chunk_size = int(conf["chuck_size"])

    data_chucks = []
    if len(file_data) < chunk_size:
        data_chucks.append(filedata)
    else:
        i = 0
        for i, _ in enumerate(file_data):
            if i % chunk_size == 0:
                data_chucks.append(file_data[i : i + chunk_size])
            i += chunk_size

    output_path = "../outputs"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    filename = (time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())) + ".csv"
    output_file = os.path.join(output_path, filename)

    # with ThreadPoolExecutor(max_workers=len(data_chucks)) as e:
    #     for i in range(len(data_chucks)):
    #         e.submit(write2csv,data_chucks[i],output_file)

    iter = [[d, output_file] for d in data_chucks]
    executor.map(write2csv, iter)

    return {"code": 200, "msg": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
