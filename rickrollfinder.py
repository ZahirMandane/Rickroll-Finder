while True:
    print("if the paste shortcut doesn't work, right click into the terminal")
    continueOrNot = input('type "link" to put in a youtube link, or press enter to quit: ')
    if continueOrNot.lower() == "link":
        print("reminder: if the paste shortcut doesn't work, right click into the terminal")
        print("Only links I have found can be added, I'm working on adding a place to give your rickroll links")
        link = input("Link: ")
        if link == "https://www.youtube.com/watch?v=dQw4w9WgXcQ":
            print("This idiot gave the official Rickroll video LOL")
        elif link == "https://www.youtube.com/watch?v=H8ZH_mkfPUY" or link == "https://www.youtube.com/watch?v=OnAQTm50598" or link == "https://www.youtube.com/watch?v=iik25wqIuFo" or link == "https://www.youtube.com/watch?v=xvFZjo5PgG0" or link == "https://www.youtube.com/watch?v=a6pbjksYUHY" or link == "https://www.youtube.com/watch?v=ub82Xb1C8os" or link == "https://www.youtube.com/watch?v=NfgZZfI_j5M" or link == "https://www.youtube.com/watch?v=QB7ACr7pUuE" or link == "https://www.youtube.com/watch?v=pKskW7wJ0v0" or link == "https://www.youtube.com/watch?v=dRV6NaciZVk" or link == "https://www.youtube.com/watch?v=iik25wqIuFo" or link == "https://www.youtube.com/watch?v=ll-mQPDCn-U":
            print("thats a rickroll")
        else:
            print("not a rickroll, or at least it isn't in my list")
    else:
        break
    