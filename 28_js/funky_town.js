var fibonacci = function(n){
	if(n == 0 || n == 1){
		return n;
	} else {
		return fib(n-1) + fib(n-2);
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
	
