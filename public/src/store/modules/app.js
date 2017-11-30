import { BASE_API_URL, service } from '../../utils/fetch'

import {
  LOGIN,
  LOGOUT,
  SET_PROFILE
} from '../mutation-types'
import { setToken, delToken, getToken, getuUserId } from '../../utils/auth'

const state = {
  isLoading: false,
  isAuth: !!getToken(),
  userId: Number(getuUserId()) || 0,
  profile: {
    first_name: '',
    last_name: '',
    bio: '',
    phone: '',
    avatar_url: ''
  }
}

const getters = {
  isLoaded: (state) => { return state.isLoading },
  isAuth: (state) => { return state.isAuth },
  getProfile: (state) => { return state.profile },
  getUserId: (state) => { return state.userId }
}

const mutations = {
  setLoading (state, toggle) {
    state.isLoading = toggle
  },
  [LOGIN] (state, token) {
    setToken(token.token, token.userId, token.ch)
    state.userId = token.userId
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
    commit(LOGIN, await token)
  },
  async logout ({ commit }) {
    commit(LOGOUT)
  },
  async reciveProfile ({ commit, state }) {
    if (state.userId > 0) {
      let user = await service.get(`${BASE_API_URL}/profile/${state.userId}`)
      commit(SET_PROFILE, user.data)
    }
  },
  async sendProfile ({ commit, state }, profile) {
    if (state.userId > 0 && profile !== {}) {
      let user = await service.post(`${BASE_API_URL}/profile/${state.userId}`, profile)
      if (user.status === 200) {
        commit(SET_PROFILE, profile)
      }
    }
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
