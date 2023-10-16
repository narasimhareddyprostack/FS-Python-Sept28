#dict.get(key)  # return value associated with key
#pop(key)       # remove entry(key:value) from dict based key.

#keys()         # return all keys
#values()       # retur nall valeus
#items()        # return all key:values 

#popitem()      # remove the random entry(key:value)

emp={'id':101, 'name':'rahul','loc':'wayand'}

print(emp.get('id'))    #101
print(emp.get('name'))  #rahul

emp.pop('loc')
emp.popitem()
print(emp)