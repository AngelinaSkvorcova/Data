vertejumi ={
    10: "izcili",
    9: "izcili",
    8: "Loti labi",
    7: "labi",
    6: "gandriz labi",
    5: "labi",
    4: "gandriz videji",
    3: "nesekmigi",
    2:  "nesekmigi",
    1: "nesekmigi",
    }
#lietotaji ievads
n=int(input("ievadiet balles no 1 lidz 10:"))
#parbaude
if 1<=n<=10:
    print(f"vertejums{vertejumi[n]}")
else:
        print("īevaditais skaitlis nav korekts. ludzu uevadiet skaitli no 1 lidz 10")