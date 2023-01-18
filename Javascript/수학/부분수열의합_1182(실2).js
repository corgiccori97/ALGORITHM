const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');

const [N, S] = input[0].split(' ').map(Number);
const numArr = input[1].split(' ').map(Number);

let count = 0;

const solve = (i, sum) => {
    if (i === N) return;
    sum += numArr[i];
    if (sum === S) count++;

    solve(i + 1, sum);
    solve(i + 1, sum - numArr[i]);
};

solve(0, 0);

console.log(count);