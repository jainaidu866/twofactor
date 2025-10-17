<template>
  <form @submit.prevent="login">
    <input v-model="username" placeholder="Username" required>
    <input v-model="password" type="password" placeholder="Password" required>
    <button type="submit">Login</button>
  </form>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return { username: '', password: '' }
  },
  methods: {
    async login() {
      await axios.post('/login', { username: this.username, password: this.password })
      this.$router.push('/dashboard')
    }
  }
}
</script>
