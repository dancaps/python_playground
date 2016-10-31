def greeting_for_all_friends(friends):
    greetings = []
    if friends == None:
        return None
    elif friends == []:
        return None
    else:
        for e in friends:
            greetings.append('Hello, ' + e + '!')

    return greetings
            

friends = ['Danny', 'Lisa', 'Jacob', 'Ryan']
#print(greeting_for_all_friends([]))

print(greeting_for_all_friends(None))
print(greeting_for_all_friends([]))
print(greeting_for_all_friends(["Bilal"]))
