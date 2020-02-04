def prime_check(num):
    import time
    start = time.time()
    prime_list = [2, 3, 5, 7]
    iters = 10
    while iters <= num + 1:
        count = 0
        for x in range(len(prime_list)):          
            if iters % prime_list[count] == 0:
                break
            elif count == len(prime_list) - 1:
                prime_list.append(iters)
            
            count += 1
            
        iters += 1
            

        
     
        
               
    print(prime_list)
    print("\n")
    print(len(prime_list))
    print(sum(prime_list))
    end = time.time()
    print("Time taken: " + str(end - start) + " seconds")
    return ""

print(prime_check(100000))
    

#Takes about 9 seconds if you put 100000