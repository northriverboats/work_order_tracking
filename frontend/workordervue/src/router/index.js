import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import ListPage from '@/components/ListPage'
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
      path: '/list',
      name: 'ListPage',
      component: ListPage
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    }
  ]
})
