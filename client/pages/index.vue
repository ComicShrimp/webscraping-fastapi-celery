<template>
  <div class="content">
    <div class="inicio">
      <img id="logo" src="../assets/Logo.svg" alt="World Dashboard logo" />
      <h1>Bem-vindo(a) ao World Dashboard !</h1>
      <p>Este site destina-se à agregar várias informações sobre o meio ambiente.</p>
      <div id="footer-incio">
        <b-icon
          id="arrow-down-icon"
          icon="arrow-down-circle"
          animation="cylon-vertical"
          @click="scrollToRef('agua')"
        ></b-icon>
      </div>
    </div>
    <div class="cards">
      <section ref="agua" id="agua">
        <h2 id="card-group-title">Água</h2>
        <b-card-group deck>
          <b-card header="Água Usada">
            <b-card-title>{{ consumo_agua_este_ano.toLocaleString("pt-BR") }} Milhões de Litros</b-card-title>
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card header="Doenças causadas pela água">
            <b-card-title>{{ mortes_doencas_agua_este_ano.toLocaleString("pt-BR") }} mortes</b-card-title>
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card header="Água potável">
            <b-card-title
              >{{ populacao_sem_acesso_a_agua_potavel.toLocaleString("pt-BR") }} pessoas</b-card-title
            >
            <b-card-text>sem acesso</b-card-text>
          </b-card>
        </b-card-group>
      </section>

      <section ref="ambiente" id="ambiente">
        <h2 id="card-group-title">Ambiente</h2>
        <b-card-group deck>
          <b-card header="Florestas perdidas">
            <b-card-title>{{ perda_floresta_este_ano.toLocaleString("pt-BR") }} hectares</b-card-title>
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card header="CO2 Emitido">
            <b-card-title>{{ emissoes_co2_este_ano.toLocaleString("pt-BR") }} toneladas</b-card-title>
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card header="Petroleo">
            <b-card-title>{{ barris_de_petroleo_restante.toLocaleString("pt-BR") }} barris</b-card-title>
            <b-card-text>para acabar</b-card-text>
          </b-card>
        </b-card-group>

        <b-card-group deck>
          <b-card header="Desertificação" style="max-width: 28.8vw">
            <b-card-title>{{ desertificacao_este_ano.toLocaleString("pt-BR") }} hectares</b-card-title>
            <b-card-text>este ano</b-card-text>
          </b-card>
          <b-card header="Quimicos" style="max-width: 40rem">
            <b-card-title>{{ quimicos_liberados.toLocaleString("pt-BR") }} Toneladas</b-card-title>
            <b-card-text>liberados no ambiente</b-card-text>
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
            desertificacao_este_ano: 0,
            quimicos_liberados: 0,
            // Água
            consumo_agua_este_ano: 0,
            mortes_doencas_agua_este_ano: 0,
            populacao_sem_acesso_a_agua_potavel: 0,
        }
    },
    mounted() {
        this.$axios.get("http://localhost:8585").then((response) => {

            this.perda_floresta_este_ano = response.data.worldometers.perda_de_floresta_este_ano;
            this.emissoes_co2_este_ano = response.data.worldometers.emissoes_co2_este_ano;
            this.barris_de_petroleo_restante = response.data.worldometers.barris_de_petroleo_restante;
            this.desertificacao_este_ano = response.data.worldometers.desertificacao_este_ano;
            this.quimicos_liberados = response.data.worldometers.quimicos_liberados;

            // Água
            this.consumo_agua_este_ano = response.data.worldometers.consumo_agua_este_ano;
            this.mortes_doencas_agua_este_ano = response.data.worldometers.mortes_doencas_agua_este_ano;
            this.populacao_sem_acesso_a_agua_potavel = response.data.worldometers.populacao_sem_acesso_a_agua_potavel;

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
  width: 30vw;
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

b-card {
  max-width: 4vw;
}
</style>
