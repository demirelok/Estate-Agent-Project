
def getValidInput(inputQuestion: str, validOptions: tuple):
    inputQuestion += " ({}): ".format(",".join(validOptions))
    response = input(inputQuestion)
    while response.lower() not in validOptions:
        response = input(inputQuestion)

    return response