/*
 IMG SOURCE: http://glyph.smarticons.co/
 COPYRIGHT: Creative Commons Attribution-Share Alike 3.0 Unported License
 */

var num = 0;
var balance = 0;
var round = 0;


function isSame(dices){
	/*
	if all the dices value are the same, then return true, else return false
	@param dices: list of dice value
	@return: true or false
	 */
	if(dices.length <= 1){
		return true;
	}
	var start = dices[0];
	for(var i =0; i<dices.length; i++){
		if(dices[i] != start){
			return false;
		}
	}
	return true;
}

function isPartSame(dices){
	/*
	if N-1 of the dices are the same, then return true
	@param dices: list of dice value
	@return: true or false
	 */
	var length = dices.length;  // length of the dices
	var dict = {};				// store dice value and its count
	for(var i=0; i<dices.length; i++){
		if(dices[i] in dict){
			dict[dices[i]] += 1
		}
		else{
			dict[dices[i]] = 1
		}
	}
	var keys = Object.keys(dict);
	if(keys.length != 2){
		return false;
	}
	else{
		if((dict[keys[0]] == length-1 && dict[keys[1]] == 1) || (dict[keys[1]] == length-1 && dict[keys[0]] == 1)){
			return true;
		}else{
			return false;
		}
	}
}

function isSequence(dices){
	/*
	if the dices value are a sequence, then return true
	@param dices: list of dice value
	@return: true or false
	 */
	if(dices.length <= 2){
		return true;
	}
	dices.sort();
	var start = dices[0];
	var second = dices[1];
	var delta = second - start;
	for(var i=2; i<dices.length; i++){
		var value = dices[i] - dices[i-1];
		if(value != delta){
			return false
		}
	}
	return true;
}

function isDifferent(dices){
	/*
	if all dice value are different, return true
	@param dices: list of dices
	@return: true or false
	 */
	if(dices.length<=1){
		return true;
	}
	var dict = {};
	for(var i=0; i<dices.length; i++){
		var dice = dices[i];
		if(!(dice in dict)){
			dict[dice] = 1
		}
	}
	var keys = Object.keys(dict);
	return keys.length == dices.length;
}

function getPoint(dices){
	/*
	get poPoint of the dices
	@param dices: list of dice value
	@return: point of the dices, integer
	 */
	var sum = 0; // first get all sum of the dices
	for(var i=0; i<dices.length; i++){
		sum += dices[i];
	}
	if(isSame(dices)){
		return 60 + sum;
	}else if(isPartSame(dices)){
		return 40 + sum;
	}else if(isSequence(dices)){
		return 20 + sum;
	}else if(isDifferent(dices)){
		return sum;
	}else{
		return 0;
	}
}

function showMsg(msg){
	/*
	show message
	@param msg: message
	 */
	var dom = document.getElementById("msg");
	dom.innerHTML = msg;
}


function addDice(dices){
	/*
	add dice to the html
	@param dices: list of dices
	 */
	var diceDiv = document.getElementById("dice");
	diceDiv.style.display= "block";
	diceDiv.innerHTML = "";
	
	var imgs = [];
	// create img element
	for(var i=0; i<dices.length; i++){
		var img = createImg(dices[i]);
		diceDiv.appendChild(img);
	}
}

function createImg(number){
	/*
	create img tag with the number
	@param number: img number
	@return: dom object
	 */
	var elem = document.createElement("img");
	elem.src = "./img/" + number + ".png";
	return elem;
}



function playRound(){
	/*
	play one round
	 */
	var dices = getRandomDice();
	addDice(dices); // create tag first, then do the animation
	animation();
}

function stopAnimation(handler){
	/*
	stop animation
	@param handler: interval handler
	 */
	var dices = getRandomDice();
	addDice(dices);
	var point = getPoint(dices);
	balance += point;
	round += 1;
	updateStatus(balance, round, point);  // update status
}


function changeImg(){
	/*
	update img source, for animation
	 */
	var diceDiv = document.getElementById("dice");
	var children = diceDiv.children;
	var dices = getRandomDice();
	for(var i=0; i<children.length; i++){
		var img = children[i];
		img.src = "./img/" + dices[i] + ".png";
	}
}

