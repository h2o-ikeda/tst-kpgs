from flask import Flask, request, render_template
from google.cloud import secretmanager

app = Flask(__name__)

@app.route('/', methods=['GET'])
def render_form():
    return render_template('ポケモン検索画面.html')

@app.route('/', methods=['POST'])
def login():

    # プロジェクトID定義
    project_id=""
    
    # シークレットID定義
    secret_id=""
    
    # シークレットマネージャーへのアクセス用のクライアント作成
    client = secretmanager.SecretManagerServiceClient()

    # シークレットマネージャーへのパス設定
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"

    # シークレットマネージャーへアクセス
    response = client.access_secret_version(request={"name": name})

    # シークレットマネージャーの値をUTF-8に変換
    payload = response.payload.data.decode("UTF-8")

    print(payload)

    # スプレッドシートの ID とシート名を設定
    ssId = ""
    sheet_name = ""

    # 認証情報を設定
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets.readonly']
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name(payload, scope)
    
    # Google Sheet APIクライアント作成
    client = gspread.authorize(credentials)

    # スプレッドシートを開く
    worksheet = client.open_by_key(ssId).worksheet(sheet_name)

    
    db =[
        {"id": "001", "pokemon": "フシギダネ","intro": "生まれて　しばらくの　あいだ　背中の　タネに　詰まった　栄養を　取って　育つ。", "hp": 45, "attack": 49, "defense": 49,"special_attack" :65, "special_defense": 65, "quickness": 45, "type": "くさ,どく"},
        {"id": "002", "pokemon": "フシギソウ", "intro": "太陽の　光を　浴びるほど　体に　力が　わいて　背中の　つぼみが　育っていく。", "hp": 60, "attack": 62, "defense": 63,"special_attack" :80, "special_defense": 80, "quickness": 60, "type": "くさ,どく"},
        {"id": "003", "pokemon": "フシギバナ", "intro": "浴びた　太陽の　光を　エネルギーに　変換できるので　夏の　ほうが　強くなる。", "hp": 80, "attack": 82, "defense": 83,"special_attack" :100, "special_defense": 100, "quickness": 80, "type": "くさ,どく"},
        ]

    if db["id"] == request.form['number']:
        return render_template('ポケモン詳細画面.html', number=request.form['number'], pokemonName=db["id"], type=db["type"], hp=db["hp"], attack=db["attack"], defense=db["defense"], special_attack=db["special_attack"], special_defense=db["special_defense"], quickness=db["quickness"])
    else:
        return render_template('ポケモン検索失敗画面.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
