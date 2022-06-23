'''
created by : dev.suhada@gmail.com
23 juni 2022

this simple code is used to upload image to s3 via api client, method POST, body field is image, type file. 
'''

from s3 import S3Client
from flask import Flask, jsonify, request

s3Client = S3Client()
app = Flask(__name__)


@app.route("/image", methods=["POST"])
def upload():
    file = request.files["image"]
    return jsonify(s3Client.upload(file))


if __name__ == "__main__":
    app.run(debug=True)
