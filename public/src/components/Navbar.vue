<template>
  <el-header>
    <el-menu mode="horizontal" :router="true">
      <div v-if="this.$store.getters.isAuth">
        <el-menu-item index="1" :route="{name: 'Hello'}">
          Hello
        </el-menu-item>
        <el-menu-item index="2" :route="{name: 'Messenger'}">
          Messenger
        </el-menu-item>
        <el-menu-item index="3" :route="{name: 'Messenger'}">
          Map
        </el-menu-item>
        <el-menu-item index="3" style="float: right;">
          <el-button @click="logout()">
            Logout
          </el-button>
        </el-menu-item>
      </div>
      <div v-else>
        <el-menu-item index="2" :route="{name: 'Registration'}">
          Register
        </el-menu-item>
        <el-menu-item index="3" :route="{name: 'Login'}">
          Login
        </el-menu-item>
      </div>
    </el-menu>
  </el-header>
</template>

<script>
import ElContainer from '../../node_modules/element-ui/packages/container/src/main.vue'
import ElHeader from '../../node_modules/element-ui/packages/header/src/main.vue';
import ElMenu from '../../node_modules/element-ui/packages/menu/src/menu.vue';
import ElMenuItem from '../../node_modules/element-ui/packages/menu/src/menu-item.vue';
import ElButton from '../../node_modules/element-ui/packages/button/src/button.vue';

export default {
  methods: {
    logout () {
      this.$store.dispatch('logout');
      this.$router.push({
        path: '/login'
      });
    }
  },
  components: {
    ElButton,
    ElMenuItem,
    ElMenu,
    ElHeader,
    ElContainer}
}
</script>
