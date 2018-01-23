yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Yale', 'Stanford', 'KAUST']

ours1 = mine + yours
print (ours1)

ours2 = []
ours2.append(mine)
ours2.append(yours)
print (ours2)
# Ours1 is "mine" + "yours" directly, a new list. Ours2 is a null set at first. Then add "mine" and "yours".

yours[1:2] = ['Harvard']
print (mine)
print (yours)
print (ours1)
print (ours2)
# Ours1 is a new list and has been defined. Ours2 has three components, [], mine and yours. If mine, one of the components, changes, the whole list changes.
