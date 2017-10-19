<template lang="pug">
  div
    h1 Hello, user ;)
    input(type="email" id="email" placeholder="e-mail")
    br
    input(type="password" id="password" placeholder="password")
    br
    button(type="submit") Sign in
    br
    router-link(to="/") Registration
</template>
<script>
export default {
  name: 'login',
  data () {
    return {
      email: '',
      password: ''
    }
  }
}
</script>
