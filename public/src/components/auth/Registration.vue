<template lang="pug">
  div
    h1 Qwa!
    el-row(:gutter="20")
      el-col(:span="8" :offset="7")
        el-form(:model="RegistrationForm" ref="RegistrationForm" label-width="150px" :rules="rules")
          el-form-item(prop="email" label="Email")
            el-input(v-model="RegistrationForm.email")
          el-form-item(prop="password" label="Password")
            el-input(v-model="RegistrationForm.password" type="password")
          el-form-item(prop="checkPass" label="Password Confirm")
            el-input(v-model="RegistrationForm.checkPass" type="password")
          el-form-item
            el-button(type="primary" @click="submitForm('RegistrationForm')") Register
            router-link(to="/login") Sign In
</template>
<script>
import axios from 'axios'

export default {
  data () {
    const validatePassword = (rule, password, callback) => {
      const validPassword = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$/
      if (password.length < 8 || password.length > 16) {
        callback(new Error('Password must be from 8 to 16 chars'))
      } else if (!validPassword.test(password)) {
        callback(new Error('Password must have digits and letters'))
      } else {
        callback()
      }
    };
    const validateConf = (rule, value, callback) => {
      if (value !== this.RegistrationForm.password) {
        callback(new Error('Two inputs don\'t match!'))
      } else {
        callback()
      }
    };
    return {
      RegistrationForm: {
        email: '',
        password: '',
        checkPass: ''
      },
      rules: {
        email: [
          { required: true, message: 'Please input email address', trigger: 'blur' },
          { type: 'email', message: 'Please input correct email address', trigger: 'blur,change' }
        ],
        password: [
          { required: true, validator: validatePassword, trigger: 'blur,change' }
        ],
        checkPass: [
          { required: true, message: 'Please input the password again', trigger: 'blur' },
          { validator: validateConf, trigger: 'blur,change' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          axios.post('http://localhost:8000/api/register', { email: this.RegistrationForm.email, password: this.RegistrationForm.password }).then(response => {
            console.log(response);
            if (response.status === 200) {
              this.$message({
                'type': 'success',
                'message': `Almost there! To complete registration please check your email ${this.RegistrationForm.email}`
              })
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

