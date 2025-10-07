from TrafficLight import TrafficLight
from Observers.CentralTrafficController import CentralTrafficController
from Observers.EmergencyResponseSystem import EmergencyResponseSystem
from Observers.TrafficDataLogger import TrafficDataLogger

class TrafficLightMonitoringDemo:

    def run():
        traffic_light = TrafficLight()

        ctc = CentralTrafficController()
        emergency_response = EmergencyResponseSystem()
        data_logger = TrafficDataLogger()

        traffic_light.add_observers(ctc)
        traffic_light.add_observers(emergency_response)
        traffic_light.add_observers(data_logger)

        traffic_light.change_state("RED")
        traffic_light.change_state("GREEN")

        traffic_light.remove_observer(data_logger)
        
        traffic_light.change_state("YELLOW")
        traffic_light.change_state("RED")

        
if __name__ == "__main__":
    TrafficLightMonitoringDemo.run()