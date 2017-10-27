import { LOGIN, LOGOUT } from '../mutation-types'
import { setToken, getToken, delToken } from '../../utils/auth'

const state = {
  isLoading: false,
  isAuth: !!getToken(),
  userName: 'user'
};

const getters = {
  isLoaded: (state) => { return state.isLoading },
  isAuth: (state) => { return state.isAuth },
  getUserName: (state) => { return state.userName }
};

const mutations = {
  setLoading (state) {
    state.isLoading = !state.isLoading
  },
  [LOGIN]: (state, token) => {
    setToken(token.token, token.ch);
    state.isAuth = true;
  },
  [LOGOUT]: (state) => {
    delToken();
    state.isAuth = false;
  }
};

const actions = {
  login: ({ commit }, token) => {
    commit('setLoading');
    commit(LOGIN, token);
    commit('setLoading');
  },
  logout: ({ commit }) => {
    commit('setLoading');
    commit(LOGOUT);
    commit('setLoading');
  }
};

export default {
  state,
  getters,
  mutations,
  actions
}
