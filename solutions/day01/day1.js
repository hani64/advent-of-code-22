const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
    input: fs.createReadStream('solutions/day1/input.txt'),
    output: null
  });

let calories = []

rl.on('line', line => {
    calories.push(line)
});

rl.on('close', () => {
  let max = [0,0,0], currMax = 0
  for(const cal of calories) {
    if(cal === "") {
      let minIdx = 0
      max.reduce((a, b, i) => { 
        return b < a ? (minIdx = i) && b : a
      })
      if(currMax > max[minIdx]) {
        max[minIdx] = currMax
      }
      currMax = 0
    }
    else {
      currMax+= Number(cal)
    }

  }
  console.log(max, max.reduce((a,b) => { return a+b }))
});