from app.models import Currency, db

class CurrencyService:

    @staticmethod
    def get_all_currencies():
        return Currency.query.all()

    @staticmethod
    def get_currency_by_id(currency_id):
        return Currency.query.get(currency_id)

    @staticmethod
    def create_currency(id, name, representation):
        new_currency = Currency(id=id, name=name, representation=representation)
        db.session.add(new_currency)
        db.session.commit()
        return new_currency

    @staticmethod
    def delete_currency(currency_id):
        currency = Currency.query.get(currency_id)
        if currency:
            db.session.delete(currency)
            db.session.commit()
        return currency