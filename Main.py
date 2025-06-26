
from Ui.Widgets.App.Dashboard import Dashboard
from Ui.Widgets.App.Welcome import Welcome

from App import app

app.gui.navigator.add('dashboard', Dashboard)
app.gui.navigator.add('welcome', Welcome)

app.start('welcome')
