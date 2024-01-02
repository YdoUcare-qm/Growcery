export default {
    template: `<div class="p-2 m-2" style="background-color: rgba(230, 230, 230); border-radius: 30px; width: 90%; display: flex; align-items: center; justify-content: space-between;">

    <h4>{{ rrequest.id }}</h4>
    <p>Store Name: {{ rrequest.sname }}</p>
    <p>Email ID: {{ rrequest.email }}</p>
    <p>Username: {{ rrequest.username }}</p>

    <div>
        <button @click="approve(1)" class="btn btn-success" style="height: 50px;width: 50px;border-radius:30px;text-align:center;">&#10003;</button>
        <button @click="approve(0)" class="btn btn-danger" style="height: 50px;width: 50px;border-radius:30px;text-align:center;">X</button>
    </div>
</div>`,
  
      props: ['rrequest'],

      data(){
        return {
            authToken: localStorage.getItem('auth-token'),
        }
      },
      methods:{

        async approve(x) {
            try {
              const requestData = {
                id : this.rrequest.id,
                status:x,
                          
              }
    
              console.log(JSON.stringify(requestData ))
        
              const res = await fetch('/api/admin', {
                method: 'PUT',
                headers: {
                  'Content-Type': 'application/json',
                  'Authentication-Token': this.authToken,
                },
                body: JSON.stringify(requestData),
              });
        
              if (res.ok) {
                const data = await res.json();
                location.reload()
                alert(data.message)
                
                
              } else {
                const data = await res.json();
                console.log(data.message)
                alert(data.message);
                
              }
            } catch (error) {
              
              console.error('Error :', error);
              alert('Error Processing Request. Please try again.');
            }
            
          
    
          },

        







    }

}