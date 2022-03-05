# ITERATE THROUGH ALL THE KEYS
states_capital={"Sikkim":"Gangtok","Bihar":'patna',"rajasthan":"jaipur","maharastra":"mumbai"}
for state in states_capital:
    print(state)

# ITERATE THROUGH ALL THE VALUES
states_capital={"Sikkim":"Gangtok","Bihar":'patna',"rajasthan":"jaipur","maharastra":"mumbai"}
for state in states_capital:
    print(states_capital[state])

# HOW TO PRINT KEYS AND VALUES TOGETHER FROM A DICTIONARY
movies={"name":"avengers","hero":"captain america","rating":9.9}
for x,y in movies.items():
    print(x,y)