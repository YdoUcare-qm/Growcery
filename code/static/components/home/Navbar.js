export default {
  template: `
  <nav class="navbar navbar-expand-lg bg-body-tertiary" style="position:fixed;top:0; width:100%; height:100px ;margin: -12px -14px -11px -11px;">
  <div class="container-fluid" style="background-color: rgba(0, 0, 0, 0.848);height:100px;">
    <a class="navbar-brand" href="#">
    <h1 style="font-weight:700; font-size:30px">
    <span style="color: rgba(85, 249, 101, 0.904);">G</span>
    <span style="color: rgba(3, 208, 44, 0.904);">r</span>
    <span style="color: rgba(41, 154, 21, 0.904);">o</span>
    <span style="color: rgba(47, 148, 29, 0.904);">w</span>
    <span style="color: rgba(40, 127, 25, 0.904);">c</span>
    <span style="color: rgba(51, 169, 30, 0.904);">e</span>
    <span style="color: rgba(3, 208, 44, 0.904);">r</span>
    <span style="color: rgba(85, 249, 101, 0.904);">y</span>
    
</h1>
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link style="color:white;font-size:20px;font-weight:400;" class="nav-link active" aria-current="page" to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link style="color:white;font-size:20px;font-weight:400;" class="nav-link" to="/login">Login</router-link>
        </li>
        <li class="nav-item">
          <router-link style="color:white;font-size:20px;font-weight:400;" class="nav-link" to="/register">Register</router-link>
        </li>
        <li class="nav-item">
          <router-link style="color:white;font-size:20px;font-weight:400;" class="nav-link" to="/sm-register">Register as Store Manager</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>`
  
}
