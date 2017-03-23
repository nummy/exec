var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var User = new Schema({
	username:{type:String,required:true, unique:true},
	firstname:{type:String,default:""},
	lastname:{type:String,default:""},
	sex:{type:String,default:""},
	age:{type: Number, default: 0}
});

var Store = new Schema({
	storename:{type:String,required:true},
	category:{type:String,default:""},
	address:{type:String,default:""},
});

var Review = new Schema({
	userID:{type:String,required:true,},
	storeID:{type:String,default:"",required:true},
	rate:{type:Number,default:0,required:true, min:0, max:10},
	comment:{type:String,default:""}
});

exports.User = mongoose.model('User', User);
exports.Store = mongoose.model('Store', Store);
exports.Review = mongoose.model('Review', Review);
