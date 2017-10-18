<template>
 <div>
    <h1>Qwa!</h1>
    <form id="registarion" @submit.prevent="validateBeforeSubmit">
        <div>
          <input name="text" type="text" placeholder="e-mail" v-model="email"><br>
          <p v-show="wrongEmail && attemptSubmit">Wrong email</p>
          <input name="password" type="password" placeholder="password" v-model="password"><br>
          <p v-show="wrongPasswordLength && attemptSubmit">Password length from 8 to 16</p>
          <p v-show="wrongPassword && attemptSubmit">In the password must be present digit and letter</p>
          <input name="password_confirmation" type="password" placeholder="password, again" v-model="password_confirmation">
          <p v-show="wrongPasswordConfirmation && attemptSubmit">Wrong password confirmation</p>
        </div>
      <button type="submit">Send</button>
  </form>
  <router-link to="/login">Sign In</router-link>
        
 </div>
</template>
<script>
import axios from 'axios'

const API_BASE = 'http://127.0.0.1:8000/api/'
const reEmail = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
const rePassword = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$/

export default {
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
      this.attemptSubmit = true
      if (!this.wrongEmailv && !this.wrongPasswordLength && !this.wrongPassword && !this.wrongPasswordConfirmation) {
        axios.post(API_BASE + 'register', {
          email: this.email,
          password: this.password
        })
        .then(response => {
          console.log(response)
          if (response.status === 200) {
            console.log({'email': this.email, 'password': this.password})
            this.$router.push({path: '/login'})
          }
        })
        .catch(e => {
          console.error(e)
        })
      }
    }
    // validateBeforeSubmit () {
    //   this.$validator
    //     .validateAll()
    //     .then(response => {
    //       // Validation success if response === true
    //       if (this.email && this.password) {
    //         axios.post(API_BASE, {
    //           email: this.email,
    //           password: this.password
    //         })
    //         .then(response => {
    //           console.log(response)
    //           if (response.status === 200) {
    //             this.$router.push({path: '/login'})
    //           }
    //         })
    //         .catch(e => {
    //           console.error(e)
    //         })
    //         console.log({'email': this.email, 'password': this.password})
    //         // this.$router.push({path: '/login'})
    //       }
    //     })
    //     .catch(e => {
    //       // Catch errors
    //       console.error(e)
    //     })
    // }
  }
}
</script>

