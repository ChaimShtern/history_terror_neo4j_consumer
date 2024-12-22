from returns.maybe import Maybe
from app.db.connection import driver


def create_country_repo(country):
    with driver.session() as session:
        query = """
        create (c:Country{
        name:$name, 
        }) return t
        """
        params = {
            "name": country['name'],
        }
        res = session.run(query, params).single()
        return (Maybe.from_optional(res.get('c'))
                .map(lambda c: dict(c)))
