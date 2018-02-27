from kiroku.models import db, Client
from kiroku.apis.v1.utils import encode_client_token

c1 = Client(name='doctor_one')
c2 = Client(name='doctor_two')
db.session.add_all([c1, c2])
db.session.commit()

c1 = Client.query.get(1)
encode_client_token(c1)