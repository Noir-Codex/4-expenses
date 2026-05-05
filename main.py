s = input().lower().strip()
parts = s.split()

def error():
    print("Некорректный формат суммы")

if len(parts) == 2:
    # "159 руб"
    if parts[0].isdigit() and parts[1] == "руб":
        rub = int(parts[0])
        print(f"{rub:.2f} ₽")
    else:
        error()

elif len(parts) == 4:
    # "100 руб 10 коп"
    if (parts[0].isdigit() and parts[2].isdigit() and
        parts[1] == "руб" and parts[3] == "коп"):

        rub = int(parts[0])
        kop = int(parts[2])

        if 0 <= kop < 100:
            total = rub + kop / 100
            print(f"{total:.2f} ₽")
        else:
            error()
    else:
        error()

else:
    error()