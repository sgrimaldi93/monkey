import logging

from infection_monkey.system_info import InfoCollector
from infection_monkey.system_info.SSH_info_collector import SSHCollector
from infection_monkey.system_info.k8s_info_collector import K8sInfoCollector

__author__ = 'uri'

LOG = logging.getLogger(__name__)


class LinuxInfoCollector(InfoCollector):
    """
    System information collecting module for Linux operating systems
    """

    def __init__(self):
        super(LinuxInfoCollector, self).__init__()

    def get_info(self):
        """
        Collect Linux system information
        Hostname, process list and network subnets
        :return: Dict of system information
        """
        LOG.debug("Running Linux collector")
        self.get_hostname()
        self.get_process_list()
        self.get_network_info()
        self.get_azure_info()
        self.info['ssh_info'] = SSHCollector.get_info()
        self.info['k8s'] = K8sInfoCollector.get_info()
        return self.info

