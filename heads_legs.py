heads = raw_input("Enter Total Heads :")
legs = raw_input("Enter Total Legs :")
heads = int(heads)
legs = int(legs)
# 35 heads and 94 legs
#heads = r/4+c/2

final_result = None
for rabit in range(heads):
    chicken = heads - rabit
    if (chicken*2 + rabit*4) == legs:
        final_result = "rabit = "+ str(rabit) +"\nchicken = "+ str(chicken)

if final_result:
    print(final_result)
else:
    print("You have entered wrong data!")
