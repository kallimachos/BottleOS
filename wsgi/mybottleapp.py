from bottle import route, default_app, template

# -------------------------------------------------------------------------------------
# This must be added in order to do correct path lookups for templates in wsgi/views/
import os
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
    'wsgi/views/'))
# -------------------------------------------------------------------------------------

@route('/')
def index():
    return '<strong>Hello World!</strong>'

# example route using a template
@route('/hello/<name>')
def index(name):
    return template('hello_name', name=name)

# route for printing debug information
@route('/debug')
def index():
    return template('<b>TEMPLATE_PATH = {{info}}', info=TEMPLATE_PATH)

application=default_app()