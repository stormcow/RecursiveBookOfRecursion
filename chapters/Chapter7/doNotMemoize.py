import functools, time, datetime


@functools.lru_cache()
def getCurrentTime() -> datetime.datetime:
    return datetime.datetime.now()


@functools.lru_cache()
def printMessage() -> None:
    print("Hello, world")


print("getting the current time twice:")
print(getCurrentTime())
print("waiting few seconds...")
time.sleep(2)
print(getCurrentTime())


print("Displaying a message twice:")
printMessage()
printMessage()
