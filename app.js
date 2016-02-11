var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var host, port;
host = 'http://localhost';
port = 3000;

app.use(express.static(__dirname + "/public"));
app.use('/bower_components', express.static(__dirname + '/bower_components'));

io.on('connection', function(socket) {
  console.log('a user just connected');
});

http.listen(3000, function () {
  console.log('listening on port ' + port + "...");
});
