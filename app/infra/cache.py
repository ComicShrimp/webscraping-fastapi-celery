import json

import redis

# TODO: adicionar .env
EXPIRATION = 43200


def connect_redis():
    # TODO: usar .env
    return redis.Redis(host="cache", port=6379)


class Cache:
    def __init__(self):
        self.conn = connect_redis()

    def save_metrics(self, metrics):
        self.conn.set("metrics", json.dumps(metrics), ex=EXPIRATION)

    def get_metrics(self):
        resultado = self.conn.get("metrics")
        if resultado is None:
            return False  # Cache Miss

        return json.loads(resultado.decode("utf-8"))
