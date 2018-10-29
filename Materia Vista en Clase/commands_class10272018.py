# my_dict = {} to create an empty dict
mi_dict =  {}
type(mi_dict)
mi_dict = {'juan' : 88, 'pedro' : 1, 'jose' : 56}
mi_dict['pedro'] # output will be 1

# To start adding/changing value pair keys we use the [] brackets
mi_dict['pedro'] = 2 # assignment of a new value for the key
mi_dict['pedro'] # output will be 2
mi_dict # output of the dictionary will include new value for the 'pedro' key
mi_dict['pedro'] = [90,10,29] # assignment of a new value for the key (in the form of a list)
mi_dict # output of the dictionary will include new value for the 'pedro' key
mi_dict['pedro'] = mi_dict['juan'] # value of two different keys is pointing to same object
mi_dict # output of the dictionary will show the new value for the 'pedro' key
del(mi_dict['pedro'])
mi_dict
