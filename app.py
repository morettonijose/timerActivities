from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS  # Importe o CORS
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
import json
import os



app = Flask(__name__)
CORS(app)  # Configure o CORS para permitir todas as origens




# Caminho absoluto para o banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance/activities.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)





# Define o modelo Activity
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    totalTime = db.Column(db.String(120), nullable=False)
    totalStart = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Activity {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'category': self.category,
            'totalTime': self.totalTime,
            'totalStart': self.totalStart
        }







# Define a classe  para retornar uma lista de atividades
class Activities(Resource):
    def get(self):
        activities = Activity.query.all()
        activity_list = [activity.to_dict() for activity in activities]
        return jsonify(activity_list)






# Define a classe  para inserir uma nova atividade na lista
class AddActivity(Resource):
    def post(self):
        data = request.get_json()
        new_activity = Activity(
            name=data['name'],
            description=data['description'],
            status=data['status'],
            category=data['category'],
            totalTime=data['totalTime'],
            totalStart=data['totalStart']
        )
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({"message": "Atividade adicionada com sucesso", "activity": new_activity.to_dict()})






# Define a classe  para atualizar uma atividade existente
class UpdateActivity(Resource):
    def put(self, id):
        try:
            data = request.get_json()
            activity = Activity.query.get(id)
            if not activity:
                return jsonify({"message": "Atividade não encontrada"})

            activity.name = data.get('name', activity.name)
            activity.description = data.get('description', activity.description)
            activity.status = data.get('status', activity.status)
            activity.category = data.get('category', activity.category)
            activity.totalTime = data.get('totalTime', activity.totalTime)
            activity.totalStart = data.get('totalStart', activity.totalStart)

            db.session.commit()
            return jsonify({"message": "Atividade atualizada com sucesso", "activity": activity.to_dict()})
        except Exception as e:
            return jsonify({"message": "Erro interno ao atualizar a atividade", "error": str(e)})





# Define a classe  para deletar uma atividade existente
class DeleteActivity(Resource):
    def delete(self, id):
        try:
            activity = Activity.query.get(id)
            if not activity:
                return jsonify({"message": "Atividade não encontrada"})

            db.session.delete(activity)
            db.session.commit()
            return jsonify({"message": "Atividade deletada com sucesso"})
        except Exception as e:
            return jsonify({"message": "Erro interno ao deletar a atividade", "error": str(e)})
        


        

# Adiciona as rotas de classes para o add_resource disponibilizar o acesso a url da API
api.add_resource(Activities, '/activities')  #rota para listar atividade
api.add_resource(AddActivity, '/activity/new')  #rota para adicionar atividade
api.add_resource(UpdateActivity, '/activity/<int:id>')   #rota para atualizar atividade
api.add_resource(DeleteActivity, '/activity/del/<int:id>')  #  rota para deletar atividade


# Configura o Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API - Controle de Atividades"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open(os.path.join(basedir, 'static/swagger.json'), 'r') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)