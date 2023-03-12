const [H, W, N, M] = require('fs').readFileSync('예제.txt').toString().trim().split(' ').map((n) => Number(n));

const width = Math.ceil(W / (M + 1));
const height = Math.ceil(H / (N + 1));

console.log(width * height);