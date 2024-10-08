from flask import Flask, request, jsonify
from utils import image_utils, color_matching
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

with open('sample_data.json') as f:
    sample = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    print(data)
    result = color_matching.find_shortest_distance(data['color'], sample)
    return jsonify({
        "image": result['swatch'],
        "name": result['name'],
        "hex": result['hex'],
        "brand": result['brand']
    }), 200

@app.route('/image', methods=['POST'])
def image_color_pallete():
    #print('hey image')
    file = request.files['image']
    print(file.filename)
    file.save(file.filename)
    print(request)
    number_of_colors = request.form['n_colors']
    #print(data)
    #json_file = request.load(json_data)
    #json_data = json.load(json_file)

    pallete = image_utils.pallette(file.filename, number_of_colors)
    print(pallete)
    for i in range(len(pallete)):
        LAB = color_matching.rgb2lab(pallete[i])
        print(LAB)
        print(color_matching.find_shortest_distance(LAB, sample))
    return str(pallete)

    print(json_data)