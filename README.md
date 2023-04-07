# start_stop_clock_by_plam
Simple start-stop clock with Kivy framework
![python_kivy_logo](https://user-images.githubusercontent.com/117172634/230564441-446c4725-94ff-4c3d-aed7-b89380ba6123.jpg)


![stop_clock](https://user-images.githubusercontent.com/117172634/230563067-8e997689-0a00-4c5f-b6af-918778d91f08.JPG)
![start_clock](https://user-images.githubusercontent.com/117172634/230563064-30a992c9-6d2c-4348-b8a7-72df2a41c402.JPG)

The codes implement a simple clock application using Python and Kivy. The Python code defines the behavior of the clock application, while the Kivy code defines the layout and appearance of the clock interface.

The Python code imports the necessary modules and defines two classes - ClockContainer and ClockApp. The ClockContainer class inherits from the BoxLayout class and defines the behavior of the clock interface. The ClockApp class inherits from the App class and defines the main application object that is used to run the clock application.

The ClockContainer class defines a method called start_stop_clock() that toggles between starting and stopping the clock. When the clock is started, the method schedules an update function called _update_time() to be called every second using the Clock.schedule_interval() method. The _update_time() function updates the clock label with the current time using the datetime.now().strftime() method.

The Kivy code defines the layout and appearance of the clock interface using Kivy's language for building user interfaces. The interface consists of a BoxLayout widget that contains a Label widget for displaying the time and a Button widget for starting and stopping the clock. The Label widget has an id of lbl_clock, which is used by the Python code to update the time displayed on the label. The Button widget has an id of btn_start_stop, which is used by the Python code to toggle the clock on and off. When the button is pressed, it calls the start_stop_clock() method defined in the Python code.
