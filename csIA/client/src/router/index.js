import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import RandomDraw from '../views/RandomDraw.vue'
import History from '../views/History.vue'
import Summary from '../views/Summary.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        title: 'Home Page'
      }
    },
    {
      path: '/draw',
      name: 'draw',
      component: RandomDraw,
      meta: {
        title: 'Random Draw Page'
      }
    },
    {
      path: '/history',
      name: 'history',
      component: History,
      meta: {
        title: 'History Page'
      }
    },
    {
      path: '/summary',
      name: 'summary',
      component: Summary,
      meta: {
        title: 'Summary Page'
      }
    }
  ]
})
router.beforeEach((to, from) => {
  document.title = to.meta?.title ?? 'Default Title'
})
export default router
