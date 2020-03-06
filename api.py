from flask import request,Flask,jsonify
import analysis

result={
    'query':'',
    'mode' : '',
    'positivity': 0
}

app=Flask(__name__)
@app.route('/searchByUser', methods=['GET']) 
def userAnalysis():
    if('id' in request.args):
        id=request.args['id']
        res=analysis.fetchTweetsByUser(id)
        result['query']=id
        result['mode']='User'
        result['positivity']=res
        return jsonify(result)
    else:
        return '400: BAD REQUEST'

@app.route('/searchByHash', methods=['GET'])
def hashanalysis():
    if('id' in request.args):
        id=request.args['id']
        res=analysis.fetchTweetsByHash(id)
        result['query']=id
        result['mode']='Hash'
        result['positivity']=res
        return jsonify(result)
    else:
        return '400: BAD REQUEST'

app.run()
