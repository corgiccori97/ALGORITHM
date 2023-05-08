const [N, ...input] = require('fs').readFileSync('예제.txt').toString().trim().split('\n');

const nodes = input.map((v) => v.split(' '));
// 자바스크립트의 reduce 함수는 배열의 각 요소를 순회하며 callback 함수의 실행 값을 누적하여 하나의 결과값을 반환합니다.
const trees = nodes.reduce((acc, [node, left, right]) => {
    acc[node] = { left, right };
    console.log(acc, node, left, right);
    return acc;
}, {});

console.log(trees);

const preorder = (node) => {
    if (node === '.') {
        return '';
    }
    const { left, right } = trees[node];
    return node + preorder(left) + preorder(right);
};

console.log(preorder('A'));