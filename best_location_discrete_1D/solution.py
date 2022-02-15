from scouting import scoutLeft, scoutRight

solutions = []
bestCompleteEval = None

incompleteSolutions = []
bestIncompleteEval = None

blocks = [1,2,3,4,5,6,7]

def evaluate(report):
    pass

def findBestBlock(domain, index):

    first = 0
    last = 7

    i = index

    if i == first: # Find all required facilities left of the index
        report = scoutRight()


    elif i == last: # Find all required facilities left of the index
        report = scoutLeft() 
    
    else:
        report = scoutLeft() + scoutRight()


for i in range(0, len(blocks)):

    solution = evaluate(blocks, i)
