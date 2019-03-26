
function mostrarEnunciado(bool) {
    var consola = document.getElementById("consola-result");
    var enunciado = document.getElementById("ver-enunciado");
    if (bool){
      intercambiar_visibilidad(enunciado,consola)
    } else {
        intercambiar_visibilidad(consola,enunciado)
    }
}

function intercambiar_visibilidad(div1, div2){
    div1.style.display = "block";
    div2.style.display = "none";
}