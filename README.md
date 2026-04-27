# 📦 StockFlow — Sistema de Controle de Estoque

Sistema web desenvolvido com Python (Flask) e HTML/CSS para cadastrar produtos e controlar o estoque disponível.

## 🚀 Funcionalidades

- Cadastrar produtos com nome, código, quantidade e preço
- Listar todos os produtos cadastrados
- Calcular valor total em estoque
- Atualizar quantidade com botões + e −
- Remover produtos
- Aviso visual para produtos com estoque baixo (menos de 5 unidades)
- Busca de produtos em tempo real por nome ou código

## 🛠️ Tecnologias utilizadas

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript

## 📂 Estrutura do projeto

```
Projeto_Estoque/
├── back_controle.py       # Back-end Flask
├── templates/
│   └── Index.html         # Interface do sistema
└── static/
    └── style.css          # Estilo da página
```

## ▶️ Como executar

1. Instale o Flask:
```
pip install flask
```

2. Execute o servidor:
```
python back_controle.py
```

3. Acesse no navegador:
```
http://localhost:5000
```

## 📚 Conteúdos trabalhados

- Listas e dicionários
- Laços de repetição
- Funções
- Cálculos
- Roteamento com Flask
- Templates com Jinja2