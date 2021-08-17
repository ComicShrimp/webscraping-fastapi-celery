from bs4 import BeautifulSoup

from app.infra import WebBrowser


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


def get_metrics_worldometers():
    metrics_worldometers = MetricsWorldometers()

    # TODO: usar pydantic
    return {

        # Ambiente
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
        "quimicos_liberados": metrics_worldometers.get_by_rel("tox_chem/this_year"),
        
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

        # Energia
        "dias_para_acabar_gas": metrics_worldometers.get_by_rel(
            "gas_days"
        ),
        "dias_para_acabar_carvao": metrics_worldometers.get_by_rel(
            "coal_days"
        ),
    }
