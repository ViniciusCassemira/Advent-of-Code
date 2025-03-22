
const fs = require('fs');

fs.readFile('./inputs/day2.txt', 'utf8', (_,file) => {
    const relatorio = file.split("\n").map(linha => linha.split(" ").map(Number));
    let relatorioSeguro = 0;

    function verDirecao(num1,num2){
        if(num1 < num2){
            return 0; 
        }else if(num1 > num2){
            return 1;
        }
    }

    function analisarRelatorio(array){
        let direcao;
        let erro = false;
        for(let i = 0; i < array.length-1; i++){
            if(i === 0){
                if(array[i] < array[i+1]){
                    direcao = 0;
                }else if (array[i] > array[i+1]){
                    direcao = 1;
                }else{
                    erro = true;
                }
            }

            if(array[i] === array[i+1] || array[i] - array[i+1] > 3 || array[i+1] - array[i] > 3  || verDirecao(array[i], array[i+1]) !== direcao){
                erro = true;
            }

        }
        if(!erro){
            relatorioSeguro ++;
        }
    }

    for(const linha in relatorio){
        analisarRelatorio(relatorio[linha]);
    }

console.log("Part 1:",relatorioSeguro);


//-----------------------------------------------------------------

const relatorio2 = file.split("\n").map(linha => linha.split(" ").map(Number));
let sum = 0;

function verDirecao2(num1,num2){
    if(num1 < num2){
        return 0; 
    }else if(num1 > num2){
        return 1;
    }
    return -1;
}

function analisarRelatorio2(array,indice){
    let direcao;
    let erro = false;
    for(let i = 0; i < array.length-1; i++){
        if(i === 0){
            if(array[i] < array[i+1]){
                direcao = 0;
            }else if(array[i] > array[i+1]){
                direcao = 1;
            }else{
                direcao = 2;
            }
        }

        if(array[i] === array[i+1] || 
           array[i-1] === array[i] || 
           array[i] - array[i+1] > 3 || 
           array[i+1] - array[i] > 3  || 
           verDirecao2(array[i], array[i+1]) !== direcao){
            erro = true;
        }

    }
    if(!erro){
        sum++;
        return 1;
    }
    
    if(indice == 1){
        analisarRelatorioPlus(array);
    }
}

function analisarRelatorioPlus(array){
    for (let i = 0; i < array.length; i++){
        const array2 = array.slice();
        array2.splice(i, 1);
        if (analisarRelatorio2(array2, 0) === 1) {
            return;
        }
    }
}

for(const linha in relatorio2){
    analisarRelatorio2(relatorio2[linha],1);
}

console.log("Part 2: ",sum);

})