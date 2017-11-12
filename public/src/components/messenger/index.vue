<template lang="pug">
    el-container
      chats
      chat
    
</template>
<script>
import Chats from './Chats'
import Chat from './Chat'

export default {
  name: 'messenger',
  components: {
    Chats,
    Chat
  }
}
</script>
