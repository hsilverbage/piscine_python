ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

# List (✅ Mutable — you can change values). Lists are editable.
ft_list[1] = "World!" 

# Tuple (❌ Immutable — you cannot change values). Tuples cannot be modified after creation.
ft_tuple = ("Hello", "France!")

# Set (⚠️ Mutable but unordered — no index access). Sets don’t allow indexing, so you can’t “change” a value directly. 
ft_set.remove("tutu!")
ft_set.add("Lyon!")

# Dictionary (✅ Mutable — change via keys). Dictionaries are editable using keys. {key : value}
ft_dict["Hello"] = "42 Lyon!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)