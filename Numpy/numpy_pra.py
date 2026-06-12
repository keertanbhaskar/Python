import numpy as np

my_list = np.array([1,2,3,4])
print(my_list)
print(type(my_list))


print("--------- Two dimensional Array -----------")
a = np.array([[1,2,3],[4,5,6]])

print(a.ndim)     # dimensions
print(a.shape)    # rows, columns
print(a.size)     # total elements
print(a.dtype)    # datatype


print("--------- Three dimensional Array -----------")
ThreeDArray = np.array([[[1,2,3],[4,5,6]],
                        [[7,8,9],[0,1,2]]
                        ])
print(ThreeDArray.ndim) #shows dimension
print(ThreeDArray.shape)

print(ThreeDArray[0,0,2]) #accessing element index wise(multidimensional indexing)

word = ThreeDArray[0,0,2] + ThreeDArray[1,0,0]





print("================ Slicing ===================")
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

# arr[start:end:step]
print(arr[0:3])
print(arr[0:4:2])
print(arr[::4])
print(arr[::-1])
print("\n")


# selecting columns
print(arr[:,0])
print(arr[:,1:4])
print(arr[:,1::2])



# rows and columns selection
print(arr[0:2,0:2])




print("================= Scalar arithmetic operations ===============")
arr1 = np.array([1,2,3,4,5])
print(arr1+1)
print(arr1*3)
print(arr1**4)

# element-wise arithmetic
arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])
print(arr3 + arr4)
print(arr3 - arr4)
print(arr3 * arr4)




# vectorized math func
arr2 = np.array([1,2,3,4,5])
print(np.sqrt(arr2))
print(np.round(arr2))
print(np.pi)

radii = np.array([1,2,3])
print(np.pi*radii**2)




# Comparison operators
scores = np.array([91,55,100,73,82,64])
print(scores == 100)
print(scores >= 80)
scores[scores < 60 ] = 0
print(scores)



print('=================== broadcasting =============')
arr5 = np.array([[1,2,3,4]])
arr6 = np.array([[1],[2],[3],[4]]) 
print(arr5*arr6)

arr7 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr8 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(arr7 + arr8)




print("================= Aggregate functions ==============")
arr9 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
print(np.std(arr9))
print(np.var(arr9))
print(np.min(arr9))
print(np.max(arr9))
print(np.sum(arr9,axis=0))


print("=========================== filtering =====================")
ages = np.array([[21,23,19,20,18,65],[70,23,15,18,19,80]])
print(ages[ages < 20])

# adults
print(ages[(ages >= 18) & (ages <= 65)])

adults = np.where(ages >= 10,ages,0)
print(adults)




print("==================Random module ==========")
rng = np.random.default_rng(seed=1)
print(rng.integers(1,101,size=(3,2))) # integers(low=1,high=7)
print(np.random.uniform(low=-1,high=1,size=3))


array1 = np.array([1,2,3,4,5])
rng.shuffle(array1)
print(array1)

fruits = np.array(['apple','orange','banana','coconut'])
fruit=rng.choice(fruits) #choice(fruits,size=(2,3))
print(fruit)



print(np.zeros((2,3)),"\n")
print(np.ones((2,2)),"\n")
print(np.eye(3),"\n")
print(np.arange(1,10,2),"\n")
print(np.linspace(0,1,5),"\n")