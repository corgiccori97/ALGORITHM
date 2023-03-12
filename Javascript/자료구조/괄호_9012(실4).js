const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const n = input[0];

const isVPS = (arr) => {
    const left = [];
    const right = [];

    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] === ')') {
            if (left.length === 0) return false;
            right.push(')');
        }

        else left.push('(');

        if ((right.length >= 1) && left.length >= right.length) {
            left.pop();
            right.pop();
        }

        console.log(left, right);
    }

    if (left.length + right.length === 0) {
        console.log('ye');
        return true;
    }
    return false;
}

for (let i = 1; i <= n; i++) {
    const result = isVPS([...input[i]]) ? 'YES' : 'NO';
    console.log(result);
}