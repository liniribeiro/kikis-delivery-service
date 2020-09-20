from src.settings import HOST, PORT

bind = f'{HOST}:{PORT}'
workers = 2
worker_class = 'gevent'
max_requests = 300
keepalive = 20
