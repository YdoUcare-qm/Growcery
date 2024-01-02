export default {
  template: `
  <div >
    <div style="margin-top:200px;width:400px;position:fixed;background-color:none;padding:30px 30px 30px 30px;right:40px;color:white;">
    <h1 style="color:white;">Login</h1>
        <div class='text-danger'>*{{error}}</div>
        <label for="user-email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="user-email" placeholder="name@example.com" v-model="cred.email">
        <label for="user-password" class="form-label">Password</label>
        <input type="password" class="form-control" id="user-password" v-model="cred.password">
        <button class="btn btn-primary mt-2" @click='login' > Login </button>
    </div> 
  </div>
  `,
  data() {
    return {
      cred: {
        email: null,
        password: null,
      },
      error: null,
    }
  },
  methods: {
    async login() {
      const res = await fetch('/user-login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.cred),
      })
      const data = await res.json()
      if (res.ok) {
        localStorage.setItem('auth-token', data.token)
        localStorage.setItem('role', data.role)
        // this.$router.push({ path: '/' })
        if (data.role=='user')
          {window.location.href = '/user';}
        else if (data.role=='sm')
          {window.location.href = '/storemanager';}
        else if (data.role=='admin')
          {window.location.href = '/admin';}
        
      } else {
        this.error = data.message
      }
    },
  },
}
