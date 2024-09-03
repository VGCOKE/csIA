import { createRouter, createWebHistory } from 'vue-router'
import RandomDraw from '../components/RandomDraw.vue'
import History from '../components/History.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/draw',
      name: 'draw',
      component: RandomDraw
    },
    {
      path: '/history',
      name: 'history',
      component: History
    }
  ]
})

export default router
