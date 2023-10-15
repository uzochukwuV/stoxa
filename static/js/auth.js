



var email = document.getElementById('register_email')
var username = document.getElementById('register_username')

email.addEventListener('keyup', (e)=>{
    let value = e.target.value
    
    if (value.length > 3){
       fetch('/validate_email', {
        body: JSON.stringify({email: value}),
        method: 'POST',
       })
       .then((res)=>{
        res.json().then((e)=>console.log(e))
       })
       .catch((e)=>{
        console.log(e)
       })
    }
});

username.addEventListener('keyup', (e)=>{
    let value = e.target.value
    
    if (value.length > 3){
       fetch('/validate_username', {
        body: JSON.stringify({username: value}),
        method: 'POST',
       })
       .then((res)=>{
        res.json().then((e)=>console.log(e))
       })
       .catch((e)=>{
        console.log(e)
       })
    }
});