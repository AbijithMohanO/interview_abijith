def find_duplicates():
    # To create a list of unique data from file.
    unique_data =[]
    for i in range(100):
        filename = str(i)+'.txt'
        with open (filename, 'r') as file:
            data = file.readlines()
            data = data[0]
            unique_data.append(str(data))
            unique_data = list(set(unique_data))
    
# Grouping files containing same content. Assumes Number of unique content is equal to 10(as given in question   
    content_list =[[] for i in range(10)]
    
    for i in range(100):
        filename = str(i)+'.txt'
        with open(filename,'r') as file:
            data = file.readlines()
            data = data[0]
            if data in unique_data:
                content_list[unique_data.index(data)].append(str(i))
    return content_list
# Driver Function
if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))
    