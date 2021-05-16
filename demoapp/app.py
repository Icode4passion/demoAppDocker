from flask import Flask 
from redis import Redis 

app = Flask(__name__)
redis = Redis(host='redis' , port = 6379)



@app.route("/")
def index():
    count = redis.incr('hits')
    return "<h3>Hello World .. You liked this page {} this many times..</h3>".format(count)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8000)

