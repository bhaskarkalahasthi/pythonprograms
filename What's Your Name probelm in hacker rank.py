def print_full_name(a, b):
    
    if(len(a) and len(b) <=10):
        print("Hello" ,a, b+"!", "You just delved into python.")
first_name = input()
last_name = input()
print_full_name(first_name, last_name)