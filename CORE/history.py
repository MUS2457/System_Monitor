def view_history(collection, n = 5) :
    if not collection:
        print("please wait until data been collected.")
        return

    count = min(n, len(collection))

    for metics in collection[-count:] :

        print(metics)





