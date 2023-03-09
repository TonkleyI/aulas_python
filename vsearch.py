# %%
def search_for_letters(frase: str, letras: str = 'aeiou') -> set:
    ''' Retorna o conjunto de vogais encontradas na "frase".
    '''
    return set(letras).intersection(set(frase))

#Docstring


# %%

search_for_letters(frase='Aulas de Python', letras = 'ae')

# %%