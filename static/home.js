$(document).ready(()=>{
    const socket = io();

    socket.on('connect', ()=>{
        console.log('connected to home')
        //setInterval(function(){ alert("Hello"); }, 10000);
        socket.emit('home_connection')
    });
    /*
    window.addEventListener('beforeunload', function (e) {
        clearInterval()
    });
    */
});


