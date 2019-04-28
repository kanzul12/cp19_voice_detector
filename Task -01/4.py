par_graph=input("enter paragraph...")
f=par_graph.split(".")
for para_graph in f:
    print(para_graph.strip().capitalize()+". ", end="")