#Alunos Exclusivos da Turma A (Diferença Múltipla) 
# Dadas três listas de turmas, encontre os alunos que estão na Turma A, 
# mas que não estão nem na Turma B nem na Turma C

turma_A = ["Zeca", "Maria", "Pedro", "Lia", "Rui"]

turma_B = ["Pedro", "João", "Ana", "Lia"]

turma_C = ["Ana", "Bia", "Rui", "Gabi"]

print(set(turma_A).difference(set(turma_B).union(set(turma_C))))

#Alunos em Pelo Menos Duas Turmas (Interseção Múltipla) 
# Usando as mesmas três listas de turmas do exercício 7, 
# encontre os alunos que estão matriculados em pelo menos duas turmas 
# (ou seja, A e B, ou A e C, ou B e C, ou A, B e C).


print(set(turma_A) & set(turma_B) | set(turma_A) & set(turma_C) | set(turma_B) & set(turma_C))
