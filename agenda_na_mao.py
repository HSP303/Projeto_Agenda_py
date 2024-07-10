agenda = {
    "pedro":{
        "tel":"99999-5468",
        "email":"pedro@email.com",
        "endereco":"av 1"
    },
    "joao":{
        "tel":"94356-5342",
        "email":"joao@email.com",
        "endereco":"av 2"
    },
    "robsom":{
        "tel":"924355-5432",
        "email":"robsom@email.com",
        "endereco":"av 3"
    },
    "janice":{
        "tel":"90546-6798",
        "email":"janice@email.com",
        "endereco":"av 4"
    },
}

#print(agenda["pedro"]["tel"])

agenda["janice"]["email"] = "janicehoepers@gmail.com"

#print(agenda["janice"]["email"])

#agenda.pop("joao")
#for contato in agenda:
#        print(contato)

agenda["vinicius"] = {
    "tel":"98707-4578",
    "email":"vinicius@gmail.com",
    "endereco":"av 5"
}
print(agenda["vinicius"]["endereco"])

for contato in agenda:
        for info in agenda[contato]:
            print(agenda[contato][info])