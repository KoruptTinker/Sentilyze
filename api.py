import flask
import jsonify
app=flask.Flask(__name__)
@app.route("/user/",methods=['GET'])
def 