# from django.db.models import Q


def collaborator_filter(filters):
    real_filter = get_real_filter(filters)
    columns = get_columns_dict(real_filter)
    m_to_m = get_m_to_m_dict(real_filter)
    sort_params = dict(columns, **m_to_m)

    return sort_params


def get_columns_dict(filters):
    column_dict = {}
    for k, v in dict(filters).items():
        if k != "main_skills" and k != "secondary_skills":
            column_dict[k + "__exact"] = v

    return column_dict


def get_m_to_m_dict(filters):
    m_to_m_dict = {}
    for k, v in dict(filters).items():
        if k == "main_skills" or k == "secondary_skills":
            if not isinstance(v, type(None)):

                m_to_m_dict.update({k + "__name__contains" : v.name})

    return m_to_m_dict


def get_real_filter(filters):
    real_filters = {}
    for k, v in filters.items():
        if filters[k] != "":
            real_filters[k] = v
    return real_filters


# def collaborator_filter(filters):
#     real_filter = get_real_filter(filters)
#     params = ""
#     for k, v in dict(real_filter).items():
#         if k == "main_skills" or k == "secondary_skills" and not isinstance(v, type(None)):
#             params += ("Q(" + k + "__name_contains = " + v.name + ") | ")
#         else:
#             params += ("Q( " + k + "__exact = " + v.name + ") | ")
#
#     # params += " Q( " + k + "__exact = " + v.name + ") |"
#
#     return params[0:-3]

