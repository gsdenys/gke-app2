from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
# from flask_restful import Resource, Api
import datetime

app = Flask(__name__) 
# api = Api(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app2:app2@35.224.118.252/stacklabstest' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) 
ma = Marshmallow(app)

class Access(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cfrom = db.Column(db.String(32))
    cip = db.Column(db.String(32))
    cdate = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, cfrom, cip):
        self.cfrom = cfrom
        self.cip = cip


class AccessSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cfrom', 'cip')


access_schema = AccessSchema() 
accesss_schema = AccessSchema(many=True)


@app.route('/', methods=['GET'])
def health():
    return ""

@app.route('/app2', methods=['GET'])
def get():
    try: id = request.args['id']
    except Exception as _: id = None

    if not id:
        access = Access.query.all()
        return jsonify(accesss_schema.dump(access))
    
    access = Access.query.get(id)
    return jsonify(access_schema.dump(access))

@app.route('/app2', methods=['POST'])
def post():
    cfrom = request.json['from']
    cip = request.json['ip']

    access = Access(cfrom, cip)
    db.session.add(access)
    db.session.commit()

    return jsonify({
        'Message': f'Access {cfrom} {cip} inserted.'
    })


db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
