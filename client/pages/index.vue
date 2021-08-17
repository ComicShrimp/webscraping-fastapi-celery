<template>
  <div class="content">
    <div class="inicio">
      <img id="logo" src="../assets/Logo.svg" alt="World Dashboard logo" />
      <h1>Bem-vindo(a) ao World Dashboard !</h1>
      <p>Este site destina-se à agregar várias informações sobre o meio metricas</p>
      <div id="footer-incio">
        <b-icon
          id="arrow-down-icon"
          icon="arrow-down-circle"
          animation="cylon-vertical"
          @click="scrollToRef('metricas')"
        ></b-icon>
      </div>
    </div>
    <div class="cards">
      <section ref="metricas" id="metricas">
        <h2 id="card-group-title">Métricas</h2>
        <b-card-group deck>
          <b-card id="agua_usada" header="Água Usada" border-variant="dark">
            <b-card-title
              ><b-icon icon="droplet-half"></b-icon>
              {{ consumo_agua_este_ano.toLocaleString("pt-BR") }} Milhões de Litros</b-card-title
            >
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card id="agua_potavel" header="Água potável" border-variant="dark">
            <b-card-title
              ><b-icon icon="droplet"></b-icon>
              {{ populacao_sem_acesso_a_agua_potavel.toLocaleString("pt-BR") }} pessoas</b-card-title
            >
            <b-card-text>sem acesso</b-card-text>
          </b-card>
          <b-card id="doencas" header="Doenças causadas pela água" border-variant="dark">
            <b-card-title
              ><b-icon icon="emoji-frown"></b-icon>
              {{ mortes_doencas_agua_este_ano.toLocaleString("pt-BR") }} mortes</b-card-title
            >
            <b-card-text>este ano</b-card-text>
          </b-card>
        </b-card-group>
        <b-card-group deck>
          <b-card id="florestas" header="Florestas perdidas" border-variant="dark">
            <b-card-title
              ><b-icon icon="tree"></b-icon>
              {{ perda_floresta_este_ano.toLocaleString("pt-BR") }} hectares</b-card-title
            >
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card id="co2" header="CO2 Emitido" border-variant="dark">
            <b-card-title
              ><b-icon icon="cloud"></b-icon>
              {{ emissoes_co2_este_ano.toLocaleString("pt-BR") }} toneladas</b-card-title
            >
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card id="quimicos" header="Quimicos" border-variant="dark">
            <b-card-title
              ><b-icon icon="exclamation-triangle"></b-icon>
              {{ quimicos_liberados.toLocaleString("pt-BR") }} Toneladas</b-card-title
            >
            <b-card-text>liberados no metricas</b-card-text>
          </b-card>
        </b-card-group>

        <b-card-group deck>
          <b-card id="gas_natural" header="Gás Natural" border-variant="dark">
            <b-card-title
              ><b-icon icon="cloud-fill"></b-icon>
              {{ dias_para_acabar_gas.toLocaleString("pt-BR") }} dias</b-card-title
            >
            <b-card-text>para acabar</b-card-text>
          </b-card>
          <b-card id="carvao" header="Carvão" border-variant="dark">
            <b-card-title
              ><b-icon icon="diamond-fill"></b-icon>
              {{ dias_para_acabar_carvao.toLocaleString("pt-BR") }} dias</b-card-title
            >
            <b-card-text>para acabar</b-card-text>
          </b-card>
          <b-card id="petroleo" header="Petroleo" border-variant="dark">
            <b-card-title
              ><b-icon icon="server"></b-icon>
              {{ barris_de_petroleo_restante.toLocaleString("pt-BR") }} barris</b-card-title
            >
            <b-card-text>para acabar</b-card-text>
          </b-card>
        </b-card-group>
      </section>
    </div>
  </div>
</template>

<script lang="js">
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

export default {
    data(){
        return {
            perda_floresta_este_ano: 0,
            emissoes_co2_este_ano: 0,
            barris_de_petroleo_restante: 0,
            quimicos_liberados: 0,
            // Água
            consumo_agua_este_ano: 0,
            mortes_doencas_agua_este_ano: 0,
            populacao_sem_acesso_a_agua_potavel: 0,
            dias_para_acabar_gas: 0,
            dias_para_acabar_carvao: 0,
        }
    },
    mounted() {
        this.$axios.get("http://localhost:8585").then((response) => {

            this.perda_floresta_este_ano = response.data.worldometers.perda_de_floresta_este_ano;
            this.emissoes_co2_este_ano = response.data.worldometers.emissoes_co2_este_ano;
            this.barris_de_petroleo_restante = response.data.worldometers.barris_de_petroleo_restante;
            this.quimicos_liberados = response.data.worldometers.quimicos_liberados;

            // Água
            this.consumo_agua_este_ano = response.data.worldometers.consumo_agua_este_ano;
            this.mortes_doencas_agua_este_ano = response.data.worldometers.mortes_doencas_agua_este_ano;
            this.populacao_sem_acesso_a_agua_potavel = response.data.worldometers.populacao_sem_acesso_a_agua_potavel;

            // Energia
            this.dias_para_acabar_gas = response.data.worldometers.dias_para_acabar_gas;
            this.dias_para_acabar_carvao = response.data.worldometers.dias_para_acabar_carvao;

        }).catch((error) => {
            console.log(error);
        });
    },
    methods: {
      scrollToRef(ref) {

        const elemento = this.$refs[ref];

        if(elemento) {
          elemento.scrollIntoView({behavior: 'smooth'});
        }

      }
    }

}
</script>

<style>
.cards {
  align-items: center;
  margin: 2% 5% 5% 5%;
  justify-content: center;
}

.inicio {
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100vh;
  margin: 10vh 0 0 0;
}

.titulo {
  text-align: center;
}

#logo {
  width: 25vw;
  margin: 0 0 10vh 0;
}

#arrow-down-icon {
  height: 4vh;
  width: 4vw;
}

#footer-incio {
  margin-top: 12vh;
}

#card-group-title {
  text-align: center;
  margin: 5vh 0vw 5vh 0vw;
}

.less-cards {
  align-items: center;
  justify-content: center;
}

.card {
  margin: 2%;
  color: #1d3557;
}

#metricas {
  height: 80vh;
}

#agua_usada .card-header {
  color: white;
  background-color: #43aa8b;
}

#doencas .card-header {
  color: white;
  background-color: #fb8b24;
}

#agua_potavel .card-header {
  color: white;
  background-color: #457b9d;
}

#florestas .card-header {
  color: white;
  background-color: #f94144;
}

#co2 .card-header {
  color: white;
  background-color: #8e9aaf;
}

#petroleo .card-header {
  color: white;
  background-color: #023047;
}

#gas_natural .card-header {
  color: white;
  background-color: #0096c7;
}

#carvao .card-header {
  color: white;
  background-color: #03071e;
}

#quimicos .card-header {
  color: white;
  background-color: #5a189a;
}
</style>
