export default {
  template: `<div style="margin-top: 200px;margin-bottom:1000px">
  <h1>Your Inbox</h1>
  <div style="display: flex; flex-wrap: wrap; gap: 20px;">
  <div v-for="(reply, index) in replies" :key='index' :reply="reply" style="width:100%" >
        <div> 
        Your request for 
        <span v-if="reply.operation==1"> adding new Category called {{reply.name}}</span>
        <span v-if="reply.operation==2"> changing {{reply.name}} to {{reply.name2}}</span>
        <span v-if="reply.operation==3"> deleting category {{reply.name}}</span>
        
        has been

        <span v-if="reply.status==1"> Accepted </span>
        <span v-if="reply.status==0"> Declined </span>

        </div>
  </div>
  </div>
  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      replies: [],
      
    }
  },
  components: {
    
  },

  async mounted() {
    const res = await fetch('/api/store/request', {
      headers: {
        'Authentication-Token': this.authToken,
      },
    });
    const data = await res.json();
    if (res.ok) {
      this.replies = data;
    } else {
      alert(data.message);
    }

  },

  methods: {

    },
  }