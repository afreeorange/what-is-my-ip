A super-simple Python 3 service that tells me what my IP address is. Will look for a header called `X-Real-IP` if the client IP is found to be `127.0.0.1` (helps if behind something like Nginx.)

Usage
-----

    python serve.py
    python serve.py <port>

[On my server](https://nikhil.io/ip),

    nohup python serve.py >> /dev/null 2>&1 &
