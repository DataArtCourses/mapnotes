<template lang="pug">
  el-main
    h1 Registration
    el-col(:span="8" :offset="7")
      el-form(:model="RegistrationForm" ref="RegistrationForm" labelWidth="150px" :rules="rules")
        el-form-item(prop="email" label="email")
          el-input(v-model.trim="RegistrationForm.email")
        el-form-item(prop="firstName" label="First Name")
          el-input(v-model.trim="RegistrationForm.firstName")
        el-form-item(prop="password" label="Password")
          el-input(v-model.trim="RegistrationForm.password" type="password")
        el-form-item(prop="checkPass" label="Password confirm")
          el-input(v-model.trim="RegistrationForm.checkPass" type="password")
        el-form-item
          el-button(type="primary" v-on:click.prevent="submitForm('RegistrationForm')") Register</el-button>
</template>
<script>
import axios from 'axios'
import { BASE_API_URL } from '../../utils/fetch'

export default {
  data () {
    const validatePassword = (rule, password, callback) => {
      const validPassword = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$/
      if (password !== this.RegistrationForm.checkPass && (password.length < 8 || password.length > 16)) {
        callback(new Error('Password must be from 8 to 16 chars'))
      } else if (password !== '' && !validPassword.test(password)) {
        callback(new Error('Password must have digits and letters'))
      } else {
        callback()
      }
    }
    const validateConf = (rule, value, callback) => {
      if (value !== this.RegistrationForm.password) {
        callback(new Error('Two inputs don\'t match!'))
      } else {
        callback()
      }
    }
    const validateName = (rule, name, callback) => {
      const validName = /^[A-Za-z]+$/
      if (name !== '' && (name.length < 4 || name.length > 40)) {
        callback(new Error('First Name must be from 4 to 40 chars'))
      } else if (name !== '' && !validName.test(name)) {
        callback(new Error('First Name must have only letters'))
      } else {
        callback()
      }
    }
    return {
      RegistrationForm: {
        email: '',
        firstName: '',
        password: '',
        checkPass: ''
      },
      rules: {
        email: [
          { required: true, message: 'Please input email address', trigger: 'blur' },
          { type: 'email', message: 'Please input correct email address', trigger: 'blur,change' }
        ],
        firstName: [
          { required: true, message: 'Please input correct First Name', trigger: 'blur' },
          { type: 'text', validator: validateName, trigger: 'blur,change' }
        ],
        password: [
          { required: true, message: 'Please input the password', trigger: 'blur' },
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
          axios.post(`${BASE_API_URL}/register`, {
            email: this.RegistrationForm.email,
            password: this.RegistrationForm.password,
            first_name: this.RegistrationForm.firstName
          })
          .then(response => {
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
          this.RegistrationForm = {
            email: '',
            firstName: '',
            password: '',
            checkPass: ''
          }
        } else {
          console.log('error submit!!');
          return false
        }
      })
    }
  }
}
</script>

