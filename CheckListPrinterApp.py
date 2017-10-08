#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
import os
import re
import sys
import time
import ConfigParser

from CheckListPrinterDlg import *



ABOUT_INFO = u'''\
CheckList打印机 V1.0

快捷键：
1 ~ 5  - 切换表单1~5
Insert - 新增
Delete - 删除
Enter  - 编辑
Space  - 反选
Up     - 光标上移
Down   - 光标下移
Left   - 选中项上移
Right  - 选中项下移

URL: https://github.com/pengshulin/checklist_printer
Peng Shullin <trees_peng@163.com> 2017
'''


class ChecklistPrintout(wx.Printout):
    def __init__(self, frame):
        wx.Printout.__init__(self)
        self.frame = frame

    def HasPage(self, page):
        return page <= 1

    def GetPageInfo(self):
        return (1, 1, 1, 1)

    def OnPrintPage(self, page):
        dc = self.GetDC()
        paper_size = paper_width, paper_height = self.frame.paper_size
        print 'set paper_size', paper_size
        print 'get paper_size', self.frame.printData.GetPaperSize()
        w, h = dc.GetSize()  # pixel size on printer
        margin_x, margin_y = self.frame.margin_x, self.frame.margin_y
        scalex = float(w) / paper_width
        scaley = float(h) / paper_height
        scale = min(scalex, scaley)
        print 'scale:', scale
        def TR(pos):
            print pos, '->', int(pos*scale)
            return int(pos*scale)
        dc.SetUserScale(scale, scale)
        #dc.SetDeviceOrigin(int(posX), int(posY))
        dc.SetDeviceOrigin(0,0)
     
        font = dc.GetFont()
        font.SetFamily( wx.FONTFAMILY_MODERN )
        font.SetFaceName( self.frame.font )
        font.SetStyle(wx.FONTSTYLE_NORMAL)
        font.SetWeight(wx.FONTWEIGHT_NORMAL)
        #font.SetNoAntiAliasing()  # eprecated
        font.SetPointSize( self.frame.font_size )
        print( 'Font encoding:', font.GetEncoding() )
        print( 'Font face name:', font.GetFaceName() )
        print( 'Font pixel size:', font.GetPixelSize() )
        print( 'Font point size:', font.GetPointSize() )
        print( 'Font family:', font.GetFamilyString() )
        print( 'Font style:', font.GetStyleString() )
        print( 'Font weight:', font.GetWeightString() )
        #dc.SetFont(font)
        dc.SetFont(font.Scale(0.3))
        posx, posy = margin_x, margin_y
        line_width = 0.05
        txt_height = self.frame.line_height
        txt_spacing = self.frame.line_spacing
        def draw_line( x0, y0, x1, y1 ):
            pen = wx.Pen('black')
            pen.SetWidth( TR(line_width) )
            dc.SetPen(pen)
            dc.DrawLine( x0, y0, x1, y1 )

        def draw_hline():
            pen = wx.Pen('black')
            pen.SetWidth( TR(line_width) )
            dc.SetPen(pen)
            y = posy+line_width/2.0
            dc.DrawLine( posx, y, paper_width-margin_x, y )
         
        def draw_text( txt, leading_char='', align='left' ):
            #if align == 'left':
            #    flag = wx.ALIGN_LEFT
            #if align == 'center':
            #    flag = wx.ALIGN_CENTRE
            #elif align == 'right':
            #    flag = wx.ALIGN_RIGHT
            #else:
            #    flag = 0
            #dc.DrawLabel( txt, (posx, posy, paper_width-margin_x, posy+txt_height), alignment=flag|wx.ALIGN_TOP )
            print 'DRAW_TEXT', txt
            W,H,D,EL = dc.GetFullTextExtent( leading_char )
            dc.DrawText( leading_char, posx, posy )
            width_limit = paper_width - margin_x * 2 - W
            height = 0.0
            txt, txt2 = list(txt), []
            x, y = posx, posy
            while True:
                h = 0
                while True:
                    w,h,d,el = dc.GetFullTextExtent( u''.join(txt) )
                    #print w,h,d,el
                    if w > width_limit:
                        txt2.insert(0, txt.pop())
                    else:
                        break
                #print txt, txt2
                dc.DrawText( u''.join(txt), x+W, y )
                y += h
                height += h
                txt, txt2 = txt2, []
                # remove leading space
                while True:
                    if not txt:
                        break
                    if not txt[0].strip():
                        txt.pop(0)
                    else:
                        break
                if not txt:
                    break
            print 'line height', height
            return height

        DRAW_SEPERATORS = True
        DRAW_SEPERATORS = False

        # draw date/time
        if self.frame.print_time:
            h = draw_text(time.strftime("%Y-%m-%d %H:%M:%S"))
            posy += h + txt_spacing 
            # draw seperator lines
            if DRAW_SEPERATORS:
                draw_hline() 
                posy += line_width * 2
        # draw check lists
        for idx in range(self.frame.list.GetItemCount()):
            txt = self.frame.list.GetItemText(idx, 0)
            checked = self.frame.list.IsChecked(idx)
            if checked:
                h = draw_text(txt, self.frame.leading_char)
                posy += h + txt_spacing 
                #if posy > paper_height / 2.0:
                #    dc.EndPage()
                #    dc.StartPage()
                #    posy = margin_y
                posx = margin_x
                # draw seperator lines
                if DRAW_SEPERATORS:
                    draw_hline() 
                    posy += line_width * 2
        # draw seperator lines
        if DRAW_SEPERATORS:
            draw_hline() 
            posy += line_width * 2
        return True





