
import Card from './Card.js';
import Cart from './Cart.js';

export default {
  template: `<div style="background-color: rgba(20,20,20);padding: 30px 30px 30px 30px;margin:20px -20px -20px -20px;">

      <input type="text" style="position:fixed; margin:-30px 20px 20px 280px;width:40%; border-radius:30px;font-size:20px; padding: 10px 10px 10px 10px; " v-model="searchQuery" placeholder="Search products or categories here..." @input="filterProducts" />
    
      <h4 v-if= " filteredProducts.length == 0 " style="color:white;">No Products or categories match your query</h4>
      <h4 v-if= " filteredProducts.length > 0 " style="color:white;">Products</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;margin-top: 150px;margin-bottom:120px;">
    
    <Card v-for="(product, index) in filteredProducts" :key='index' :product="product" @addToCart="addToCart" />
    <Cart v-if="cartItems.length>0":cartItems="cartItems" @removeFromCart="removeFromCart" style="position:fixed; bottom:0;" />
  </div>
  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      products: [],
      cartItems: JSON.parse(localStorage.getItem('cartItems')) || [],
      searchQuery:''
    }
  },
  components: {
    Card,
    Cart,
  },

  async mounted() {
    const res = await fetch('/api/user', {
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
    const storedCartItems = localStorage.getItem('cartItems');
    this.cartItems = storedCartItems ? JSON.parse(storedCartItems) : [];
  },

  methods: {
    addToCart(product, quantity, price) {
      this.cartItems.push({ product, quantity, price });
      this.updateLocalStorage();
    },
    removeFromCart(index) {
      this.cartItems.splice(index, 1);
      this.updateLocalStorage();
    },
    updateLocalStorage() {
      localStorage.setItem('cartItems', JSON.stringify(this.cartItems));
    },
  },
  computed: {
    filteredProducts() {
      const query = this.searchQuery.toLowerCase();
      return this.products.filter(
        (product) =>
          product.p_name.toLowerCase().includes(query) || product.category.toLowerCase().includes(query)
      );
    }
    },
};
