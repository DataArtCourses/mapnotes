<template lang="pug">
  div(class=messenger)
    div(class="out_messages")
      div(v-for="message in messages" key="message.dateTime")
        p {{ message.text }}
        small {{ message.dateTime}}
    div(class="input_message")
      input(type="text" v-model="new_message.text")
      button(@click="sendMessage()") Send
</template>
<script>
export default {
  name: 'messanger',
  data () {
    return {
      messages: [],
      new_message: {
        text: '',
        dateTime: ''
      }
    }
  },
  methods: {
    sendMessage () {
      if (this.new_message.text) {
        this.new_message.dateTime = Date.now()
        this.messages.push(this.new_message)
        this.new_message = {text: '', dateTime: ''}
      }
    }
  }
}
</script>

