var express = require('express');
var router = require('./router');
var bodyParser = require("body-parser");

var app = express();
app.use(bodyParser.json());
app.use(router);

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('app listening at http://%s:%s', host, port);
});