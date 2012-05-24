from flask import Flask, url_for, request
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
        return 'Attempting to change coffeeshop {0}'.format(shopid)
    elif request.method == 'PUT':
        return 'Attempting to update coffeshop {0}'.format(shopid)
    elif request.method == 'DELETE':
        return 'Deleting coffeeshop {0}'.format(shopid)
    else:
        return 'method not supported'

if __name__ == '__main__':
    app.debug = True
    app.run()
