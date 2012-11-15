Scrup S3
========

A simple server to receive [Scrup](https://github.com/rsms/scrup) screenshots, 
upload to S3 and return a public viewable URL to the image.

+ Ready for Heroku
+ Minimal code, easy to understand and customize

Setup
-----

1. Clone and `cd scrup-s3`
2. `$ virtualenv venv`
3. `$ heroku create scrup-xxxx`
4. `$ touch .env`

Sample `.env`

    AWS_ACCESS_KEY_ID=...
    AWS_SECRET_ACCESS_KEY=...
    PORT=8000
    S3_BUCKET=s3.solberg.is
    S3_CNAME=s3.solberg.is

You can omit the `S3_CNAME` if you haven’t set one up.

Test
----

    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ foreman start

Point your current scrup to localhost:8000 and try Ctrl+Shift+4-ing something.

Deploy
------

    $ heroku config:push
    $ git push heroku master
