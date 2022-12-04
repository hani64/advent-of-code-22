import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

let calories: string[] = []

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

