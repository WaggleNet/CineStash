import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import ProjectListPage from '../components/ProjectList.vue'
import ProjectViewPage from '../components/ProjectView.vue'
import SettingsPage from '../components/Settings.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectListPage
  },
  {
    path: '/projects/:id',
    name: 'project',
    component: ProjectViewPage
  },
  {
    path: '/settings',
    name: 'settings',
    components: SettingsPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
