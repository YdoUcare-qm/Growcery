import SMHome from './SMHome.js'
import SMInbox from './SMInbox.js'
import SMCategory from './SMCategory.js'


const routes = [
  { path: '/', component: SMHome, name: 'Home' },
  { path: '/inbox', component: SMInbox, name: 'Login' },
  { path: '/category/:category', name:'Category',component: SMCategory },

]

export default new VueRouter({
  routes,
})
