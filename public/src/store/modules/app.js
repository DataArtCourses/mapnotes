import { LOGIN, LOGOUT } from '../mutation-types'

const store = {
  isLoading: false,
  isAuth: false,
  token: ''
};

const getters = {
  isLoaded: state => state.isLoaded,
  isAuth: state => state.isAuth,
  token: state => state.token
};

const mutations = {
  setLoading (state, toggle) {
    state.isLoading = toggle
  },
  [LOGIN]: (state, user) => {
    state.isAuth = true
  },
  [LOGOUT]: (state) => {
    state.isAuth = false
  }
};

export default {
  store,
  getters,
  mutations
}
