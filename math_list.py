class math_list:
    
    def __init__(self, array):
        self.math_list = [] #The actual instance of a list that will store all of the data
        
        #Make sure that none of the items passed into the class are anyting other than floats or ints
        for x in array:
            if(not type(x) == float and not type(x) == int): 
                print("arguments can only be floats or integers")
                return
            self.math_list.append(float(x)) #adds all obejects to the list and casting them as floats
            
    def __str__(self):
        return str(self.math_list) #returns the string representation of the math_list list
        
    def __eq__(self, math_list2):
        if(self.length() != math_list2.length()):
            return False
        for i in range(0, self.length()):
            if(self.get(i) != math_list2.get(i)):
                return False
        return True
        
    
    #Basic Funtions
    
    #Find the max value
    def get_max(self):
        vmax = self.get(0)
        for i in range(0, self.length()):
            if (self.get(i) > vmax):
                vmax = self.get(i)
        return vmax
    
    #Find the min value
    def get_min(self):
        vmin = self.get(0)
        for i in range(0, self.length()):
            if (self.get(i) < vmin):
                vmin = self.get(i)
        return vmin
        
    #Find the sum of the list
    def get_sum(self):
        total = 0
        for i in self.math_list:
            total = total + i
        return total
    
    #Find the mean of the list
    def get_mean(self):
        return self.get_sum() / self.length()
        
    #find the meadian of the list
    def get_median(self):
        temp_list = math_list(self.math_list)
        print(temp_list)
        self.sort()
        r_value = 0.0
        if (self.length() % 2 == 0):
            r_value = self.get(self.length()//2) + self.get(self.length()//2 - 1)
            r_value = r_value / 2
        else:
            r_value = self.get(self.length()//2)
        for i in range(0, temp_list.length()):
            self.set_to(i, temp_list.get(i))
        return r_value
        
    #Find the mode(s) of the list
    def get_mode(self):
        count = [[], []]
        for i in self.math_list:
            found = False
            for j in range(0, len(count[0])):
                if(i == count[0][j]):
                    count[1][j] = count[1][j] + 1
                    found = True
            if(not found):
                count[0].append(i)
                count[1].append(1)
        index = [0]
        for i in range(1, len(count[0])):
            if (count[1][i] > count[1][index[0]]):
                    index = [i]
            elif(count[1][i] == count[1][index[0]]):
                    index.append(i)
        r_val = []
        for i in range(0, len(index)):
            r_val.append(self.get(index[i]))
        return r_val
    
    #get the standard deviation of the list
    def get_stdv(self):
        mean = self.get_mean()
        total = 0
        for i in self.math_list:
            total = total + ((i - mean) ** 2)
        return (total / self.length()) ** float(1/2)
    
    #Sort the array using quick sort
    def sort(self, low = 0, high = None):
        if(high == None):
            high = self.length() - 1
        if(low < high):
            pi = self.__partition(low, high)
            
            self.sort(low, pi - 1)
            self.sort(pi + 1, high)
            
    
    #IO funtions as well as basic information about characteristics of the list
    
    #gets the length of the math_list
    def length(self):
        return len(self.math_list) #returns the length of the math_list list
        
    #get value from list    
    def get(self, index):
        return self.math_list[index]
    
    #set math_list at index to new value
    def set_to(self, index, new_value):
        if(self.__check_type([new_value])):
            print("The math_list only accepts ints and floats")
            return
        self.math_list[index] = float(new_value)
        
    #append arbitrary number of values at end of list
    def append(self, *values):
        if(self.__check_type(values)):
            print("The math_list only accepts ints and floats")
            return
        for x in values:
            self.math_list.append(float(x))
    
    #insert arbitrary number of values at index
    def insert(self, *values, index):
        if(self.__check_type(values)):
            print("The math_list only accepts ints and floats")
            return
        for i in range(1, len(values) - 1):
            self.math_list.insert(float(values[-i]))
            
    #remove items from list from start paramater to end parameter        
    def remove(self, start, end):
        diff = end - start + 1
        for i in range(0, diff):
            self.pop(start)
    
    #remove item by index from list and return removed item
    def pop(self, index):
        return self.math_list.pop(index)
    
    #swap two elements of the math list    
    def swap(self, x, y):
        self.math_list[x], self.math_list[y] = self.math_list[y], self.math_list[x]
        
    #File I/0
    
    #write list to file
    def write_to_file(self, path):
        file = open(path, "wb")
        
        
    #methods not ment to be accessed outside of the class
    
    #make sure only ints and floats are being added to the list
    def __check_type(self, values):
        for i in values:
            if(not type(i) == int and type(i) == float):
                return False
        return True
        
    #used for sorting the list    
    def __partition(self, low, high):
        i = low - 1
        pivot = self.get(high)
        for j in range(low, high):
            if(self.get(j) < pivot):
                i = i+1
                self.swap(i, j)
                
        self.swap(i+1, high)
        return i+1
    
    #used to convert a float to bytes
    def float_to_binary(self, num):
        hex_r = float.hex(num)
        print(hex_r)
        base = int(hex_r[4:17], 16)
        print(base)
        
