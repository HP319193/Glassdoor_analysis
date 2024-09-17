from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
import os
import pandas as pd

app = Flask(__name__)

# Create a folder to store uploaded files if it doesn't exist
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

def substr_check(target_string, substrings):
    try:
        return any(substring in target_string for substring in substrings)
    except:
        return False
@app.route('/upload', methods=['POST', 'GET'])
def upload_files():
    if request.method == "POST":
        if 'csvFile' not in request.files or 'jsonFile' not in request.files:
            return jsonify({"error": "No file part"}), 400

        csv_file = request.files['csvFile']
        json_file = request.files['jsonFile']

        if csv_file.filename != '':
            csv_path = os.path.join(UPLOAD_FOLDER, csv_file.filename)
            csv_file.save(csv_path)

        if json_file.filename != '':
            json_path = os.path.join(UPLOAD_FOLDER, json_file.filename)
            json_file.save(json_path)

        reviews = pd.read_csv(csv_path)

        with open(json_path, 'r') as f:
            standards = json.load(f)
        
        res_data = {}
        for index, row in reviews.iterrows():
            isin = row['ISIN']
            
            if isin not in res_data:
                res_data[isin] = {}
                for key, value in standards.items():
                    res_data[isin]['reviews'] = 0
                    res_data[isin][key] = 0

            res_data[isin]['reviews'] += 1
            pros = row['pros']
            cons = row['cons']

            for key, value in standards.items():
                if substr_check(pros, value[0]):
                    res_data[isin][key] += 1
                if substr_check(cons, value[0]):
                    res_data[isin][key] += 1
                if substr_check(pros, value[1]):
                    res_data[isin][key] -= 1
                if substr_check(cons, value[1]):
                    res_data[isin][key] -= 1

        dim_data = {}
        for key, value in standards.items():
            dim_data[key] = 0
        
        for isin, isin_val in res_data.items():
            for key, value in isin_val.items():
                if key != "reviews":
                    dim_data[key] += value
        
        for key, value in dim_data.items():
            value /= len(dim_data)
        
        with open('result/data.json', 'w') as json_file:
            json.dump(res_data, json_file, indent=4)
        
        with open('result/dim.json', 'w') as json_file:
            json.dump(dim_data, json_file, indent=4)

        isin_list = list(res_data.keys())
        return render_template('graph.html', isin_list = isin_list)

    if request.method == "GET":
        with open('result/data.json', 'r') as file:
            data = json.load(file)
        isin_list = list(data.keys())
        
        return render_template('graph.html', isin_list = isin_list)
    
@app.route('/getValue', methods=['POST'])
def getValue():
    isin_num = request.get_json().get("ISIN")

    with open('result/data.json', 'r') as file:
        data = json.load(file)

    with open('result/dim.json', 'r') as file:
        dim = json.load(file)

    tableData = []
    for key, value in dim.items():
        tableData.append({"dim": key, "val": data[isin_num][key], "avg": dim[key]/len(data)})

    chartData = {}
    keys_view = dim.keys()
    labels = list(keys_view)

    values1 = []
    values2 = []
    for key, value in dim.items():
        values1.append(data[isin_num][key])
        values2.append(dim[key]/len(data))
    
    chartData['labels'] = labels
    chartData['values1'] = values1
    chartData['values2'] =values2

    return jsonify({'tableData': tableData, "chartData": chartData})
if __name__ == '__main__':
    app.run(debug=True)
