def create_attr_model_user(data, obj):
    for i in data.items():
        if hasattr(obj, i[0]):
            setattr(obj, f'company_{i[0]}', i[1])
            continue
        if isinstance(i[1], dict):
            create_attr_model_user(data=i[1], obj=obj)
        else:
            setattr(obj, i[0], i[1])


def create_attr_model_post(data, obj):
    for i in data.items():
        if isinstance(i[1], dict):
            create_attr_model_post(data=i[1], obj=obj)
        else:
            setattr(obj, i[0], i[1])
