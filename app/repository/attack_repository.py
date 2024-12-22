from app.db.crud import merge
from app.models import Attack


def create_attack(attack: Attack):
    group_params = attack.group.model_dump()
    country_params = attack.country.model_dump()
    rel_params = attack.model_dump(exclude={"country", "group"})
    rel = "ATTACKED"
    merge(
        node_one_params=group_params,
        node_one_labels=['Group'],
        node_two_params=country_params,
        node_two_labels=['Country'],
        rel=rel,
        rel_params=rel_params
    )


