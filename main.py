from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def render_form():
    return render_template('�|�P�����������.html')

@app.route('/', methods=['POST'])
def login():
    db ={"id": "001", "pokemon": "�t�V�M�_�l", "hp": 45, "attack": 49, "defense": 49,"special_attack" :65, "special_defense": 65, "quickness": 45, "type": "����,�ǂ�"}

    if db["id"] = request.form['number']:
        return render_template('�|�P�����ڍ׉��.html', number=request.form['number'], pokemonName=db["id"], type=db["type"], hp=db["hp"], attack=db["attack"], defense=db["defense"], special_attack=db["special_attack"], special_defense=db["special_defense"], quickness=db["quickness"])
    else:
        return render_template('�|�P�����������s���.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
