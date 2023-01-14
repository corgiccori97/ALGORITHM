// 유클리드 호제법
const input = require('fs').readFileSync('예제.txt').toString().trim().split(' ');

const [n, m] = input.map((item) => Number(item));

function gcd(n1, n2) {
    return n2 ? gcd(n2, n1 % n2) : n1;
}

answer = gcd(n, m);

console.log(answer);
console.log(n * m / answer);