from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/health')
def health():
    return jsonify({'ok': True})
@app.route('/api/extract', methods=['POST'])
def extract():
    # expects multipart/form-data with file field 'invoice'
    # placeholder: return fixed structure
    return jsonify({
        'vendor': 'ACME Corp',
        'date': '2026-03-01',
        'total': '123.45',
        'line_items': [
            {'desc':'Service','qty':1,'price':'123.45'}
        ]
    })
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
