// =======================
// CANVAS
// =======================

let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");


// =======================
// IMAGENS DO PAINEL
// =======================

let painelPuzzleFechado = new Image();
let painelPuzzleAberto = new Image();

painelPuzzleFechado.src = "img/painelpuzzleFechado.png";
painelPuzzleAberto.src = "img/painelpuzzleAberto.png";


// =======================
// VARIÁVEIS DO PUZZLE
// =======================

let codigoCorreto = "";
let textoDigitado = "";
let energiaCaiu = false;
let jogoIniciado = false;


// =======================
// PAINEL DO PUZZLE
// =======================

const painelPuzzle = {
    x: 0,
    y: 0,
    width: 200,
    height: 200,
    img: painelPuzzleFechado,

    desenhar: function(){
        ctx.drawImage(this.img, this.x, this.y, this.width, this.height);
    }
};


// =======================
// ELEVADOR GRANDE
// =======================

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
};


// =======================
// ELEVADOR PEQUENO
// =======================

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
};


// =======================
// ANDARES
// =======================

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
};


// =======================
// ÁREA DOS ANDARES
// =======================

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
};


// =======================
// FUNDO DO PUZZLE
// =======================

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
};


// =======================
// MENU DO PLAYER
// =======================

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
};


// =======================
// OBJETO DA ENERGIA
// =======================

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
};


// =======================
// ABRIR / FECHAR PAINEL
// =======================

document.addEventListener("keydown", function(event) {

    if (event.key.toLowerCase() === "m") {

        if (painelPuzzle.img === painelPuzzleFechado) {
            painelPuzzle.img = painelPuzzleAberto;
            return;
        }

        if (painelPuzzle.img === painelPuzzleAberto && energiaCaiu == false) {
            painelPuzzle.img = painelPuzzleFechado;
            return;
        }
    }

});


// =======================
// CONTROLE DOS ANDARES
// =======================

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


// =======================
// DIGITAR CÓDIGO NO PAINEL
// =======================

document.addEventListener("keydown", function(event) {

    if (energiaCaiu == true && painelPuzzle.img === painelPuzzleAberto) {

        if (event.key === "Backspace") {
            textoDigitado = textoDigitado.slice(0, -1);
            return;
        }

        let tecla = event.key.toUpperCase();

        if (tecla.length == 1 && tecla >= "A" && tecla <= "Z") {
            textoDigitado += tecla;
            console.log("Digitado:", textoDigitado);
        }

        if (textoDigitado.length == 3) {

            if (textoDigitado == codigoCorreto) {
                console.log("Código correto! Energia voltou.");

                elevadorpequeno.velocidade = 1;
                energiaCaiu = false;
                codigoCorreto = "";
                textoDigitado = "";
                painelPuzzle.img = painelPuzzleFechado;
            } else {
                console.log("Código errado!");
                textoDigitado = "";
            }
        }
    }

});


// =======================
// SISTEMA DA ENERGIA
// =======================

function puzzleenergia(){  

    setInterval(function(){

        if (energiaCaiu == false) {

            let number = Math.floor(Math.random() * 2) + 1;
            console.log(number);

            if (number == 1){
                elevadorpequeno.velocidade = 0;
                energiaCaiu = true;
                gerarCodigo();
            }

            if (number == 2){
                elevadorpequeno.velocidade = 1;
            }
        }

    }, 5000);
}


// =======================
// GERAR CÓDIGO ALEATÓRIO
// =======================

function gerarCodigo(){

    let codigos = ["MXF", "FXT", "KXT"];

    let numero = Math.floor(Math.random() * codigos.length);

    codigoCorreto = codigos[numero];
    textoDigitado = "";

    console.log("Código gerado:", codigoCorreto);
}


// =======================
// INICIAR JOGO
// =======================

function iniciarJogo(){

    if (jogoIniciado == false) {
        jogoIniciado = true;
        puzzleenergia();
    }
}

painelPuzzleFechado.onload = iniciarJogo;
painelPuzzleAberto.onload = iniciarJogo;


// =======================
// DESENHAR TUDO NA TELA
// =======================

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

    painelPuzzle.desenhar();
    if (energiaCaiu == true){
        ctx.fillStyle = "black";
        ctx.font = "20px Arial";
        ctx.fillText("CODIGO: " + codigoCorreto, 300, 40);
    }
    if (energiaCaiu == true && painelPuzzle.img === painelPuzzleAberto) {
        ctx.fillStyle = "white";
        ctx.font = "20px Arial";

        // Posição do texto:
        // primeiro número = X
        // segundo número = Y
    
        ctx.fillText(textoDigitado, 130, 100);
    }

    requestAnimationFrame(desenharTudo);
}

desenharTudo();