from returns.maybe import Maybe
from app.db.connection import driver


def create_group_repo(group):
    with driver.session() as session:
        query = """
        create (g:Group{
        name:$name, 
        }) return g
        """
        params = {
            "name": group['name'],
        }
        res = session.run(query, params).single()
        return (Maybe.from_optional(res.get('g'))
                .map(lambda g: dict(g)))
