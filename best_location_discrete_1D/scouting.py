from msilib.schema import Error


Report = list # type alias

class Report:
    
    def __init__(self, origin, facilitiesFound: dict, complete):

        self.origin = origin
        self.facilities = facilitiesFound
        self.complete = complete

    def __add__(self, other: dict):

        if self.origin != other.origin:
            raise ValueError("Can't join reports with different origin points")

        facilities = {}
        for f in self.facilities:
            facilities[f] = self.facilities[f]
        
    

def completeReport(origin, facilities):
    return Report(origin, facilities, True)

def incompleteReport(origin, facilities):
    return Report(origin, facilities, False)


class DirectedScout:

    LEFT = 0
    RIGHT = 1

    def __init__(self, searchSpace, start, requirements, direction):
        self.domain = searchSpace
        self.direction = direction

        self.start = start
        self.index = start

        self.requirements = requirements

    def search(self) -> Report:
        return 

    def advance(self):
        
        if self.direction == DirectedScout.LEFT:
            self.index -= 1
        
        if self.direction == DirectedScout.RIGHT:
            self.index += 1


def scoutLeft(searchSpace, start, requirements) -> Report:

    return DirectedScout(searchSpace, start, requirements, DirectedScout.LEFT)

def scoutRight(searchSpace, start, requirements) -> Report:

    return DirectedScout(searchSpace, start, requirements, DirectedScout.RIGHT)