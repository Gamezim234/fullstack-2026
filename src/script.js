let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

const elevadorgrande = {
    x: 0,
    y: 200,
    width: 200,
    height: 200,
    color: "gray",
    desenhar: function() {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}
const elevadorpequeno = {
    x: 200,
    y: 340,
    width: 60,
    height: 60,
    color: "orange",
    posicaoAtual: 340,
    velocidade: 1,
    desenhar: function() {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    },
    atualizar: function() {
     if(this.y < this.posicaoAtual){
        this.y += this.velocidade;
     } 
     if(this.y > this.posicaoAtual){
        this.y -= this.velocidade;
     }
    }
}
const andares = {
    terreo: {
        x: 260,
        y: 340,
        width: 240,
        height: 60,
        color: "blue",
    },
    andar1: {
        x: 260,
        y: 280,
        width: 240,
        height: 60,
        color: "purple",
    },
    andar2: {
        x: 260,
        y: 220,
        width: 240,
        height: 60,
        color: "gray",
    },
    andar3: {
        x: 260,
        y: 160,
        width: 240,
        height: 60,
        color: "yellow",
    },
    andar4: {
        x: 260,
        y: 100,
        width: 240,
        height: 60,
        color: "black",
    },
    desenhar: function() {
        ctx.fillStyle = this.terreo.color;
        ctx.fillRect(this.terreo.x, this.terreo.y, this.terreo.width, this.terreo.height);
        ctx.fillStyle = this.andar1.color;
        ctx.fillRect(this.andar1.x, this.andar1.y, this.andar1.width, this.andar1.height);
        ctx.fillStyle = this.andar2.color;
        ctx.fillRect(this.andar2.x, this.andar2.y, this.andar2.width, this.andar2.height);
        ctx.fillStyle = this.andar3.color;
        ctx.fillRect(this.andar3.x, this.andar3.y, this.andar3.width, this.andar3.height);
        ctx.fillStyle = this.andar4.color;
        ctx.fillRect(this.andar4.x, this.andar4.y, this.andar4.width, this.andar4.height);
    }
}

const elevadoreandares = {
    x: 200,
    y: 100,
    width: 300,
    height: 300,
    color: "red",
    desenhar: function() {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}
const puzzle = {
    x: 0,
    y: 0,
    width: 200,
    height: 200,
    color: "green",
    desenhar: function() {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}
const menuplayer = {
    x: 200,
    y: 0,
    width: 300,
    height: 100,
    color: "yellow",
    desenhar: function() {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}
const energia = {
    x: 115,
    y: 250,
    width: 50,
    height: 50,
    color: "yellow",
    desenhar: function() {
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}
document.addEventListener("keydown", function(event) {
    if (event.key === "1"){
        elevadorpequeno.posicaoAtual = andares.terreo.y;
    }
    if (event.key === "2"){
        elevadorpequeno.posicaoAtual = andares.andar1.y;
    }   
    if (event.key === "3"){
        elevadorpequeno.posicaoAtual = andares.andar2.y;
    }
    if (event.key === "4"){
        elevadorpequeno.posicaoAtual = andares.andar3.y;
    }
    if (event.key === "5"){
        elevadorpequeno.posicaoAtual = andares.andar4.y;
    }

});

function puzzleenergia(){  

   setTimeout(function(){
     number = Math.floor(Math.random() * 2) + 1 ;
    console.log(number)
    if (number == 1){
     elevadorpequeno.velocidade = 0       
   }
   if (number == 2){
    elevadorpequeno.velocidade = 1
   };
   }, 5000)

   
}

function desenharTudo() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    elevadorgrande.desenhar();
    elevadoreandares.desenhar();
    elevadorpequeno.atualizar();
    elevadorpequeno.desenhar();
    puzzle.desenhar();
    menuplayer.desenhar();
    andares.desenhar();
    energia.desenhar();
    requestAnimationFrame(desenharTudo);
}

puzzleenergia();
desenharTudo();