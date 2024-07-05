try:
    for i in range(3):
        print(3/i)
except:
    print("You divided by 0")
    print(‘This prints because the exception was handled’)