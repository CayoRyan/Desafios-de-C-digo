def matrix_sum(matrix1, matrix2):
    # Verificar se as matrizes têm o mesmo tamanho
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Matrizes de tamanhos diferentes, não é possível realizar a soma
    
    # Inicializar uma matriz para armazenar a soma
    result = [[0]*len(matrix1[0]) for _ in range(len(matrix1))]
    
    # Realizar a soma elemento por elemento
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

# Exemplo de uso
if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    result = matrix_sum(matrix1, matrix2)
    if result:
        print("A soma das matrizes é:")
        for row in result:
            print(row)
    else:
        print("As matrizes têm tamanhos diferentes e não podem ser somadas.")
