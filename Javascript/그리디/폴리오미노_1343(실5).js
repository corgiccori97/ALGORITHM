let input = require('fs').readFileSync('예제.txt').toString().trim();

const solution = () => {
    result = [];
    for (i of input.split(".")) {
        let re = "";
        if (i) {
            if (i.length % 4 === 0) {
                re = 'AAAA'.repeat(i.length / 4);
            }
            else if (i.length % 4 === 2) {
                re = 'AAAA'.repeat(Math.floor(i.length / 4)) + 'BB';
            }
            else {
                result = [-1];
                break;
            }
            result = [...result, re];
        }
        else { result = [...result, ""]; }
    }
    console.log(result.join("."));
};

solution();