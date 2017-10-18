import Vue from 'vue'
import Router from 'vue-router'
import {
  Registration,
  Messenger,
  Login,
  Hello } from '@/components/'

Vue.use(Router)

export default new Router({
  hashbang: false,
  routes: [
    {
      path: '/',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/hello',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/messenger',
      name: 'Messenger',
      component: Messenger
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
