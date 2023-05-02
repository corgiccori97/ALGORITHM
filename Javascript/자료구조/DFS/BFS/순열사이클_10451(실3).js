const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const T = +input[0];

let graph = [];
let visited = [];

const dfs = (v) => {
    visited[v] = true;

    for (let i = 0; i < graph.length; i++) {
        if (graph[v][i] === 1 && !visited[i]) {
            dfs(i);
        }
    }

    return visited;
}

for (let i = 0; i < T;i++) {
    const N = +input[2 * i + 1];
    const arr = input[2 * i + 2].split(' ').map(Number);
    graph = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
    visited = [...Array(N + 1).fill(false)];
    let cycle = 0;

    for (let x = 1; x < N + 1; x++) {
        const y = arr[x - 1];
        graph[x][y] = 1;
        graph[y][x] = 1;
    }

    for (let j = 1; j < N + 1; j++) {
        if (!visited[j]) {
            dfs(j);
            cycle += 1;
        }
    }

    console.log(cycle);
}