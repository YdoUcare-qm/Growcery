
export default {
    template: `
        <div>
                <h1>{{category.category}}</h1>
                <div>
                <button @click="categoryProducts(category)" class="btn btn-warning m-2" style="width:90%;">View Products</button>
                <button @click="OpenEditModal" class="btn btn-warning m-2" style="width:90%;">Edit Category</button>
                <button @click="OpenDeleteModal"class="btn btn-warning m-2" style="width:90%;">Delete Category</button>
                </div>
        
        
<!-- Edit Cat Modal -->
            <div v-if="EditCatModal" class="modal" style="display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); justify-content: center; align-items: center;">
                <div class="modal-content" style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); max-width: 400px; width: 100%; text-align: center;">
                <span class="close" style="position: absolute; top: 10px; right: 10px; font-size: 20px; cursor: pointer;" @click="CloseEditModal">&times;</span>
            
            <h1>{{category.category}}</h1>
            <label for="cat_name" class="form-label">Category Name</label>
            <input type="text" class="form-control" id="cat_name" v-model="cat_name">
            
                <button class="btn btn-primary" @click="EditCat" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer;">Request Edit Category</button>
                </div>
            </div>


  <!-- delete Cat Modal -->
        <div v-if="DeleteCatModal" class="modal" style="display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); justify-content: center; align-items: center;">
                <div class="modal-content" style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); max-width: 400px; width: 100%; text-align: center;">
                <span class="close" style="position: absolute; top: 10px; right: 10px; font-size: 20px; cursor: pointer;" @click="CloseDeleteModal">&times;</span>

                <h3>Are you sure you want to delete the Category {{category.category}}? </h3>
                <h6>All the products in the category will be removed</h6>
                
            <button class="btn btn-primary" @click="DeleteCat" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer;">Request Delete Category</button>
            </div>
        
</div>
</div>
    `,
  
    props: ['category'],
    data() {
      return {
        userRole: localStorage.getItem('role'),
        authToken: localStorage.getItem('auth-token'),

        cat_name:'',

        EditCatModal:false,
        DeleteCatModal:false,
      };
    },
    methods: {
        categoryProducts( category ) {
            this.$router.push({name:'Category',params:{category:category.category}});
          },
          OpenEditModal() {
            this.EditCatModal = true;
          },
          CloseEditModal() {
            this.EditCatModal = false;
          },
          OpenDeleteModal() {
            this.DeleteCatModal = true;
          },
          CloseDeleteModal() {
            this.DeleteCatModal = false;
          },


          async EditCat(){
            try {
                const requestData={
                    operation:2,
                    name:this.category.category,
                    name2:this.cat_name
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
                  this.CloseEditModal()
                  location.reload()
                  alert('Request for editing Category Placed!');
                  
                } else {
                  const data = await res.json();
                  
                  alert(data.message);
                  
                }
              } catch (error) {
                
                console.error('Error', error);
                alert('Error');
              }
              
            
          },
          async DeleteCat(){
            try {
                const requestData={
                    operation:3,
                    name:this.category.category,
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
                  this.CloseDeleteModal()
                  location.reload()
                  alert('Request for Category Deletion Placed!');
                  
                } else {
                  const data = await res.json();
                  
                  alert(data.message);
                  
                }
              } catch (error) {
                
                console.error('Error', error);
                alert('Error');
              }
              
            
          },
          }
      
      
    };
  