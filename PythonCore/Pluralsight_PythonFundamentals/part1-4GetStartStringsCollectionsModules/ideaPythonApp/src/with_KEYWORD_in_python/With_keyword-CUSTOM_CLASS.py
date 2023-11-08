class Timer:
    def func(self):
        print(self)

    def func1(self):
        print("hello")

    def __enter__(self):
        print("Enter context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


with Timer() as t:
    t.func()

