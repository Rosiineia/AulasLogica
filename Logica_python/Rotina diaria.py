relogio_despertou = (input("Que horas são?"))
if relogio_despertou > "6h":
    print("Pode levantar!!")

elif relogio_despertou == "6h":
    print("Ativar soneca.")
else:
    print("Ainda é cedo não precisa levanar")

nome = input("Qual seu nome?")
print("Bom dia!!" + nome + ', espero que tenha dormido bem!!')

comecar = input("Vamos começar?")
if comecar == 'sim':
    print("Vamos lá então!!")
else:
    print("Ok, começamos quanto estiver pronto(a).")
    #ir ao banheiro

ir_ao_banheiro=input("O banheiro está ocupado? ")
if ir_ao_banheiro!= 'sim':
    print("pode entrar!")
else:
    print("Aguarde, por favor")
#café da manhã

tomar_café = input("Você vai tomar café da manhã?")
if tomar_café =='sim':
    print("Otimo, vamos pegar a cafeteira")
else:
    print("Ok, tenha um otimo dia então!")
tomando_café= input("Tem café na cafeteira? ")
if tomando_café =='sim':
    print("Pode servir o café")
else:
    print("Por favor, faça o café")











