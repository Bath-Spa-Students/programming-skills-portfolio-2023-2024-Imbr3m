# defining functions
def make_shirt(size="Large", message="I love Python"):
    print(f"creating the shirt... size {size} with the print: '{message}'.")

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size="Medium")

# Making a shirt of any size with a different message
make_shirt(size="small", message="JOJO!!!")
