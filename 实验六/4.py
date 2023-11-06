def find_senior(lst): 
    max_age = 0
    oldest_developers = []
    
    for developer in lst:
        age = developer['age']
        if age > max_age:
            max_age = age
            oldest_developers = [developer]
        elif age == max_age:
            oldest_developers.append(developer)
    
    return oldest_developers