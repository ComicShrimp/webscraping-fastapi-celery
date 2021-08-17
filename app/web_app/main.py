import json

import redis
from bs4 import BeautifulSoup
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Message-Code", "content-disposition"],
)


class WebBrowser:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.browser = webdriver.Chrome(
            "/usr/src/app/webdriver/chromedriver", chrome_options=chrome_options
        )

    def get_html_from_url(self, url):
        self.browser.get(url)
        return self.browser.page_source


class MetricsWorldometers:
    def __init__(self):
        html = WebBrowser().get_html_from_url("https://www.worldometers.info")
        self.bs = BeautifulSoup(html, "html.parser")

    def get_by_rel(self, rel):
        parent = self.bs.find("span", {"rel": rel})
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
    metrics_worldometers = MetricsWorldometers()

    return {
        "perda_de_floresta_este_ano": metrics_worldometers.get_by_rel(
            "forest_loss/this_year"
        ),
        "emissoes_co2_este_ano": metrics_worldometers.get_by_rel(
            "co2_emissions/this_year"
        ),
        "barris_de_petroleo_restante": metrics_worldometers.get_by_rel("oil_reserves"),
        "populacao_sem_acesso_a_agua_potavel": metrics_worldometers.get_by_rel(
            "nowater_population"
        ),
        "desertificacao_este_ano": metrics_worldometers.get_by_rel(
            "desert_land_formed/this_year"
        ),
        "quimicos_liberados": metrics_worldometers.get_by_rel(
            "tox_chem/this_year"
        ),

        # Água
        "consumo_agua_este_ano": metrics_worldometers.get_by_rel(
            "water_consumed/this_year"
        ),
        "mortes_doencas_agua_este_ano": metrics_worldometers.get_by_rel(
            "water_disax/this_year"
        ),
        "populacao_sem_acesso_a_agua_potavel": metrics_worldometers.get_by_rel(
            "nowater_population"
        ),
        
        
        
    }


def connect_redis():
    # TODO: usar .env
    return redis.Redis(host="cache", port=6379)


# TODO: aumentar expiração
EXPIRATION = 30


def save_in_cache(metrics):
    r = connect_redis()
    r.set("metrics", json.dumps(metrics), ex=EXPIRATION)


def get_cache():
    r = connect_redis()
    resultado = r.get("metrics")
    if resultado is None:
        return False  # Cache Miss

    return json.loads(resultado.decode("utf-8"))


@app.get("/")
async def root():
    metrics_cache = get_cache()
    if not metrics_cache:
        worldometers = metrics_from_worldometers()
        metrics = {"worldometers": worldometers}
        save_in_cache(metrics)
        return metrics

    return metrics_cache
