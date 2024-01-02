

export default {
  template: `<div>

  <div style="position:fixed; margin-top:20px; right:20px">
  <button @click="download" class="btn btn-success" v-if="orders.length>0">Download Monthly report</button>
  </div>
  <div style="margin-top:100px;">
  <h1 style="color:white;">Your Order History</h1>
  
  <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top:50px">

  

  <div v-for="(order, index) in orders" :key='index' :order="order" style="width:100%;" >
        <h4 style="color:white;" >{{ order.details.p_name }}</h4>
        <p style="color:white;">{{ order.details.category }}</p>
        <p style="color:white;">Mfg.Date {{ order.details.added_date }}</p>
        <p style="color:white;">Expiry Date {{ order.details.expiry_date }}</p>
        <p style="color:white;">{{ order.quantity }} {{order.details.unit_SI}}s @ {{ order.price }}$ on {{order.order_date}}</p>
        <p style="color:white;">Store : {{ order.details.store_name }}</p>
  </div>
  </div>
  </div>
  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      orders: [],
      
    }
  },
  components: {
    
  },

  async mounted() {
    const res = await fetch('/api/user/order', {
      headers: {
        'Authentication-Token': this.authToken,
      },
    });
    const data = await res.json();
    if (res.ok) {
      this.orders = data;
    } else {
      alert(data.message);
    }

  },

  methods: {
    async download() {
      const res = await fetch('/download-csv', {
        headers: {
          'Authentication-Token': this.authToken,
        },
      });
      if (res.ok) {
        const blob = await res.blob();

        // Create a temporary anchor element
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = 'monthly_report.csv'; // Set the desired file name

        // Trigger the click event to start the download
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
  
    },
    },
  }
