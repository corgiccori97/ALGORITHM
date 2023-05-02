const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const T = +input[0];

let graph = [];
let visited = [];

let current = 1;

// 상하좌우 x, y
let vectors = [[0, 1], [0, -1], [-1, 0], [1, 0]];

const bfs = (x, y) => {
    let Queue = [];
    Queue.push([x, y]);

    while (Queue.length) {
        let dequeue = Queue.shift();
        let [a, b] = dequeue.map(Number);
        visited[a][b] = true;

        for (vector of vectors) {
            const [a_add, b_add] = vector.map(Number);
            const [new_a, new_b] = [a + a_add, b + b_add];
            if (new_a >= 0 && new_b >= 0) {
                if (graph[new_a][new_b] === 1 && !visited[new_a][new_b]) {
                    visited[new_a][new_b] = true;
                    Queue.push([new_a, new_b]);
                } 
            }
        }
    }
}

for (let i = 0; i < T; i++) {
    let worm = 0;
    const [M, N, K] = input[current].split(' ').map(Number);
    graph = Array.from(Array(M + 1), () => Array(N + 1).fill(0));
    visited = Array.from(Array(M + 1), () => Array(N + 1).fill(false));

    for (let i = current; i < current + K; i++) {
        const [x, y] = input[i + 1].split(' ').map(Number);
        graph[x][y] = 1;
    }

    for (let i = 0; i < M; i++) {
        for (let j = 0; j < N; j++) {
            if (!visited[i][j] && graph[i][j]) {
                bfs(i, j);
                worm += 1;
            }
        }
    }
    
    current += K + 1;

    bfs(0, 0);
    console.log(worm);
}