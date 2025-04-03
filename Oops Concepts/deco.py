def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx

@greet
def helo():
    print("hello woeld")

helo()