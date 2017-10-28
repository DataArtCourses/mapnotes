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
  getChats: (state) => { return state.chats }
}

const mutations = {
  [SET_CHATS] (state, chats) { state.chats = chats },
  [SET_CHAT_MESSAGES] (state, messages) { state.chat = messages },
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
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
