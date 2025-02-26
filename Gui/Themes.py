
from Gui import Colors
from Gui import Fonts


class Theme:
    SplitterBackgroundColor = Colors.COLOR_VSC_TERTIARY
    
    WelcomeLogoFont       = Fonts.FONT_GEOLOGICA_BLACK
    WelcomeLogoFontWeight = Fonts.Font.Black
    WelcomeLogoFontSize   = 48
    WelcomeLogoColor      = Colors.COLOR_BS_LIGHT

    WelcomeOpenProjectFont       = Fonts.FONT_GEOLOGICA_BLACK
    WelcomeOpenProjectFontWeight = Fonts.Font.Black
    WelcomeOpenProjectFontSize   = 18
    WelcomeOpenProjectColor      = Colors.COLOR_BS_LIGHT

    DashboardScreenBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBorderColor     = Colors.COLOR_VSC_TERTIARY
    DashboardBodyBackgroundColor   = Colors.COLOR_VSC_PRIMARY
    DashboardFooterBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardFooterBorderColor     = Colors.COLOR_VSC_TERTIARY

    DashboardReportsListSectionBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardReportSectionBackgroundColor      = Colors.COLOR_VSC_SECONDARY
    
    DashboardNoReportSelectedFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardNoReportSelectedFontWeight = Fonts.Font.Black
    DashboardNoReportSelectedFontSize   = 18
    DashboardNoReportSelectedColor      = Colors.COLOR_BS_SECONDARY


class DefaultTheme(Theme):
    pass


CurrentTheme = DefaultTheme
