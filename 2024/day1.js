let part1 = 0;
let part2 = 0;
const fs = require('fs');

fs.readFile('./inputs/day1.txt', 'utf8', (_, file) => {
    
    const input = file;
    const esquerda = [];
    const direita = [];
    const esquerda2 = [];
    const direita2 = [];

    function somarDistancia(num1,num2){
        if(num1 > num2){
            return num1 - num2;  
        } 
        else if(num1 < num2){
            return num2 - num1;
        }
        else{
            return 0;
        }
    } 

    function bubbleSort(lista){
        const tam = lista.length;
        for(let i = 0; i < tam; i++){
            for(let j = 0; j < tam - 1 - i; j++){
                if (lista[j] > lista[j+1]){
                    let temp = lista[j+1];
                    lista[j+1] = lista[j];
                    lista[j] = temp;
                }
            }
        }
        return lista
    }


    let inputFormat = input.split("\n");

    for (const linha in inputFormat){
        let temp = inputFormat[linha].split("   ").map(Number);
        
        esquerda.push(temp[0]);
        direita.push(temp[1]);

    }

    bubbleSort(esquerda);
    bubbleSort(direita);

    for(let i = 0; i < esquerda.length; i++){
        part1 += somarDistancia(esquerda[i],direita[i]);
    }

    console.log(part1);

//---------------------------------------------------------------

    for (const linha in inputFormat){
        const temp = inputFormat[linha].split("   ").map(Number);
        
        esquerda2.push(temp[0]);
        direita2.push(temp[1]);
    }
    
    for(const numero in esquerda2){
        
        let repeticao = 0;
    
        for(const numero2 in direita2){
            if(direita2[numero2] === esquerda2[numero]){
                repeticao ++;
            }
        }
    
        part2 += esquerda2[numero] * repeticao;
    
    }
    
    console.log(part2);
});