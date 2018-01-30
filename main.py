while True :
    print('please choose from 0 to 7')
    print(' 1- MergeSort')
    print(' 2- Stack')
    print(' 3- HeapTree')
    print(' 4- BST')
    print(' 5- HeapSort')
    print(' 6- BucketSort')
    print(' 7- Prim')
    print(' 0- Quit')
    a = input()
    if a == '1':
        import mergesort

    elif a == '2':
        import stack

    elif a == '3':
        import heaptree

    elif a == '4':
        import BST

    elif a == '5':
        import heapsort

    elif a == '6':
        import bucketsort

    elif a == '7':
        import prim

    elif a == '0':
        break
