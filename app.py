# encoding=utf-8

import os
import datetime
from uuid import uuid4

from flask import Flask, request
from boto import connect_s3
from boto.s3.key import Key

s3 = connect_s3()
bucket = s3.get_bucket(os.environ['S3_BUCKET'])
hostname = os.environ.get('S3_CNAME', bucket.name + ".s3.amazonaws.com")

headers = {'Content-Type': 'image/png'}

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get("DEBUG") == "true"


@app.route('/')
def index():
    return ''


@app.route('/', methods=['POST'])
def receiver():
    key = Key(bucket)
    key.key = 'scrn/{}/{}.png'.format(datetime.date.today().year, uuid4().hex)
    key.set_contents_from_string(
        request.data, headers=headers, policy="public-read")
    return 'http://{}/{}'.format(hostname, key.key)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ['PORT']))
