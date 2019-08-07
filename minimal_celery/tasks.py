from celery import Celery
import time

app = Celery('tasks', broker='amqp://localhost//', backend='rpc://localhost//')

#app.conf.broker_heartbeat = 0


@app.task
def add(x, y):
    time.sleep(5)
    return x + y

@app.task
def reverse(word):
    time.sleep(10)
    return word[::-1]
