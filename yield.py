def messages():
    yield "Hello World"
    yield "Hi! there!"
    yield "This is from the generator"


for message in messages():
    print(message)