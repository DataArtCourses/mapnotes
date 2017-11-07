<template lang="pug">
    el-main.messenger
      div(v-if="this.$route.params.chat_id")
        div.out_messages
          el-card.box-card(v-for="message in messages" key="message.message_id")
            p {{ message.message_body }}
            small {{ message.time }}
        div.input_message
          textarea(rows="4" cols="50" v-model="new_message.text")
          button(@click="sendMessage") Send
      div(v-else)
        p Please choose the chat
</template>
<script>
export default {
  name: 'messenger',
  data () {
    return {
      new_message: {
        text: '',
        dateTime: ''
      }
    }
  },
  computed: {
    messages () {
      return this.$store.getters.getChat
    }
  },
  mounthed () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    sendMessage () {
      if (this.new_message.text) {
        this.new_message.dateTime = Date.now();
        this.messages.push(this.new_message);
        this.new_message = {text: '', dateTime: ''}
      }
    },
    fetchData () {
      this.$store.dispatch('reciveChat', +this.$route.params.chat_id)
    }
  }
}
</script>

