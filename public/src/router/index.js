import Vue from 'vue'
import Router from 'vue-router'
import {
  Registration,
  Messenger,
  Login,
  Hello } from '@/components/';

Vue.use(Router);

export default new Router({
  hashbang: false,
  routes: [
    {
      path: '/',
      redirect: '/login',
      name: 'login'
    },
    {
      path: '/registration',
      name: 'registration',
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
