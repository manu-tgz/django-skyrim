
let btnEdit=document.getElementById('btn-edit')
let btnSubmit=document.getElementById('btn-submit')
let firstName=document.getElementById('firstName')
let lastName=document.getElementById('lastName')
let email=document.getElementById('email')
let username=document.getElementById('username')
let password1=document.getElementById('password1')
let password2=document.getElementById('password2')
let hidden=document.getElementById('hidden')


function myenable(){
    firstName.disabled=false
    lastName.disabled=false
    email.disabled=false
    username.disabled=false
    password1.disabled=false
    password2.disabled=false
    hidden.style.display='block'

    const container=document.getElementById('profile')

    container.innerHTML= `<button type="submit" class="btn btn-primary" style="margin-top: 20px; font-size: 18pt;" id="btn-submit"><i class="fa fa-check" aria-hidden="true"></i></button>
                          <button type="button" class="btn btn-secondary" style="margin-top: 20px; font-size: 18pt;" onclick="mydisable()"><i class="fa fa-times fa-check" aria-hidden="true"></i></button>`
    
    
}

 function mydisable(){
     firstName.disabled=true
     lastName.disabled=true
     email.disabled=true
     username.disabled=true
     password1.disabled=true
     password2.disabled=true
     hidden.style.display= 'none'

     const container=document.getElementById('profile')
     container.innerHTML= `<button type="button" class="btn btn-secondary" style=" margin-top: 20px; font-size: 18pt;" onclick="myenable()" id="btn-edit"><i class="fa fa-pencil fa-fw"></i></button>`
     
     const messages=document.getElementById('messages')
     messages.innerText=""
                   
 }



