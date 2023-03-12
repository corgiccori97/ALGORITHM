const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
let [str, n, ...operators] = input;

const temp = new Array(str.length - 1).fill(0);
let current = str.length - 1;

const operate = {
    'L': () => current -= 1,
    'D': () => current += 1,
    'B': () => {
        temp[current - 1] = -1;
        current -= 1;
    },
    'P': (x) => {
        temp[current] = x;
        current -= 1;
    }
}

for (let i = 0; i < operators.length; i++) {
    if (operators[i][0] !== 'P') {
        operate[operators[i][0]];
    }
    else {
        const addFunc = operators['P'];
        val = addFunc(operators[i][2]);
        console.log(val);
    }
}
