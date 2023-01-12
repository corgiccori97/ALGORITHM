const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');

const isPrime = (num) => {
    if (num === 1) return false;

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if ((num % i) === 0) return false; 
    }
    return true;
}

const [n, m] = input.map(e => parseInt(e));

for (let i = n; i <= m; i++) {
    isPrime(i) ? console.log(i) : null;
}