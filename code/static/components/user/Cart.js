// Cart.js
export default {
    template: `<div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: rgba(45,45,45); padding: 10px; text-align: center;">
      <h2 style="color:white;">Your Cart</h2>
      <ul style="list-style: none; padding: 0; display: flex; flex-wrap: wrap; justify-content: center;">
        <li v-for="(item, index) in cartItems" :key="index" style="margin: 5px; padding: 5px; border-radius: 20px;color:white; background-color: rgba(0,0,0); position: relative;width:210px;text-align:left;">
          {{ item.product.p_name }} - {{ item.quantity }} {{ item.product.unit_SI }}
          <button @click="removeFromCart(index)" class="btn btn-danger" style="padding:0px 0px 0px 0px;height:25px;width:30px;border-radius:30px;position: absolute; right: 5px; cursor: pointer;color:white;font-weight:700;text-align:center;">X</button>
        </li>
      </ul>
  
      <router-link :to="{ path: '/order'}">
        <button style="margin-top: 10px;" class="btn btn-warning">Proceed to Checkout</button>
      </router-link>
    </div>`,
  
    props: ['cartItems'],
    methods: {
      removeFromCart(index) {
        this.$emit('removeFromCart', index);
      },
    },
  };
  