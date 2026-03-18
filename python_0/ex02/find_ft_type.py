def all_thing_is_obj(object: any) -> int:

    type_names = {
        list : "List : ",
        tuple : "Tuple : ",
        set : "Set : ",
        dict : "Dict : "
    }

    object_type = type(object)
    type_name = type_names.get(object_type, "Type not found")
    kitchen = " is in the kitchen : "

    if (object_type == str) :
        print(f"{object}{kitchen}{object_type}")
    elif (type_name == "Type not found") :
        print(type_name)
    else :
        print(f"{type_name}{object_type}")
    return 42
