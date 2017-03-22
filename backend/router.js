var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var models = require('./models');
var User = models.User;
var Store = models.Store;
var Review = models.Review;

mongoose.connect("mongodb://localhost/demo");

router.get('/users', function (req, res) {
	var query = req.query;
	var params = {};
	if(query){
		params = query;
	}
	User.find(query, function(err, doc) { 
        res.json({"users":doc}); 
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
	var id = req.query.id;
	var data = req.body;
	delete data.username;
	delete data.firstname;
	delete data.lastname;
	try{
		var sid = mongoose.Types.ObjectId(id); 
		User.update({_id:sid},data, function(err, user){
			if(err){
				res.sendStatus(404);
			}else{
				res.json(user);
			}
		});
	}catch(e){
		res.sendStatus(404);
	}
});

router.post('/user', function(req, res){
	var data = req.body;
	var username = data.username;
	if(username){
		var user = User(data);
		user.save(function(err, u){
			if(err){
				res.sendStatus(403);
			}else{
				res.json(u);
			}
		});
	}else{
		res.sendStatus(403);
	}
});

router.delete('/user', function(req, res){
	var id = req.query.id;
	if(id){
		try{
			var sid = mongoose.Types.ObjectId(id); 
			User.remove({_id:sid}, function(err, user){
				if(err){
					res.sendStatus(404);
				}else{
					res.json("ok")
				}
			});
		}catch(e){
			res.sendStatus(404);
		}
	}else{
		res.sendStatus(404);
	}
});

/*router for store*/
router.get('/stores', function (req, res) {
	var query = req.query;
	var params = {};
	if(query){
		params = query;
	}
	Store.find(query, function(err, doc) { 
        res.json({"stores":doc}); 
    }); 
});

router.get('/store', function(req, res){
	var id = req.query.id;
	if(id){
		try{
			var sid = mongoose.Types.ObjectId(id); 
			Store.findOne({_id:sid}, function(err, store){
				if(err){
					res.sendStatus(404);
				}else{
					if(user){
						res.json(store);
					}else{
						res.sendStatus(404);
					}
				}
			});
		}catch(e){
			res.sendStatus(404);
		}
	}else{
		res.sendStatus(404);
	}
});

router.put('/store', function(req, res){
	var id = req.query.id;
	var data = req.body;
	try{
		var sid = mongoose.Types.ObjectId(id); 
		Store.update({_id:sid}, data, function(err, store){
			if(err){
				res.sendStatus(404);
			}else{
				res.json(store);
			}
		});
	}catch(e){
		res.sendStatus(404);
	}
});

router.delete('/store', function(req, res){
	var id = req.query.id;
	if(id){
		try{
			var sid = mongoose.Types.ObjectId(id); 
			Store.remove({_id:sid}, function(err, store){
				if(err){
					res.sendStatus(404);
				}else{
					res.json("deleted")
				}
			});
		}catch(e){
			res.sendStatus(404);
		}
	}else{
		res.sendStatus(404);
	}
});

router.post('/store', function(req, res){
	var data = req.body;
	var storename = data.storename;
	if(storename){
		var store = Store(data);
		store.save(function(err, s){
			if(err){
				res.sendStatus(403);
			}else{
				res.json(s);
			}
		});
	}else{
		res.sendStatus(403);
	}
});

/*route for review*/
router.get('/review', function (req, res) {
	var id = req.query.id;
	var storeId = req.query.storeid;
	var userId = req.query.userId;
	if(id){
		try{
			var sid = mongoose.Types.ObjectId(id); 
			Review.findOne({id:sid}, function(err, doc) { 
        		if(err){
        			res.sendStatus(404);
        		}
        		res.json(doc); 
    		}); 
		}catch(e){
			res.sendStatus(404);
		}
	}

	if(storeId){ 
		Review.find({storeId:storeId}, function(err, doc) { 
        	if(err){
        		res.sendStatus(404);
        	}
        	res.json({"reviews":doc}); 
    	}); 
	}

	if(userId){ 
		Review.find({userId:userId}, function(err, doc) { 
        	if(err){
        		res.sendStatus(404);
        	}
        	res.json({"reviews":doc}); 
    	}); 
	}
	return res.json({"reviews":[]});
});


router.put('/review', function(req, res){
	var id = req.query.id;
	var data = req.body;
	delete data.storeId;
	delete data.userId;
	try{
		var sid = mongoose.Types.ObjectId(id); 
		Review.update({_id:sid}, data, function(err, store){
			if(err){
				res.sendStatus(404);
			}else{
				res.json(store);
			}
		});
	}catch(e){
		res.sendStatus(404);
	}
});

router.delete('/review', function(req, res){
	var id = req.query.id;
	var storeId = req.query.storeId;
	var userId = req.query.userId;
	if(id){
		try{
			var sid = mongoose.Types.ObjectId(id); 
			Review.remove({_id:sid}, function(err, store){
				if(err){
					res.sendStatus(404);
				}else{
					res.json("deleted")
				}
			});
		}catch(e){
			res.sendStatus(404);
		}
	}
	if(storeId){
		Review.remove({storeId:storeId}, function(err, store){
			if(err){
				res.sendStatus(404);
			}else{
				res.json("deleted")
			}
		});
	}
	if(userId){
		Review.remove({userId:userId}, function(err, store){
			if(err){
				res.sendStatus(404);
			}else{
				res.json("deleted")
			}
		});
	}
	res.sendStatus(404);
});

router.post('/review', function(req, res){
	var data = req.body;
	var userId = data.userId;
	var storeId = data.storeId;
	var rate = parseInt(data.rate);
	if(storeId && userId && rate >=0 && rate<=10){
		var Review = Review(data);
		Review.save(function(err, s){
			if(err){
				res.sendStatus(403);
			}else{
				res.json(s);
			}
		});
	}else{
		res.sendStatus(403);
	}
});


module.exports = router;