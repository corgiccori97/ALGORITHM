const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');

const arrNum = input.map((item) => Number(item));
const primeNum = [2];

const isPrime = (num) => {
    if (num === 1) return false;
    
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }

    return true;
}

for (let j = 3; )