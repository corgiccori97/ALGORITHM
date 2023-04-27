const cases = require('fs').readFileSync('예제.txt').toString().trim().split('\n');
console.log(cases);
const vowels = ['a', 'e', 'i', 'o', 'u'];

let i = 0;
while (cases[i] !== 'end') {
    // 테스트케이스와 길이가 같은 빈 배열 생성
    let chkArr = [...Array(cases[i].length - 1)];
    let pass = true;

    // 2. 모음이 3개 혹은 자음이 3개 연속으로 올 경우 체크
    let consonant = 0;
    let vowel = 0;
    
    for (let j = 0; j < cases[i].length; j++) {
        let str = cases[i][j];
        
        // 3. 'e'와 'o'가 아닌 글자가 연속적으로 두 번 올 경우
        if (str === cases[i][j + 1] && str !== 'e' && str !== 'o') {
            pass = false;
            break;
        }

        // 모음일 경우 빈 배열에 1을, 자음일 경우 0을 추가
        if (str === vowels[0] || str === vowels[1] || str === vowels[2] ||  str === vowels[3] ||  str === vowels[4]) {
            consonant = 0;
            vowel += 1;
            chkArr[j] = 1;
        }
        else {
            vowel = 0;
            consonant += 1;
            chkArr[j] = 0;
        }

        if (consonant === 3 || vowel === 3) {
            pass = false;
            break;
        }
    }

    // 1. 모음을 하나도 포함하지 않을 경우
    if (!chkArr.reduce((a, b) => a + b)) pass = false;

    (pass ? console.log(`<${cases[i]}> is acceptable.`) : console.log(`<${cases[i]}> is not acceptable.`));
    i += 1;
}