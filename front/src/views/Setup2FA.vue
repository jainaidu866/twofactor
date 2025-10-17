<template>
  <div>
    <p>Scan the QR code with your authenticator app:</p>
    <img :src="qrUri" alt="QR Code">
    <button @click="enable2FA">Enable 2FA</button>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return { qrUri: '' }
  },
  async mounted() {
    const res = await axios.get('/setup_2fa')
    this.qrUri = res.data.qr_uri
  },
  methods: {
    async enable2FA() {
      await axios.post('/setup_2fa')
      this.$router.push('/verify-2fa')
    }
  }
}
</script>
