<template lang="pug">
  el-aside(width="450px" style="background-color: rgb(238, 241, 246)")
      ul
        li(v-for="chat in chatsList" :key="chat.chatId")
          img(:src="chat.chatWith.avatarUrl" width="80px")
          b {{ chat.chatWith.userName }} 
          br
          span {{ chat.lastMessage.body }}
          small {{ chat.lastMessage.time }}
</template>
<script>
export default {
  computed: {
    chatsList () {
      return this.$store.getters.getChats
    }
  },
  mounted () {
    this.$store.dispatch('reciveChats')
  }
}
</script>
