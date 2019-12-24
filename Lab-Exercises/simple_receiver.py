from flask import Flask, request
from pprint import pprint 

#Initialize the Flask app
app = Flask(__name__)

@app.route('/<path:path>', methods = ['POST'])
def collect(path):
    try:
        fh = open('/tmp/nxos.log', 'a')
        fh.write(request.data)
        pprint(request.data)
        fh.write('\n\n')
    except KeyboardInterrupt:
        fh.close()
    return ''

# Entry point to the Application
if __name__ == '__main__':
    with open('/tmp/nxos.log', 'w') as fh:
        fh.write('Initializing log...\n\n')

    app.run(host='0.0.0.0', port=50000, debug=True)
