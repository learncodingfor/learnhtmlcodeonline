import gevent
from flask import copy_current_request_context

@app.route('/')
def index():
    @copy_current_request_context
    def do_some_work():
        # do some work here, it can access flask.request or
        # flask.session like you would otherwise in the view function.
        return "hi"
        ...
    gevent.spawn(do_some_work)
    return 'Regular response
    @app.route('/videos')
    def videos():
         return "hello"
