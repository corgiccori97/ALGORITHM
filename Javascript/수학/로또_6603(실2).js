const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');

let idx = 0;
while (input[idx].length !== 1) {
    const [k, ...s] = input[idx++].split(' ').map(Number);

    function dfs(v, arr) {
        if (arr.length === 6) {
            console.log(...arr);
            return;
        }

        for (let i = v; i < k; i++) {
            dfs(i + 1, [...arr, s[i]]);
        }
    }

    dfs(0, []);
}