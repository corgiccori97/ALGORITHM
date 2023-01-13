const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');

let caseNumber = Number(input[0])
let arrNumber = input[1].split(' ').map((item) => Number(item));
let answer = 0;

const isPrime = (num) => {
    if (num === 1) return false;

    for(let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }

    return true;
}

for (let i = 0; i < arrNumber.length; i++) {
    if (isPrime(arrNumber[i])) answer++;
}

console.log(answer);