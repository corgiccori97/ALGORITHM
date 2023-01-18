const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n').map(Number);

const isPrime = (num) => {
    if (num === 1) return false;

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }

    return true;
}

for (let i = 0; i < input.length; i++) {
    const n = input[i];
    if (!n) break;
    let left = 2;
    let right = n - 2;

    while (!isPrime(left) || !isPrime(right)) {
        left += 1;
        right -= 1;
    }

    console.log(n + " = " + left + " + " + right);
}