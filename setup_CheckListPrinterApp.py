#coding:utf-8
from distutils.core import setup
import py2exe

setup(
    name=u'Checklist Printer',
    version='1.1',
    description='print checklists using thermo-printer',
    author='Peng Shulin',
    windows = [
        {
            "script": "CheckListPrinterApp.py",
            "icon_resources": [(1, 'img\\checklist.ico')],
        }
    ],
    options = {
        "py2exe": {
            "compressed": 1,
            "optimize": 2,
            "dist_dir": "dist",
        }
    },
)
