<template>
  <div id="app">
    <navbar></navbar>
    <router-view v-loading.fullscreen.lock="this.$store.getters.isLoaded" element-loading-text="Loading..." element-loading-background="rgba(0, 0, 0, 0.8)"></router-view>
  </div>
</template>
<script>
import Navbar from './components/Navbar'

export default {
  name: 'app',
  components: {
    Navbar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
