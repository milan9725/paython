class X:
    print("Class X ")
obj=X()

if isinstance(obj,(X)):
    print("obj is an instance ")
else:
    print("obj is not an instance")