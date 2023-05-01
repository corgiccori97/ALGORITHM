const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);

let graph = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
let visited = [...Array(N + 1).fill(false)];
let cnt = 0;

for (i of input.slice(1)) {
    const [x, y] = i.split(' ').map(Number);
    graph[x][y] = 1;
    graph[y][x] = 1;
}

const dfs = (v) => {
    visited[v] = true;
    
    for (let i = 1; i < graph.length; i++) {
        if (graph[v][i] === 1 && !visited[i]) {
            dfs(i);
        }
    }
}

for (let i = 1; i < graph.length; i++) {
    if (!visited[i]) {
        cnt += 1;
        dfs(i);
    }
}

console.log(cnt);