function animation(){
	/*
	change img src per 50 milliseconds,clear the interval 1 seconds later
	 */
	var handler = setInterval(changeImg, 50);
	setTimeout((function(handler){
		return function(){
			clearInterval(handler);
			stopAnimation();
		}
	})(handler),1000);
}


function getRandomDice(){
	/*
	get random dice value list
	@return: list of dices
	 */
	var dices = [];
	for(var i=0; i<num; i++){
		dices.push(Math.floor(Math.random()*6) + 1);
	}
	return dices;
}

function updateStatus(balance, round, point){
	/*
	update balance, round, potint status
	@param balance: balance point
	@param round: round
	@param point: current round point
	 */
	var balanceElem = document.getElementById("balance");
	var roundElem = document.getElementById("round");
	var pointElem = document.getElementById("point");
	balanceElem.innerHTML = balance;
	roundElem.innerHTML = round;
	pointElem.innerHTML = point;
}


function setup(){
	/**
	 * setup operations
	 */
	var continueBtn = document.getElementById("continue");
	var playBtn = document.getElementById("play");
	var endBtn = document.getElementById("end");
	var numDiv = document.getElementById("num");
	var diceDiv = document.getElementById("dice");
	diceDiv.style.display= "none";
	numDiv.value = "";
	playBtn.style.display = "inline";
	continueBtn.style.display = "none";
	endBtn.style.display = "none";
	showMsg("");
}

document.getElementById("play").onclick = function(){
	/**
	 * click event for play button
	 */
	var promptDiv = document.getElementById("prompt");
	var confirmBtn = document.getElementById("confirm");
	var playBtn = document.getElementById("play");
	var diceDiv = document.getElementById("dice");
	var resultDiv = document.getElementById("result");
	var stageElem = document.getElementById("stage");
	stageElem.innerHTML = "Setup";
	resultDiv.style.display = "none";
	diceDiv.style.display= "none";
	diceDiv.innerHTML = "";
	promptDiv.style.display = "block";
	confirmBtn.style.display = "inline";
	playBtn.style.display = "none";
	num = 0;
	round = 0;
	balance = 0;
};



document.getElementById("confirm").onclick = function(){
	/**
	 * click event for confirm button
	 */
	num = document.getElementById("num").value;
	if(num <3 || num >6){
		showMsg("The dice number must between 3 and 6");
	}else{
		var promptDiv = document.getElementById("prompt");
		var continueBtn = document.getElementById("continue");
		var endBtn = document.getElementById("end");
		var confirmBtn = document.getElementById("confirm");
		var stageElem = document.getElementById("stage");
		stageElem.innerHTML = "Play";
		continueBtn.style.display = "inline";
		endBtn.style.display = "inline";
		confirmBtn.style.display = "none";
		promptDiv.style.display= "none";
		showMsg("");
		playRound();
	}
};

document.getElementById("continue").onclick = function(){
	/**
	 * click event for continue button
	 */
	playRound();
};
document.getElementById("end").onclick = function(){
	/**
	 * click event for stop button
	 */
	var resultDiv = document.getElementById("result");
	resultDiv.style.display = "block";
	var roundSpan = document.getElementById("roundRes");
	var balanceSpan = document.getElementById("balanceRes");
	var avgSpan = document.getElementById("avg");
	roundSpan.innerHTML = round;
	balanceSpan.innerHTML = balance;
	avgSpan.innerHTML = balance/round;
	var stageElem = document.getElementById("stage");
	stageElem.innerHTML = "End";
	setup();
};


/*
function test(){
	// test function
	var dices = [3,3,3,3];
	console.log(getPoint(dices)==72);
	dices = [4,4,4,6];
	console.log(getPoint(dices)==58);
	dices = [2,5,2,2];
	console.log(getPoint(dices)==51);
	dices = [3,4,5,6];
	console.log(getPoint(dices)==38);
	dices = [4,3,2,1];
	console.log(getPoint(dices)==30);
	dices = [4,6,3,5];
	console.log(getPoint(dices)==38);
	dices = [4,5,3,1];
	console.log(getPoint(dices)==13);
	dices = [3,6,2,5];
	console.log(getPoint(dices)==16);
	dices = [4,5,3,3];
	console.log(getPoint(dices)==0);
}

test();
*/