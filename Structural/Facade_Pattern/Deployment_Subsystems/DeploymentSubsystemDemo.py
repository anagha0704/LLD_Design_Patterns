from DeploymentFacade import DeploymentFacade

class DeploymentSubsystemDemo:

    def run():
        facade = DeploymentFacade()
        facade.deploy_application()

if __name__ == "__main__":
    DeploymentSubsystemDemo.run()