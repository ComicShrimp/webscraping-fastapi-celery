<template>
  <div class="content">
    <div class="inicio">
      <img id="logo" src="../assets/Logo.svg" alt="World Dashboard logo" />
      <h1>Bem-vindo(a) ao World Dashboard !</h1>
      <p>Este site destina-se à agregar várias informações sobre o meio ambiente.</p>
      <b-icon icon="arrow-down-circle" animation="cylon-vertical"></b-icon>
    </div>
    <section id="metricas" class="info-header">
      <h1 class="titulo">Métricas</h1>
    </section>
    <div class="cards">
      <b-card-group deck>
        <b-card header="Florestas perdidas">
          <b-card-title>{{ perda_floresta_este_ano }} de hectares</b-card-title>
          <b-card-text>este ano</b-card-text>
        </b-card>
        <b-card header="CO2 Emitido">
          <b-card-title>{{ emissoes_co2_este_ano }} toneladas</b-card-title>
          <b-card-text>este ano</b-card-text>
        </b-card>
        <b-card header="Petroleo">
          <b-card-title>{{ barris_de_petroleo_restante }} barris</b-card-title>
          <b-card-text>para acabar</b-card-text>
        </b-card>
      </b-card-group>
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
        }
    },
    mounted() {
        this.$axios.get("http://localhost:8585").then((response) => {
            this.perda_floresta_este_ano = response.data.worldometers.perda_de_floresta_este_ano;
            this.emissoes_co2_este_ano = response.data.worldometers.emissoes_co2_este_ano;
            this.barris_de_petroleo_restante = response.data.worldometers.barris_de_petroleo_restante;
        }).catch((error) => {
            console.log(error);
        });
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
  margin: 5% 0% 0% 0%;
}

.titulo {
  text-align: center;
}

#logo {
  width: 30%;
  margin: 0% 0% 5% 0%;
}
</style>
