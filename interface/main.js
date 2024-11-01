async function connect() {
  let client_id = document.getElementById("client_id").value;
  await eel.connect_rpc(client_id)();

  if (!client_id) {
    alert("client_id error");
    return;
  } else {
    let inputElements = document.getElementsByTagName("input");
    for (let i = 0; i < inputElements.length; i++) {
      inputElements[i].disabled = false;
    }
    let disconnect_button = document.getElementById("disconnect_button");
    let connect_button = document.getElementById("connect_button");
    disconnect_button.setAttribute(
      "class",
      "waves-effect waves-light btn-flat"
    );
    connect_button.setAttribute(
      "class",
      "waves-effect waves-light btn-flat disabled"
    );
  }
}
async function update() {
  let deliver = new Map();
  deliver["details"] = document.getElementById("details").value;
  deliver["state"] = document.getElementById("state").value;
  deliver["img_url"] = document.getElementById("img_url").value;
  deliver["little_img"] = document.getElementById("little_img").value;

  await eel.update(deliver)();
}
async function disconnect() {
  await eel.disconnect_rpc()();
  let disconnect_button = document.getElementById("disconnect_button");
  let connect_button = document.getElementById("connect_button");
  disconnect_button.setAttribute(
    "class",
    "waves-effect waves-light btn-flat disabled"
  );
  connect_button.setAttribute("class", "waves-effect waves-light btn-flat");

  let inputElements = document.getElementsByTagName("input");
  for (let i = 1; i < inputElements.length; i++) {
    console.log(i);
    inputElements[i].disabled = true;
  }

  // document.querySelector('p').textContent = "close";
}
