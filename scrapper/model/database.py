from scrapper.app_factory import db


class BaseModel(object):
    model_db = db

    @staticmethod
    def migrate_db():
        from scrapper.model.nse_stock import NseStock
        from scrapper.model.stock_price import StockPrice

        return [NseStock, StockPrice]
