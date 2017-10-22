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
        <el-menu-item index="3" :route="{name: 'Map'}">
          Map
        </el-menu-item>
        <el-menu-item index="3" :route="{name: 'Profile'}">
          Profile
        </el-menu-item>
        <div class="profile-actions">
          <el-menu-item index="" disabled="">
          Welcome back, {{ this.$store.email }}.
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
export default {
  methods: {
    logout () {
      this.$store.dispatch('logout');
      this.$router.push({
        path: '/login'
      });
    }
  }
}
</script>
