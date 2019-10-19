import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import ProjectListPage from '../components/ProjectList.vue'
import ProjectViewPage from '../components/ProjectView.vue'
import SettingsPage from '../components/Settings.vue'
import CamerasPage from '../components/Cameras.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/projects'
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
    path: '/cameras',
    name: 'cameras',
    component: CamerasPage
  },
  {
    path: '/settings',
    name: 'settings',
    component: SettingsPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
