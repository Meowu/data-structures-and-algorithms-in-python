class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    @property
    def name(self):
        return self._name

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)


class ScoreBoard:
    def __init__(self, capacity=10):

        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):

        return '\n'.join(str(self._board[i]) for i in range(self._n))

    def add(self, entry):

        score = entry.get_score()

        appendable = self._n < len(self._board) or score > self._board[-1].get_score()

        if appendable:

            if self._n < len(self._board):
                self._n += 1

            k = self._n - 1

            while k > 0 and self._board[k - 1].get_score() < score:
                self._board[k] = self._board[k - 1]
                k -= 1
            self._board[k] = entry
