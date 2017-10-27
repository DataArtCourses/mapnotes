import Vue from 'vue'
import Vuex from 'vuex'

import app from './modules/app'
import map from './modules/map'

Vue.use(Vuex);

const store = new Vuex.Store({
  strict: true,
  modules: {
    app,
    map
  },
  store: {},
  getters: {},
  mutations: {},
  actions: {}
});

export default store
