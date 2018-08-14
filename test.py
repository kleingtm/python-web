from stellar_base.address import Address
publickey = 'GCSNF6RJBAVWMBSUNL4JYIETGYCOKZ3FWCUNTZDRORGJ4BLU2FE5SGOV'
address = Address(address=publickey, network='public') # address = Address(address=publickey,network='public') for livenet
print(address.get()) # get the updated information