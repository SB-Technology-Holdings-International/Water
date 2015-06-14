$.ajax({
    url: 'http://192.168.1.168:9000',
    type:'POST',
    data:
    {
        ssid: 'sdfsdfsd',
        passwd: '3gs'
    },
    success: function(msg)
    {
        alert('Info Sent');
    }
});
