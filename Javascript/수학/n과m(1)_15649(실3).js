const input = require('fs').readFileSync('예제.txt').toString().trim().split(' ');

const [n, m] = input.map((item) => Number(item));

function solution(n, m) {
    const seq = [];
    const visited = [...Array(n)].fill(false);
    let answer = 0;

    function dfs(k) {
        if (m === k) {
            console.log(seq.join(' '));
            return;
        }

        for (let i = 1; i <= n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                seq[k] = i;
                dfs(k + 1);
                visited[i] = false;
            }
        }
    }
    
    dfs(0);
    return answer;
}

solution(n, m);