var express = require('express');
var path = require('path');
var router = require('./router');
var bodyParser = require("body-parser");

var app = express();
app.use(bodyParser.json());
app.use(router);
app.use(express.static(path.join(__dirname, 'public')))

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('app listening at http://%s:%s', host, port);
});