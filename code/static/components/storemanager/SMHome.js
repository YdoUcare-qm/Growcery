
import Card from './SMCard2.js';


export default {
  template: `
  <div style="margin-top: 200px;margin-bottom:1000px;margin-left:40px">

  <button v-if="categories.length>0" class="btn btn-primary" @click="download" style="font-weight:700;background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 40px; cursor: pointer;width:100%;align-items:center;">Download Monthly Sales Report</button>
      
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: left;margin:30px 30px;">
    <Card v-for="(category, index) in categories" :key='index' :category="category" style="background-color: rgba(200,200,200); width:200px; border-radius:30px ;text-align:center;" />
    <button @click="OpenNewModal"style="background-color: rgba(200,200,200); width:200px; border-radius:30px ;text-align:center;">Request New Category</button> 
    </div>
    
    
  

  <!-- Add Cat Modal -->
  <div v-if="NewCatModal" class="modal" style="display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); justify-content: center; align-items: center;">
    <div class="modal-content" style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); max-width: 400px; width: 100%; text-align: center;">
    <span class="close" style="position: absolute; top: 10px; right: 10px; font-size: 20px; cursor: pointer;" @click="CloseNewModal">&times;</span>
          
            <h1>Add New Category?</h1>
            <label for="cat_name" class="form-label">Category Name</label>
            <input type="text" class="form-control" id="cat_name" v-model="cat_name">
            
      <button class="btn btn-primary" @click="AddNewCat" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer;">Request New Category</button>
    </div>
    </div>
  
</div>
  

  `,

  data() {
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      categories: [],

      cat_name:'',

      NewCatModal:false,
      
    }
  },
  components: {
    Card,
  },

  async mounted() {
    const res = await fetch('/get-category', {
      headers: {
        'Authentication-Token': this.authToken,
      },
      
    });
    const data = await res.json();
    if (res.ok) {
      this.categories = data;
    } else {
      
    }
    
    
  },

  methods: {
    
    OpenNewModal() {
      this.NewCatModal = true;
    },
    CloseNewModal() {
      this.NewCatModal = false;
    },
    
    async AddNewCat(){
      try {
          const requestData={
              operation:1,
              name:this.cat_name,
              name2:null
          }
          
          const res = await fetch('/api/store/request', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': this.authToken,
            },
            body: JSON.stringify(requestData),
          });
    
          if (res.ok) {
            this.CloseNewModal()
            location.reload()
            alert('Request for New Category Placed!');
            
          } else {
            const data = await res.json();
            
            alert(data.message);
            
          }
        } catch (error) {
          
          console.error('Error', error);
          alert('Error');
        }
        
      
    },
    async download() {
      const res = await fetch('/download-sales-csv', {
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
};