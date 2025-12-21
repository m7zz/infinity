const nomes = ["Maria", "Pedro", "Aline", "João", "Ricardo"];

// for basico
for (let i =0; i <nomes.length; i++) {
    console.log(`- ${nomes[i]}`);
}

// For Of
console.log("For of");
for (let nome of nomes) {
    console.log(`- ${nome}`);
}

// For Each
console.log("For Each")
nomes.forEach( (nome) => console.log(`- ${nome}`))