from flask import Flask, render_template, request, redirect, url_for
from model.basic.definition.skill import Skill
import model.connection.mydatabase as db

paths = {"ACE": "ACE", "AQU": "ÁQUILA", "ARA": "ARAUTO", "ARC": "ARCANTE", "BAR": "BARDO", "CHE": "CHEVALIER",
             "CRU": "CRUZADO", "DRU": "DRUIDA", "ENC": "ENCANTADOR", "EVO": "EVOCADOR", "GUN": "GUNSLINGER",
             "HAS": "HASSASSIN", "ILU": "ILUSIONISTA", "KAL": "KALINIER", "LAN": "LANCET", "MON": "MONGE",
             "NEB": "NÉBULO", "PAL": "PALADINO", "PHA": "PHASER", "SHE": "SHEPIAN", "TEC": "TECNOCLASTA",
             "TIM": "TIMESEER", "VAL": "VALETE", "VIB": "VIBRATA"}

categories = ['INTRINSECA', 'PADRAO', 'SUPORTE', 'REACAO', 'MOVIMENTO', 'PERFEITA']

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/skills')
def skills():
    skills_list = db.get_all_skills()
    return render_template('skills.html', categories=categories, paths=paths, skills=skills_list)


@app.route('/add-skill', methods=['POST', ])
def add_skill():
    response = request.form
    skill = Skill(**response)
    db.upload_new_skill(skill)
    return redirect('/skills')


@app.route('/skills/<skill_id>')
def update_delete_skill(skill_id):
    skill = db.get_skill_by_id(skill_id)
    return render_template('update-delete-skill.html', skill=skill, categories=categories, paths=paths)


@app.route('/skills/update-skill', methods=['POST', ])
def update_skill():
    response = request.form
    skill = Skill(**response)
    db.update_skill(skill)
    return redirect('/skills')


@app.route('/skills/delete-skill', methods=['POST', ])
def delete_skill():
    skill_id = request.form["delete"]
    db.delete_skill(skill_id)
    return redirect('/skills')
