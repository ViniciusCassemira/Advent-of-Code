// Função para extrair todos os 'mul(a, b)' de uma string
function extrairMul(expression) {
    const regex = /mul\((\d+),(\d+)\)/g; // Expressão regular para capturar 'mul(a, b)'
    let resultados = [];
    let match;