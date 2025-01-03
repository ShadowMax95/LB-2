from bottle import route, run
@route('/')
def hello():
    response = "<html><body><h1><i>Hello world!</i></h1></body></html>"
    return response

if __name__ == '__main__':
    run(host='localhost', port=8000)
