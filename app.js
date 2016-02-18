var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var mongo = require('mongodb').MongoClient;

var host, port;
host = 'http://localhost';
port = 5000;

app.use(express.static(__dirname + "/public"));
app.use('/bower_components', express.static(__dirname + '/bower_components'));

mongo.connect('mongodb://localhost/greenlightdb', function (error, db) {
  if (error) {
    return error;
  }

  var logs = db.collection('logs');
  var date = new Date();
  logs.insert({
    'date': date
  });
});

// trafficLight model
var trafficLight = {
  "lights": {
    "red": {
      "status": "off"
    },
    "yellow": {
      "status": "on"
    },
    "green": {
      "status": "off"
    }
  },
  "mode": "normal",
  getLights: function () {
    return this.lights;
  },
  getLightStatus: function(light) {
    return this.lights[light].status;
  },
  setLightStatus: function(light, status) {
    this.lights[light].status = status;
  }
}

// server-side events
io.on('connection', function(socket) {

  // update css on connection (based on trafficLight model)
  socket.emit('update frontend', trafficLight.lights);

  // update trafficLight state based on button click event
  socket.on('lite clicked', function (liteId) {
    var light = liteId.split('-')[0];

    // debug mode
    if (trafficLight.mode === 'debug') {
      var currentStatus = trafficLight.lights[light].status;
      trafficLight.setLightStatus(light, (currentStatus === 'on' ? 'off' : 'on'));

    }
    // normal mode
    else {
      for (lite in trafficLight.lights) {
        trafficLight.setLightStatus(lite, 'off');
      }
      trafficLight.setLightStatus(light, 'on');
    }
    io.emit('update frontend', trafficLight.lights);
  });

  socket.on('disconnect', function () {

  });

});

http.listen(port, function () {
  console.log('listening on port ' + port + "...");
});
