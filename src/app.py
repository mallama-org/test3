import datetime
import logging
import socket

from flask import Flask, jsonify, request


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.before_request
def log_request():
    logger.info("request %s %s", request.method, request.path)


@app.route("/")
def root():
    return jsonify({"status": "ok", "message": "python-app root"})


@app.route('/api/v1/info')
def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You can do it! >:)',
        'deployed_on': 'ArgoCD!',
        'env': 'dev'
        

    })

@app.route('/api/v1/healthz')
def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")

