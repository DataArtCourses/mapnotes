import {
  LOGIN,
  LOGOUT,
  SET_PROFILE
} from '../mutation-types'
import { setToken, getToken, delToken } from '../../utils/auth'

const state = {
  isLoading: false,
  isAuth: !!getToken(),
  userId: 1100,
  profile: {}
}

const getters = {
  isLoaded: (state) => { return state.isLoading },
  isAuth: (state) => { return state.isAuth },
  getProfile: (state) => { return state.profile },
  getUserId: (state) => { return state.userId }
}

const mutations = {
  setLoading (state) {
    state.isLoading = !state.isLoading
  },
  [LOGIN] (state, token) {
    setToken(token.token, token.ch)
    state.isAuth = true
  },
  [LOGOUT] (state) {
    delToken()
    state.isAuth = false
  },
  [SET_PROFILE] (state, profile) {
    state.profile = profile
  }
}

const actions = {
  async login ({ commit }, token) {
    commit(LOGIN, token)
  },
  async logout ({ commit }) {
    commit(LOGOUT)
  },
  async reciveProfile ({ commit, state }) {
    let users = await require('../../../mocks/_users.json')
    let userInfo = users.filter(user => { return user.userId === state.userId })[0]
    commit(SET_PROFILE, userInfo)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
