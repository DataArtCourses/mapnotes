// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import { getToken } from './utils/auth'

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(require('vue-moment'))

router.beforeEach((to, from, next) => {
  store.commit('setLoading', true)
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!getToken()) {
      next({
        name: 'Registration'
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

router.afterEach((to, from) => {
  store.commit('setLoading', false)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  render: h => h(App)
});
