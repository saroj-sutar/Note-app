import os
def new_note():
    with open (input("Enter new note file name : ")+(".txt"), "w+") as n:
        n.read()


def add_text ():
    with open(input("Enter file name : ")+(".txt"), "w+") as r:
        
        ent_txt = input("Type your note here : ")
        r.write(f"{ent_txt}")
    

def update_text():
    with open(input("Enter file name : ")+(".txt"), "a") as u:
        u.write(input("Type your note here : "))
        
def find_replace ():
    with open(input("Enter file name : ")+(".txt"), "r+") as f:
        data = f.read()
        new_tx = data.replace(input("Enter search text : "), input("Enter replace text : "))
        f.seek(0)
        f.truncate()
        f.write(new_tx)
        
def view_note ():
    with open(input("Enter file name : ")+(".txt"), "r") as re:
        data = re.read()
        
        print(f"✅ >>>> {data}")

def delet_note():
    os.remove(input("Enter file name : ")+(".txt"))

def rename_file():
    i = input("Enter old file name : ")+(".txt")
    with open(i, "r") as nw:
        data = nw.read()

    j = input("Enter new file name : ")+(".txt")
    
    with open(j, "w") as ap:
        ap.write(data)
    
    os.remove(i)

# Main function

while True:
    print("\n_____Note app_____\n")
    print("Press 1 : Create a new note file")
    print("Press 2 : Add text")
    print("Press 3 : Clear all existing text and write new text")
    print("Press 4 : Find and Replace text")
    print("Press 5 : View note file")
    print("Press 6 : Rename exiting note file")
    print("Press 7 : Delete note file\n")

    choose = int(input("Enter service number : "))
    print("")

    if choose == 1:
        new_note()
    elif choose == 2:
        update_text()
    elif choose == 3:
        add_text ()
    elif choose == 4:
        find_replace ()
    elif choose == 5:
        view_note ()
    elif choose == 6:
        rename_file()
    elif choose == 7:
        delet_note()
    else:
        print("⚠️ Invalid input. Please choose a valid service number from the above list")
        break

    

