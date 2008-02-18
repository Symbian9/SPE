# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4cvs on Tue Jul 19 19:57:59 2005

import sys, wx

def _(x):
    return x

MENUS =[
OPEN_WORKSPACE, SAVE_WORKSPACE, SAVE_WORKSPACE_AS, 

SAVE_COPY, SAVE_UML_AS, PRINT_UML_SETUP, PRINT_UML_PREVIEW, PRINT_UML,

CUT, COPY, PASTE, REMEMBER_OPEN_FILES,

GO_TO_LINE, BROWSE_SOURCE,
AUTO_COMPLETE, SHOW_DOCSTRING, INDENT, DEDENT, COMMENT, UNCOMMENT, INSERT_SEPARATOR,
INSERT_SIGNATURE, EXECUTE, PREFERENCES,

WHITESPACE, LINENUMBERS, INDENTATION_GUIDES, RIGHT_EDGE_INDICATOR,
AS_NOTEBOOK, AS_COLUMNS, AS_ROWS,
END_OF_LINE_MARKER, SIDEBAR, SHELL, TOOLBAR, CLEAR_OUTPUT, REFRESH,

RUN, RUN_WITHOUT_ARGUMENTS, RUN_TERMINAL, RUN_TERMINAL_WITHOUT_ARGUMENTS, 
RUN_TERMINAL_WITHOUT_ARGUMENTS_EXIT, IMPORT, RUN_DEBUG, DEBUG,
BROWSE_OBJECT_WITH_PYFILLING, TEST_REGULAR_EXPRESSION_WITH_KIKI,
DESIGN_A_GUI_WITH_WXGLADE, DESIGN_A_GUI_WITH_XRC, CHECK_SOURCE_WITH_PYCHECKER,
OPEN_TERMINAL_EMULATOR, BROWSE_FOLDER, RUN_IN_TERMINAL_EMULATOR,
RUN_IN_TERMINAL_EMULATOR__EXIT,

LOAD_IN_BLENDER, REFERENCE_IN_BLENDER, REDRAW_BLENDER_WINDOW,
BLENDER_PYTHON_MANUAL, BLENDER_PYTHON_TUTORIAL, BLENDER_HOMEPAGE,
DOWNLOAD_BLENDER, FORUM_BLENDER_PYTHON, FORUM_ELYSIUN_PYTHON,
ADD_SPE_TO_BLENDER,

SPE_HOMEPAGE, FORUM_SPE, AUTHORS_HOMEPAGE, CONTACT_AUTHOR, PYTHON_HOMEPAGE,
PYTHON_ANNOUNCEMENTS,
PYTHON_COOKBOOK, PYTHON_DAILY, PYTHON_FOR_ARTISTS, PYTHON_PACKAGE_INDEX,

NEXT,PREVIOUS,

MANUAL, KEYBOARD_SHORTCUTS, PYTHON_LIBRARY, PYTHON_REFERENCE,
PYTHON_DOCUMENTATION_SERVER, WXGLADE_MANUAL, WXGLADE_TUTORIAL, WXWINDOWS_DOCUMENTATION,
DONATE, ABOUT
] =\
[wx.NewId() for x in range(86)]

CHILD_MENUS=[
wx.ID_SAVE, wx.ID_SAVEAS, SAVE_COPY, wx.ID_CLOSE, REMEMBER_OPEN_FILES,
SAVE_UML_AS, PRINT_UML_SETUP, PRINT_UML_PREVIEW, PRINT_UML,

wx.ID_UNDO, wx.ID_REDO, CUT, COPY, PASTE, wx.ID_REPLACE,
wx.ID_FIND, GO_TO_LINE, BROWSE_SOURCE,
AUTO_COMPLETE, INDENT, DEDENT, COMMENT, UNCOMMENT, INSERT_SEPARATOR,
INSERT_SIGNATURE, EXECUTE, 

WHITESPACE, INDENTATION_GUIDES, RIGHT_EDGE_INDICATOR,
AS_NOTEBOOK, AS_COLUMNS, AS_ROWS,
END_OF_LINE_MARKER, SIDEBAR,

RUN, RUN_WITHOUT_ARGUMENTS, IMPORT, RUN_DEBUG, DEBUG,
CHECK_SOURCE_WITH_PYCHECKER,

NEXT,PREVIOUS]#LINENUMBERS,

BLENDER_MENUS = [LOAD_IN_BLENDER, REFERENCE_IN_BLENDER,]


