<template>
 <div>
    <h1>Qwa!</h1>
   <el-row :gutter="20">
    <el-col :span="8" :offset="7">
      <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="150px" :rules="rules">
        <el-form-item prop="email" label="Email">
          <el-input v-model="dynamicValidateForm.email"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="Password">
          <el-input v-model="dynamicValidateForm.password" type="password"></el-input>
        </el-form-item>
        <el-form-item prop="checkPass" label="Password Confirm">
          <el-input v-model="dynamicValidateForm.checkPass" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('dynamicValidateForm')">Register</el-button>
          <router-link to="/login">Sign In</router-link>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>



 </div>
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
        callback(new Error('Password must have consists digits and letters'))
      } else {
        callback()
      }
    }
    const validateConf = (rule, value, callback) => {
      if (value !== this.dynamicValidateForm.password) {
        callback(new Error('Two inputs don\'t match!'))
      } else {
        callback()
      }
    }
    return {
      dynamicValidateForm: {
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
          axios.post('http://localhost:8000/api/register', { email: this.dynamicValidateForm.email, password: this.dynamicValidateForm.password }).then(response => {
            console.log(response)
            if (response.status === 200) {
              console.log({'email': this.dynamicValidateForm.email, 'password': this.dynamicValidateForm.password})
              this.$router.push({path: '/login'})
            }
          }).catch(e => {
            console.error(e)
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

