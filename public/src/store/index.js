import Vue from 'vue';
import Vuex from 'vuex';

import app from './modules/app';

Vue.use(Vuex);

const store = new Vuex.Store({
  strict: true,
  modules: {
    app
  },
  store: {},
  getters: {},
  mutations: {},
  actions: {}
});

export default store
