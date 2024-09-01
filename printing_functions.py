from newtask import show_message


acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
unprinted_designs = acc[:]
complete_modles = []
show_message(acc)


print("ghjg",unprinted_designs)
while unprinted_designs:
    current_design =unprinted_designs.pop()
    print (f'Printing model: {current_design}')
    complete_modles.append (current_design)
    
print ("\nThe foloing models have been printed:")
for complete_model in complete_modles:
    print (complete_model)