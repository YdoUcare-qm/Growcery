
import SMCard from './SMCard.js';


export default {
  template: `<div style="margin-top: 200px;margin-bottom:1000px">
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
    <SMCard v-for="(product, index) in products" :key='index' :product="product"  />
    <button @click="openModal" style="background-color: rgba(200,200,200); width:200px; border-radius:30px ;text-align:center;">Add New Product</button>
    
  </div>

  <!-- Add Product Modal -->
  <div v-if="NewProductModal" class="modal" style="display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); justify-content: center; align-items: center;">
    <div class="modal-content" style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); max-width: 400px; width: 100%; text-align: center;">
    <span class="close" style="position: absolute; top: 10px; right: 10px; font-size: 20px; cursor: pointer;" @click="closeModal">&times;</span>

            <label for="p_name" class="form-label">Product Name</label>
            <input type="text" class="form-control" id="p_name" v-model="p_name">
            
            <label for="rem_units" class="form-label">Stock</label>
            <input type="number" class="form-control" id="rem_units" v-model="rem_units">

            <label for="rate" class="form-label">Rate Price</label>
            <input type="number" class="form-control" id="rate" v-model="rate">
            
            <label for="unit_SI" class="form-label">SI unit</label>
            <input type="text" class="form-control" id="unit_SI" v-model="unit_SI">

            <label for="img" class="form-label">Image URL</label>
            <input type="text" class="form-control" id="img" v-model="img">

            <label for="added_date" class="form-label">Added Date</label>
            <input type="date" class="form-control" id="added_date" v-model="added_date">

            <label for="expiry_date" class="form-label">Expiry Date</label>
            <input type="date" class="form-control" id="img" v-model="expiry_date">

      <button class="btn btn-primary" @click="addNewProduct" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer;">Add New Product</button>
    </div>
  </div>

  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      products: [],
      category: this.$route.params.category,
      NewProductModal : false,

      
        p_name : '',
        
        rem_units:'',
        added_date:'',
        expiry_date:'',
        rate:'',
        unit_SI:'',
        img:'',
      
    }
  },
 
  components: {
    SMCard,
   
  },

  async mounted() {
    console.log(this.category)
    const res = await fetch(`/api/store?category=${encodeURIComponent(this.category)}`, {
      headers: {
        'Authentication-Token': this.authToken,
      },
      
    });
    const data = await res.json();
    if (res.ok) {
      this.products = data;
    } else {
      alert(data.message);
    }
    
  },
  created(){
    
  },

  methods: {
    openModal() {
        this.NewProductModal = true;
      },
    closeModal() {
        this.NewProductModal = false;
      },
    
    async addNewProduct() {
        try {
          const requestData = [{
            p_id:this.p_id,
            p_name:this.p_name,
            category:this.category,
            rem_units:this.rem_units,
            added_date:this.added_date,
            expiry_date:this.expiry_date,
            rate:this.rate,
            unit_SI:this.unit_SI,
            img:this.img          
          }]

          console.log(JSON.stringify({ data: requestData }))
    
          const res = await fetch('/api/store', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': this.authToken,
            },
            body: JSON.stringify({ data: requestData }),
          });
    
          if (res.ok) {
            this.closeModal()
            location.reload()
            alert('Product Added!');
            
          } else {
            const data = await res.json();
            
            alert(data.message);
            
          }
        } catch (error) {
          
          console.error('Error Adding Product:', error);
          alert('Error Adding Product. Please try again.');
        }
        
      

      },
      
    },
  
};
