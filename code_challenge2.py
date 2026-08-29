money = 19863

print("The amount of money received:", money)
print("1000:", int(money)//1000)
print("500:", int(money)%1000//500)
print("200:", int(money)%1000%500//200)
print("100:", int(money)%1000%500%200//100)
print("50:", int(money)%1000%500%200%100//50)
print("20:", int(money)%1000%500%200%100%50//20)
print("10:", int(money)%1000%500%200%100%50%20//10)
print("5:", int(money)%1000%500%200%200%100%50%20%10//5)
print("1:", int(money)%1000%500%200%200%100%50%20%10%5//1)
