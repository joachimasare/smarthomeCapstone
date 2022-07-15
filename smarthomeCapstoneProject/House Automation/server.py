from bottle import Bottle, run, request, response
import simplejson as json

app = Bottle()

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.get('/ajax/')
def ajax_handler():
    function_name = request.query["function"]

    # Logic for controlling things
    print(function_name)

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({"success": True})

run(app, host='localhost', port=8080, debug=True)
