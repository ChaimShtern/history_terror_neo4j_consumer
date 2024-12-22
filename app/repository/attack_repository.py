from returns.maybe import Maybe
from app.db.connection import driver
import toolz as t


def create_attack_repo(attack):
    with driver.session() as session:
        query = """
        match(c: Country{name:$country_name})
        match(g: Group{name:$group_name})
        create (a:Attack{type:$type,
                target:$target })
        merge(g) - [:ATTACKED]->(a) -[:WAS_IN] -> (c)

        return c, g, a
        """
        params = {
            "country_name": attack['country_name'],
            "group_name": attack['group_name'],
            "type": attack['type'],
            "target": attack['target'],
        }
        res = session.run(query, params).data()
        return t.pipe(
            res,
            t.partial(t.pluck, 'c'),
            list
        )
