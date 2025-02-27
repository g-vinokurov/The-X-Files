
from Gui import Colors
from Gui import Fonts


class Theme:
    SplitterBackgroundColor = Colors.COLOR_VSC_SECONDARY

    ScrollHorizontalHandleBackgroundColor = Colors.COLOR_BS_LIGHT
    ScrollHorizontalBorderColor           = Colors.COLOR_BS_LIGHT
    ScrollHorizontalBorderRadius          = 0
    ScrollHorizontalHandleBorderRadius    = 0
    ScrollVerticalHandleBackgroundColor   = Colors.COLOR_BS_LIGHT
    ScrollVerticalBorderColor             = Colors.COLOR_BS_LIGHT
    ScrollVerticalBorderRadius            = 0
    ScrollVerticalHandleBorderRadius      = 0

    ScrollPreHorizontalHandleBackgroundColor = Colors.COLOR_BS_LIGHT
    ScrollPreHorizontalBorderColor           = Colors.COLOR_BS_LIGHT
    ScrollPreHorizontalBorderRadius          = 0
    ScrollPreHorizontalHandleBorderRadius    = 0
    ScrollPreVerticalHandleBackgroundColor   = Colors.COLOR_BS_LIGHT
    ScrollPreVerticalBorderColor             = Colors.COLOR_BS_LIGHT
    ScrollPreVerticalBorderRadius            = 0
    ScrollPreVerticalHandleBorderRadius      = 0

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
    DashboardNoReportSelectedFontSize   = 16
    DashboardNoReportSelectedColor      = Colors.COLOR_WHITE

    DashboardNoReportsFoundFont       = Fonts.FONT_GEOLOGICA_BLACK
    DashboardNoReportsFoundFontWeight = Fonts.Font.Black
    DashboardNoReportsFoundFontSize   = 16
    DashboardNoReportsFoundColor      = Colors.COLOR_WHITE

    DashboardReportPropertyValueFont       = Fonts.FONT_GEOLOGICA_EXTRA_LIGHT
    DashboardReportPropertyValueFontWeight = Fonts.Font.ExtraLight
    DashboardReportPropertyValueFontSize   = 10
    DashboardReportPropertyValueColor      = Colors.COLOR_WHITE
    


class DefaultTheme(Theme):
    pass


CurrentTheme = DefaultTheme
