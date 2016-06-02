import os
from flask import Flask

import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
if 'FLASK_DEBUG' in os.environ:
    app.debug = True

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/api/v1/items')
def Initialize():
    print 'this is a test';
    return app.send_static_file('jake.html')

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
