const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n').map(Number);

const isPrime = (num) => {
    if (num === 1) return false;

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }   

    return true;
}

for (let i = 0; i < input.length; i++) {
    let count = 0;

    if (input[i] === 0) break;

    for (let j = input[i] + 1; j <= input[i] * 2; j++) {
        if (isPrime(j)) count++;
    }

    console.log(count);
}