from Subsystems.BuildSystem import BuildSystem
from Subsystems.DeploymentServer import DeploymentServer
from Subsystems.TestFramework import TestFramework
from Subsystems.VersionContol import VersionControl

class DeploymentFacade:

    def __init__(self):
        self.vcs = VersionControl()
        self.build = BuildSystem()
        self.tests = TestFramework()
        self.deploy_server = DeploymentServer()

    def deploy_application(self):
        print("Starting deployment via Facade.....\n")
        self.vcs.fetch_latest_code()
        self.build.buil_project()
        self.tests.run_tests()
        self.deploy_server.deploy()
        print("\nDeployment completed!")