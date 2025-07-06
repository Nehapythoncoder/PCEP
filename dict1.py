def rename_key(my_dict,old_key,new_key):
    if old_key in my_dict:
        my_dict[new_key]= my_dict.pop(old_key)
        return my_dict
sample_dict = {"name":"Tara","RollNo":130046,"Mark":486,"Age":16}
print("Before Rename Key of Dictionary = ",sample_dict)
sample_dict = rename_key(sample_dict,"RollNo","RegNo")
sample_dict = rename_key(sample_dict,"Mark","Mark10")
print("After Rename Key of a Dictionary=",sample_dict)
