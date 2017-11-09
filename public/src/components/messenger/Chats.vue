<template lang="pug">
  el-aside(width="450px" style="background-color: rgb(238, 241, 246)")
    div.scroll
      ul
        li(v-for="chat in chatsList" :key="chat.chatId")
          el-badge.item(:value="chat.unread")
            img.circle(:src="chat.chatWith.avatarUrl" width="80px")
            router-link(:to="`/messenger/${chat.chatId}`")
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
<style lang="scss" scoped>
.scroll {
  height: 650px;
  overflow-y: scroll;
}
ul {
  list-style-type: none;
}
.item {
  margin-top: 10px;
  margin-right: 40px;
  .circle{
    border-radius: 40px;
  }
}
</style>
