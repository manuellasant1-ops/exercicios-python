nota_avaliacao= float(input("nota da avaliação (0 a 10):"))
projetos_entregues= int(input("projetos entregues no semestre:"))

if nota_avaliacao>= 8.0 and projetos_entregues >= 3:
    print("bonus de desempenho aprovado!")
else:
    print("bonus negado. metas nao atingidas integralmente.")