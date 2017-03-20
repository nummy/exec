var express = require('express');
var app = express();

app.get('/users', function (req, res) {
  res.send('Hello World!');
});

app.put('/user', function(req, res){
	res.send("put user");
});

app.post('/user', function(req, res){
	res.send('post user');
});

app.delete('/user', function(req, res){
	res.send('delete user');
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('app listening at http://%s:%s', host, port);
});