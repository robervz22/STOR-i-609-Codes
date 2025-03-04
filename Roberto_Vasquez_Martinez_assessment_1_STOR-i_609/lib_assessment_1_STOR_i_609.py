from typing import Type, List, Union


#################################
# Generic Backtracking function #
#################################
def backtrack(P: Type, c) -> None:
    """Generic backtrack function

    Args:
        P (Class): A Class that implements the problem to solve
        c (_type_): Format of the candidates corresponding to the class P
    """
    # Stopping conditions
    if P.reject(c):
        return
    if P.accept(c):
        P.output(c)
        return
    s = P.first(c)  # descendent
    backtrack(P, s)  # Recur on descendent
    s = P.next(c)  # brother node
    backtrack(P, s)  # Recur on brother node


################################
# Problem 1: Integer Partition #
################################
class Partition:
    """Class tha implements the methods for Integer Partition problem"""

    def __init__(self, n: int) -> None:
        """Constructor

        Args:
            n (int): Attempt integer to find partitions
        """
        self.n: int = n
        self.partitions: List[List[int]] = []

    def reject(self, c: List[Union[List[int], int]]) -> bool:
        """Reject method

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            bool: True if the rejection condition complies, otherwise False
        """
        if c[2] <= 0 or c[1] < 0:
            return True
        return False

    def accept(self, c: List[Union[List[int], int]]) -> bool:
        """Accept method

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            bool: True if the candidate is accepted, otherwise False
        """
        if c[1] == 0:
            return True
        return False

    def first(self, c: List[Union[List[int], int]]) -> List[Union[List[int], int]]:
        """Obtains the next candidate in depth

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            List[Union[List[int], int]]: Immediate next candidate
        """
        c[0].append(c[2])
        return [c[0], self.n - sum(c[0]), c[2]]

    def next(self, c: List[Union[List[int], int]]) -> List[Union[List[int], int]]:
        """Next candidate in breadth

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            List[Union[List[int], int]]: Immediate next candidate
        """
        c[0].pop()
        return [c[0], self.n - sum(c[0]), c[2] - 1]

    def output(self, c: List[Union[List[int], int]]) -> None:
        """Save a copy of the input candidate in a class attribute

        Args:
            c (List[Union[List[int], int]]): Candidate
        """
        self.partitions.append(c[0].copy())  # Append accepted solution

    def solve(self) -> None:
        """Initialize properly the backtracking algorithm for finding the solution

        Raises:
            RuntimeError: An error appears if the class is not initialized in advance
        """
        if not hasattr(self, "n"):
            raise RuntimeError("Cannot use method: Class is not initialized")

        def backtrack(c: List[Union[List[int], int]]) -> None:
            # Stopping conditions
            if self.reject(c):
                return
            if self.accept(c):
                self.output(c)
                return
            s = self.first(c)  # descendent
            backtrack(s)  # Recur on descendent
            s = self.next(c)  # brother node
            backtrack(s)  # Recur on brother node

        backtrack([[], self.n, self.n])  # Start backtracking with initial conditions

    def print(self) -> None:
        """Print all the partitions of n"""
        for part in self.partitions:
            print(part, end="\n")


########################
# Problem 2: Gray code #
########################
class GrayCode:
    """Class that implements the methods for genering a Gray Code using backtracking algorithm"""

    def __init__(self, n: int) -> None:
        """Constructor

        Args:
            n (int): Number of bits
        """
        self.n: int = n  # Number of bits
        self.code: List[int] = []  # Code saved in decimal representation

    def reject(self, c: List[Union[List[int], int]]) -> bool:
        """Reject method

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            bool: True if the rejection condition complies, otherwise False
        """
        if len(c[0]) > 1:
            if len(c[0]) != len(set(c[0])) or len(c[0]) > (1 << self.n):
                return True
        return False

    def accept(self, c: List[Union[List[int], int]]) -> bool:
        """Accept method

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            bool: True if the candidate is accepted, otherwise False
        """
        if len(c[0]) == len(set(c[0])) and len(c[0]) == (1 << self.n):
            return True
        else:
            return False

    def first(self, c: List[Union[List[int], int]]) -> List[Union[List[int], int]]:
        """Obtains the next in candidate in depth

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            List[Union[List[int], int]]: Immediate next candidate
        """
        if len(self.code) == 0:
            next_code: int = c[0][-1] ^ (1 << 0)
            c[0].append(next_code)
            return [c[0], 0]
        return c

    def next(self, c: List[Union[List[int], int]]) -> List[Union[List[int], int]]:
        """Next candidate in breadth

        Args:
            c (List[Union[List[int], int]]): Candidate

        Returns:
            List[Union[List[int], int]]: Immediate next candidate
        """
        if len(self.code) == 0:
            c[0].pop()
            index: int = (c[1] + 1) % self.n
            next_code: int = c[0][-1] ^ (1 << index)
            c[0].append(next_code)
            return [c[0], index]
        return c

    def output(self, c: List[Union[List[int], int]]) -> None:
        """Save the input candidate in a class attribute

        Args:
            c (List[Union[List[int], int]]): Candidate
        """
        self.code = c[0]
        return

    def solve(self) -> None:
        """Initialise properly the backtracking algorithm for finding the solution

        Raises:
            RuntimeError: An error appears if the class is not initialised in advance
        """
        if not hasattr(self, "n"):
            raise RuntimeError("Cannot use method: Class is not initialized")

        def backtrack(c: List[Union[List[int], int]]) -> None:
            # Stopping conditions
            if self.reject(c):
                return
            if self.accept(c):
                self.output(c)
                return
            s = self.first(c)  # descendent
            backtrack(s)  # Recur on descendent
            s = self.next(c)  # brother node
            backtrack(s)  # Recur on brother node

        backtrack([[0], 0])  # Start backtracking with initial conditions

    def print(self) -> None:
        """Print the Gray code obtained"""
        for c in self.code:
            print(format(c, f"0{self.n}b"), end="\n")