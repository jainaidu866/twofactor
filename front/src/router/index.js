import { createRouter, createWebHistory } from 'vue-router'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import Setup2FA from '../views/Setup2FA.vue'
import Verify2FA from '../views/Verify2FA.vue'

const routes = [
  { path: '/register', component: Register },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/setup-2fa', component: Setup2FA },
  { path: '/verify-2fa', component: Verify2FA }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
