import time

def delayer(function):
    print("started")
    def inner():
        time.sleep(5)
        function()


    inner()


@delayer
def hello():
    print("Hello!")
