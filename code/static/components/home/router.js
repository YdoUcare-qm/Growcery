import Home from './Home.js'
import Login from './Login.js'
import Register from './Register.js'
import SMRegister from './SMRegister.js'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/register', component: Register },
  { path: '/sm-register', component: SMRegister },
]

export default new VueRouter({
  routes,
})
