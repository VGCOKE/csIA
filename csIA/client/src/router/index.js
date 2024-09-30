import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import RandomPicker from '../views/RandomPicker.vue'
import SpinningWheel from '../views/SpinningWheel.vue'
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
        title: 'Home'
      }
    },
    {
      path: '/randompicker',
      name: 'randompicker',
      component: RandomPicker,
      meta: {
        title: 'Random Picker'
      },
    },
    {
      path: '/spin',
      name: 'spin',
      component: SpinningWheel,
      meta: {
        title: 'Spinning wheel'
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
