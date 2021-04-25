const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

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
    if (message.length < 2 || message.length > 30) {
        document.getElementById('error').classList.remove('d-none')
        return null
    }
    document.getElementById('error').classList.add('d-none')
    message = `<div class="bg-warning my-2 p-2 rounded" style="display: inline-block; font-size: 20px;">
            <div style="display: flex; flex-direction: row; align-items: center;">
            {% if request.user.avatar %}
            <img src='https://cdn.discordapp.com/avatars/{{loginuser.id}}/{{loginuser.avatar}}.png' width="20px" style="border-radius: 50%;">
            {% else %}
            <img src="https://discord.com/assets/1cbd08c76f8af6dddce02c5138971129.png" width="20px" style="border-radius: 50%;">
            {% endif %}
            <strong class="text-success mx-2" style="font-size: 16px">` + cuser + "</strong></div>" + message + "</div><br>"
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
    var textarea = document.getElementById('chat-log')
    if (textarea.selectionStart == textarea.selectionEnd) {
        textarea.scrollTop = textarea.scrollHeight;
    }
};