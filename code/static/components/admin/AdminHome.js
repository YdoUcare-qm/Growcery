import Card from './RequestsCard.js'
import Card2 from './RegistrationCard.js'
import AdminNavbar from './AdminNavbar.js'


new Vue ({
  el: '#app',
  template: `
  <div>
  <AdminNavbar :key='has_changed'/>
   <h1>Welcome admin</h1>
    <h3 v-if="requests.length>0 && registrationrequests.length>0">No Pending Requests</h3>
   <h3 v-if="requests.length>0">Approval Requests from Store Managers</h3>
  <Card v-for="(request, index) in requests" :key='index' :request="request"  />
  <h3 v-if="registrationrequests.length>0">New Registration Requests</h3>
  <Card2 v-for="(rrequest,indx) in registrationrequests" v-bind:key="rrequest.id"  :rrequest="rrequest"  />
  </div>`,

  data() {
    return {
      has_changed:true,
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      requests: [],
      registrationrequests:[]
    }
  },
  components: {
    Card,
    Card2,
    AdminNavbar
    
  },
  async mounted() {
    const res = await fetch('/api/admin', {
      headers: {
        'Authentication-Token': this.authToken,
      },
    });
    const data = await res.json();
    if (res.ok) {
      this.requests = data.category;
      this.registrationrequests = data.registration;
    } else {
      alert(data.message);
    }

  },


})
