var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var User = new Schema({
	username:String,
	firstname:String,
	lastname:String,
	sex:String,
	age:int
});

exports.User = mongoose.model('User', User);