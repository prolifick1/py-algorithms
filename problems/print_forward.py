def print_forward(llist):
    if(!llist):
        return
    print(llist.val)
    print_forward(llist.next)

