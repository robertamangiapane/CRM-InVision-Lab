from .models import *


def get_filters(filters):
    real_filter = get_real_filter(filters)
    columns = get_columns_dict(real_filter)
    m_to_m = get_m_to_m_dict(real_filter)
    sort_params = dict(columns, **m_to_m)

    return sort_params


def get_columns_dict(filters):
    column_dict = {}
    for k, v in dict(filters).items():
        if not isinstance(v, Skill) and v is not None:
            column_dict[k + "__exact"] = v

    return column_dict


def get_m_to_m_dict(filters):
    m_to_m_dict = {}
    for k, v in dict(filters).items():

        if isinstance(v, Skill):
            m_to_m_dict.update({k + "__name__contains" : v.name})

    return m_to_m_dict


def get_real_filter(filters):
    real_filters = {}
    for k, v in filters.items():
        if filters[k] != "":
            real_filters[k] = v
    return real_filters


