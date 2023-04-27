const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
const [N, score, P] = [...input[0].split(' ').map((num) => Number(num))];
if (N) {
    const arr = [...input[1].split(' ').map((num) => Number(num))];
    
    let rank = 0;

    if (arr[arr.length - 1] >= score && N === P) {
        console.log(-1);
    }

    else {
        for (let i = 0; i < N; i++) {
            if (arr[i] <= score) {
                rank = i + 1;
                break;
            }
        }
        console.log(rank);
    }

}

else {
    console.log(1);
}