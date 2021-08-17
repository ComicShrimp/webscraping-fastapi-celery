<template>
  <div class="content">
    <img src="../assets/Logo.svg" alt="World Dashboard logo" />
    <h1>Bem vindo(a) ao World Dashboard !!!</h1>
    <div class="content">
      <p>Este site destina-se à agregar várias informações sobre o meio ambiente.</p>
    </div>
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
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: center;
}
</style>
