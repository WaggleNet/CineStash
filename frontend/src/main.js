import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import SweatAlert2 from 'vue-sweetalert2'
import Viewer from 'v-viewer'

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
Vue.component('fa-icon', FontAwesomeIcon)
library.add(fas)
library.add(fab)
library.add(far)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'viewerjs/dist/viewer.css'

import './wagglenet-theme.sass'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(Viewer)
Vue.use(SweatAlert2)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
