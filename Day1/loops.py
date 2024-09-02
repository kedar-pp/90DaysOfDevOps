# list data structure
# list--> data structure which can hold multipe values of multiple type
# array--> data structure which csn hold multiple values of same type

list_of_cloud=["aws","azure","gcp","digitsl ocean","utho","alibaba","oracle"]

print(list_of_cloud)

# add a new cloud Salesforce

list_of_cloud.append("Salesforce")

# add new cloud IBM cloud

list_of_cloud.append("IBM cloud")

print(list_of_cloud)

list_of_cloud.insert(2,"Heroku")

print(list_of_cloud)

# for count of elements in list

print(len(list_of_cloud))

# iteration of list

for cloud in list_of_cloud:
    print(" ")
    print(cloud)

for i in range(1,11):
    print("Happy Learning")