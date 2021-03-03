def problem31():
    ways = 1
    for a in range(3):
        for b in range(1+int((200-100*a)/50)):
            for c in range(1+int((200-100*a-50*b)/20)):
                for d in range(1+int((200-100*a-50*b-20*c)/10)):
                    for e in range(1+int((200-100*a-50*b-20*c-10*d)/5)):
                        for f in range(1+int((200-100*a-50*b-20*c-10*d-5*e)/2)):
                            ways += 1
    return ways 
