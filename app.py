from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Root endpoint that returns a simple hello world message"""
    return jsonify({
        'message': 'Hello, World!',
        'status': 'success'
    })
    
@app.route('/test')
def test_endpoint():
    """Test endpoint that returns a simple test message"""
    return jsonify({
        'message': 'This is a test endpoint',
        'status': 'success'
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Flask Hello World API'
    })


@app.route('/danger')
def run_dangerous_command():
    """
    Intentionally insecure endpoint for testing CodeQL.
    It executes a shell command based on untrusted user input.
    DO NOT USE THIS IN PRODUCTION.
    """
    cmd = request.args.get('cmd', '')
    # This is vulnerable to command injection and should be flagged by CodeQL
    os.system(cmd)
    return jsonify({
        'status': 'executed',
        'command': cmd
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

