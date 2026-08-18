score = 0
print ("=====Python-Quiz=====")
print("Which planet is closest to sun")
print("A. Venus","B. Mars","C. Mercury","D. Jupiter", sep ="\n")
Answer =input("Enter answer")
if Answer == "C" :
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
print(f"1/{score}")

print("Which party won election in 2018 ")
print(f"A. Pakistan Muslim League | PML-N", f"B. Pakistan Peoples Party | PPP", f"C. Pakistan Tehreek-e-Insaf | PTI", f"D. Muttahida Qaumi Movement – Pakistan | MQM-P", sep ="\n")
Answer = input("Enter answer")
if Answer == "C" :
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
print(f"2/{score}")

print("When First war of independence was done in india for against british era")
print(f"A. 1843", f"B. 1798", f"C. 1903", f"D. 1857", sep = "\n")
Answer = input("Enter answer")
if Answer == "D" :
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
print("===== Quiz-Finished =====")
print("")
print(f"Final score =3/{score}")
if score == 3:
    print("Excellent")
elif score == 2:
    print("Good")
elif score == 1:
    print("Better than nothing")
else:
    print("Better luck next time")