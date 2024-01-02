
export default {
    template: `<div class="p-2" style="background-color: rgba(10,10,10); color:white; width:300px; border-radius:30px ;text-align:center;">
      <span hidden>{{product.id}}</span>
      <h4>{{ product.p_name }}</h4>
      <p>{{ product.rem_units }} units remaining</p>
      <p>Mfg.Date {{ product.added_date }}</p>
      <p>Expiry Date {{ product.expiry_date }}</p>
      <p>Rate : {{ product.rate }}$/{{ product.unit_SI }}</p>
      <p>Store : {{ product.store_name }}</p>
      <p>Category : {{ product.category }}</p>
      <div style="text-align:center;">
      <button v-if="product.rem_units > 0" class="btn" style="width:90%; background-color:rgba(85, 249, 101, 0.904); border-radius:30px;" @click="openModal">Buy</button>
      <button v-if="product.rem_units === 0" style="justify-content: middle;width:90%;border-radius:30px;" class="btn btn-danger">Out Of Stock</button>
      </div>
  
      <!-- Modal -->
      <div v-if="showModal" class="modal" style="display: flex; position: fixed; top: 0; left: 0; width: 100%; height: 100%; color: rgba(0, 0, 0); justify-content: center; align-items: center;">
        <div class="modal-content" style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); max-width: 400px; width: 100%; text-align: center;">
        <div style="height:30px;width;60px;border-radius:30px;background-color:red;position: absolute; top: 10px; right: 10px; font-size: 20px; cursor: pointer;" @click="closeModal">
          <span class="close" style="padding: 10px 10px 10px 10px;color:white;font-weight:700;" >&times;</span>
        </div>
          <h4> Add {{ product.p_name }} to Cart?</h4>
          <label for="quantity">Quantity:</label>
          <input
          type="number"
          id="quantity"
          v-model.number="selectedQuantity"
          :min="1"
          :max="product.rem_units"
          @input="handleQuantityInput"
          style="margin-bottom: 10px; padding: 5px;"
        />
          <button class="btn btn-primary" @click="addToCart" style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 20px; cursor: pointer;">Add to Cart</button>
        </div>
      </div>
    </div>`,
  
    props: ['product'],
    data() {
      return {
        showModal: false,
        selectedQuantity: 1,
      };
    },
    methods: {
        handleQuantityInput() {
            // Ensure that selectedQuantity is a positive integer and capped to rem_units
            this.selectedQuantity = Math.min(Math.max(parseInt(this.selectedQuantity) || 1, 1), this.product.rem_units);
          },
      
         
      openModal() {
        this.showModal = true;
      },
      closeModal() {
        this.showModal = false;
      },
      addToCart() {
        this.$emit('addToCart', this.product, this.selectedQuantity, this.product.rate * this.selectedQuantity);
        this.closeModal();
      },
    },
  };
  