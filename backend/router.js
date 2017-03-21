var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var models = require('./models');
var User = models.User;

mongoose.connect("mongodb://localhost/demo");

router.get('/users', function (req, res) {
	var query = req.query;
	var params = {};
	if(query){
		params = query;
	}
	User.find(query, function(err, doc) { 
        res.json(doc); 
    }); 
});

router.get('/user', function(req, res){
	var id = req.query.id;
	var username = req.query.username;
	User.find({id:id}, function(err, doc) { 
        res.json(doc); 
    }); 
});

router.put('/user', function(req, res){
	var id = req.query.id;
	if(id){

	}else{
		
	}
	res.send("put user");
});

router.post('/user', function(req, res){
	var user = new User({ 
        "username": "m1ssionP0zzible",
        "firstname":"Tom",
        "lastname":"Cruise",
        "sex": "M",
        "age": 54
    }); 
    user.save(); 
	res.send('post user');
});

router.delete('/user', function(req, res){
	var id = req.query.id;
	if(id){

	}else{

	}
	res.send('delete user');
});

module.exports = router;