from time import sleep
import wx
import eel
import pandas as pd

eel.init("web")

selected_files = []


@eel.expose
def dialogBox(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE | wx.STAY_ON_TOP | wx.RESIZE_BORDER
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard,
                           style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPaths()
    else:
        path = None
    dialog.Destroy()
    return path


@eel.expose
def save_py(paths):
    selected_files = []
    selected_files = paths[0]
    merge_files(selected_files)


def merge_files(file_list):
    excl_list = []
    for file in file_list:
        excl_list.append(pd.read_excel(file))

    # merged excel file.
    excl_merged = pd.DataFrame()
    for excl_file in excl_list:

        excl_merged = excl_merged.append(
            excl_file, ignore_index=True)
    excl_merged.to_excel('master.xlsx', index=False)


eel.start("index.html", mode='chrome', size=(700, 400))
