from flask import Flask, render_template, send_from_directory, url_for
from flask_s3 import FlaskS3

app = Flask(__name__)

#Set the S3 bucket name for the site's static resources
app.config['FLASKS3_BUCKET_NAME'] = 'com-jaygreco-zappa'

#NOTE: This is needed in order to force Flask-S3 to set the MIME type during upload.
#Without this line, CSS on S3 will not be served because of modern browser security.
app.config['FLASKS3_FORCE_MIMETYPE'] = True

#Instantiate flask-s3 to handle static resources
s3 = FlaskS3(app)

#The one and only route
@app.route('/')
def index():
    return render_template('index.html')

#This is only needed for local development.
if __name__ == '__main__':
    app.run(debug=True) 