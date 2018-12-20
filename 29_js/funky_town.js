// Team extends Everything
// Hasif Ahmed and Aleksandra
// SoftDev1 pd8
// K29 -- Sequential Progression II: Electric Boogaloo
// 2018-12-20


var fibonacci = function(n){
    if(n == 0 || n == 1){
	return n;
    } else {
	return fibonacci(n-1) + fibonacci(n-2);
    }
}
var gcd = function(a,b){
    if(a == b){
	return a;
    }

    var g = 0;
    if(a < b){
	smaller = a;
    } else {
	smaller = b;
    }

    div = smaller;

    while(div >= 1){
	if( a % div == 0 && b % div == 0){
	    g = div;
	    return div;
	}
	div--;
    }
}

var students = ['Aaron', 'Emma', 'Bo'];

var randomStudent = function(){
    var randint = Math.floor(Math.random() * 10) % students.length;
    return students[randint];
}

var displayfib = () => {
    var results = fibonacci(2);
    console.log(results);
    document.getElementById('fib_res').innerHTML = results;
};

var displayrs = () => {
    var results = randomStudent();
    console.log(results);
    document.getElementById('randstu_res').innerHTML = results;
};

var displaygcd = () => {
    var results = gcd(100,90);
    console.log(results);
    document.getElementById('gcd_res').innerHTML = results;
};

var fibbut = document.getElementById("fib");
//console.log(fibbut);
fibbut.addEventListener('click', displayfib);

var stud = document.getElementById("randstu");
//console.log(stud);
stud.addEventListener('click', displayrs);

var great = document.getElementById("gcd");
//console.log(great);
great.addEventListener('click', displaygcd);
