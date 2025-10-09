import easygui as EG 

msg="Cartoon"
title="Navigation"
myList=["Next", "Previous","Exit"]
myImg = ["og_og_1504606122276554174.jpg" , "fotooboi_20na_20stenu_20zeleniy_20les_20colnce_20luchi.jpg" , "forest-background-oarmsvqkfjvn7all.jpg" , "13721bc89f189384292619b51a678ab9.jpg" , "river-background-g767jii3xd0slrso.jpg" , "vccba0jg9w2xoxwayvxnm7kltw7xozpx.jpg"]

def viewCartoon(index):
    choosen = EG.buttonbox(msg, title, myList, myImg[index])
    if choosen == "Exit":
        exit(0)
        elif choosen == "Next":
            index = index + 1 
            if index == 5:
                index = 0
                viewCartoon(index)
             else:
                index = index - 1 
                if index == - 1:
                    index = 4 
                    viewCartoon(index)   




viewCartoon(0)

#EG.buttonbox(msg, title, myList)