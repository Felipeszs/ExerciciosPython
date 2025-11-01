# Verificação de Permissões (Subconjunto) 
# Um sistema tem uma lista de permissões necessárias para executar uma ação 
# e uma lista das permissões que um usuário possui. 
# Verifique se o usuário tem todas as permissões necessárias.

permissoes_necessarias = ["admin", "read", "write"]

usuario_1_permissoes = ["read", "write", "admin", "delete"]

usuario_2_permissoes = ["read", "write"]

def isPermission(usuario):
    return set(permissoes_necessarias) <= set(usuario)
     

print(isPermission(usuario_1_permissoes))
print(isPermission(usuario_2_permissoes))