//這邊必須要async funciton 因為python返回需要時間，而JS 又不會block，
//所以需要用async function 加上await去呼叫PY function
async function connect(){ 
    let client_id = document.getElementById('client_id').value;
    result = await eel.connect_rpc(client_id)()  
}
async function update(){ 
    let client_id = document.getElementById('client_id').value;
    let state = document.getElementById('state').value;
    let img_url = document.getElementById('img_url').value;
    result = await eel.update(client_id, state, img_url)()  
}
async function disconnect(){ 
    result = await eel.disconnect_rpc(client_id)()  
    
    //最後將返回的值設定在HTML上的<p>內
    document.querySelector('p').textContent = "close"
}