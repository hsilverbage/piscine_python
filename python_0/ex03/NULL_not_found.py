def NULL_not_found(object: any) -> int:

    match object:
        case False:
           print(f"Fake: {object} {type(object)}")
        case "":
            print(f"Empty: {object} {type(object)}")
        case 0:
            print(f"Zero: {object} {type(object)}")
        case None:
            print(f"Nothing: {object} {type(object)}")
        case _:
            if type(object) is float and (object != object) :
                print(f"Cheese: {object} {type(object)}")
            else :
                print("Type not NULL_not_found")
                return 1
    return 0
