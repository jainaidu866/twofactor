<template>
  <form @submit.prevent="register">
    <input v-model="username" placeholder="Username" required>
    <input v-model="password" type="password" placeholder="Password" required>
    <button type="submit">Register</button>
  </form>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return { username: '', password: '' }
  },
  methods: {
    async register() {
      await axios.post('/register', { username: this.username, password: this.password })
      this.$router.push('/login')
    }
  }
}
</script>
