from src.settings import HOST, PORT

bind = f"0.0.0.0:7000"
workers = 2
worker_connections = 1000
max_requests = int(workers * worker_connections)
keepalive = 2
max_requests_jitter = 5
timeout = 40

