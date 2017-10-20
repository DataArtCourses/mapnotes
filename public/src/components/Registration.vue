<template>
 <el-container>
  <el-header>We are pleased to invite you to join Mapified!</el-header>
  <el-main center >
    <el-row :gutter="20">
    <el-col :span="8" :offset="8">
      <el-form @submit.prevent="validateBeforeSubmit">
        <el-form-item label="Email">
          <p v-show="wrongEmail && attemptSubmit">Wrong email</p>
          <el-input name="text" type="text" v-model="email" placeholder="e-mail"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <p v-show="wrongPasswordLength && attemptSubmit">Password length from 8 to 16</p>
          <p v-show="wrongPassword && attemptSubmit">In the password must be present digit and letter</p>
          <el-input name="password" type="password" placeholder="password" v-model="password"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input name="password_confirmation" type="password" placeholder="repeat password" v-model="password_confirmation"></el-input>
            <p v-show="wrongPasswordConfirmation && attemptSubmit">Wrong password confirmation</p>
        </el-form-item>
        <el-form-item>
          <el-button nativeType="submit" round @click.prevent="validateBeforeSubmit">Send</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
  </el-main>
</el-container>


</template>
<script>
import axios from 'axios'
import ElButton from '../../node_modules/element-ui/packages/button/src/button.vue'
import ElFormItem from '../../node_modules/element-ui/packages/form/src/form-item.vue'
// import { Message } from 'element-ui';

const API_BASE = 'http://127.0.0.1:8000/api/'
const reEmail = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
const rePassword = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$/

export default {
  components: {
    ElFormItem,
    ElButton},
  data () {
    return {
      email: '',
      password: '',
      password_confirmation: '',
      attemptSubmit: false
    }
  },
  computed: {
    wrongEmail () {
      return !reEmail.test(this.email)
    },
    wrongPasswordLength () {
      return this.password.length < 8 || this.password.length > 16
    },
    wrongPassword () {
      return !rePassword.test(this.password)
    },
    wrongPasswordConfirmation () {
      return this.password !== this.password_confirmation
    }
  },
  methods: {
    validateBeforeSubmit () {
      this.attemptSubmit = true;
      if (!this.wrongEmail && !this.wrongPasswordLength && !this.wrongPassword && !this.wrongPasswordConfirmation) {
        axios.post(API_BASE + 'register', {
          email: this.email,
          password: this.password
        })
        .then((response) => {
          if (response.status === 200) {
            this.$message({
              type: 'success',
              message: `Almost there! We've sent you an email on ${this.email} address.`
            })
          } else {
            this.$message({
              type: 'warning',
              message: 'Something went wrong, but it\'s not your fault! Try again later :)'
            })
          }
        })
        .catch((err) => {
          this.$message({
            type: 'error',
            message: `${err.response.data.error}`
          })
        })
      }
    }
  }
}
</script>

