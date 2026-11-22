
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DeepHat Simulator</title>
<style>
body {
    background: #050505;
    color: #00ff66;
    font-family: monospace;
    text-align: center;
    padding: 30px 12px;
}
.box {
    border: 1px solid #00ff66;
    padding: 25px;
    max-width: 500px;
    margin: 40px auto;
    border-radius: 12px;
}
button {
    background: #00ff66;
    color: black;
    border: 0;
    padding: 15px 25px;
    border-radius: 7px;
    font-weight: bold;
}
#resultado { margin-top: 25px; }
</style>
</head>
<body>
<div class="box">
<h1>DEEPHAT SECURITY</h1>
<p>SIMULADOR DE SEGURANÇA</p>
<button onclick="iniciar()">INICIAR SIMULAÇÃO</button>
<div id="resultado"></div>
</div>
<script>
function iniciar() {
    let resultado = document.getElementById("resultado");
    let i = 0;
    resultado.innerHTML = "Iniciando simulação...";
    let timer = setInterval(() => {
        i += 10;
        resultado.innerHTML = "Análise fictícia: " + i + "%";
        if (i >= 100) {
            clearInterval(timer);
            resultado.innerHTML =
            "<h2>SIMULAÇÃO CONCLUÍDA!</h2>" +
            "<p>Nenhum dispositivo foi afetado.</p>" +
            "<h2>😂 ERA BRINCADEIRA!</h2>";
        }
    }, 300);
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
