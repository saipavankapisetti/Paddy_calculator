from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num_bags = int(request.form['num_bags'])
        bag_weight = float(request.form['bag_weight'])
        price_per_bag = float(request.form['price_per_bag'])

        total_weight_kg = (num_bags * bag_weight) / 75.0
        total_amount = price_per_bag * total_weight_kg

        response = jsonify({'total_weight_kg': total_weight_kg, 'total_amount': total_amount})
        response.headers['Content-Type'] = 'application/json'
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

