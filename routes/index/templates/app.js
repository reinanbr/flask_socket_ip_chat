function generateKey() {
    var chars = '0123456789abcdefghijklmnopqrstuvwxyz';
    var length = 8;
    var key = '';
    for (var i = 0; i < length; i++) {
      var randomIndex = Math.floor(Math.random() * chars.length);
      key += chars.charAt(randomIndex);
    }
    return key;
  }
  



const socket = io('http://192.168.3.57:5000')
username=generateKey()

socket.on('connect', function() {
    socket.emit('connected', {'userKey':username,'text': 'I\'m connected!'});
    socket.on('connected',(data)=>{
        console.log(data)
        if(data.connected){
            $('#server_status').html(`<small>${data.user.session_id} [${data.countUsers} users online]</small><i title='Server Online' class="material-icons" style='color:green'>brightness_1</i>`)
        }

    });
});
socket.on('disconnect',()=>{
    socket.emit('disconnect');
    $('#server_status').html(`<i title='Server Offline' class="material-icons red">brightness_1</i>`)
});

window.onbeforeunload = function () {
    socket.emit('disconnected', {'userKey':username,'text':`I'm exit`});

}