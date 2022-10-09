from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/skills')
def skills():
    paths = {"ACE": "ACE", "AQU": "ÁQUILA", "ARA": "ARAUTO", "ARC": "ARCANTE", "BAR": "BARDO", "CHE": "CHEVALIER",
             "CRU": "CRUZADO", "DRU": "DRUIDA", "ENC": "ENCANTADOR", "EVO": "EVOCADOR", "GUN": "GUNSLINGER",
             "HAS": "HASSASSIN", "ILU": "ILUSIONISTA", "KAL": "KALINIER", "LAN": "LANCET", "MON": "MONGE",
             "NEB": "NÉBULO", "PAL": "PALADINO", "PHA": "PHASER", "SHE": "SHEPIAN", "TEC": "TECNOCLASTA",
             "TIM": "TIMESEER", "VAL": "VALETE", "VIB": "VIBRATA"}
    categories = ['INTRINSECA', 'PADRAO', 'SUPORTE', 'REACAO', 'MOVIMENTO', 'PERFEITA']
    return render_template('skills.html', categories=categories, paths=paths)
