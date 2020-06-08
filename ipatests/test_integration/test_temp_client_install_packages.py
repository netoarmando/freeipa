from ipatests.pytest_ipa.integration import tasks
from ipatests.test_integration.base import IntegrationTest


class TestInstallClientPackages(IntegrationTest):
    num_clients = 1

    def test_install_client_packages(self):
        tasks.install_packages(self.clients[0], ["postfix"])
