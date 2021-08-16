import json

import redis
from bs4 import BeautifulSoup
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI()


class PageVisit:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.browser = webdriver.Chrome(
            "/usr/src/app/webdriver/chromedriver", chrome_options=chrome_options
        )

    def get_html(self, url):
        self.browser.get(url)
        return self.browser.page_source


def get_metric_from_worldometers(rel):
    html = PageVisit().get_html("https://www.worldometers.info")

    bs = BeautifulSoup(html, "html.parser")

    parent = bs.find("span", {"rel": rel})
    numbers = parent.findChildren("span")

    # Provavelmente não é o melhor jeito de pegar esse valor numérico mas funciona
    # TODO: melhorar essa metodologia de criação do número
    metric_str = ""
    for number in numbers:
        try:
            if int(number.text) > 0:
                metric_str += number.text
        except:
            pass

    return int(metric_str)


def metrics_from_worldometers():
    return {
        "perda_de_floresta_este_ano": get_metric_from_worldometers(
            "forest_loss/this_year"
        ),
        "emissoes_co2_este_ano": get_metric_from_worldometers(
            "co2_emissions/this_year"
        ),
        "dias_para_acabar_o_petroleo": get_metric_from_worldometers("oil_reserves"),
        "populacao_sem_acesso_a_agua_potavel": get_metric_from_worldometers(
            "nowater_population"
        ),
        "desertificacao_em_toneladas_este_ano": get_metric_from_worldometers(
            "desert_land_formed/this_year"
        ),
    }


def connect_redis():
    # TODO: usar .env
    return redis.Redis(host="cache", port=6379)


EXPIRATION = 30


def save_in_cache(metrics):
    r = connect_redis()
    r.set("metrics", json.dumps(metrics), ex=EXPIRATION)


def get_cache():
    r = connect_redis()
    resultado = r.get("metrics")
    if resultado is None:
        return False  # Cache Miss

    resultado.decode("utf-8")
    return json.loads(resultado)


@app.get("/")
async def root():
    metrics_cache = get_cache()
    if not metrics_cache:
        worldometers = metrics_from_worldometers()
        metrics = {"worldometers": worldometers}
        save_in_cache(metrics)
        return metrics

    return metrics_cache
