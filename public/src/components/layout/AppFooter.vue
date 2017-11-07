<template lang="pug">
  p Footer
</template>
<script>
export default {
  mounted () {
    // user profile loader
    this.$store.dispatch('reciveProfile')
  }
}
</script>

