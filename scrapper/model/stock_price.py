from scrapper.model.database import BaseModel


class StockPrice(BaseModel.model_db.Model):
    __tablename__ = 'stock_price'

    AppDb = BaseModel.model_db

    id = AppDb.Column(AppDb.Integer, primary_key=True)
    stock_id = AppDb.Column(AppDb.Integer, AppDb.ForeignKey('nse_stock.id', ondelete='SET NULL'), nullable=False)
    date = AppDb.Column(AppDb.Date, primary_key=True)
    high = AppDb.Column(AppDb.Float, nullable=True)
    low = AppDb.Column(AppDb.Float, nullable=True)
    closing_price = AppDb.Column(AppDb.Float, nullable=True)
    prev_year_high = AppDb.Column(AppDb.Float, nullable=True)
    prev_year_low = AppDb.Column(AppDb.Float, nullable=True)

    stock = AppDb.relationship('NseStock', backref='stock_price', lazy=True)

    def __int__(self, s_id, date, high, low, vwap, prev_high, prev_low):
        self.stock_id = s_id
        self.date = date
        self.high = high
        self.low = low
        self.closing_price = vwap
        self.prev_year_high = prev_high
        self.prev_year_low = prev_low

    def __repr__(self):
        return f'Stock:{self.nse_stock.name} high:{self.high} low:{self.low} vwap:{self.closing_price}'
