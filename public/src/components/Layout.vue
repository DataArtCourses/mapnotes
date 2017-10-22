<template lang="pug">
  div(class="main")

    messenger
</template>
<script>
import Messenger from './messenger/Messenger'

export default {
  name: 'main-app',
  components: {
    Messenger
  }
}
</script>

