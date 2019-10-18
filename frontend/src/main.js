import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import Viewer from 'v-viewer'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'viewerjs/dist/viewer.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(Viewer)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
