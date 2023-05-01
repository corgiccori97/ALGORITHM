const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const [N, M, V] = input[0].split(' ').map(Number);

let dfs_result = [];
let bfs_result = [];

let graph = Array.from(Array(N + 1), () => Array(N + 1).fill(0));
let visited = [...Array(N + 1).fill(false)];
let visited2 = [...Array(N + 1).fill(false)];

for (let i of input.slice(1)) {
    let [x, y] = i.split(' ').map(Number);
    graph[x][y] = 1;
    graph[y][x] = 1;
}

// dfs
const dfs = (v) => {
    visited[v] = true;
    dfs_result.push(v);

    for (let i = 1; i < graph.length; i++) {
        if (visited[i] === false && graph[v][i] === 1) {
            dfs(i);
        }
    }
}

// bfs
const bfs = (v) => {
    let Queue = [];
    Queue.push(v);
    bfs_result.push(v);

    while (Queue.length) {
        let dequeue = Queue.shift();
        visited2[dequeue] = true;
        for (let i = 1; i < graph.length; i++) {
            if (graph[dequeue][i] === 1 && visited2[i] === false) {
                visited2[i] = true;
                Queue.push(i);
                bfs_result.push(i);
            }
        } 
    }

}

dfs(V);
bfs(V);
console.log(dfs_result.join(' '));
console.log(bfs_result.join(' '));