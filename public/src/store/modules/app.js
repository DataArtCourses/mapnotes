import { LOGIN, LOGOUT } from '../mutation-types'

export const store = {
  isLoading: false,
  isAuth: false,
  token: ''
}

export const getters = {
  isLoaded: state => state.isLoaded,
  isAuth: state => state.isAuth,
  token: state => state.token
}

export const mutations = {
  setLoading (state, toggle) {
    state.isLoading = toggle
  },
  [LOGIN]: (state, user) => {
    state.isAuth = true
  },
  [LOGOUT]: (state) => {
    state.isAuth = false
  }
}
