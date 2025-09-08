from Fan import Fan
from Light import Light
from Button import Button
from RemoteControlSystem import RemoteControlSystem
from FanCommand import FanCommand
from LightCommand import LightCommand

remote = RemoteControlSystem()
remote.add_button("Fan", Button(FanCommand(Fan())))
remote.button_click("Fan")
remote.button_click("Fan")
remote.button_click("Fan")
remote.button_click("Fan")

remote.add_button("Light", Button(LightCommand(Light())))
remote.button_click("Light")
remote.button_click("Light")
remote.button_click("Light")