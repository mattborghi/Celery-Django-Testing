from tasks import *

def run(result,result2):
    visitedResult = False
    visitedAddition = False
    while True:
        if result.ready() and not visitedResult:
            print("Reverse run!")
            print(result.get())
            print("\n")
            visitedResult = True
        if result2.ready() and not visitedAddition:
            print("addition run!")
            print(result2.get())
            print("\n")
            visitedAddition = True
        if result.ready() and result2.ready() and visitedAddition and visitedResult:
            print("Both results were run!")
            return 0


if __name__ == "__main__":
    result  = reverse.delay('Some long string that needs to be reversed!!')
    result2 = add.delay(5645,564)

    run(result, result2)