import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import MiniGame from './components/MiniGame.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/mini-game', component: MiniGame }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
