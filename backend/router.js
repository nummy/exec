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
	if(id || username){
		if(id){
			try{
				var sid = mongoose.Types.ObjectId(id); 
				User.findOne({_id:sid}, function(err, user){
					if(err){
						res.sendStatus(404);
					}else{
						if(user){
							res.json(user);
						}else{
							res.sendStatus(404);
						}
					}
				});
			}catch(e){
				res.sendStatus(404);
			}
		
		}
		if(username){
			User.findOne({username:username}, function(err, user){
				if(err){
					res.sendStatus(404);
				}else{
					if(user){
						res.json(user);
					}else{
						res.sendStatus(404);
					}
					
				}
			});
		}
	}else{
		res.sendStatus(404);
	}
	
});

router.put('/user', function(req, res){
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