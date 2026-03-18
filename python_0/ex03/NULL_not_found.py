def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    print(obj_type)
    print(object)

    match object:
        case str():
            print("is str")
        case int():
            print("is int")
        case float():
            print("is floateur")
        case None:
            print("air")
    # error 
        # return 1
    # all good 
    return 0

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not NULL_not_found
1