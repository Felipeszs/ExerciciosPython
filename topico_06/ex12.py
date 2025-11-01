#Lista de Presença Completa (União) 
# Você tem listas de alunos que participaram de duas aulas diferentes (Aula de Manhã e Aula de Tarde). 
# Crie uma lista única com o nome de todos os alunos que participaram de pelo menos uma das aulas, sem duplicatas.

aula_manha = ["Zeca", "Maria", "Pedro", "Lia"]

aula_tarde = ["Pedro", "Lia", "Ana", "Bia"]

alunos_participaram = []
alunos_participaram.append(set(aula_manha).union(set(aula_tarde)))

print(alunos_participaram)