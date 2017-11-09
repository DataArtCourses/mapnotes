<template lang="pug">
  el-main(v-if="this.$route.params.chat_id").messenger
    div#container
      el-card(v-for="message in messages" key="message.message_id")
        p {{ message.message_body }}
        small {{ message.time | moment("from", "now", true) }}
    el-footer.input_message  
      textarea(rows="4" cols="120" v-model="message_body"  @keyup.enter="sendMessage")
      button(@click="sendMessage") Send
  el-main(v-else)
    p Please choose the chat
</template>
<script>
export default {
  name: 'chat',
  data () {
    return {
      message_body: ''
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
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    sendMessage () {
      if (this.message_body) {
        let message = {
          message_body: this.message_body,
          time: Date.now(),
          user_id: this.$store.getters.getUserId
        }
        this.$store.dispatch('sendMessage', { message: message, chat_id: +this.$route.params.chat_id })
        this.message_body = ''
        this.scrollToEnd()
      }
    },
    fetchData () {
      this.$store.dispatch('reciveChat', +this.$route.params.chat_id)
      this.scrollToEnd()
    },
    scrollToEnd () {
      this.$nextTick(() => {
        let container = this.$el.querySelector('#container')
        container.scrollTop = container.scrollHeight
      })
    }
  }
}
</script>
<style lang="scss">
#container {
  height: 550px;
  overflow-y: auto;
}

</style>

