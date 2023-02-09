const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n').map(Number);
const stack = []

let sum = 0;

for (let i = 1; i < input.length; i++) {
    if (input[i] === 0 && (stack)) stack.pop();
    else stack.push(input[i]);
}

for (let i = 0; i < stack.length; i++) {
    sum += stack[i];
}

console.log(sum);