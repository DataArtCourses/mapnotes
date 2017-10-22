<template lang="pug">
    section
      el-header
        el-menu(class="el-menu-demo" mode="horizontal" :router="true")
          el-menu-item(index="1" :route="{name: 'Hello'}" v-if="this.$store.getters.isAuth") Hello
           el-menu-item(index="1" :route="{name: 'Messenger'}" v-if="this.$store.getters.isAuth") Messenger
            el-menu-item(index="1" :route="{name: 'Map'}" v-if="this.$store.getters.isAuth") Map
          el-menu-item(index="2" :route="{name: 'Registration'}")
            el-button(type="primary" v-if="!this.$store.getters.isAuth" plain) Registration
          el-menu-item(index="3" :route="{name: 'Login'}")
            el-button(type="success" v-if="!this.$store.getters.isAuth" plain) Log In
            el-button(type="warning" @click="logout()" v-else plain) Log Out
</template>

<script>
import ElContainer from '../../node_modules/element-ui/packages/container/src/main.vue'

export default {
  methods: {
    logout () {
      this.$store.dispatch('logout')
    }
  },
  components: {ElContainer}
}
</script>