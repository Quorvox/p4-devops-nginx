# -*- coding: utf-8 -*-
# проверка что nginx и api отвечают (для compose: export BASE=http://localhost:8080)
import os
import urllib.request

base = os.environ.get("BASE", "http://localhost:8080")
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # мимо проксей

for path in ("/api/health", "/"):
    with opener.open(base + path, timeout=5) as r:
        body = r.read().decode("utf-8")
        print(path, r.status, dict(r.headers).get("X-Served-By", "-"), body[:80])
        assert r.status == 200
print("checks ok")
