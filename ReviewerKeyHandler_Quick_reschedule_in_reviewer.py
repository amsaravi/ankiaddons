# Date:     January 27, 2016
# Author:   Benjamin Gray
# File:     Quick_Reschedule.py
# Purpose:  Quickly reschedule cards in anki to a user specified interval using sched.reschedCards()
# Version:  0.2

reschedule_shortcut = '-'
#reschedule_four_weeks = 'm'
reschedule_tomorrow = '+'
edit_occupyImage = u"oخ"
edit_rtl = u"rRق"
key_add_note = u"nNد"
key_english = u"ث"
rtl_fileds_arr=[u"Back", u"Footer", u"extra", u"عقب"]

from image_occlusion_2.image_occlusion import ImageOcc_Add
from aqt import mw
from aqt.utils import tooltip, getText, showInfo
from aqt.reviewer import Reviewer
import re
from MyTag_Toggler import redraw_card
from aqt.utils import getText

# prompt for new interval, and set it

def promptNewInterval(self, card):

    dayString = getText("Number of days until next review: ")
    try:
        days = int(dayString[0])
    except ValueError:
        return

    if days > 0:
        mw.col.sched.reschedCards( [card.id], days, days )
        tooltip('Rescheduled for review in ' + str(days) + ' days'  )
        mw.reset()

# replace _keyHandler in reviewer.py to add a keybinding

def newKeyHandler(self, evt):
    key = unicode(evt.text())
    card = mw.reviewer.card
    if not key:
        origKeyHandler(self, evt)
        return
    elif key == reschedule_shortcut:
        mw.checkpoint(_("Reschedule card"))
        promptNewInterval(self, card)
        #    elif key == reschedule_four_weeks:
        #mw.checkpoint(_("Reschedule card"))
        #mw.col.sched.reschedCards( [card.id], 21, 42 )
        #tooltip('Rescheduled for review in 3-6 weeks'  )
        #mw.reset()
    elif key == reschedule_tomorrow:
        mw.checkpoint(_("Reschedule card"))
        mw.col.sched.reschedCards( [card.id], 1, 1 )
        tooltip('Rescheduled for review tomorrow'  )
        mw.reset()
    elif key in edit_occupyImage:
        patt=r"""<img.*?src=(["'])(.*?)\1"""
        pattern = re.compile(patt, flags=re.I|re.M|re.S)
        note = mw.reviewer.card.note()
        field_names = [item[0] for item in note.items()]
        imagename=""
        field_name=""
        valid_ext=False
        for fldName in field_names:
            m = pattern.search(note[fldName])
            if(m):
                imagename = m.group(2)
                valid_ext = imagename.endswith((".jpg",".jpeg",".gif",".png"))
                if(valid_ext):
                    field_name=fldName
                    break
        if(valid_ext):
            try:
                mw.reviewer.image_occlusion
            except:
                mw.reviewer.image_occlusion = ImageOcc_Add(mw.reviewer)
                
            mw.reviewer.image_occlusion.add_notes(field_name)
    elif key in edit_rtl:
        mw.checkpoint(_("Made RTL"))
        note = mw.reviewer.card.note()
        for item in note.items():
            if item[0] in rtl_fileds_arr:
                note[item[0]] = "<div class='f r'>" + note[item[0]] + "</div>"
                note.flush()
                redraw_card()
    elif key in key_add_note :
        if key!="N":
            import win32api
            win32api.LoadKeyboardLayout('00000429',1) # to switch to english
        text, ok = getText("your note on this card?")
        if ok:
            note = mw.reviewer.card.note()
            for item in note.items():
                if item[0] in rtl_fileds_arr:
                    note[item[0]] = note[item[0]] + "<p class=\"%(className)s\">%(text)s</p>" % \
                        {'className':"floatLeft" if key=="N" else "f r",
                        'text':text}
                    note.flush()
                    redraw_card()
    elif key in key_english:
        import win32api
        win32api.LoadKeyboardLayout('00000409',1) # to switch to english
    else:
        origKeyHandler(self, evt)

origKeyHandler = Reviewer._keyHandler
Reviewer._keyHandler = newKeyHandler

