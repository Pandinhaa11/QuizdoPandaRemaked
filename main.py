print("Bem-vindo ao Quiz!")
print("--------------------")
print("beta 1.1 no gui")

perguntas = [
    {
        "pergunta": "Por quem a gravidade foi descoberta?",
        "respostas": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Leonardo da Vinci"],
        "correta": "Isaac Newton"
    },
    {
        "pergunta": "Por qual o orgão que os seres humanos respiram?",
        "respostas": ["Coração", "Pulmão", "Fígado", "Rim"],
        "correta": "Pulmão"
    },
    {
        "pergunta": "Qual foi o país que os Portugueses descobriram?",
        "respostas": ["Alemanha", "Espanha", "Brasil", "Índia"],
        "correta": "Brasil"
    },
    {
        "pergunta": "Qual o nome do dispositivo que os computadores usam? Dica:usa espaço",
        "respostas": ["Disco Rígido", "Unidade de CD", "Memória RAM", "Pendrive"],
        "correta": "Disco Rígido"
    },
        
    {
        "pergunta": "Qual é o componente responsável por armazenar temporariamente dados que a CPU está utilizando?",
        "respostas": ["Disco Rígido", "Memória RAM", "Placa Mãe", "Fonte de alimentação"],
        "correta": "Memória RAM"
    },
    {
        "pergunta": "Quanto é 9 + 10?",
        "respostas": ["18", "19","20","21","22",],
        "correta": "19"
    }

]

pontos = 0

for pergunta in perguntas:
    print(pergunta["pergunta"])
    for i, resposta in enumerate(pergunta["respostas"]):
        print(f"{i+1}. {resposta}")
    resposta_usuario = input("Escolha uma opção: ")
    if pergunta["respostas"][int(resposta_usuario) - 1] == pergunta["correta"]:
        print("Parabéns, você acertou!")
        pontos += 1
    else:
        print(f"Erro, a resposta correta é {pergunta['correta']}")
        pontos -= 1

print(f"Você fez {pontos} pontos!")
print("Pressione qualquer tecla para sair...")
input()