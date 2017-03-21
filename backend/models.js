var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var User = new Schema({
	username:{type:String,required:true, unique:true},
	firstname:{type:String,default:""},
	lastname:{type:String,default:""},
	sex:{type:String,default:""},
	age:{type: Number, default: 0}
});

exports.User = mongoose.model('User', User);