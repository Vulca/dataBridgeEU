from flask import Flask, render_template
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


# Initialisation de Flask
app = Flask(__name__)

# Configuration de la base de données PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres.tfiqvrdvcikhpaoioovd:Ahxw9lAU0ClMBxTj@aws-0-us-west-1.pooler.supabase.com:6543/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy
db = SQLAlchemy(app)

# Activer le contexte d'application
with app.app_context():
    # Automap pour mapper automatiquement les tables
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)

    # Mapping des tables depuis Supabase
    ApplicationRow = Base.classes.application
    MakerSpace = Base.classes.Maker_spaces
    OtherStructure = Base.classes.Other_structure
    RoleDistribution = Base.classes.role_distribution

@app.route('/')
def index():
    return "Flask et PostgreSQL fonctionnent !"

@app.route("/init-db")
def init_db():
    db.create_all()
    return "Tables créées dans la base de données !"

@app.route('/funds-table')
def funds_table():
    # Crée une session pour interagir avec la base de données
    session = Session(db.engine)

    # Requête SQLAlchemy pour regrouper et sommer les financements par origine
    funds = session.query(
        ApplicationRow.application_origin_fund,  # Colonne pour l'origine des financements
        db.func.sum(db.func.coalesce(db.cast(ApplicationRow.application_grant, db.Float), 0))  # Somme des grants
    ).group_by(
        ApplicationRow.application_origin_fund  # Regrouper par origine
    ).all()

    # Passer les résultats au template
    return render_template('funds_table.html', data=funds)
if __name__ == "__main__":
    app.run(debug=True)