from flask import Flask, request, redirect, render_template
import redis
import os

app = Flask(__name__)
r = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    decode_responses=True
)

@app.route('/')
def index()
    names = r.lrange('names', 0, -1)
    return render_template('index.html', names=names)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name', '').strip()
    if name:
        r.rpush('names', name)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1)