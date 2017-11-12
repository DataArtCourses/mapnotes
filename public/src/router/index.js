import Vue from 'vue'
import Router from 'vue-router'

import lazyLoading from './lazyLoading'

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/registration',
      name: 'Registration',
      component: lazyLoading('auth/Registration')
    },
    {
      path: '/messenger',
      name: 'Messenger',
      component: lazyLoading('messenger/index'),
      children: [
        {
          path: ':chat_id',
          meta: {
            requiresAuth: true
          }
        }
      ],
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/profile/:user_id',
      name: 'Profile',
      component: lazyLoading('users/Profile'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/map',
      name: 'Map',
      component: lazyLoading('map/index'),
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: ':pin_id',
          meta: {
            requiresAuth: true
          }
        }
      ]
    },
    {
      path: '*',
      redirect: '/map'
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
})
