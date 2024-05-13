from models.production_line import ProductionLine
from models.harness import HarnessModel

from database import db


class ProductionJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ref = db.Column(db.String(50))
    production_line_id = db.Column(db.Integer, db.ForeignKey('production_line.id'))
    harness_id = db.Column(db.Integer, db.ForeignKey('harness.id'))
    demanded_quantity = db.Column(db.Integer, default=0)
    delivered_quantity = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)

    def __init__(self,ref,production_line_id, harness_id, demanded_quantity,delivered_quantity,status  ) -> None:
        super().__init__()
        self.ref = ref
        self.production_line_id = production_line_id
        self.harness_id = harness_id
        self.demanded_quantity = demanded_quantity
        self.delivered_quantity = delivered_quantity
        self.status = status

    def to_dict(self):
        production_line = ProductionLine.query.get(self.production_line_id)
        harness = HarnessModel.query.get(self.harness_id)
        return {
            'id': self.id,
            'ref': self.ref,
            'production_line_id': self.production_line_id,
            'harness': harness.to_dict(),
            'demanded_quantity': self.demanded_quantity,
            'delivered_quantity': self.delivered_quantity,
            'production_line': production_line.to_dict(),
            'status': self.status
        }
