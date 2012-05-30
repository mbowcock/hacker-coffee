import psycopg2
import config
from flask import Flask, url_for, request, json, Response, jsonify, g

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(database=config.database, user=config.username, password=config.password)

@app.before_request
def before_request():
    g.db = connect_db()
    g.cur = g.db.cursor()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'cur'):
        g.cur.close()
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/', methods=['GET'])
def api_root():
    return 'hacker coffee root'

@app.route('/coffeeshops', methods=['GET', 'POST'])
def api_coffeeshops():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            # write post data to database
            data = request.json
            g.cur.execute(
                    """insert into coffeeshops (name, address, city, state, zip, description) 
                    values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(
                        data["name"], 
                        data["address"], 
                        data["city"],
                        data["state"],
                        data["zip"],
                        data["description"]))
            g.db.commit()
            return 'coffeeshop added'
        else:
            return '415 Unsupported media type'
    elif request.method == 'GET':
        g.cur.execute("select name, address, city, state, zip, description from coffeeshops")
        rows = [dict((g.cur.description[i][0], value) for i, value in enumerate(row)) for row in g.cur.fetchall()]
        resp = Response(json.dumps(rows), status=200, mimetype='application/json')
        return resp
    else:
        return 'Method not supported'

@app.route('/coffeeshops/<shopid>', methods=['GET', 'POST', 'DELETE'])
def api_coffeeshop(shopid):
    if request.method == 'GET':
        return 'Viewing shop {0}'.format(shopid)
    elif request.method == 'POST':
        if request.header['Content-Type'] == 'application/json':
            return 'updating coffeeshop {0}'.format(shopid)
        else:
            return '415 Unsupported media type'
    elif request.method == 'DELETE':
        return 'Deleting coffeeshop {0}'.format(shopid)
    else:
        return 'method not supported'

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404, 
            'message': 'Not Found: {0}'.format(request.url)
            }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
