from flask import Flask, jsonify, request
app = Flask(__name__) 
app.json.ensure_ascii = False


jogos = [
    {"id": 1, "titulo": "The Last of Us", "genero": "Ação", "ano_lancamento": 2013},
    {"id": 2, "titulo": "Detroit: Become Human", "genero": "Aventura", "ano_lancamento": 2018},
    {"id": 3, "titulo": "God of War", "genero": "Ação", "ano_lancamento": 2018},
    {"id": 4, "titulo": "Devil May Cry 5", "genero": "Ação", "ano_lancamento": 2019}
]

# Variável para armazenar o ID do próximo jogo 
next_id = max([jogo['id'] for jogo in jogos]) + 1 if jogos else 1




# 1. Rota raiz  retornando uma mensagem
@app.route('/')
def home():
   
    return jsonify({ 'mensagem':'Bem-vindo à minha API de jogos de videogame!'})
# 2. Rota para pegar os dados de todos 0os jogos

@app.route('/dados', methods=['GET'])
def get_dados_jogos():
    
    return jsonify(jogos)



# 3. Obter um jogo por ID
@app.route('/jogos/<int:jogo_id>', methods=['GET'])
def get_jogo_por_id(jogo_id):
    for jogo in jogos:
        if jogo["id"] == jogo_id:
            return jsonify(jogo)
    return jsonify({"erro": "Jogo não encontrado"}), 404

# 4. Adicionar um novo jogo


if __name__ == '__main__':
    app.run(debug=True) 
