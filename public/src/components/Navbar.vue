<template>
      <el-header>
    <el-menu mode="horizontal" :router="true">
      <el-row>
    <el-col :span="12" :offset="6">
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
        <div class="profile-actions">
          <el-menu-item index="" disabled="">
          Welcome back, {{this.$store.email}}.
        </el-menu-item>
        <el-menu-item index="3">
          <el-button type="primary" @click="logout()">
            Logout
          </el-button>
        </el-menu-item>
        </div>
      </div>
      <div v-else class="profile-actions">
        <el-menu-item index="2" :route="{name: 'Registration'}">
          <el-button type="plain">Registration</el-button>
        </el-menu-item>
        <el-menu-item index="3" :route="{name: 'Login'}">
          <el-button type="plain">Login</el-button>
        </el-menu-item>
      </div>
      </el-col>
  </el-row>
    </el-menu>
  </el-header>

</template>

<style>
  .profile-actions {
    float: right;
  }
</style>

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
