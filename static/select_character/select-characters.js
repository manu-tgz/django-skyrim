
let added=[]
let removed=[]

function add(btn){
    const id=btn.id
    const index = removed.indexOf(id)
    if(index !== -1)
    {
        removed.splice(index,1)
    }
    else
    {
        added.push(id)
    }
    const container=document.getElementById("container-"+id)
    container.innerHTML=`<button type="button" id="${id}" onclick="remove(this)" class="btn btn-outline-danger"><i class="fa fa-minus" aria-hidden="true"></i></button>`

    const list_container = document.getElementById("container-list")
    list_container.textContent = ""
    for (let index = 0; index < added.length; index++) {
        list_container.innerHTML += `<input type="hidden" name="register_fighter" value="${added[index]}">`
    }
    for (let index = 0; index < removed.length; index++) {
        list_container.innerHTML += `<input type="hidden" name="remove_fighter" value="${removed[index]}">`
    }
}

function remove(btn){
    const id=btn.id
    const index = added.indexOf(id)
    if(index !== -1)
    {
        added.splice(index,1)
    }
    else
    {
        removed.push(id)
    }
    
    const container=document.getElementById("container-"+id)
    container.innerHTML=`<button type="button" id="${id}" onclick="add(this)" class="btn btn-outline-success"><i class="fa fa-plus" aria-hidden="true"></i></button>`

    const list_container = document.getElementById("container-list")
    list_container.textContent = ""
    for (let index = 0; index < added.length; index++) {
        list_container.innerHTML += `<input type="hidden" name="register_fighter" value="${added[index]}">`
    }
    for (let index = 0; index < removed.length; index++) {
        list_container.innerHTML += `<input type="hidden" name="remove_fighter" value="${removed[index]}">`
    }

}

function myclear(){
    const container_preview = document.getElementById('container-preview_filters')
    container_preview.textContent = ""
}