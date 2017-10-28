import Vue from 'vue'
import Vuex from 'vuex'

import { app, map, chat } from './modules'

Vue.use(Vuex);

const store = new Vuex.Store({
  strict: true,
  modules: {
    app,
    map,
    chat
  },
  store: {},
  getters: {},
  mutations: {},
  actions: {}
});

export default store
