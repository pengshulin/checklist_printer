; CheckList Printer App

[Setup]
AppName=Checklist printer V1.0
AppVersion=1.0
DefaultDirName={pf}\ChecklistPrinter
DefaultGroupName=Checklist printer
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
OutputDir=app_dist
OutputBaseFilename=checklist_printer_setup_v1.0

[Files]
Source: "dist\*"; DestDir: "{app}"
Source: "img\*"; DestDir: "{app}\img"
Source: "locale\zh_CN\LC_MESSAGES\*"; DestDir: "{app}\locale\zh_CN\LC_MESSAGES"

[Icons]
Name: "{group}\Checklist printer"; Filename: "{app}\CheckListPrinterApp.exe"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"
