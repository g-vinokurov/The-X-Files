
import sys

from Gui.Widgets.Screens.Welcome.Screen import ScreenWelcome
from Gui.Widgets.Screens.Dashboard.Screen import ScreenDashboard

from App import app


if __name__ == '__main__':
    app.gui.navigator.register('welcome', ScreenWelcome)
    app.gui.navigator.register('dashboard', ScreenDashboard)
    app.gui.navigator.goto('welcome')
    app.gui.show()
    sys.exit(app.exec())
