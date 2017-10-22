<template lang="pug">
  el-main
    el-row(:gutter="20")
      el-col(:span="8" :offset="7")
        el-form(:model="LoginForm" ref="LoginForm" label-width="150px" )
          el-form-item(prop="email" label="Email" :rules="rules")
            el-input(v-model="LoginForm.email" placeholder="e-mail")
          el-form-item(prop="password" label="Password" :rules="[{required: true}]")
            el-input(type="password" v-model="LoginForm.password" placeholder="password")
          el-form-item
            el-checkbox(v-model="LoginForm.checked") Remember Me 
            br
            el-button(type="primary" @click="submitForm('LoginForm')") Log In
            router-link(to="/registration") Registration
            
</template>
<script>
import axios from 'axios'

export default {
  name: 'login',
  data () {
    return {
      LoginForm: {
        email: '',
        password: '',
        checked: false
      },
      rules: [
        { required: true, message: 'Please input email address', trigger: 'blur' },
        { type: 'email', message: 'Please input correct email address', trigger: 'blur,change' }
      ]
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          axios.post('http://localhost:8000/api/login', { email: this.LoginForm.email, password: this.LoginForm.password }).then(response => {
            console.log(response);
            if (response.status === 200) {
              this.$store.dispatch('login', {token: response.data.token, ch: this.LoginForm.checked})
              this.$router.push({path: '/hello'})
            }
          }).catch(e => {
            this.$message({
              type: 'error',
              message: `${e.response ? e.response.data.error : e}`
            })
          })
        } else {
          console.log('error submit!!');
          return false
        }
      })
    }
  }
}
</script>

