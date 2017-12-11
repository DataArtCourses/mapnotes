<template lang="pug">
  el-menu.menu(mode="horizontal" :router="true")
    div(v-if="this.$store.getters.isAuth")
      el-row.bg(:gutter="10")
        el-col(:xs="4" :sm="4" :md="3" :lg="3" :xl="3")
          router-link(:to="{name: 'Map'}")
            img.logo(src="../../assets/Mapified.png")
        el-col.search(:xs="8" :sm="8" :md="7" :lg="7" :xl="7")
          el-input(v-model='search', placeholder='search')
            el-button(slot='append', icon='el-icon-search')
        el-col.icons(:xs="4" :sm="4" :md="4" :lg="4" :xl="4" :offset="1")
          div.cont
            el-col(:xs="1" :sm="1" :md="1" :lg="1" :xl="1")
              div.ch
                el-menu-item(:route="{name: 'Map'}" index="1")
                  img(src='../../assets/pin.png')
              div.ch
                img.line(src='../../assets/line.png')
            el-col(:xs="1" :sm="1" :md="1" :lg="1" :xl="1")
              div.ch
                el-menu-item(:route="{name: 'Friends'}" index="2")
                  img(src='../../assets/friends.png')
              div.ch
                img.line(src='../../assets/line.png')
            el-col(:xs="1" :sm="1" :md="1" :lg="1" :xl="1")
              div.ch
                el-menu-item(:route="{name: 'Messenger'}" index="3")
                  img(src='../../assets/messages.png')
              div.ch
                img.line(src='../../assets/line.png')
            el-col(:xs="1" :sm="1" :md="1" :lg="1" :xl="1")
              div.ch
                el-menu-item(:route="{name: 'Notifications'}" index="4")
                  img(src='../../assets/notifications.png')
        el-col(:xs="1" :sm="1" :md="1" :lg="1" :xl="1" :offset="1")
          div.avatar
            el-menu-item(:route="{name:'Profile', params: { user_id: `${this.$store.getters.getUserId}`}}" index="5")
              img(:src="userInfo.avatar_url || 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'")
        el-col(:xs="1" :sm="1" :md="1" :lg="1" :xl="1" :offset="5")
          el-button.button_auth(type="primary" @click="logout") Logout
    div.profile-actions(v-else)
      el-menu-item(index="1")
        el-input(v-model.trim="LoginForm.email" placeholder="e-mail" )
      el-menu-item(index="2")
        el-input(type="password" v-model.trim="LoginForm.password" placeholder="password" @keyup.enter="submitForm('LoginForm')")
      el-menu-item(index="3")
        el-checkbox(v-model="checked") Remember me
      el-menu-item(index="4")
        el-button(type="primary" @click="submitForm('LoginForm')") Log in
</template>
<script>
import axios from 'axios'
import { BASE_API_URL } from '../../utils/fetch'

export default {
  data () {
    return {
      LoginForm: {
        email: '',
        password: ''
      },
      checked: true,
      search: ''
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout');
      this.$router.push({ name: 'Registration' });
    },
    submitForm () {
      axios.post(`${BASE_API_URL}/login`, { email: this.LoginForm.email, password: this.LoginForm.password })
        .then(response => {
          if (response.status === 200) {
            this.$store.dispatch('login', {userId: response.data.user_id, token: response.data.token, ch: this.checked})
            this.LoginForm.email = ''
            this.LoginForm.password = ''
            this.$nextTick(() => {
              this.$store.dispatch('reciveProfile')
              this.$router.push({name: 'Map'})
            })
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
  },
  computed: {
    userInfo: {
      get () {
        if (this.$store.getters.getProfile && this.$store.getters.isAuth) {
          return this.$store.getters.getProfile
        }
      }
    }
  },
  beforeCreate () {
    this.$store.dispatch('reciveProfile')
  }
}
</script>
<style>
  .menu{
    line-height: 0px;
  }
  .bg{
    background-color: #151515;
  }
  .logo{
    padding: 30px 0 20px 0;
  }
  .search{
    padding-top: 17px;
  }
  .icons{
    color: #fff;

  }
  .icon{
    padding-top: 20px;
  }
  .cont {
    display: flex;
    justify-content: space-between;
  }
  .ch {
    margin: 5px 2px;
  }
  .line{
    margin-top: 15px;
  }
  .avatar{
    padding-top: 7px;
  }
  .profile-actions{
    margin-top: 10px;
  }
  .name{
    font-size: 16px;
    color: #fff;
  }
  .button_auth{
    margin-top: 20px;
  }
  .avatar img {
    width: 45px;
    border-radius: 10px;
  }
</style>
