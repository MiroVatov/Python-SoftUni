
class HDMICable:
    @staticmethod
    def connect_to_device_via_hdmi_cable(device): pass


class RCACable:
    @staticmethod
    def connect_to_device_via_rca_cable(device): pass


class EthernetCable:
    @staticmethod
    def connect_to_device_via_ethernet_cable(device): pass


class PowerOutlet:
    @staticmethod
    def connect_device_to_power_outlet(device): pass


class Television(RCACable, HDMICable, PowerOutlet):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class dvd_player(HDMICable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(HDMICable, PowerOutlet, EthernetCable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EthernetCable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


dvd = dvd_player
TVcable = Television
Power_outlet = PowerOutlet
TV = Television
dvd.connect_to_device_via_hdmi_cable(TVcable)
TV.connect_device_to_power_outlet(Power_outlet)
router = Router
internet = EthernetCable
router.connect_to_device_via_ethernet_cable(internet)
router.connect_device_to_power_outlet(Power_outlet)
cable_tv = RCACable
TV.connect_to_device_via_rca_cable(cable_tv)
