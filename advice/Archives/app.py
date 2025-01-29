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

@app.route('/data/funds')
def data_funds():
    print("La route /data/funds a été appelée.")  # Debug
    session = Session(db.engine)
    funds = session.query(
        ApplicationRow.application_origin_fund,
        ApplicationRow.application_call_year,
        db.func.sum(db.cast(ApplicationRow.application_grant, db.Float))
    ).group_by(
        ApplicationRow.application_origin_fund,
        ApplicationRow.application_call_year
    ).all()
    print(funds)  # Debug : affiche les résultats dans la console

    data = [
        {"origin_fund": fund, "call_year": year, "total_grant": total}
        for fund, year, total in funds
    ]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)