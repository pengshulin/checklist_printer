; CheckList Printer App

[Setup]
AppName=Checklist打印机 V1.0
AppVersion=1.0
DefaultDirName={pf}\ChecklistPrinter
DefaultGroupName=Checklist打印机
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
OutputDir=app_dist
OutputBaseFilename=checklist_printer_setup_v1.0

[Files]
Source: "dist\*"; DestDir: "{app}"
Source: "img\*"; DestDir: "{app}\img"

[Icons]
Name: "{group}\Checklist打印机"; Filename: "{app}\CheckListPrinterApp.exe"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"
