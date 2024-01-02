import UserHome from './UserHome.js'
import UserHistory from './UserHistory.js'
import UserOrder from './UserOrder.js'

const routes = [
  { path: '/', component: UserHome, name: 'Home' },
  { path: '/history', component: UserHistory, name: 'History' },
  { path: '/order', component: UserOrder }

]

export default new VueRouter({
  routes,
})
