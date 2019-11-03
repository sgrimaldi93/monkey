from abc import ABCMeta, abstractmethod


class HostScanner(metaclass=ABCMeta):
    @property
    @abstractmethod
    def is_host_alive(self, host):
        raise NotImplementedError()
