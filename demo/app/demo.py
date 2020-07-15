from flask import Flask
import os, socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
hostname = socket.gethostname()

@app.route('/')
def index():
  return 'Hello, from sunny %s!\n' % hostname


if __name__ == '__main__':
  app.run()
