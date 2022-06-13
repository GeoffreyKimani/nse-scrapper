from scrapper.model.database import BaseModel


class NseStock(BaseModel.model_db.Model):
    __tablename__ = 'nse_stock'

    AppDb = BaseModel.model_db

    # fields
    id = AppDb.Column(AppDb.Integer, primary_key=True)
    name = AppDb.Column(AppDb.String, nullable=False)
    sector = AppDb.Column(AppDb.String, nullable=False)
    isin_code = AppDb.Column(AppDb.String, nullable=False, unique=True)

    def __int__(self, name, sector, code):
        self.name = name
        self.sector = sector
        self.isin_code = code

    def __repr__(self):
        return f'Stock:{self.name} Sector:{self.sector}'

    @staticmethod
    def stock_exists(code):
        if NseStock.query.filter(
                NseStock.isin_code == code
        ).first():
            return True
        return False
