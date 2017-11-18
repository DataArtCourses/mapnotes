<template lang="pug">
  el-main(v-if="this.$route.params.chat_id").messenger
    div#container-chat
      el-card(v-for="message in messages" key="message.message_id")
        p {{ message.message_body }}
        small {{ message.time | moment("from", "now", true) }}
    el-footer.input_message  
      textarea(rows="4" cols="120" v-model="messageBody"  @keyup.enter="sendMessage")
      button(@click="sendMessage") Send
  el-main(v-else)
    p Please choose the chat
</template>
<script>
export default {
  name: 'chat',
  data () {
    return {
      messageBody: ''
    }
  },
  computed: {
    messages () {
      return this.$store.getters.getChat
    }
  },
  created () {
    this.fetchData()
  },
  updated () {
    this.scrollToEnd()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    sendMessage () {
      if (this.messageBody) {
        let message = {
          message_body: this.messageBody,
          time: Date.now(),
          user_id: this.$store.getters.getUserId
        }
        this.$store.dispatch('sendMessage', { message: message, chat_id: +this.$route.params.chat_id })
        this.messageBody = ''
        this.scrollToEnd()
      }
    },
    fetchData () {
      this.$store.dispatch('reciveChat', +this.$route.params.chat_id)
    },
    scrollToEnd () {
      this.$nextTick(() => {
        let container = this.$el.querySelector('#container-chat')
        if (this.$route.params.chat_id) {
          container.scrollTop = container.scrollHeight
        }
      })
    }
  }
}
</script>
<style lang="scss">
#container-chat {
  height: 550px;
  overflow-y: auto;
}

</style>

