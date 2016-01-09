from bottle import route, run, template, debug

@route('/hello/<param>')
def index(param):
    return template('<b>Hello {{name}}</b>!', name=param)

@route('/pizza/<param1>/<param2>')
def index(param1,param2):
    return template('<b>your pizza order with base {{name1}} and topping {{name2}} is ready to pick up </b>!', name1=param1,name2=param2)

@route('/')
def index_page():
    return 'This is index page \n '


@route('/test')
def test_page():
    return 'This is a hot test page'

debug(True)
run(host='localhost', port=8081)




