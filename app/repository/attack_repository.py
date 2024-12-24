from returns.maybe import Maybe
from app.db.connection import driver
import toolz as t


def create_attack_repo(attack):
    with driver.session() as session:
        query = """
        merge(r: Region{name:$region_name})
        merge(c: Country{name:$country_name})
        merge(g: Group{name:$group_name})
        merge(g) - [:ATTACKED{type:$type,
                target:$target}]-> (c)
        merge (c) -[:IS_IN]-> (r)
        return c, g,r
        """
        params = {
            "country_name": attack['country_name'],
            "group_name": attack['group_name'],
            "type": attack['type'],
            "target": attack['target'],
            "region_name": attack['region_name']
        }
        res = session.run(query, params).data()
        return t.pipe(
            res,
            t.partial(t.pluck, 'c'),
            list
        )
