def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Elemento encontrado, retornar índice
        elif arr[mid] < target:
            left = mid + 1  # Buscar na metade direita do array
        else:
            right = mid - 1  # Buscar na metade esquerda do array
            
    return -1  # Elemento não encontrado

# Exemplo de uso
if __name__ == "__main__":
    arr = [2, 5, 7, 11, 15, 18, 22, 25]
    target = 18
    
    index = binary_search(arr, target)
    if index != -1:
        print(f"O elemento {target} foi encontrado no índice {index}.")
    else:
        print(f"O elemento {target} não foi encontrado no array.")
