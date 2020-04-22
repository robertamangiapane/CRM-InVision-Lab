def collaborator_filter(filters):
    columns = []
    m_to_m = []

    for k, v in dict(filters).items():
        if k == "main_skills":
            m_to_m.append(k)
        else:
            columns.append(k)

    print(columns)
    print(m_to_m)
