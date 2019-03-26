
function mostrarEnunciado(bool) {
    var consola = document.getElementById("consola-result");
    var enunciado = document.getElementById("ver-enunciado");
    if (bool){
      intercambiar_visibilidad(enunciado,consola)
    } else {
        intercambiar_visibilidad(consola,enunciado)
    }
    cambiarColorEnunciado(bool);
}

function intercambiar_visibilidad(div1, div2){
    div1.style.display = "block";
    div2.style.display = "none";
}

function cambiarColorEnunciado(bool) {
    var boton_consola = document.getElementById("bt-consola");
    var boton_enunciado = document.getElementById("bt-enunciado");
    if (bool){
        intercambiar_colores(boton_enunciado,boton_consola);
    }else {
        intercambiar_colores(boton_consola, boton_enunciado);
    }
}

function intercambiar_colores(bot1,bot2){
    bot1.style.color = "black"; 
    bot1.style.background = "#dcdde1";
    bot2.style.color = "white"; 
    bot2.style.background = "inherit";
}