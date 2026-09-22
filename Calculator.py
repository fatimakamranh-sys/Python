while True:
   num = float(input("enter first number:"))
   operation = input("enter operation (+, -, *, /): ")
   num2 = float(input("enter second number:"))

   if operation == "+":
     result = num + num2
   elif operation == "-":
     result= num - num2
   elif operation == "*":
     result = num * num2
   elif operation == "/":
     result = num/num2
   else: 
     print("invalid operation")
     result = None

   if result is not None:
     print(f"{num} { operation} {num2} = { result}")

   again = input("calculate again? (y/n):")
   if again.lower() != "y":
     print("Goodbye")
     break
    