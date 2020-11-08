t = int(input("Введите время в секундах: "))
(h,t) = divmod(t,3600)
(m,s) = divmod(t,60)
if h < 10:
    h = f"0{h}"
if m < 10:
    m = f"0{m}"
if s < 10:
    s = f"0{s}"
print(f"{h}:{m}:{s}")

