# if error occure then we need to print the blow line also run

inp=input("enter number")
try:
    for i in range(1,10):
        print(f'{inp} X {i} = {int(inp)*i}')
except Exception as e:
    print(e)

print("code to print")