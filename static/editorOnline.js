function modificarTitulo(text){
    var titulo = document.getElementById("tituloVis");
    titulo.innerHTML = text;
}

function modificarParrafo(text){
    var parrafo = document.getElementById("parrafoEj");
    text = parseText(text);
    parrafo.innerHTML = text;
}

function parseText(text){
    text = text.replace(/s_code/g,"<pre class=\"language-python\"><code class=\"language-python\">");
    text = text.replace(/\n/g,"<br>");
    return text.replace(/e_code/g,"</code></pre>");
}