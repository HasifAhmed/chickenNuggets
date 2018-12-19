// Team extends Everything
// Hasif Ahmed and Thomas Zhao
// SoftDev1 pd8
// K28 -- Sequential Progression
// 2018-12-18

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

    g = 0;
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
