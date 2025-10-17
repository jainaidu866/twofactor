<template>
  <form @submit.prevent="verify">
    <input v-model="otp" placeholder="Enter OTP" required>
    <button type="submit">Verify</button>
  </form>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return { otp: '' }
  },
  methods: {
    async verify() {
      await axios.post('/verify_2fa', { otp: this.otp })
      this.$router.push('/dashboard')
    }
  }
}
</script>
