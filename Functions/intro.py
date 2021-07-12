def say_hello():
    print("Hello")

say_hello()

#parameters
def say_something(name, emoji):
    print(f'Hey {name} {emoji}')

say_something('Sid',':)')#positional arguements
say_something('SidB',":')")

#keyword arguements(bad practice)
say_something(emoji=':)',name='Sidd')

