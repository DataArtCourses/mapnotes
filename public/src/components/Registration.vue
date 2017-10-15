<template>
 <div>
    <h1>Qwa!</h1>
    <form id="registarion" @submit.prevent="validateBeforeSubmit()" method="POST">
        <div>
          <input v-validate="'required|email'" name="email" type="text" placeholder="Email" v-model="email"><br>
          <input v-validate="'required|min:8'" name="password" type="password" class="form-control" placeholder="Password"><br>
          <input v-validate="'required|confirmed:password'" name="password_confirmation" type="password" data-vv-as="password" placeholder="Password, Again" v-model="password">
        </div>

      <div v-show="errors.any()">
        <div v-if="errors.has('email')"> 
          {{ errors.first('email') }}
        </div>
        <div v-if="errors.has('password')">
          {{ errors.first('password') }}
        </div>
        <div v-if="errors.has('password_confirmation')">
          {{ errors.first('password_confirmation') }}
        </div>
      </div>
      <button type="submit">Send</button>
  </form>
        
 </div>
</template>
<script>
import axios from 'axios'
const API_BASE = 'http://127.0.0.1:8000/api/users'

export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    validateBeforeSubmit () {
      this.$validator
        .validateAll()
        .then(response => {
          // Validation success if response === true
          if (this.email && this.password) {
            axios.post(API_BASE, {
              email: this.email,
              password: this.password
            })
            .then(response => {
              this.$router.push({path: '/hello'})
            })
            .catch(e => {
              console.error(e)
            })
          }
        })
        .catch(e => {
          // Catch errors
          console.error(e)
        })
    }
  }
}
</script>

