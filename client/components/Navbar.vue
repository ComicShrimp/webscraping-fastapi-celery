<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-brand href="#">
        <img src="../assets/Logo.svg" alt="World Dashboard logo" id="logo" />
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item class="navbar-item"> <NuxtLink to="/">Inicio</NuxtLink></b-nav-item>
        <b-nav-item href="#">Florestas</b-nav-item>
        <b-nav-item href="#">Ar</b-nav-item>
        <b-nav-item href="#">Água</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<style>
#logo {
  width: 5vw;
  height: 5vh;
}

.nuxt-link-exact-active {
  color: white !important;
}

.nuxt-link-active {
  color: aqua !important;
}
</style>