class Palette(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Palette.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.logo = wx.StaticBitmap(self, -1, wx.Bitmap("skins/default/blenpy.png", wx.BITMAP_TYPE_ANY))
        self.previous = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/tab_left.png", wx.BITMAP_TYPE_ANY))
        self.next = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/tab_right.png", wx.BITMAP_TYPE_ANY))
        self.find = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/viewmag.png", wx.BITMAP_TYPE_ANY))
        self.goto = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/goto.png", wx.BITMAP_TYPE_ANY))
        self.browse_source = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/thumbnail.png", wx.BITMAP_TYPE_ANY))
        self.check = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/pychecker.png", wx.BITMAP_TYPE_ANY))
        self.dedent = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/dedent.png", wx.BITMAP_TYPE_ANY))
        self.indent = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/indent.png", wx.BITMAP_TYPE_ANY))
        self.comment = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/comment.png", wx.BITMAP_TYPE_ANY))
        self.uncomment = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/uncomment.png", wx.BITMAP_TYPE_ANY))
        self.run = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/run.png", wx.BITMAP_TYPE_ANY))
        self.imprt = wx.BitmapButton(self, -1, wx.Bitmap("skins\\default\\import.png", wx.BITMAP_TYPE_ANY))
        self.sidebar = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/view_left_right.png", wx.BITMAP_TYPE_ANY))
        self.run_verbose = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/debug.png", wx.BITMAP_TYPE_ANY))
        self.shell = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/view_top_bottom.png", wx.BITMAP_TYPE_ANY))
        self.donate = wx.BitmapButton(self, -1, wx.Bitmap("skins/default/donate.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.evt_previous, self.previous)
        self.Bind(wx.EVT_BUTTON, self.evt_next, self.next)
        self.Bind(wx.EVT_BUTTON, self.evt_find, self.find)
        self.Bind(wx.EVT_BUTTON, self.evt_goto, self.goto)
        self.Bind(wx.EVT_BUTTON, self.evt_browse_source, self.browse_source)
        self.Bind(wx.EVT_BUTTON, self.evt_check, self.check)
        self.Bind(wx.EVT_BUTTON, self.evt_dedent, self.dedent)
        self.Bind(wx.EVT_BUTTON, self.evt_indent, self.indent)
        self.Bind(wx.EVT_BUTTON, self.evt_comment, self.comment)
        self.Bind(wx.EVT_BUTTON, self.evt_uncomment, self.uncomment)
        self.Bind(wx.EVT_BUTTON, self.evt_run, self.run)
        self.Bind(wx.EVT_BUTTON, self.evt_import, self.imprt)
        self.Bind(wx.EVT_BUTTON, self.evt_sidebar, self.sidebar)
        self.Bind(wx.EVT_BUTTON, self.evt_run_verbose, self.run_verbose)
        self.Bind(wx.EVT_BUTTON, self.evt_shell, self.shell)
        self.Bind(wx.EVT_BUTTON, self.evt_donate, self.donate)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Palette.__set_properties
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.previous.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.previous.SetToolTipString(_("Previous window | Ctrl+Shift+`"))
        self.previous.SetSize(self.previous.GetBestSize())
        self.next.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.next.SetToolTipString(_("Next window | Ctrl+`"))
        self.next.SetSize(self.next.GetBestSize())
        self.find.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.find.SetToolTipString(_("Find & replace... | Ctrl+F"))
        self.find.SetSize(self.find.GetBestSize())
        self.goto.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.goto.SetToolTipString(_("Go to line... | Ctrl+G"))
        self.goto.SetSize(self.goto.GetBestSize())
        self.browse_source.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.browse_source.SetToolTipString(_("Browse source | Ctrl+Enter"))
        self.browse_source.SetSize(self.browse_source.GetBestSize())
        self.check.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.check.SetToolTipString(_("Check source with pychecker | Ctrl+Alt+C"))
        self.check.SetSize(self.check.GetBestSize())
        self.dedent.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.dedent.SetToolTipString(_("Dedent | Shift+Tab"))
        self.dedent.SetSize(self.dedent.GetBestSize())
        self.indent.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.indent.SetToolTipString(_("Indent | Tab"))
        self.indent.SetSize(self.indent.GetBestSize())
        self.comment.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.comment.SetToolTipString(_("Comment | Alt+3"))
        self.comment.SetSize(self.comment.GetBestSize())
        self.uncomment.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.uncomment.SetToolTipString(_("Uncomment | Alt+4"))
        self.uncomment.SetSize(self.uncomment.GetBestSize())
        self.run.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.run.SetToolTipString(_("Run | F9"))
        self.run.SetSize(self.run.GetBestSize())
        self.imprt.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.imprt.SetToolTipString(_("Import | F10"))
        self.imprt.SetSize(self.imprt.GetBestSize())
        self.sidebar.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.sidebar.SetToolTipString(_("Show/hide sidebar | F11"))
        self.sidebar.SetSize(self.sidebar.GetBestSize())
        self.run_verbose.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.run_verbose.SetToolTipString(_("Run verbose | Ctrl+Alt+R"))
        self.run_verbose.SetSize(self.run_verbose.GetBestSize())
        self.shell.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.shell.SetToolTipString(_("Show/hide shell | F12"))
        self.shell.SetSize(self.shell.GetBestSize())
        self.donate.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.donate.SetToolTipString(_("Please donate, if you enjoy SPE."))
        self.donate.SetSize(self.donate.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Palette.__do_layout
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        sizer_palette = wx.GridSizer(1, 2, 0, 0)
        sizer_main.Add(self.logo, 0, 0, 0)
        sizer_palette.Add(self.previous, 0, 0, 0)
        sizer_palette.Add(self.next, 0, 0, 0)
        sizer_palette.Add(self.find, 0, 0, 0)
        sizer_palette.Add(self.goto, 0, 0, 0)
        sizer_palette.Add(self.browse_source, 0, 0, 0)
        sizer_palette.Add(self.check, 0, 0, 0)
        sizer_palette.Add(self.dedent, 0, 0, 0)
        sizer_palette.Add(self.indent, 0, 0, 0)
        sizer_palette.Add(self.comment, 0, 0, 0)
        sizer_palette.Add(self.uncomment, 0, 0, 0)
        sizer_palette.Add(self.run, 0, 0, 0)
        sizer_palette.Add(self.imprt, 0, 0, 0)
        sizer_palette.Add(self.sidebar, 0, 0, 0)
        sizer_palette.Add(self.run_verbose, 0, 0, 0)
        sizer_palette.Add(self.shell, 0, 0, 0)
        sizer_palette.Add(self.donate, 0, 0, 0)
        sizer_main.Add(sizer_palette, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_main)
        sizer_main.Fit(self)
        # end wxGlade

    def evt_indent(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_dedent(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_comment(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_uncomment(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_run(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_import(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_find(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_goto(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_browse_source(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_shell(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_check(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_donate(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_previous(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_next(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_sidebar(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

    def evt_run_verbose(self, event): # wxGlade: Palette.<event_handler>
        event.Skip()

# end of class Palette


class Bar(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Bar.__init__
        wx.MenuBar.__init__(self, *args, **kwds)
        self.file = wx.Menu()
        self.file.Append(wx.ID_NEW, _("&New\tCtrl+N"), "", wx.ITEM_NORMAL)
        self.file.Append(wx.ID_OPEN, _("&Open file(s)...\tCtrl+O"), "", wx.ITEM_NORMAL)
        self.file.Append(wx.ID_SAVE, _("&Save\tCtrl+S"), "", wx.ITEM_NORMAL)
        self.file.Append(wx.ID_SAVEAS, _("Save &As...\tCtrl+Alt+S"), "", wx.ITEM_NORMAL)
        self.file.Append(SAVE_COPY, _("Sa&ve a Copy...\tShift+Ctrl+Alt+S"), "", wx.ITEM_NORMAL)
        self.file.AppendSeparator()
        self.file.Append(OPEN_WORKSPACE, _("Open &Workspace"), "", wx.ITEM_NORMAL)
        self.file.Append(SAVE_WORKSPACE, _("Save Workspace"), "", wx.ITEM_NORMAL)
        self.file.Append(SAVE_WORKSPACE_AS, _("Save Workspace As..."), "", wx.ITEM_NORMAL)
        self.file.AppendSeparator()
        self.file.Append(SAVE_UML_AS, _("Save Uml As...\tCtrl+Shift+S"), "", wx.ITEM_NORMAL)
        self.file.Append(PRINT_UML_SETUP, _("Page Uml Setup..."), "", wx.ITEM_NORMAL)
        self.file.Append(PRINT_UML_PREVIEW, _("Print Uml Preview..."), "", wx.ITEM_NORMAL)
        self.file.Append(PRINT_UML, _("Print Uml..."), "", wx.ITEM_NORMAL)
        self.file.AppendSeparator()
        self.file.Append(wx.ID_CLOSE, _("&Close\tCtrl+W"), "", wx.ITEM_NORMAL)
        self.file.Append(wx.ID_EXIT, _("&Exit\tAlt+F4"), "", wx.ITEM_NORMAL)
        self.file.AppendSeparator()
        self.file.Append(REMEMBER_OPEN_FILES, _("&Remember open file(s)"), "", wx.ITEM_CHECK)
        self.Append(self.file, _("&File"))
        self.edit = wx.Menu()
        self.edit.Append(wx.ID_UNDO, _("&Undo\tCtrl+Z"), "", wx.ITEM_NORMAL)
        self.edit.Append(wx.ID_REDO, _("&Redo\tCtrl+Y"), "", wx.ITEM_NORMAL)
        self.edit.AppendSeparator()
        self.edit.Append(CUT, _("Cut"), "", wx.ITEM_NORMAL)
        self.edit.Append(COPY, _("&Copy"), "", wx.ITEM_NORMAL)
        self.edit.Append(PASTE, _("&Paste"), "", wx.ITEM_NORMAL)
        self.edit.AppendSeparator()
        self.edit.Append(EXECUTE, _("&Execute in shell\tCtrl+Shift+E"), "", wx.ITEM_NORMAL)
        self.edit.AppendSeparator()
        self.edit.Append(wx.ID_REPLACE, _("&Find && replace...\tCtrl+F"), "", wx.ITEM_NORMAL)
        self.edit.Append(wx.ID_FIND, _("Find &Next\tF3"), "", wx.ITEM_NORMAL)
        self.edit.Append(GO_TO_LINE, _("&Go to line...\tCtrl+G"), "", wx.ITEM_NORMAL)
        self.edit.Append(BROWSE_SOURCE, _("&Browse source\tCtrl+Enter"), "", wx.ITEM_NORMAL)
        self.edit.Append(AUTO_COMPLETE, _("&Auto complete\tCtrl+Space"), "", wx.ITEM_NORMAL)
        self.edit.Append(SHOW_DOCSTRING, _("&Show docstring\tCtrl+Shift+Space"), "", wx.ITEM_NORMAL)
        self.edit.AppendSeparator()
        self.edit.Append(INDENT, _("&Indent"), "", wx.ITEM_NORMAL)
        self.edit.Append(DEDENT, _("&Dedent\tShift+Tab"), "", wx.ITEM_NORMAL)
        self.edit.Append(COMMENT, _("Co&mment\tAlt+3"), "", wx.ITEM_NORMAL)
        self.edit.Append(UNCOMMENT, _("U&nComment\tAlt+4"), "", wx.ITEM_NORMAL)
        self.edit.AppendSeparator()
        self.edit.Append(INSERT_SEPARATOR, _("Insert &separator...\tAlt+I"), "", wx.ITEM_NORMAL)
        self.edit.Append(INSERT_SIGNATURE, _("Insert &signature\tCtrl+Shift+I"), "", wx.ITEM_NORMAL)
        self.edit.AppendSeparator()
        self.edit.Append(PREFERENCES, _("&Preferences...\tCtrl+Alt+P"), "", wx.ITEM_NORMAL)
        self.Append(self.edit, _("&Edit"))
        self.view = wx.Menu()
        self.view.Append(WHITESPACE, _("&Whitespace"), "", wx.ITEM_CHECK)
        self.view.Append(INDENTATION_GUIDES, _("&Indentation guides"), "", wx.ITEM_CHECK)
        self.view.Append(RIGHT_EDGE_INDICATOR, _("Ri&ght edge indicator"), "", wx.ITEM_CHECK)
        self.view.Append(END_OF_LINE_MARKER, _("&End-of-line marker"), "", wx.ITEM_CHECK)
        self.view.AppendSeparator()
        self.view.Append(AS_NOTEBOOK, _("As &notebook"), "", wx.ITEM_NORMAL)
        self.view.Append(AS_COLUMNS, _("As &columns"), "", wx.ITEM_NORMAL)
        self.view.Append(AS_ROWS, _("As &rows"), "", wx.ITEM_NORMAL)
        self.view.AppendSeparator()
        self.view.Append(SIDEBAR, _("&Sidebar\tCtrl+F12"), "", wx.ITEM_CHECK)
        self.view.Append(SHELL, _("S&hell\tF12"), "", wx.ITEM_CHECK)
        self.view.AppendSeparator()
        self.view.Append(CLEAR_OUTPUT, _("Clear &output"), "", wx.ITEM_NORMAL)
        self.view.Append(REFRESH, _("&Refresh\tF5"), "", wx.ITEM_NORMAL)
        self.Append(self.view, _("&View"))
        self.tools = wx.Menu()
        self.tools.Append(RUN, _("Run\\Stop\tCtrl+R"), "", wx.ITEM_NORMAL)
        self.tools.Append(RUN_WITHOUT_ARGUMENTS, _("Run without arguments/Stop\tCtrl+Shift+R"), "", wx.ITEM_NORMAL)
        self.tools.AppendSeparator()
        self.tools.Append(RUN_DEBUG, _("Run/Stop with &WinPdb\tCtrl+F9"), "", wx.ITEM_NORMAL)
        self.tools.Append(DEBUG, _("&Debug with winpdb...\tAlt+F9"), "", wx.ITEM_NORMAL)
        self.tools.AppendSeparator()
        self.tools.Append(RUN_TERMINAL, _("&Run in terminal\tF9"), "", wx.ITEM_NORMAL)
        self.tools.Append(RUN_TERMINAL_WITHOUT_ARGUMENTS, _("Run in terminal without &arguments\tShift+F9"), "", wx.ITEM_NORMAL)
        self.tools.Append(RUN_TERMINAL_WITHOUT_ARGUMENTS_EXIT, _("Run in terminal without &arguments && exit\tCtrl+Shift+F9"), "", wx.ITEM_NORMAL)
        self.tools.AppendSeparator()
        self.tools.Append(IMPORT, _("&Import in shell\tF10"), "", wx.ITEM_NORMAL)
        self.tools.AppendSeparator()
        self.tools.Append(BROWSE_OBJECT_WITH_PYFILLING, _("&Browse object with PyFilling...\tCtrl+Alt+F"), "", wx.ITEM_NORMAL)
        self.tools.Append(TEST_REGULAR_EXPRESSION_WITH_KIKI, _("Test regular expression with &Kiki...\tCtrl+K"), "", wx.ITEM_NORMAL)
        self.tools.Append(DESIGN_A_GUI_WITH_WXGLADE, _("Design a &gui with wxGlade...\tCtrl+Alt+G"), "", wx.ITEM_NORMAL)
        self.tools.Append(DESIGN_A_GUI_WITH_XRC, _("Design a gui with &XRC...\tCtrl+Alt+X"), "", wx.ITEM_NORMAL)
        self.tools.Append(CHECK_SOURCE_WITH_PYCHECKER, _("&Check source with PyChecker\tCtrl+Alt+C"), "", wx.ITEM_NORMAL)
        self.tools.AppendSeparator()
        self.tools.Append(BROWSE_FOLDER, _("Browse &folder\tCtrl+Shift+F"), "", wx.ITEM_NORMAL)
        self.tools.Append(OPEN_TERMINAL_EMULATOR, _("Open &terminal...\tCtrl+Shift+T"), "", wx.ITEM_NORMAL)
        self.Append(self.tools, _("&Tools"))
        self.blender = wx.Menu()
        self.blender.Append(LOAD_IN_BLENDER, _("&Load into Blender\tCtrl+B"), "", wx.ITEM_NORMAL)
        self.blender.Append(REFERENCE_IN_BLENDER, _("&Reference in Blender\tCtrl+Alt+B"), "", wx.ITEM_NORMAL)
        self.blender.AppendSeparator()
        self.blender.Append(REDRAW_BLENDER_WINDOW, _("Re&draw Blender window\tF5"), "", wx.ITEM_NORMAL)
        self.blender.AppendSeparator()
        self.blender.Append(BLENDER_PYTHON_MANUAL, _("Blender Python &manual..."), "", wx.ITEM_NORMAL)
        self.blender.Append(BLENDER_PYTHON_TUTORIAL, _("Blender Python &tutorial..."), "", wx.ITEM_NORMAL)
        self.blender.AppendSeparator()
        self.blender.Append(BLENDER_HOMEPAGE, _("Blender &homepage..."), "", wx.ITEM_NORMAL)
        self.blender.Append(DOWNLOAD_BLENDER, _("&Download Blender..."), "", wx.ITEM_NORMAL)
        self.blender.Append(FORUM_BLENDER_PYTHON, _("Forum &Blender Python..."), "", wx.ITEM_NORMAL)
        self.blender.Append(FORUM_ELYSIUN_PYTHON, _("Forum &Blenderartists Python..."), "", wx.ITEM_NORMAL)
        self.blender.AppendSeparator()
        self.blender.Append(ADD_SPE_TO_BLENDER, _("&Add SPE and Winpdb to Blender menu..."), "", wx.ITEM_NORMAL)
        self.Append(self.blender, _("&Blender"))
        self.links = wx.Menu()
        self.links.Append(SPE_HOMEPAGE, _("&Spe homepage..."), "", wx.ITEM_NORMAL)
        self.links.Append(FORUM_SPE, _("&Forum spe..."), "", wx.ITEM_NORMAL)
        self.links.AppendSeparator()
        self.links.Append(PYTHON_HOMEPAGE, _("&Python homepage..."), "", wx.ITEM_NORMAL)
        self.links.Append(PYTHON_ANNOUNCEMENTS, _("Python &announcements..."), "", wx.ITEM_NORMAL)
        self.links.Append(PYTHON_COOKBOOK, _("Python cook&book..."), "", wx.ITEM_NORMAL)
        self.links.Append(PYTHON_DAILY, _("Python &daily..."), "", wx.ITEM_NORMAL)
        self.links.Append(PYTHON_PACKAGE_INDEX, _("Python package &index..."), "", wx.ITEM_NORMAL)
        self.links.AppendSeparator()
        self.links.Append(AUTHORS_HOMEPAGE, _("&Authors homepage"), "", wx.ITEM_NORMAL)
        self.Append(self.links, _("&Links"))
        self.window = wx.Menu()
        self.window.Append(NEXT, _("&Next\tCtrl+`"), "", wx.ITEM_NORMAL)
        self.window.Append(PREVIOUS, _("&Previous\tCtrl+Shift+`"), "", wx.ITEM_NORMAL)
        self.Append(self.window, _("&Window"))
        self.help = wx.Menu()
        self.help.Append(MANUAL, _("&Manual..."), "", wx.ITEM_NORMAL)
        self.help.Append(KEYBOARD_SHORTCUTS, _("&Keyboard shortcuts..."), "", wx.ITEM_NORMAL)
        self.help.AppendSeparator()
        self.help.Append(PYTHON_LIBRARY, _("Python &library..."), "", wx.ITEM_NORMAL)
        self.help.Append(PYTHON_REFERENCE, _("Python &reference..."), "", wx.ITEM_NORMAL)
        self.help.Append(PYTHON_DOCUMENTATION_SERVER, _("Python documentation &server..."), "", wx.ITEM_NORMAL)
        self.help.AppendSeparator()
        self.help.Append(WXGLADE_MANUAL, _("wxGlade manual..."), "", wx.ITEM_NORMAL)
        self.help.Append(WXGLADE_TUTORIAL, _("wx&Glade tutorial..."), "", wx.ITEM_NORMAL)
        self.help.Append(WXWINDOWS_DOCUMENTATION, _("wxWindows documentation..."), "", wx.ITEM_NORMAL)
        self.help.AppendSeparator()
        self.help.Append(DONATE, _("&Donate..."), "", wx.ITEM_NORMAL)
        self.help.Append(ABOUT, _("&About..."), "", wx.ITEM_NORMAL)
        self.Append(self.help, _("&Help"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.menu_new, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.menu_open_files, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.menu_save, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.menu_save_as, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU, self.menu_save_copy, id=SAVE_COPY)
        self.Bind(wx.EVT_MENU, self.menu_open_workspace, id=OPEN_WORKSPACE)
        self.Bind(wx.EVT_MENU, self.menu_save_workspace, id=SAVE_WORKSPACE)
        self.Bind(wx.EVT_MENU, self.menu_save_workspace_as, id=SAVE_WORKSPACE_AS)
        self.Bind(wx.EVT_MENU, self.menu_save_uml_as, id=SAVE_UML_AS)
        self.Bind(wx.EVT_MENU, self.menu_print_uml_setup, id=PRINT_UML_SETUP)
        self.Bind(wx.EVT_MENU, self.menu_print_uml_preview, id=PRINT_UML_PREVIEW)
        self.Bind(wx.EVT_MENU, self.menu_print_uml, id=PRINT_UML)
        self.Bind(wx.EVT_MENU, self.menu_close, id=wx.ID_CLOSE)
        self.Bind(wx.EVT_MENU, self.menu_exit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.menu_remember_open_files, id=REMEMBER_OPEN_FILES)
        self.Bind(wx.EVT_MENU, self.menu_undo, id=wx.ID_UNDO)
        self.Bind(wx.EVT_MENU, self.menu_redo, id=wx.ID_REDO)
        self.Bind(wx.EVT_MENU, self.menu_cut, id=CUT)
        self.Bind(wx.EVT_MENU, self.menu_copy, id=COPY)
        self.Bind(wx.EVT_MENU, self.menu_paste, id=PASTE)
        self.Bind(wx.EVT_MENU, self.menu_execute, id=EXECUTE)
        self.Bind(wx.EVT_MENU, self.menu_find__replace, id=wx.ID_REPLACE)
        self.Bind(wx.EVT_MENU, self.menu_find_next, id=wx.ID_FIND)
        self.Bind(wx.EVT_MENU, self.menu_go_to_line, id=GO_TO_LINE)
        self.Bind(wx.EVT_MENU, self.menu_browse_source, id=BROWSE_SOURCE)
        self.Bind(wx.EVT_MENU, self.menu_auto_complete, id=AUTO_COMPLETE)
        self.Bind(wx.EVT_MENU, self.menu_show_docstring, id=SHOW_DOCSTRING)
        self.Bind(wx.EVT_MENU, self.menu_indent, id=INDENT)
        self.Bind(wx.EVT_MENU, self.menu_dedent, id=DEDENT)
        self.Bind(wx.EVT_MENU, self.menu_comment, id=COMMENT)
        self.Bind(wx.EVT_MENU, self.menu_uncomment, id=UNCOMMENT)
        self.Bind(wx.EVT_MENU, self.menu_insert_separator, id=INSERT_SEPARATOR)
        self.Bind(wx.EVT_MENU, self.menu_insert_signature, id=INSERT_SIGNATURE)
        self.Bind(wx.EVT_MENU, self.menu_preferences, id=PREFERENCES)
        self.Bind(wx.EVT_MENU, self.menu_whitespace, id=WHITESPACE)
        self.Bind(wx.EVT_MENU, self.menu_indentation, id=INDENTATION_GUIDES)
        self.Bind(wx.EVT_MENU, self.menu_right_edge_indicator, id=RIGHT_EDGE_INDICATOR)
        self.Bind(wx.EVT_MENU, self.menu_end_of_line_marker, id=END_OF_LINE_MARKER)
        self.Bind(wx.EVT_MENU, self.menu_as_notebook, id=AS_NOTEBOOK)
        self.Bind(wx.EVT_MENU, self.menu_as_columns, id=AS_COLUMNS)
        self.Bind(wx.EVT_MENU, self.menu_as_rows, id=AS_ROWS)
        self.Bind(wx.EVT_MENU, self.menu_sidebar, id=SIDEBAR)
        self.Bind(wx.EVT_MENU, self.menu_shell, id=SHELL)
        self.Bind(wx.EVT_MENU, self.menu_clear_output, id=CLEAR_OUTPUT)
        self.Bind(wx.EVT_MENU, self.menu_refresh, id=REFRESH)
        self.Bind(wx.EVT_MENU, self.menu_run, id=RUN)
        self.Bind(wx.EVT_MENU, self.menu_run_without_arguments, id=RUN_WITHOUT_ARGUMENTS)
        self.Bind(wx.EVT_MENU, self.menu_run_debug, id=RUN_DEBUG)
        self.Bind(wx.EVT_MENU, self.menu_debug, id=DEBUG)
        self.Bind(wx.EVT_MENU, self.menu_run_terminal, id=RUN_TERMINAL)
        self.Bind(wx.EVT_MENU, self.menu_run_terminal_without_arguments, id=RUN_TERMINAL_WITHOUT_ARGUMENTS)
        self.Bind(wx.EVT_MENU, self.menu_run_terminal_without_arguments_exit, id=RUN_TERMINAL_WITHOUT_ARGUMENTS_EXIT)
        self.Bind(wx.EVT_MENU, self.menu_import, id=IMPORT)
        self.Bind(wx.EVT_MENU, self.menu_browse_object_with_pyfilling, id=BROWSE_OBJECT_WITH_PYFILLING)
        self.Bind(wx.EVT_MENU, self.menu_test_regular_expression_with_kiki, id=TEST_REGULAR_EXPRESSION_WITH_KIKI)
        self.Bind(wx.EVT_MENU, self.menu_design_a_gui_with_wxglade, id=DESIGN_A_GUI_WITH_WXGLADE)
        self.Bind(wx.EVT_MENU, self.menu_design_a_gui_with_xrc, id=DESIGN_A_GUI_WITH_XRC)
        self.Bind(wx.EVT_MENU, self.menu_check_source_with_pychecker, id=CHECK_SOURCE_WITH_PYCHECKER)
        self.Bind(wx.EVT_MENU, self.menu_browse_folder, id=BROWSE_FOLDER)
        self.Bind(wx.EVT_MENU, self.menu_open_terminal_emulator, id=OPEN_TERMINAL_EMULATOR)
        self.Bind(wx.EVT_MENU, self.menu_load_in_blender, id=LOAD_IN_BLENDER)
        self.Bind(wx.EVT_MENU, self.menu_reference_in_blender, id=REFERENCE_IN_BLENDER)
        self.Bind(wx.EVT_MENU, self.menu_blender_python_manual, id=BLENDER_PYTHON_MANUAL)
        self.Bind(wx.EVT_MENU, self.menu_blender_python_tutorial, id=BLENDER_PYTHON_TUTORIAL)
        self.Bind(wx.EVT_MENU, self.menu_blender_homepage, id=BLENDER_HOMEPAGE)
        self.Bind(wx.EVT_MENU, self.menu_download_blender, id=DOWNLOAD_BLENDER)
        self.Bind(wx.EVT_MENU, self.menu_forum_blender_python, id=FORUM_BLENDER_PYTHON)
        self.Bind(wx.EVT_MENU, self.menu_forum_elysiun_python, id=FORUM_ELYSIUN_PYTHON)
        self.Bind(wx.EVT_MENU, self.menu_add_spe_to_blender, id=ADD_SPE_TO_BLENDER)
        self.Bind(wx.EVT_MENU, self.menu_spe_homepage, id=SPE_HOMEPAGE)
        self.Bind(wx.EVT_MENU, self.menu_forum_spe, id=FORUM_SPE)
        self.Bind(wx.EVT_MENU, self.menu_python_announcements, id=PYTHON_ANNOUNCEMENTS)
        self.Bind(wx.EVT_MENU, self.menu_python_cookbook, id=PYTHON_COOKBOOK)
        self.Bind(wx.EVT_MENU, self.menu_python_daily, id=PYTHON_DAILY)
        self.Bind(wx.EVT_MENU, self.menu_python_package_index, id=PYTHON_PACKAGE_INDEX)
        self.Bind(wx.EVT_MENU, self.menu_authors_homepage, id=AUTHORS_HOMEPAGE)
        self.Bind(wx.EVT_MENU, self.menu_next, id=NEXT)
        self.Bind(wx.EVT_MENU, self.menu_previous, id=PREVIOUS)
        self.Bind(wx.EVT_MENU, self.menu_manual, id=MANUAL)
        self.Bind(wx.EVT_MENU, self.menu_keyboard_shortcuts, id=KEYBOARD_SHORTCUTS)
        self.Bind(wx.EVT_MENU, self.menu_python_library, id=PYTHON_LIBRARY)
        self.Bind(wx.EVT_MENU, self.menu_python_reference, id=PYTHON_REFERENCE)
        self.Bind(wx.EVT_MENU, self.menu_python_documentation_server, id=PYTHON_DOCUMENTATION_SERVER)
        self.Bind(wx.EVT_MENU, self.menu_wxglade_manual, id=WXGLADE_MANUAL)
        self.Bind(wx.EVT_MENU, self.menu_wxglade_tutorial, id=WXGLADE_TUTORIAL)
        self.Bind(wx.EVT_MENU, self.menu_wxwindows_documentation, id=WXWINDOWS_DOCUMENTATION)
        self.Bind(wx.EVT_MENU, self.menu_donate, id=DONATE)
        self.Bind(wx.EVT_MENU, self.menu_about, id=ABOUT)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Bar.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Bar.__do_layout
        pass
        # end wxGlade

    def menu_new(self, event): # wxGlade: Bar.<event_handler>
        print 'New'
        event.Skip()

    def menu_open(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_save(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_save_as(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_open_workspace(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_save_workspace_as(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_save_workspace(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_close(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_exit(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_remember_open_files(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_undo(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_redo(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_cut(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_copy(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_paste(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_find__replace(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_go_to_line(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_browse_source(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_auto_complete(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_indent(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_dedent(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_comment(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_uncomment(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_insert_separator(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_insert_signature(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_insert_signature' not implemented"
        event.Skip()

    def menu_execute(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_execute' not implemented"
        event.Skip()

    def menu_execute_verbose(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_execute_verbose' not implemented"
        event.Skip()

    def menu_preferences(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_refresh(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_whitespace(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_indentation(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_right_edge_indicator(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_end_of_line_marker(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_as_notebook(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_as_notebook' not implemented"
        event.Skip()

    def menu_as_columns(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_as_columns' not implemented"
        event.Skip()

    def menu_as_rows(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_as_rows' not implemented"
        event.Skip()

    def menu_sidebar(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_shell(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_run(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_run_without_arguments(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_run_terminal(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_run_terminal' not implemented"
        event.Skip()

    def menu_run_terminal_without_arguments(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_run_terminal_without_arguments' not implemented"
        event.Skip()

    def menu_run_terminal_without_arguments_exit(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_run_terminal_without_arguments_exit' not implemented"
        event.Skip()

    def menu_import(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_browse_object_with_pyfilling(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_test_regular_expression_with_kiki(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_design_a_gui_with_wxglade(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_design_a_gui_with_xrc(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_check_source_with_pychecker(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_browse_folder(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_open_terminal_emulator(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_load_in_blender(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_reference_in_blender(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_blender_python_manual(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_blender_python_tutorial(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_blender_homepage(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_download_blender(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_forum_blender_python(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_forum_elysiun_python(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_spe_homepage(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_forum_spe(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_authors_homepage(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_contact_author(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_active_python_distribution(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_enthought_python_distribution(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_python_announcements(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_python_cookbook(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_python_daily(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_python_package_index(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_manual(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_keyboard_shortcuts(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_python_library(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_python_reference(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_python_documentation_server(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_wxglade_manual(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_wxglade_tutorial(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_wxwindows_documentation(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_donate(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_about(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_find_next(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_open_files(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_next(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_previous(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_debug(self, event): # wxGlade: Bar.<event_handler>
        event.Skip()

    def menu_save_uml_as(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_save_uml_as' not implemented"
        event.Skip()

    def menu_print_uml_setup(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_print_uml_setup' not implemented"
        event.Skip()

    def menu_uml_preview(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_uml_preview' not implemented"
        event.Skip()

    def menu_print_uml(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_print_uml' not implemented"
        event.Skip()

    def menu_print_uml_preview(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_print_uml_preview' not implemented"
        event.Skip()

    def menu_run_without_arguments(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_run_without_arguments' not implemented"
        event.Skip()

    def menu_run_debug(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_run_debug' not implemented"
        event.Skip()

    def menu_run_without_arguments_exit(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_run_without_arguments_exit' not implemented"
        event.Skip()

    def menu_toolbar(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_toolbar' not implemented"
        event.Skip()

    def menu_show_docstring(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_show_docstring' not implemented"
        event.Skip()


    def menu_save_copy(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_save_copy' not implemented"
        event.Skip()

    def menu_clear_output(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_clear_output' not implemented"
        event.Skip()

    def menu_add_spe_to_blender(self, event): # wxGlade: Bar.<event_handler>
        print "Event handler `menu_add_spe_to_blender' not implemented"
        event.Skip()

# end of class Bar


