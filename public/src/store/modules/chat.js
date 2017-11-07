import {
  SET_CHATS,
  SET_CHAT_MESSAGES,
  ADD_CHAT,
  SEND_MESSAGE,
  EDIT_MESSAGE,
  DELETE_MESSAGE
} from '../mutation-types'

const state = {
  chats: [],
  chat: []
}

const getters = {
  getChats: (state) => state.chats,
  getChat: (state) => state.chat
}

const mutations = {
  [SET_CHATS] (state, chats) { state.chats = chats },
  [SET_CHAT_MESSAGES] (state, chat) {
    state.chat = chat.chat
    let index = state.chats.findIndex((data) => data.chatId === chat.chatId)
    state.chats[index].unread = 0
  },
  [ADD_CHAT] (state, user) { state.chats.push(user) },
  [SEND_MESSAGE] (state, message) { state.chat.push(message) },
  [EDIT_MESSAGE] (state, message) {
    let indexMsg = state.chat.map(msg => msg.id).indexOf(message.id)
    state.chat[indexMsg].body = message.body
  },
  [DELETE_MESSAGE] (state, message) {
    state.chat = state.chat.filter(msg => {
      return msg.id !== message.id
    })
  }
}

const actions = {
  async reciveChats ({ commit }) {
    let chats = await require('../../../mocks/_chats.json')
    commit(SET_CHATS, chats)
  },
  async reciveChat ({ commit }, chatId) {
    if (chatId) {
      let chat = await require(`../../../mocks/_chat${chatId}.json`).sort((a, b) => { return Date.parse(a.time) - Date.parse(b.time) })
      commit(SET_CHAT_MESSAGES, { 'chat': chat, 'chatId': chatId })
    }
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
