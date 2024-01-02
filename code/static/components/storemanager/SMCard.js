
export default {
    template: `<div class="p-2" style="background-color: rgba(200,200,200); width:200px; border-radius:30px ;text-align:center;">
      <span hidden>{{product.id}}</span>
      <h4>{{ product.p_name }}</h4>
      <p>{{ product.rem_units }} units remaining</p>
      <p>Mfg.Date {{ product.added_date }}</p>
      <p>Expiry Date {{ product.expiry_date }}</p>
      <p>Rate : {{ product.rate }}$/{{ product.unit_SI }}</p>
      <p>Store : {{ product.store_name }}</p>
      <p>Category : {{ product.category }}</p>
      <div style="text-align:center;">
      <button @click="openEditModal" class="btn btn-info m-1" style="width:90%" >Edit</button>
      <button @click="openDelModal"style="justify-content: middle;width:90%" class="btn btn-danger m-1">Delete</button>
      </div>
  
     

      <!-- Edit Product Modal -->
      <div v-if="EditProductModal" class="modal" style="display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); justify-content: center; align-items: center;">
        <div class="modal-content" style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); max-width: 400px; width: 100%; text-align: center;">
          <span class="close" style="position: absolute; top: 10px; right: 10px; font-size: 20px; cursor: pointer;" @click="closeEditModal">&times;</span>
              
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
          
              <button class="btn btn-primary" @click="editProduct" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer;">Edit the Product</button>
        </div>
      </div>

      <!-- Delete Product Modal -->
      <div v-if="DelProductModal" class="modal" style="display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); justify-content: center; align-items: center;">
        <div class="modal-content" style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); max-width: 400px; width: 100%; text-align: center;">
          <span class="close" style="position: absolute; top: 10px; right: 10px; font-size: 20px; cursor: pointer;" @click="closeDelModal">&times;</span>
          <h4>Are you sure you want to delete {{ product.p_name }}?</h4>
         
          <button class="btn btn-primary" @click="delProduct" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer;">Delete Product</button>
        </div>
      </div>
    </div>`,
  
    props: ['product'],
    data() {
      return {
        EditProductModal: false,
        DelProductModal: false,
        authToken: localStorage.getItem('auth-token'),

        p_id : this.product.id,
        p_name : this.product.p_name,
        category: this.product.category,
        rem_units:this.product.rem_units,
        added_date:this.product.added_date,
        expiry_date:this.product.expiry_date,
        rate:this.product.rate,
        unit_SI:this.product.unit_SI,
        img:this.product.img,
        selectedQuantity: 1,
      };
    },
    methods: {
        handleQuantityInput() {
            
            this.selectedQuantity = Math.max(parseInt(this.selectedQuantity) || 1, 1);
          },
      
         
      openEditModal() {
        this.EditProductModal = true;
      },
      closeEditModal() {
        this.EditProductModal = false;
      },
      openDelModal() {
        this.DelProductModal = true;
      },
      closeDelModal() {
        this.DelProductModal = false;
      },
      
      async editProduct() {
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
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': this.authToken,
            },
            body: JSON.stringify({ data: requestData }),
          });
    
          if (res.ok) {
            this.closeEditModal()
            location.reload()
            
            
          } else {
            const data = await res.json();
            
            alert(data.message);
            
          }
        } catch (error) {
          
          console.error('Error Editing Product:', error);
          alert('Error Editing Product. Please try again.');
        }
        alert('Product Edited!');
      

      },
      async delProduct(){
        try {
          
          const res = await fetch('/api/store', {
            method: 'DELETE',
            headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': this.authToken,
            },
            body: JSON.stringify({ p_id : this.p_id }),
          });
    
          if (res.ok) {
            this.closeDelModal()
            location.reload()
            
            
          } else {
            const data = await res.json();
            
            alert(data.message);
            
          }
        } catch (error) {
          
          console.error('Error Deleting Product:', error);
          alert('Error Deleting Product. Please try again.');
        }
        alert('Product Deleted!');
      


      }
    },
  };
  