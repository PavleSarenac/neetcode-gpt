class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        current_x = init
        for _ in range(iterations):
            current_gradient = 2 * current_x
            current_x -= learning_rate * current_gradient
        return round(current_x, 5)
