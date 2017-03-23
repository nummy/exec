var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var models = require('./models');
var User = models.User;
var Store = models.Store;
var Review = models.Review;

mongoose.connect("mongodb://localhost/demo");

router.get('/users', function (req, res) {
	User.find(req.query, function(err, doc) { 
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
	try{
		var sid = mongoose.Types.ObjectId(id); 
		User.update({_id:sid},data, function(err, doc){
			if(err){
				res.sendStatus(404);
			}else{
				if(doc.n ==  1){
					User.findOne({_id:sid}, function(err, user){
						res.json(user);
					});
				}else{
					res.sendStatus(404);
				}
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
	try{
		var sid = mongoose.Types.ObjectId(id);
		Review.remove({userId:id}); 
		User.remove({_id:sid}, function(err, result){
			if(err){
				res.sendStatus(404);
			}else{
				res.json({"ret":0,"deleted":1});
			}
		});
	}catch(e){
		res.sendStatus(404);
	}
});

/*router for store*/
router.get('/stores', function (req, res) {
	Store.find(req.query, function(err, doc) { 
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
					if(store){
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
		Store.update({_id:sid}, data, function(err, doc){
			if(err){
				res.sendStatus(404);
			}else{
				if(doc.n == 1){
					Store.findOne({_id:sid}, function(err, store){
						res.json(store);
					})
				}else{
					res.sendStatus(404)
				}
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
			Review.remove({storeId:id});
			Store.remove({_id:sid}, function(err, store){
				if(err){
					res.sendStatus(404);
				}else{
					res.json({"ret":0,"deleted":1})
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
	var userId = req.query.userid;
	if(id){
		try{
			var sid = mongoose.Types.ObjectId(id); 
			Review.findOne({_id:sid}, function(err, doc) { 
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
		console.log(121);
		Review.find({storeID:storeId}, function(err, doc) { 
        	if(err){
        		res.sendStatus(404);
        	}
        	res.json({"reviews":doc}); 
    	}); 
	}

	if(userId){ 
		console.log(1212);
		Review.find({userID:userId}, function(err, doc) { 
        	if(err){
        		res.sendStatus(404);
        	}
        	res.json({"reviews":doc}); 
    	}); 
	}
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
	var storeId = req.query.storeID;
	var userId = req.query.userID;
	if(id){
		console.log(12);
		try{
			var sid = mongoose.Types.ObjectId(id); 
			Review.remove({_id:sid}, function(err, result){
				if(err){
					res.sendStatus(404);
				}else{
					res.json("ok");
				}
			});
		}catch(e){
			res.sendStatus(404);
		}
	}
	if(storeId){
		console.log(121);
		Review.remove({storeID:storeId}, function(err, result){
			if(err){
				res.sendStatus(404);
			}else{
				res.json("ok");
			}
		});
	}
	if(userId){
		console.log(1122);
		Review.remove({userID:userId}, function(err, result){
			if(err){
				res.sendStatus(404);
			}else{
				res.json("ok");
			}
		});
	}
});

router.post('/review', function(req, res){
	var data = req.body;
	var userID = data.userID;
	var storeID = data.storeID;
	var rate = parseInt(data.rate);

	if(storeID && userID && rate >=0 && rate<=10){
		console.log(12);
		var review = Review(data);
		review.save(function(err, s){
			if(err){
				console.log(err);
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