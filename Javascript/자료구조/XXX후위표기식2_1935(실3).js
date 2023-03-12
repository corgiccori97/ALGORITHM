const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const [n, expressionBefore, ...num] = input;
const stack = [];
const calculator = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => a / b,
}

const expression = expressionBefore.split('');

for (let i = 0; i < expression.length; i++) {
    if (expression[i] == "+" || expression[i] == "-" || expression[i] == "*" || expression[i] == "/") {
        const secondNum = stack.pop();
        const firstNum = stack.pop();
        const calculatorFunc = calculator[expression[i]];
        answerValue = calculatorFunc(firstNum, secondNum);
        stack.push(answerValue);
    }

    else {
        stack.push(expression[i].charCodeAt(0) - 64);
    }
}

console.log((Math.floor(stack[0] * 100) / 100).toFixed(2));