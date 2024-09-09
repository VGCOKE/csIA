import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import RandomDraw from '../views/RandomDraw.vue'
import DrawPage from '../views/DrawPage.vue'
import History from '../views/History.vue'
import HistoryDetailView from '../views/HistoryDetailView.vue'
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
      path: '/randomdraw',
      name: 'randomdraw',
      component: RandomDraw,
      meta: {
        title: 'Random Draw Page'
      },
    },
    {
      path: '/draw',
      name: 'draw',
      component: DrawPage,
      meta: {
        title: 'Drawing wheel Page'
      },
    },
    {
      path: '/history',
      name: 'history',
      component: History,
      meta: {
        title: 'History'
      }
    },
    {
      path: '/history/:id',
      name: 'history-detail',
      component: HistoryDetailView,
      meta: {
        title: 'History details'
      }
    },
    {
      path: '/summary',
      name: 'summary',
      component: Summary,
      meta: {
        title: 'Summary'
      }
    }
  ]
})
router.beforeEach((to, from) => {
  document.title = to.meta?.title ?? 'Default Title'
})
export default router
