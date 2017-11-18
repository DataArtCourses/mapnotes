<template lang="pug">
    el-menu(mode="horizontal" :router="true")
      el-row
        el-col(:span="12" :offset="6")
          div(v-if="this.$store.getters.isAuth")
            el-menu-item(index="1" :route="{name: 'Map'}") Map
            el-menu-item(index="2" :route="{name: 'Messenger'}") Messenger
            div(class="profile-actions")
              el-menu-item(index="3" :route="{name:'Profile', params: { user_id: `${this.$store.getters.getUserId}`}}") Welcome back, {{ this.$store.getters.getUserInfo.userName }}
              el-menu-item(index="4")
                el-button(type="primary" @click="logout") Logout
          div(v-else class="profile-actions")
            el-menu-item(index="1")
              el-input(v-model="LoginForm.email" placeholder="e-mail")
            el-menu-item(index="2")
              el-input(type="password" v-model="LoginForm.password" placeholder="password")
            el-menu-item(index="3") 
              el-checkbox(v-model="LoginForm.checked") Remember me
            el-menu-item(index="4")
              el-button(type="primary" @click="submitForm('LoginForm')") Log in
</template>
<script>
import axios from 'axios'

export default {
  data () {
    return {
      LoginForm: {
        email: '',
        password: '',
        checked: true
      }
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout');
      this.$router.push({ name: 'Registration' });
    },
    submitForm () {
      axios.post('http://localhost:8000/api/login', { email: this.LoginForm.email, password: this.LoginForm.password })
      .then(response => {
        console.log(response)
        if (response.status === 200) {
          this.$store.dispatch('login', {token: response.data.token, ch: this.LoginForm.checked})
          this.$router.push({name: 'Map'})
        }
      })
      .catch(e => {
        this.$message({
          showClose: true,
          type: 'error',
          message: `${e.response ? e.response.data.error : e}`
        })
      })
    }
  }
}
</script>
<style>
  .profile-actions {
    float: right;
  }
</style>