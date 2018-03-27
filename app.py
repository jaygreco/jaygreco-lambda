from flask import Flask, render_template, send_from_directory
app = Flask(__name__,  static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    print path
    return send_from_directory('static', path)

# We only need this for local development.
if __name__ == '__main__':
    app.run(debug=True)