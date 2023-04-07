from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class ClockContainer(BoxLayout):
    def __init__(self):
        super(ClockContainer, self).__init__()
        self._clk = None
        self.btn_start_stop = self.ids.btn_start_stop
        self.lbl_clock = self.ids.lbl_clock
        self.btn_start_stop.text = "Start"
        self.btn_start_stop.background_color = [0, 1, 0]

    def start_stop_clock(self):
        if self._clk:
            self._clk.cancel()
            self._clk = None
            self.btn_start_stop.text = "Start"
            self.btn_start_stop.background_color = [0, 1, 0]
        else:
            self._clk = Clock.schedule_interval(self._update_time, 1)
            self.btn_start_stop.text = "Stop"
            self.btn_start_stop.background_color = [1, 0, 0, 1]

    def _update_time(self, *largs):
        self.lbl_clock.text = datetime.now().strftime("%H:%M:%S")


class ClockApp(App):
    def build(self):
        return ClockContainer()


if __name__ == "__main__":
    app = ClockApp()
    app.title = "Clock"
    app.run()
