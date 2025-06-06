from flask import Flask, render_template, jsonify,request
from flask_cors import CORS
from config import config

app = Flask(__name__)

CORS(app)

@app.route('/api/test', methods=['GET'])
def test():
    return {'message': 'API funcionando!'}

@app.route('/api/testPost',methods=['POST'])
def testPost():
    data = request.get_json()
    return jsonify({
        'received': data,
        'status': 'success'
    })



if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()

