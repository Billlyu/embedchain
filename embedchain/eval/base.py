from abc import ABC, abstractmethod

from embedchain.utils.eval import EvalData


class BaseMetric(ABC):
    """Base class for a metric.

    This class provides a common interface for all metrics.
    """

    def __init__(self):
        """
        Initialize the BaseMetric.
        """

    @abstractmethod
    def evaluate(self, dataset: list[EvalData]):
        """
        Abstract method to evaluate the dataset.

        This method should be implemented by subclasses to perform the actual
        evaluation on the dataset.

        :param dataset: dataset to evaluate
        :type dataset: list[EvalData]
        """
        raise NotImplementedError()
