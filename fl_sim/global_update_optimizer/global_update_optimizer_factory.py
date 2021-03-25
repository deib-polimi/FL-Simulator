from fl_sim import Status
from .static_optimizer import StaticOptimizer
from .best_rt_optimizer import BestRTOptimizer


class GlobalUpdateOptimizerFactory:

    @staticmethod
    def get_optimizer(optimizer: str, epochs: int, batch_size: int, num_examples: int, status: Status, logger):
        if optimizer == "static":
            return StaticOptimizer(epochs, batch_size, num_examples, status, logger)
        elif optimizer == "bestrt":
            return BestRTOptimizer(epochs, batch_size, num_examples, status, logger)