class MainFrame(MyFrame):

    DEFAULT_DPI = 300
    DEFAULT_PAPER_SIZE = (58.0, 297.0)
    DEFAULT_MARGIN_X = 3.0
    DEFAULT_MARGIN_Y = 10.0
    DEFAULT_FONT = u'宋体'
    DEFAULT_FONT_SIZE = 12
    DEFAULT_LINE_HEIGHT = 6.0
    DEFAULT_LINE_SPACING = 2.0
    DEFAULT_LEADING_CHAR = u'□'
    DEFAULT_PRINT_TIME = True

    SHEET_NUM = 5

    def __init__(self, *args, **kwds):
        MyFrame.__init__( self, *args, **kwds )
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.list.Bind(wx.EVT_LEFT_DCLICK, self.OnEdit)
        self.list.Bind(wx.EVT_KEY_DOWN, self.OnKey)

        dirs = wx.StandardPaths.Get()
        self.config_dir = dirs.GetUserDataDir()
        self.config_file = os.path.join( self.config_dir, 'config.conf' )
        self.sheets_file = os.path.join( self.config_dir, 'sheets.conf' )

        self.list.InsertColumn(0, "TODO")
        self.list.SetFont( self.list.GetFont().MakeLarger() )

        self.paper_size = self.DEFAULT_PAPER_SIZE
        self.margin_x = self.DEFAULT_MARGIN_X
        self.margin_y = self.DEFAULT_MARGIN_Y
        self.dpi = self.DEFAULT_DPI
        self.font = self.DEFAULT_FONT
        self.font_size = self.DEFAULT_FONT_SIZE
        self.line_height = self.DEFAULT_LINE_HEIGHT
        self.line_spacing = self.DEFAULT_LINE_SPACING
        self.leading_char = self.DEFAULT_LEADING_CHAR
        self.print_time = self.DEFAULT_PRINT_TIME

        self.printData = wx.PrintData()

        self.timer_info = wx.Timer(self)

        self.sheets = [[[], []] for i in range(self.SHEET_NUM)]
        self.sheet_num = 0

        self.loadConfig()
        self.loadSheets()
        print self.sheets
        for i in range(len(self.sheets[self.sheet_num][0])):
            idx = self.list.InsertStringItem( sys.maxint, self.sheets[self.sheet_num][0][i] )
            if i in self.sheets[self.sheet_num][1]:
                self.list.CheckItem(idx)
        menu = eval('self.frame_menubar.menu_sheet_%d'% (self.sheet_num+1))
        menu.Check() 

        self.SetAcceleratorTable(wx.AcceleratorTable([  \
            (wx.ACCEL_NORMAL, ord('1'),   1021),  # sheet 1
            (wx.ACCEL_NORMAL, ord('2'),   1022),  # sheet 2 
            (wx.ACCEL_NORMAL, ord('3'),   1023),  # sheet 3 
            (wx.ACCEL_NORMAL, ord('4'),   1024),  # sheet 4 
            (wx.ACCEL_NORMAL, ord('5'),   1025),  # sheet 5 
            ]))


    def OnClose(self, event):
        self.saveSheets()
        self.saveConfig()
        self.Destroy()
        event.Skip()
 
    def OnResize(self, event):
        self.list.SetColumnWidth(0, self.list.GetSize()[0]-25)
        event.Skip()
    
    def info( self, info, info_type=wx.ICON_WARNING ):
        if info:
            self.bar_info.ShowMessage(info, info_type)
            self.timer_info.Start( 5*1000, oneShot=True )
        else:
            self.bar_info.Dismiss()

    def OnTimer( self, event ):
        self.bar_info.Dismiss()
        event.Skip()
 
    def OnAbout(self, event):
        self.info( '' )
        dlg = wx.MessageDialog(self, ABOUT_INFO, u'关于', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def loadConfig( self ):
        try:
            cfgfile = ConfigParser.ConfigParser()
            cfgfile.read( self.config_file )

            width = float(cfgfile.get( 'config', 'paper_width' ))
            height = float(cfgfile.get( 'config', 'paper_height' ))
            self.paper_size = (width, height)

            margin_x = float(cfgfile.get( 'config', 'margin_x' ))
            margin_y = float(cfgfile.get( 'config', 'margin_y' ))
            self.margin_x = margin_x
            self.margin_y = margin_y
    
            font = cfgfile.get( 'config', 'font' ).decode(encoding='utf8')
            self.font = font
            
            font_size = int(float(cfgfile.get( 'config', 'font_size' )))
            self.font_size = font_size
                    
            line_spacing = float(cfgfile.get( 'config', 'line_spacing' ))
            self.line_spacing = line_spacing
 
            leading_char = cfgfile.get( 'config', 'leading_char' ).decode(encoding='utf8')
            self.leading_char = leading_char
            
            sheet_num = int(cfgfile.get( 'config', 'sheet_num' ))
            self.sheet_num = sheet_num

            print_time = bool(int(cfgfile.get( 'config', 'print_time' )))
            self.print_time = print_time

        except Exception as e:
            print e
            print( 'load config failed' )
 

    def saveConfig( self ):
        cfgfile = ConfigParser.ConfigParser()
        cfgfile.add_section( 'config' )
        try:
            cfgfile.set( 'config', 'paper_width', str(self.paper_size[0]) )
            cfgfile.set( 'config', 'paper_height', str(self.paper_size[1]) )
        except:
            pass
        try:
            cfgfile.set( 'config', 'margin_x', str(self.margin_x) )
            cfgfile.set( 'config', 'margin_y', str(self.margin_y) )
        except:
            pass
        try:
            cfgfile.set( 'config', 'font', self.font.encode('utf-8'))
        except: 
            pass
        try:
            cfgfile.set( 'config', 'font_size', str(self.font_size) )
        except:
            pass
        try:
            cfgfile.set( 'config', 'line_spacing', str(self.line_spacing) )
        except:
            pass
        try:
            cfgfile.set( 'config', 'leading_char', self.leading_char.encode('utf-8'))
        except: 
            pass
        try:
            cfgfile.set( 'config', 'sheet_num', str(self.sheet_num) )
        except:
            pass
        try:
            cfgfile.set( 'config', 'print_time', str(int(self.print_time)) )
        except:
            pass
        try:
            if not os.path.isdir( self.config_dir ):
                os.mkdir( self.config_dir )
            cfgfile.write(open( self.config_file, 'w+'))
        except:
            pass
 
    def loadSheets( self ):
        try:
            cfgfile = ConfigParser.ConfigParser()
            cfgfile.read( self.sheets_file )
        except:
            return

        def loadOneSheet( sheet_num ):
            section = 'sheet%d'% sheet_num 
            checklist = []
            checked = []
            idx = 0
            try:
                while True:
                    try:
                        checklist.append( unicode(cfgfile.get( section, str(idx) ), encoding='utf-8') )
                        idx += 1
                    except:
                        break
                for i in cfgfile.get( section, 'checked' ).split(','):
                    if i.strip():
                        checked.append( int(i) )
            except Exception as e:
                print( e )
                print( 'load %s failed'% section )
            return checklist, checked

        for i in range(5):
            self.sheets[i] = loadOneSheet( i+1 )

    def saveSheets( self ):
        self.doUpdateCurrentSheet() 
        cfgfile = ConfigParser.ConfigParser()

        def saveOneSheet( idx ):
            section = 'sheet%d'% (idx+1)
            cfgfile.add_section( section )
            for i in range(len(self.sheets[idx][0])):
                try:
                    cfgfile.set( section, str(i), self.sheets[idx][0][i].encode('utf-8') )
                except:
                    pass
            cfgfile.set( section, 'checked', ','.join(map(str, self.sheets[idx][1])) )

        for i in range(self.SHEET_NUM):
            saveOneSheet( i )
        try:
            if not os.path.isdir( self.config_dir ):
                os.mkdir( self.config_dir )
            cfgfile.write(open( self.sheets_file, 'w+'))
        except:
            pass
   
    def OnKey( self, event ):
        keycode = event.GetKeyCode()
        #print 'keycode', keycode
        if keycode == wx.WXK_SPACE:
            # toggle
            idx = self.list.GetFirstSelected()
            checked = self.list.IsChecked(idx)
            self.list.CheckItem( idx, False if checked else True )
        elif keycode == wx.WXK_UP:
            idx = self.list.GetFirstSelected()
            if idx == -1:
                idx = self.list.GetFocusedItem()
                if idx != -1:
                    self.list.Select(idx, 1)
            elif idx:
                self.list.Select(idx, 0)
                self.list.Select(idx-1, 1)
        elif keycode == wx.WXK_DOWN:
            cnt = self.list.GetItemCount()
            idx = self.list.GetFirstSelected()
            if idx == -1:
                idx = self.list.GetFocusedItem()
                if idx != -1:
                    self.list.Select(idx, 1)
            elif idx < cnt-1:
                self.list.Select(idx, 0)
                self.list.Select(idx+1, 1)
        elif keycode == wx.WXK_LEFT:
            self.OnGoUp( event )
        elif keycode == wx.WXK_RIGHT:
            self.OnGoDown( event )
        elif keycode == wx.WXK_RETURN:
            self.OnEdit( event )
        elif keycode == wx.WXK_INSERT:
            self.OnAppend( event )
        elif keycode == wx.WXK_DELETE:
            self.OnRemove( event )
        else:
            print 'ignored keycode', keycode

    def OnAppend( self, event ):
        dlg = wx.TextEntryDialog( self, u'输入新的项目：', u'添加', '')
        if dlg.ShowModal() == wx.ID_OK:

            val = dlg.GetValue().strip()
            if val:
                #self.list.Select( self.list.GetFirstSelected(), 0 )
                idx = self.list.InsertStringItem( sys.maxint, val )
                self.list.CheckItem(idx)
                self.list.Select(idx)
        dlg.Destroy()

    def OnRemove( self, event ):
        idx = self.list.GetFirstSelected()
        cnt = self.list.GetItemCount()
        if idx == -1:
            return
        self.list.DeleteItem( idx )
        if idx < cnt - 1:
            self.list.Select( idx )
            

    def OnGoTop( self, event ):
        idx = self.list.GetFirstSelected()
        if idx == -1 or idx == 0:
            return
        txt = self.list.GetItemText(idx, 0)
        checked = self.list.IsChecked(idx)
        self.list.DeleteItem( idx )
        self.list.InsertStringItem( 0, txt )
        if checked:
            self.list.CheckItem( 0 )
        self.list.Select(0)

    def OnGoUp( self, event ):
        idx = self.list.GetFirstSelected()
        if idx == -1 or idx == 0:
            return
        txt = self.list.GetItemText(idx, 0)
        checked = self.list.IsChecked(idx)
        self.list.DeleteItem( idx )
        self.list.InsertStringItem( idx-1, txt )
        if checked:
            self.list.CheckItem( idx-1 )
        self.list.Select(idx-1)

    def OnGoDown( self, event ):
        idx = self.list.GetFirstSelected()
        cnt = self.list.GetItemCount()
        if idx == -1 or idx == cnt-1:
            return
        txt = self.list.GetItemText(idx, 0)
        checked = self.list.IsChecked(idx)
        self.list.DeleteItem( idx )
        self.list.InsertStringItem( idx+1, txt )
        if checked:
            self.list.CheckItem( idx+1 )
        self.list.Select(idx+1)

    def OnGoBottom( self, event ):
        idx = self.list.GetFirstSelected()
        cnt = self.list.GetItemCount()
        if idx == -1 or idx == cnt-1:
            return
        txt = self.list.GetItemText(idx, 0)
        checked = self.list.IsChecked(idx)
        self.list.DeleteItem( idx )
        self.list.InsertStringItem( cnt-1, txt )
        if checked:
            self.list.CheckItem( cnt-1 )
        self.list.Select(cnt-1)

    def OnEdit( self, event ):
        idx = self.list.GetFirstSelected()
        if idx == -1:
            return
        txt = self.list.GetItemText(idx, 0)
        dlg = wx.TextEntryDialog( self, u'修改项目：', u'修改', txt)
        if dlg.ShowModal() == wx.ID_OK:
            val = dlg.GetValue().strip()
            if val:
                self.list.SetItemText( idx, val )
        dlg.Destroy()

    def OnPrint( self, event ):
        self.printData.SetOrientation(wx.PORTRAIT)
        self.printData.SetPrintMode(wx.PRINT_MODE_PRINTER)
        self.printData.SetQuality( self.dpi )
        self.printData.SetPaperSize( self.paper_size )
        pdd = wx.PrintDialogData(self.printData)
        printer = wx.Printer(pdd)
        printout = ChecklistPrintout(self)
        if printer.Print(self, printout, True):
            self.printData = wx.PrintData( printer.GetPrintDialogData().GetPrintData() )
            self.info( u'打印完成！' )
        else:
            self.info( '' )
        printout.Destroy()


    def OnSetup( self, event ):
        dlg = SetupDialog( self )
        w, h = self.paper_size
        dlg.text_ctrl_paper_width.SetValue( str(w) )
        dlg.text_ctrl_paper_height.SetValue( str(h) )
        dlg.text_ctrl_margin_x.SetValue( str(self.margin_x) )
        dlg.text_ctrl_margin_y.SetValue( str(self.margin_y) )
        dlg.combo_box_font.SetValue( self.font )
        dlg.text_ctrl_font_size.SetValue( str(self.font_size) )
        dlg.text_ctrl_line_spacing.SetValue( str(self.line_spacing) )
        dlg.combo_box_leading_char.SetValue( unicode(self.leading_char) )
        dlg.checkbox_print_time.SetValue( self.print_time )

        e = wx.FontEnumerator()
        e.EnumerateFacenames()
        filtered_fonts = []
        for f in e.GetFacenames():
            try:
                str(f)  # 过滤掉ASCII名称的英文字体
                continue
            except:
                if f.startswith('@'):
                    continue  # 过滤掉@开头的字体（Windows下的旋转字体）
                pass
            filtered_fonts.append( f )
        dlg.combo_box_font.AppendItems( filtered_fonts )

        if dlg.ShowModal() == wx.ID_OK:
            width = float(dlg.text_ctrl_paper_width.GetValue())
            height = float(dlg.text_ctrl_paper_height.GetValue())
            margin_x = float(dlg.text_ctrl_margin_x.GetValue())
            margin_y = float(dlg.text_ctrl_margin_y.GetValue())
            font = dlg.combo_box_font.GetValue()
            font_size = int(float(dlg.text_ctrl_font_size.GetValue()))
            line_spacing = float(dlg.text_ctrl_line_spacing.GetValue())
            leading_char = dlg.combo_box_leading_char.GetValue().lstrip()
            print_time = dlg.checkbox_print_time.GetValue()

            self.paper_size = (width, height)
            self.margin_x = margin_x
            self.margin_y = margin_y
            self.font = font
            self.font_size = font_size
            self.line_spacing = line_spacing
            self.leading_char = leading_char
            self.print_time = print_time
        dlg.Destroy()

    def OnImport( self, event ):
        dlg = wx.FileDialog( self, message="Choose import txt file", defaultDir=self.config_dir, 
                defaultFile='', wildcard="Txt file (*.txt)|*.txt", style=wx.OPEN )
        if dlg.ShowModal() == wx.ID_OK:
            count = 0
            for l in open( dlg.GetPath().strip(), 'r' ).readlines():
                l = l.strip()
                if not l:
                    continue
                idx = self.list.InsertStringItem( sys.maxint, l.decode('utf8') )
                self.list.CheckItem( idx )
                count += 1 
            self.info( u'成功导出%d个项目'% count )
        event.Skip()

    def OnExport( self, event ):
        dlg = wx.FileDialog( self, message="Choose export txt file", defaultDir=self.config_dir, 
                defaultFile='', wildcard="Txt file (*.txt)|*.txt", style=wx.SAVE )
        if dlg.ShowModal() == wx.ID_OK:
            f = open( dlg.GetPath().strip(), 'w+' )
            for i in range(self.list.GetItemCount()): 
                txt = self.list.GetItemText(i)
                f.write( txt.encode('utf-8') )
                f.write( '\r\n' )
            f.close()
            self.info( u'导出至%s'% dlg.GetPath() )
        event.Skip()

    def OnMenuSwitchSheet1(self, event):
        self.frame_menubar.menu_sheet_1.Check()
        self.doSwitchSheet(0)
        event.Skip()

    def OnMenuSwitchSheet2(self, event):
        self.frame_menubar.menu_sheet_2.Check()
        self.doSwitchSheet(1)
        event.Skip()

    def OnMenuSwitchSheet3(self, event):
        self.frame_menubar.menu_sheet_3.Check()
        self.doSwitchSheet(2)
        event.Skip()

    def OnMenuSwitchSheet4(self, event):
        self.frame_menubar.menu_sheet_4.Check()
        self.doSwitchSheet(3)
        event.Skip()

    def OnMenuSwitchSheet5(self, event):
        self.frame_menubar.menu_sheet_5.Check()
        self.doSwitchSheet(4)
        event.Skip()

       
    def doUpdateCurrentSheet(self):
        checklist, checked = [], []
        for i in range(self.list.GetItemCount()):
            checklist.append( self.list.GetItemText(i) )
            if self.list.IsChecked(i):
                checked.append(i)
        self.sheets[self.sheet_num] = [checklist, checked]

    def doSwitchSheet(self, new):
        # update old
        self.doUpdateCurrentSheet() 
        # clear ctrl
        self.list.DeleteAllItems()
        # restore new
        for i in range(len(self.sheets[new][0])):
            print self.sheets[new][0][i]
            idx = self.list.InsertStringItem( sys.maxint, self.sheets[new][0][i] )
            if i in self.sheets[new][1]:
                self.list.CheckItem(idx)
        self.sheet_num = new
            
            






if __name__ == "__main__":
    gettext.install("app")
    app = wx.App(0)
    app.SetAppName( 'CheckListPrinterApp' )
    dialog_1 = MainFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
