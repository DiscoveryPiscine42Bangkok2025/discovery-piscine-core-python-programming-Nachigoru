def greetings(name ="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

greetings('Alexsandra')
greetings('Wil')
greetings()
greetings(42)