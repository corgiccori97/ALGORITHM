const [N, ...arr] = require('fs').readFileSync('예제.txt').toString().trim().split('\n').map(Number);

class Heap {
    constructor() {
        this.heap = [];
    }

    swap(index1, index2) {
        let temp = this.items[index1];
        this.items[index1] = this.items[index2];
        this.items[index2] = temp;
    }
}

class MinHeap extends Heap {
    bubbleUp() {
        let index = this.items.length - 1;

    }
}