import { LOGIN, LOGOUT } from '../mutation-types'
import { setToken, getToken, delToken } from '../../utils/auth'

const state = {
  isLoading: false,
  isAuth: !!getToken(),
  userName: 'User',
  userId: 'user-test'
};

const getters = {
  isLoaded: (state) => { return state.isLoading },
  isAuth: (state) => { return state.isAuth },
  getUserName: (state) => { return state.userName },
  getUserId: (state) => { return state.userId }
};

const mutations = {
  setLoading (state) {
    state.isLoading = !state.isLoading
  },
  [LOGIN] (state, token) {
    setToken(token.token, token.ch);
    state.isAuth = true;
  },
  [LOGOUT] (state) {
    delToken();
    state.isAuth = false;
  }
};

const actions = {
  async login ({ commit }, token) {
    await commit('setLoading');
    await commit(LOGIN, token);
    await commit('setLoading');
  },
  async logout ({ commit }) {
    await commit('setLoading');
    await commit(LOGOUT);
    await commit('setLoading');
  }
};

export default {
  state,
  getters,
  mutations,
  actions
}
