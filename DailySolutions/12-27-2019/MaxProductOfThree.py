def maximum_product_of_three(array):
    if(len(array) < 3):
        return
        
    maxProduct = array[0] * array[1] * array[2]
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                currentProduct = array[i] * array[j] * array[k]
                maxProduct = max(currentProduct, maxProduct)

    return maxProduct
    

