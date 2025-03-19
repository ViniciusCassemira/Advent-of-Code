let part1 = 0;
let part2 = 0;
const fs = require('fs');

fs.readFile('./inputs/day2.txt', 'utf8', (_, file) => {
    
    const input = file;
    inputArray = input.split('\n');    

    inputArray.forEach(current => {
        const regex = /\d+/g;
        const values = current.match(regex);
        const arrayLowestValue = values.sort((a, b) => a - b).slice(0,2);
        
        //Part 1
        part1 += 2*(values[0]*values[1]) + 2*(values[1]*values[2]) + 2*(values[0]*values[2]) + (arrayLowestValue[0] * arrayLowestValue[1]);

        //Part2
        part2 += (arrayLowestValue[0]*2) + (arrayLowestValue[1]*2) + (values[0] * values[1] * values[2]);
        
    }); 
    console.log(`Part1: ${part1}`);
    console.log(`Part2: ${part2}`);
});