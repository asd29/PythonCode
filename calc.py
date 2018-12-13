def sum(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y

try:
        while True:
                print("enter first no.")
                num1=int(input())
                print("enter second no.")
                num2=int(input())
                print("enter choice\n 1-add\n 2-subtract\n 3-multiplication\n 4-division\n 5-exit\n")
                choice= int(input())
                if choice==1:
                        res=sum(num1,num2)
                elif choice==2:
                        res=sub(num1,num2)
                elif choice==3:
                        res=mul(num1,num2)
                elif choice==4:
                        res=div(num1,num2)
                elif choice==5:
                        break;
                print(res)
except ValueError:
	print("no. should be entered")
except Exception as e:
        print(e)
