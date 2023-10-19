async function connect(){ 
    let client_id = document.getElementById('client_id').value;
    result = await eel.connect_rpc(client_id)();
    let inputElements = document.getElementsByTagName('input');
    for(let i = 0; i<inputElements.length;i++){
        console.log(i);
        inputElements[i].disabled = false;
    }
}
async function update(){ 
    let client_id = document.getElementById('client_id').value;
    let details = document.getElementById('details').value;
    let state = document.getElementById('state').value;
    let img_url = document.getElementById('img_url').value;
    let little_img = document.getElementById('little_img').value;
    result = await eel.update(details, state, img_url, little_img)();
}
async function disconnect(){ 
    result = await eel.disconnect_rpc(client_id)();
    
    //最後將返回的值設定在HTML上的<p>內
    document.querySelector('p').textContent = "close";
}