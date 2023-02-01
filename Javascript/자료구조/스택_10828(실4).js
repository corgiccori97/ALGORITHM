const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const n = input[0];

const stack = [];
const answer = [];

const commandSthing = {
    push: x => {
        stack.push(x);
    },
    pop: () => {
        return stack.length === 0 ? -1 : stack.pop()
    },
    size: () => {
        return stack.length;
    },
    empty: () => {
        return stack.length === 0 ? 1 : 0
    },
    top: () => {
        return stack.length === 0 ? -1 : stack[stack.length - 1]
    }
}

for (let i = 1; i <= n; i++) {
    const [command, num] = input[i].trim().split(/\s/g);
    if (command === 'push') commandSthing.push(parseInt(num));
    else answer.push(commandSthing[command]());
}

console.log(answer.join('\n'));