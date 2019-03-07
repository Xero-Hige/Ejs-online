# def dividir_por_enteros(lista, k):

def pruebas():
    assert dividir_por_enteros([1,3,2],4) == ([1,3,2],[],[])
    assert dividir_por_enteros([],5) == ([],[],[])
    assert dividir_por_enteros([9.3,4,7,5],5) == ([3,4],[5],[9,7])


pruebas()
