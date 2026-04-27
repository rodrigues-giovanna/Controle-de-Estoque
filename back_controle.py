from flask import Flask, render_template, request, redirect


app = Flask(__name__)

estoque = []

@app.route("/")
def index():
    total_geral = sum(p['total_item'] for p in estoque)
    return render_template("index.html", produtos = estoque, total_geral = total_geral)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    #coloqquei o try para evitar que o sistema quebre caso o usuário insira um valor inválido, como texto no campo de quantidade ou preço. Se ocorrer um erro, ele redireciona de volta para a página inicial.
    try:
        nome = request.form.get("nome")
        codigo = request.form.get("codigo")
        quantidade = int(request.form.get("quantidade"))
        preco = float(request.form.get("preco"))

    except (ValueError, TypeError):
        return redirect("/")
    
    novo_produto = {
        "nome":nome,
        "codigo":codigo,
        "quantidade":quantidade,
        "preco":preco,
        "total_item": quantidade * preco
    }
    estoque.append(novo_produto)
    return redirect("/")

@app.route("/remover/<int:indice>")
def remover(indice):
    if 0 <= indice < len(estoque):
        estoque.pop(indice)
    return redirect("/")

@app.route("/editar/<int:indice>/<acao>")
def editar(indice, acao):
    if 0 <= indice < len(estoque):
        if acao == 'aumentar':
            estoque[indice]['quantidade'] += 1
        elif acao == 'diminuir' and estoque[indice]['quantidade'] > 0:
            estoque[indice]['quantidade'] -= 1

        estoque[indice]['total_item'] = estoque[indice]['quantidade'] * estoque[indice]['preco']
        # ⬇️⬇️⬇️ LINHA MODIFICADA ⬇️⬇️⬇️
        return redirect(f'/#produto-{indice}')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)