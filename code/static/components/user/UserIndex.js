import router from './UserRouter.js'
import UserNavbar from './UserNavbar.js'

router.beforeEach((to, from, next) => {
  if (to.name !== 'Login' && !localStorage.getItem('auth-token') ? true : false)
    next({ name: 'Login' })
  else next()
})

new Vue({
  el: '#app',
  template: `<div>
  <div class="m-2">
  <UserNavbar :key='has_changed'/>
  <router-view class="m-3"/>
  </div>
  </div>`,
  router,
  components: {
    UserNavbar,
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