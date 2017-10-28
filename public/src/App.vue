<template lang="pug">
  #app
    el-container
      el-header
        app-header
      router-view
      el-footer
        app-footer
</template>
<script>
import AppHeader from './components/layout/AppHeader'
import AppFooter from './components/layout/AppFooter'

export default {
  name: 'app',
  components: {
    AppHeader,
    AppFooter
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
