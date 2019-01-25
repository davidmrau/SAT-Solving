# SAT-Solving
SAT Solving in Python


## Abstract
Sudoku is a very well known puzzle that many people consider as a fun game. It can be translated into a propositional SAT-Problem and subsequently solved by a computer. The goal of this paper is to examine the impact of the number of givens and rotational-symmetry on the computational complexity of Sudokus. In the course of this research several encodings (extended-, optimal-, minimal encoding) were examined. In this research the minimal encoding was chosen to convert the Sudoku into the Conjunctive Normal Form (CNF). The resulting set of clauses was fed to a SAT-Solver and statistics were collected about the solving process in order to gain insights about the complexity. We propose the hypothesis that the number of givens is negatively correlated with the computational complexity, whereas the symmetry has no impact. This can be confirmed in the course of the work.

The full paper can be found in this repository under paper.pdf
