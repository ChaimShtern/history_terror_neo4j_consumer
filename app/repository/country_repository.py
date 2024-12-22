from app.db.crud import create


def create_country(country: str):
    return create({"name": country}, ["Country"])

