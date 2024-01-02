import router from './SMRouter.js'
import Navbar from './SMNavbar.js'



new Vue({
  el: '#app',
  template: `<div>
  <div class="m-2">
  <Navbar :key='has_changed'/>
  <router-view class="m-3"/>
  </div>
  </div>`,
  router,
  components: {
    Navbar,
  },
  data: {
    has_changed: true,
  },
  watch: {
    $route(to, from) {
      this.has_changed = !this.has_changed
    },
  },
})