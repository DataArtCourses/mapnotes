import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/HelloWorld'
import Registration from '@/components/Registration'
import Messenger from '@/components/Messenger'

Vue.use(Router)

export default new Router({
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
