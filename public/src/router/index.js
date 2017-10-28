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
      component: lazyLoading('messenger/Messenger'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/profile/:id',
      name: 'Profile',
      component: lazyLoading('users/Profile'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/map',
      name: 'Map',
      component: lazyLoading('map/Map'),
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: ':id',
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
