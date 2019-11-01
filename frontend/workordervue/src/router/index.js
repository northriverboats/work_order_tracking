import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import Test from '@/components/Test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    }
  ]
})
