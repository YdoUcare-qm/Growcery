// Order.js
export default {
    template: `<div>
    <div style="margin-top:100px;">
      <h2 style="color:white;">Your Order</h2>
      <ul>
      <h1 v-if="cartItems.length==0">Add Items to the Cart First</h1>
        <li v-for="(item, index) in cartItems" :key="index" style="color:white;">
          {{ item.product.p_name }} - Quantity: {{ item.quantity }} - Total: {{ item.price }} $
        </li>
      </ul>
      <button v-if="cartItems.length > 0"@click="placeOrder" class="btn btn-success" style="margin-top: 10px;">Place Order - Total: {{ calculateTotal() }} $</button>
    </div>
    </div>`,
  
    data() {
      return {
        cartItems: JSON.parse(localStorage.getItem('cartItems')) || [],
        authToken: localStorage.getItem('auth-token')
      };
    },
  
    methods: {
      calculateTotal() {
        return this.cartItems.reduce((total, item) => total + item.price, 0);
      },
      async placeOrder() {
        try {
          
          const cartList = JSON.parse(localStorage.getItem('cartItems')) || [];
            console.log(cartList)
          
          const requestData = cartList.map(item => ({
            p_id: item.product.id,      
            quantity: item.quantity,
            price: item.price,          
            order_date: new Date().toISOString().split('T')[0],
          }));

          console.log(JSON.stringify({ data: requestData }))
    
          const res = await fetch('/api/user/order', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': this.authToken,
            },
            body: JSON.stringify({ data: requestData }),
          });
    
          if (res.ok) {
            // Handle successful response, e.g., show a success message
            alert('Order placed successfully!');
            localStorage.setItem('cartItems', JSON.stringify([]));
            window.location.href = '/user';
          } else {
            const data = await res.json();
            // Handle unsuccessful response, e.g., show an error message
            alert(data.message);
            
          }
        } catch (error) {
          // Handle any errors that occurred during the fetch
          console.error('Error placing order:', error);
          alert('Error placing order. Please try again.');
        }
        
      },
    },
    mounted() {
        
      },
  };
  