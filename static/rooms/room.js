const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onopen = function(e) {
    cuser = document.getElementById('cuser').textContent
    message = `<div class="text-white my-2 p-1 rounded text-center" style="display: block; font-size: 16px;">` + cuser + ` joined the room</div>`
    chatSocket.send(JSON.stringify({
        'message': message
    }));
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').innerHTML += (data.message + '\n');
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    cuser = document.getElementById('cuser').textContent
    cuserid = document.getElementById('cuserid').textContent
    cuseravatar = document.getElementById('cuseravatar').textContent
    if (cuseravatar.length < 1) {
        link = 'https://discord.com/assets/1cbd08c76f8af6dddce02c5138971129.png'
    } else {
        link = `<img width="20px" height="20px" style="border-radius: 50%;" src="https://cdn.discordapp.com/avatars/` + cuserid + `/` + cuseravatar + `.png">`
    }
    if (message.length < 2) {
        document.getElementById('error').classList.remove('d-none')
        return null
    }
    document.getElementById('error').classList.add('d-none')
    message = `<div class="bg-warning my-2 p-2 rounded" style="display: inline-block; font-size: 20px;">
            <div style="display: flex; flex-direction: row; align-items: center;">` + link +
        `<strong class="text-success mx-2" style="font-size: 16px">` + cuser + "</strong></div style='white-space: normal;'>" + message + "</div><br>"
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
    var textarea = document.getElementById('chat-log')
    if (textarea.selectionStart == textarea.selectionEnd) {
        textarea.scrollTop = textarea.scrollHeight;
    }
};