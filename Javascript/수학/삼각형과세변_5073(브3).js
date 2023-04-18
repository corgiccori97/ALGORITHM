const input = require('fs').readFileSync('예제.txt').toString().trim().split('\n');

for (let i = 0; i < input.length - 1; i++) {
    const sortedArr = [...input[i].split(' ').map((num) => Number(num))].sort();
    const checkInvalid = sortedArr[0] + sortedArr[1] - sortedArr[2];
    !checkInvalid ? console.log("Invalid") 
    :sortedArr[0] === sortedArr[1] && sortedArr[1] === sortedArr[2] ? console.log("Equilateral") 
    :sortedArr[0] === sortedArr[1] | sortedArr[1] === sortedArr[2] ? console.log("Isosceles")
    :console.log("Scalene");
}



