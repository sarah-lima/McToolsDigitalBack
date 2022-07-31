from crypt import methods
from flask import Flask, redirect, url_for, request as req
from flask_cors import CORS
from request_data import get
import controller.bcb_data
# controller.bcb_data.get_data(init_data='10/09/2000', terminal_data='10/09/2001', file_type='JSON')

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_data():
    return get()


@app.route("/create", methods=["POST"])
def create_data():
    return controller.bcb_data.create_data()


@app.route('/', methods=["POST"])
def get_data_interval():
    args = req.args
    print(args)
    controller.bcb_data.get_data(args.get("init_data"), args.get("terminal_data"), args.get("file_type"))
    return redirect(url_for('static', filename='data_bcb.json' if args.get("file_type")=='JSON' else 'data_bcb.xlsx'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


