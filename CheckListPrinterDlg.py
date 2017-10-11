#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade f172c83ff51d+ on Wed Oct 11 14:51:28 2017
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from wx import InfoBar
from wx.lib.mixins.listctrl import CheckListCtrlMixin
class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    def __init__(self, parent, id=-1, *args, **kwargs):
        wx.ListCtrl.__init__(self, parent, id, style=wx.LC_REPORT|wx.LC_SINGLE_SEL)
        CheckListCtrlMixin.__init__(self, imgsz=(20,20))
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        self.menu_sheet = wx.Menu()
        item = self.frame_menubar.menu_sheet_1 = wx.MenuItem(self.menu_sheet, 1021, _("1"), "", wx.ITEM_RADIO)
        self.menu_sheet.AppendItem(self.frame_menubar.menu_sheet_1)
        self.Bind(wx.EVT_MENU, self.OnMenuSwitchSheet1, id=item.GetId())
        item = self.frame_menubar.menu_sheet_2 = wx.MenuItem(self.menu_sheet, 1022, _("2"), "", wx.ITEM_RADIO)
        self.menu_sheet.AppendItem(self.frame_menubar.menu_sheet_2)
        self.Bind(wx.EVT_MENU, self.OnMenuSwitchSheet2, id=item.GetId())
        item = self.frame_menubar.menu_sheet_3 = wx.MenuItem(self.menu_sheet, 1023, _("3"), "", wx.ITEM_RADIO)
        self.menu_sheet.AppendItem(self.frame_menubar.menu_sheet_3)
        self.Bind(wx.EVT_MENU, self.OnMenuSwitchSheet3, id=item.GetId())
        item = self.frame_menubar.menu_sheet_4 = wx.MenuItem(self.menu_sheet, 1024, _("4"), "", wx.ITEM_RADIO)
        self.menu_sheet.AppendItem(self.frame_menubar.menu_sheet_4)
        self.Bind(wx.EVT_MENU, self.OnMenuSwitchSheet4, id=item.GetId())
        item = self.frame_menubar.menu_sheet_5 = wx.MenuItem(self.menu_sheet, 1025, _("5"), "", wx.ITEM_RADIO)
        self.menu_sheet.AppendItem(self.frame_menubar.menu_sheet_5)
        self.Bind(wx.EVT_MENU, self.OnMenuSwitchSheet5, id=item.GetId())
        self.frame_menubar.Append(self.menu_sheet, _("Sheet"))
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.list = CheckListCtrl(self, wx.ID_ANY)
        self.bar_info = InfoBar(self, wx.ID_ANY)
        self.bitmap_button_append = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/list-add.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_remove = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/list-remove.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_edit = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/gtk-edit.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_go_top = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/go-top.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_go_up = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/go-up.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_go_down = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/go-down.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_go_bottom = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/go-bottom.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_import = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/document-import.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_export = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/document-export.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_setup = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/document-properties.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_about = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("img/help-info.png", wx.BITMAP_TYPE_ANY))
        self.button_print = wx.Button(self, wx.ID_ANY, _("Print"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnAppend, self.bitmap_button_append)
        self.Bind(wx.EVT_BUTTON, self.OnRemove, self.bitmap_button_remove)
        self.Bind(wx.EVT_BUTTON, self.OnEdit, self.bitmap_button_edit)
        self.Bind(wx.EVT_BUTTON, self.OnGoTop, self.bitmap_button_go_top)
        self.Bind(wx.EVT_BUTTON, self.OnGoUp, self.bitmap_button_go_up)
        self.Bind(wx.EVT_BUTTON, self.OnGoDown, self.bitmap_button_go_down)
        self.Bind(wx.EVT_BUTTON, self.OnGoBottom, self.bitmap_button_go_bottom)
        self.Bind(wx.EVT_BUTTON, self.OnImport, self.bitmap_button_import)
        self.Bind(wx.EVT_BUTTON, self.OnExport, self.bitmap_button_export)
        self.Bind(wx.EVT_BUTTON, self.OnSetup, self.bitmap_button_setup)
        self.Bind(wx.EVT_BUTTON, self.OnAbout, self.bitmap_button_about)
        self.Bind(wx.EVT_BUTTON, self.OnPrint, self.button_print)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        s = _("Checklist printer")
        #print type(s), s
        self.SetTitle(_("Checklist printer"))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("img/icon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((518, 751))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bitmap_button_append.SetSize(self.bitmap_button_append.GetBestSize())
        self.bitmap_button_remove.SetSize(self.bitmap_button_remove.GetBestSize())
        self.bitmap_button_edit.SetSize(self.bitmap_button_edit.GetBestSize())
        self.bitmap_button_go_top.SetSize(self.bitmap_button_go_top.GetBestSize())
        self.bitmap_button_go_up.SetSize(self.bitmap_button_go_up.GetBestSize())
        self.bitmap_button_go_down.SetSize(self.bitmap_button_go_down.GetBestSize())
        self.bitmap_button_go_bottom.SetSize(self.bitmap_button_go_bottom.GetBestSize())
        self.bitmap_button_import.SetSize(self.bitmap_button_import.GetBestSize())
        self.bitmap_button_export.SetSize(self.bitmap_button_export.GetBestSize())
        self.bitmap_button_setup.SetSize(self.bitmap_button_setup.GetBestSize())
        self.bitmap_button_about.SetSize(self.bitmap_button_about.GetBestSize())
        self.button_print.SetMinSize((-1, 50))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add((20, 20), 0, 0, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_12.Add(self.list, 1, wx.EXPAND, 0)
        sizer_12.Add(self.bar_info, 0, wx.EXPAND, 0)
        sizer_3.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_3.Add((5, 20), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_append, 0, 0, 0)
        sizer_4.Add((20, 10), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_remove, 0, 0, 0)
        sizer_4.Add((20, 10), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_edit, 0, 0, 0)
        sizer_4.Add((20, 20), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_go_top, 0, 0, 0)
        sizer_4.Add((20, 10), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_go_up, 0, 0, 0)
        sizer_4.Add((20, 10), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_go_down, 0, 0, 0)
        sizer_4.Add((20, 10), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_go_bottom, 0, 0, 0)
        sizer_4.Add((20, 20), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_import, 0, 0, 0)
        sizer_4.Add((20, 10), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_export, 0, 0, 0)
        sizer_4.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_4.Add(self.bitmap_button_setup, 0, 0, 0)
        sizer_4.Add((20, 10), 0, 0, 0)
        sizer_4.Add(self.bitmap_button_about, 0, 0, 0)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_2.Add(self.button_print, 0, wx.EXPAND, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add((20, 20), 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        self.SetSize((518, 751))
        # end wxGlade

    def OnMenuSwitchSheet1(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnMenuSwitchSheet1' not implemented!")
        event.Skip()

    def OnMenuSwitchSheet2(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnMenuSwitchSheet2' not implemented!")
        event.Skip()

    def OnMenuSwitchSheet3(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnMenuSwitchSheet3' not implemented!")
        event.Skip()

    def OnMenuSwitchSheet4(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnMenuSwitchSheet4' not implemented!")
        event.Skip()

    def OnMenuSwitchSheet5(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnMenuSwitchSheet5' not implemented!")
        event.Skip()

    def OnAppend(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnAppend' not implemented!")
        event.Skip()

    def OnRemove(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnRemove' not implemented!")
        event.Skip()

    def OnEdit(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnEdit' not implemented!")
        event.Skip()

    def OnGoTop(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnGoTop' not implemented!")
        event.Skip()

    def OnGoUp(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnGoUp' not implemented!")
        event.Skip()

    def OnGoDown(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnGoDown' not implemented!")
        event.Skip()

    def OnGoBottom(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnGoBottom' not implemented!")
        event.Skip()

    def OnImport(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnImport' not implemented!")
        event.Skip()

    def OnExport(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnExport' not implemented!")
        event.Skip()

    def OnSetup(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnSetup' not implemented!")
        event.Skip()

    def OnAbout(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnAbout' not implemented!")
        event.Skip()

    def OnPrint(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnPrint' not implemented!")
        event.Skip()

# end of class MyFrame

class SetupDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SetupDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.text_ctrl_paper_width = wx.TextCtrl(self, wx.ID_ANY, _("50"))
        self.text_ctrl_paper_height = wx.TextCtrl(self, wx.ID_ANY, _("297"))
        self.text_ctrl_margin_x = wx.TextCtrl(self, wx.ID_ANY, _("5"))
        self.text_ctrl_margin_y = wx.TextCtrl(self, wx.ID_ANY, _("5"))
        self.combo_box_font = wx.ComboBox(self, wx.ID_ANY, choices=[_(u"\u5b8b\u4f53"), _(u"\u9ed1\u4f53"), _(u"\u6977\u4f53")], style=wx.CB_DROPDOWN)
        self.text_ctrl_font_size = wx.TextCtrl(self, wx.ID_ANY, _("12"))
        self.text_ctrl_line_spacing = wx.TextCtrl(self, wx.ID_ANY, _("5"))
        self.combo_box_leading_char = wx.ComboBox(self, wx.ID_ANY, choices=[_(u"\u25a1"), _(u"\u25ef"), _(u"\u25ce"), _(u"\u25b3"), _(u"\u25bd"), _(u"\u2606"), _(u"\u25c7"), _(u"\u2609"), _(u"\u25a0"), _(u"\u25b2"), _(u"\u25bc"), _(u"\u25c6"), _(u"\u25cf"), _(u"\u2605")], style=wx.CB_DROPDOWN)
        self.checkbox_print_time = wx.CheckBox(self, wx.ID_ANY, _("Print datetime"))
        self.button_ok = wx.Button(self, wx.ID_OK, "")
        self.button_cancel = wx.Button(self, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SetupDialog.__set_properties
        self.SetTitle(_("Setup"))
        self.combo_box_font.SetMinSize((200, -1))
        self.combo_box_font.SetSelection(0)
        self.combo_box_leading_char.SetMinSize((80, -1))
        self.combo_box_leading_char.SetSelection(0)
        self.checkbox_print_time.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SetupDialog.__do_layout
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add((20, 20), 0, 0, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, _("Page width"))
        sizer_9.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        sizer_9.Add((5, 20), 0, 0, 0)
        sizer_9.Add(self.text_ctrl_paper_width, 0, wx.ALIGN_CENTER, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, _("mm"))
        sizer_9.Add(label_4, 0, wx.ALIGN_CENTER, 0)
        sizer_9.Add((20, 20), 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, _("Page height"))
        sizer_9.Add(label_5, 0, wx.ALIGN_CENTER, 0)
        sizer_9.Add((5, 20), 0, 0, 0)
        sizer_9.Add(self.text_ctrl_paper_height, 0, wx.ALIGN_CENTER, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, _("mm"))
        sizer_9.Add(label_6, 0, wx.ALIGN_CENTER, 0)
        sizer_9.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_9, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, _("Margin horizontal"))
        sizer_10.Add(label_7, 0, wx.ALIGN_CENTER, 0)
        sizer_10.Add((5, 20), 0, 0, 0)
        sizer_10.Add(self.text_ctrl_margin_x, 0, wx.ALIGN_CENTER, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, _("mm"))
        sizer_10.Add(label_8, 0, wx.ALIGN_CENTER, 0)
        sizer_10.Add((20, 20), 0, 0, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, _("Margin vertical"))
        sizer_10.Add(label_9, 0, wx.ALIGN_CENTER, 0)
        sizer_10.Add((5, 20), 0, 0, 0)
        sizer_10.Add(self.text_ctrl_margin_y, 0, wx.ALIGN_CENTER, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, _("mm"))
        sizer_10.Add(label_10, 0, wx.ALIGN_CENTER, 0)
        sizer_10.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_10, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, _("Font"))
        sizer_8.Add(label_1, 0, wx.ALIGN_CENTER, 0)
        sizer_8.Add((5, 20), 0, 0, 0)
        sizer_8.Add(self.combo_box_font, 0, wx.ALIGN_CENTER, 0)
        sizer_8.Add((20, 20), 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, _("Font size"))
        sizer_8.Add(label_2, 0, wx.ALIGN_CENTER, 0)
        sizer_8.Add((5, 20), 0, 0, 0)
        sizer_8.Add(self.text_ctrl_font_size, 0, wx.ALIGN_CENTER, 0)
        sizer_8.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_8, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, _("Line spacing"))
        sizer_11.Add(label_11, 0, wx.ALIGN_CENTER, 0)
        sizer_11.Add((5, 20), 0, 0, 0)
        sizer_11.Add(self.text_ctrl_line_spacing, 0, wx.ALIGN_CENTER, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, _("mm"))
        sizer_11.Add(label_12, 0, wx.ALIGN_CENTER, 0)
        sizer_11.Add((20, 20), 0, 0, 0)
        label_13 = wx.StaticText(self, wx.ID_ANY, _("Leading char"))
        sizer_11.Add(label_13, 0, wx.ALIGN_CENTER, 0)
        sizer_11.Add((5, 20), 0, 0, 0)
        sizer_11.Add(self.combo_box_leading_char, 0, wx.ALIGN_CENTER, 0)
        sizer_11.Add((20, 20), 0, 0, 0)
        sizer_11.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_13.Add(self.checkbox_print_time, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13.Add((0, 0), 0, 0, 0)
        sizer_13.Add((0, 0), 0, 0, 0)
        sizer_13.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_13, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_7.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_7.Add(self.button_ok, 0, 0, 0)
        sizer_7.Add((20, 20), 0, 0, 0)
        sizer_7.Add(self.button_cancel, 0, 0, 0)
        sizer_6.Add(sizer_7, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, 0, 0)
        self.SetSizer(sizer_5)
        sizer_5.Fit(self)
        self.Layout()
        # end wxGlade

# end of class SetupDialog
