A super-simple Python 3 service that tells me what my IP address is. Will look for a header called `X-Real-IP` if the client IP is found to be `127.0.0.1` (helps if behind something like Nginx.)

If `?full` or `?f` is specified as a query string, will attempt to look up the [freegeoip](https://freegeoip.net) service for GeoIP data.

Usage
-----

    python serve.py
    python serve.py <port>

<kbd>CTRL</kbd>+<kbd>c</kbd> to kill. Here's how I run this [on my server](https://nikhil.io/ip),

    nohup python serve.py >> /dev/null 2>&1 &

So to query, I simply

```bash
# Basic info
curl https://nikhil.io/ip

# GeoIP info
curl https://nikhil.io/ip?f
curl https://nikhil.io/ip?full
```
