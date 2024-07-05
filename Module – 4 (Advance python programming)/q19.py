try:
    x=10/0  
except Exception as error:
    print("Exception caught :",error)
finally:
    print("This will always execute.")