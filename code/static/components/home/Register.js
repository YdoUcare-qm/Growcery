export default {
    template: `
    <div >
      <div style="margin-top:200px;width:400px;position:fixed;background-color:none;padding:30px 30px 30px 30px;right:40px;color:white;">
      <h1 style="color:white;">Register</h1>
          <div class='text-danger'>*{{error}}</div>
          <label for="user-email" class="form-label">Email address</label>
          <input type="email" class="form-control" id="user-email" placeholder="name@example.com" v-model="cred.email">
          <label for="user-name" class="form-label">Username</label>
          <input type="email" class="form-control" id="user-name" placeholder="username" v-model="cred.username">
          <label for="user-password" class="form-label">Password</label>
          <input type="password" class="form-control" id="user-password" v-model="cred.password">
          <button class="btn btn-primary mt-2" @click='register' > Register </button>
      </div> 
    </div>
    `,
    data() {
      return {
        cred: {
          username: null,  
          email: null,
          password: null,
        },
        error: null,
      }
    },
    methods: {
      async register() {
        const res = await fetch('/user-register', {
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
        //   this.$router.push({ path: '/' })
          window.location.href = '/user';  
        } else {
          this.error = data.message
        }
      },
    },
  }