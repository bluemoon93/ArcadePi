#!/usr/bin/python3

import subprocess
import os
from os import listdir
from os.path import isfile, join
from tkinter import *
from Gui import Application


def default_keymap_dict():
    print("Building default key mod map")

    # if error, feed default xmodmap.dict into system with xmodmap
    with open("xmodmap.dict") as f:
        for line in f:
            subprocess.Popen(["xmodmap", "-e", line.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)

    # build correct dictionary
    return {'XF86AudioPlay': '215', 'Katakana': '98', 'KP_Equal': '125', 'Pause': '127',
            'XF86AudioMedia': '234', 'h': '43', 'dead_acute': '35', 'x': '53', 'Shift_L': '50', '7': '16',
            'KP_End': '87', 'apostrophe': '20', 'g': '42', 'XF86Documents': '243', 'XF86Search': '225', '3': '12',
            'Menu': '135', 'f': '41', 'j': '44', 's': '39', 'period': '60', 'q': '24', 'plusminus': '126',
            'XF86AudioMute': '121', 'XF86MyComputer': '165', 'Prior': '112', 'KP_Subtract': '82',
            'XF86Copy': '141', 'XF86Back': '166', 'KP_Home': '79', 'comma': '59', '1': '10',
            'XF86AudioPrev': '173', 'Hiragana_Katakana': '101', 'Hiragana': '99', 'XF86Launch2': '157',
            'XF86Close': '214', 'b': '56', 'XF86Forward': '167', 'Insert': '118', 'XF86Cut': '145', 'i': '31',
            'XF86RotateWindows': '161', 'XF86AudioRecord': '175', 'XF86AudioNext': '171', 'Print': '218',
            'XF86AudioForward': '216', 'XF86Sleep': '150', 'v': '55', 'Next': '117', 'Mode_switch': '203',
            'XF86Launch5': '192', 'XF86Eject': '170', 'NoSymbol': '207', 'XF86LaunchA': '128', 'y': '29',
            'parenleft': '187', 'XF86Explorer': '152', 'XF86Launch3': '210', 'KP_Begin': '84', 'KP_Right': '85',
            'Right': '114', 'XF86Xfer': '155', 'm': '58', '9': '18', 'XF86Launch4': '211', 'XF86Launch8': '195',
            'Cancel': '231', 'Tab': '23', 'XF86TaskPane': '162', 'Super_L': '133', 'KP_Multiply': '63',
            'XF86AudioMicMute': '198', '2': '11', 'Left': '113', 'Delete': '119', 'l': '46', 'KP_Enter': '104',
            'F2': '68', '4': '13', 'parenright': '188', 'F8': '74', 'Linefeed': '109', 'XF86Game': '228',
            'KP_Insert': '90', 'Hangul_Hanja': '131', 'XF86Display': '235', 'KP_Up': '80', 'XF86LaunchB': '212',
            'XF86Shop': '229', 'Muhenkan': '102', 'z': '52', 'XF86ScrollUp': '185', 'minus': '61',
            'XF86ScrollDown': '186', 'KP_Add': '86', 'Return': '36', 'XF86Save': '242', 'XF86Launch6': '193',
            'XF86AudioRewind': '176', 'XF86Open': '142', 'XF86AudioLowerVolume': '122', 'masculine': '48',
            'Home': '110', 'XF86WebCam': '220', 'XF86Suspend': '213', 'XF86WWW': '158', 'XF86TouchpadOff': '201',
            'F11': '95', 'k': '45', 'backslash': '49', 'XF86Launch7': '194', 'XF86WakeUp': '151',
            'XF86Battery': '244', 'KP_Next': '89', 'XF86MailForward': '241', 'XF86KbdBrightnessUp': '238',
            'Alt_L': '64', 'XF86Send': '239', 'XF86KbdLightOnOff': '236', 'XF86WLAN': '246', 'KP_Divide': '106',
            'XF86Mail': '223', 'XF86MonBrightnessDown': '232', 'u': '30', 'XF86MonBrightnessUp': '233',
            'XF86AudioStop': '174', 'XF86Messenger': '224', 'Help': '146', 'Shift_R': '62', 'less': '94',
            'XF86TouchpadToggle': '199', 'F12': '96', 'XF86Finance': '227', 'n': '57', 'XF86ScreenSaver': '160',
            'space': '65', 'XF86KbdBrightnessDown': '237', 'SunFront': '140', 'plus': '34', 'e': '26', 'F6': '72',
            '8': '17', 'Caps_Lock': '66', 'KP_Down': '88', 'Redo': '190', 'KP_Delete': '91', 'KP_Left': '83',
            'KP_Prior': '81', 'XF86TouchpadOn': '200', 'Down': '116', 'F1': '67', '5': '14', 'End': '115',
            'F7': '73', 'XF86Reload': '181', 'XF86Bluetooth': '245', 'a': '38', 'Control_L': '37', 'o': '32',
            'r': '27', 'F9': '75', 'XF86Launch9': '196', 'dead_tilde': '51', 'XF86Phone': '177', 'Hangul': '130',
            'Henkan_Mode': '100', 'F5': '71', 'XF86Go': '226', 'Control_R': '105', 'ISO_Level3_Shift': '108',
            'BackSpace': '22', 'SunProps': '138', 'XF86Favorites': '164', 'XF86Calculator': '148',
            'XF86AudioPause': '209', 'Up': '111', 'w': '25', 'F4': '70', 'XF86Reply': '240', 'Num_Lock': '77',
            'F10': '76', 'Super_R': '134', '6': '15', 'Undo': '139', 'XF86Launch1': '156', 'XF86Tools': '191',
            'Scroll_Lock': '78', 'KP_Decimal': '129', 'c': '54', '0': '19', 'ccedilla': '47',
            'XF86HomePage': '180', 'XF86DOS': '159', 'p': '33', 'XF86Paste': '143', 'F3': '69',
            'XF86MenuKB': '147', 'XF86PowerOff': '124', 't': '28', 'XF86AudioRaiseVolume': '123', 'd': '40',
            'guillemotleft': '21', 'Escape': '9', 'Find': '144', 'XF86New': '189'}


print("Arcade Starting...")

# To get the mouse working, from https://ubuntuforums.org/showthread.php?t=475139
os.environ['SDL_VIDEO_X11_DGAMOUSE'] = "0"  # visible in this process + all children

# app starts, run "xmodmap -pke > xmodmap_curr.dict"
# todo output into file
p = subprocess.Popen(["xmodmap", "-pke"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE)

# check xmodmap_curr.dict and build dictionary of keys -> values; 
key_values = {}
try:
    # Read key-map
    with open("xmodmap_curr.dict") as f:
        for line in f:
            key_values[line[14:].split(" ")[0]] = line[8:11].strip()
except:
    # if error, reset to default
    key_values = default_keymap_dict()
# if no error, but incomplete key-map, reset to default
if len(key_values) < 122:
    key_values = default_keymap_dict()

games_list = [f[:-5] for f in listdir("GameConfigs") if isfile(join("GameConfigs", f))
              and f.endswith(".conf") and f != "default.conf"]
games_list.sort()

print("Loaded")
print(games_list)

root = Tk()
app = Application(root, games_list, key_values, True)
root.mainloop()
