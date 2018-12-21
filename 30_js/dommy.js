// Team extends Everything (Hasif Ahmed, Thomas Zhao)
// SoftDev pd8
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-21

var changeHeading = function(e){
    var h = document.getElementById("h");
    h.innerHTML = this.innerHTML;
    console.log(e);
};

var changeHeadingBack = function(e){
    var h = document.getElementById("h");
    h.innerHTML = "Hello World"
    console.log(e);
};

var removeItem = function(e){
    this.remove();
};

var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++){
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', changeHeadingBack);
    lis[i].addEventListener('click', removeItem)
}


var addItem = function(e){
    var list = document.getElementById('thelist');
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    list.appendChild(item);
    item.addEventListener('click', removeItem);
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', changeHeading);
};



var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n){
    if(n < 2){
	return 1;
    }
    else{
	return fib(n-1) + fib(n-2);
    }
};


var counter = 1;
var addFib = function(){
    var list = document.getElementById('fiblist');
    var item = document.createElement("li");
    list.appendChild(item);
    item.innerHTML = "" + fib(counter);
    counter += 1;
    //INSERT STUFF HERE
};

/*
var addFib2 = function(e){
    console.log(e);
    //INSERT STUFF HERE, THIS ONE IS DYNAMIC PROGRAMMING (SEE QAF)
};
*/

var fb = document.getElementById('fb');
fb.addEventListener("click", addFib);


/*
// THE THINGS WE DID TOGETHER IN CLASS
var title = document.getElementById("thelist");
title.addEventListener('mouseover', function(e){console.log(e);});


var button = document.getElementById("b");
button.addEventListener('click',function(e){ console.log(e);});

var button2 = document.getElementById("fb");
button2.addEventListener('click',function(e){ console.log(e);});
*/
