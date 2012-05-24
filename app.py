from flask import Flask, url_for, request, json, Response, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def api_root():
    return 'hacker coffee root'

@app.route('/coffeeshops', methods=['GET'])
def api_coffeeshops():
    return 'List of coffeeshops'

@app.route('/coffeeshops/<shopid>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_coffeeshop(shopid):
    print "inside /coffeeshops/..."
    if request.method == 'GET':
        return 'Viewing shop {0}'.format(shopid)
    elif request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            return 'Attempting to change coffeeshop {0}'.format(shopid)
        else:
            return '415 Unsupported media type'
    elif request.method == 'PUT':
        if request.headers['Content-Type'] == 'application/json':
            return 'Attempting to update coffeshop {0}'.format(shopid)
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
