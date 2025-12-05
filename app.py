from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Root endpoint that returns a simple hello world message"""
    return jsonify({
        'message': 'Hello, World! v0.0.3',
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

