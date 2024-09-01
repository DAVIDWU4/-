def show_message(apple):
    sent_message = []
    while apple:
        save = apple.pop(0)
        print (save)
        sent_message.append(save)
        print (f"apple: {apple}")
        print ("sent message: ",sent_message)
    return(apple,sent_message)