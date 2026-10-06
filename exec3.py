idade = int(input("idade do candidato:"))
if idade >= 18:
    print("✅Acesso liberado ao sistema de RH")
    print("iniciando processo de admissão...")
else:
    print("❌bloqueio de sistema: candidato menor de idade.")