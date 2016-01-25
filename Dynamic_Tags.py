# -*- coding: utf-8 -*-
# Copyright: itraveller, 2013 <itraveller@mail.ru>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html


'''
This script is an add-on for Anki 2.0.11

Synopsis:

Dynamic tag - the name of special tokens that are used on the preliminary stage
of rendering cards. This system is designed to access the program variables and
is a superstructure over HTML and javascript. The program already has built 
structures of this type (links to note fields, special fields, template 
functions). From a programming standpoint, this approach is known as 
pre-processing and these tokens - as preprocessor directives.

The add-on includes three groups of dynamic tags:

1) Anki variable dynamic tags - group of tags, which return values ​​of the
   corresponding program variables.
2) User-defined dynamic tags - group of tags, which return the result of 
   (the user-defined) functional processing of the program data.
3) User-defined macros - group of tags, which already provide complete 
   solutions for the processing of data presented in the previous groups.

Dynamic tags can be used as variables for javascript, as ready macros or just
as snipetts to simplify card templates.

Notes:

1) If you use the mobile versions of the program, the structure 
   'Platform-Specific CSS (see manual) + .class {display: none;}' will 
   help get rid of unwanted messages about unused fields.
2) Most of the presented tags are used for debugging purposes, so you should 
   not need to burden by them the card images, as it diverts attention from 
   the main content.
3) Content of dynamic tags can be easily modified with styles like any other 
   element of HTML.

Tag descriptions can be found in the relevant function definitions.

To apply a dynamic tag just paste into a card template this expression: 
{{@tag_name}}

'''

import time
from anki.hooks import addHook
from anki.utils import intTime


def addFields(fields, model, data, col):

    # test values ​​for non-real card
    class test:
        ivl, factor, lapses, type, reps, mod, due, odue, odid, queue = \
        1, 2500, 1, 1, 1, 0, 0, 0, 0 ,0
    # try to get the card data
    try: 
        val = col.getCard(data[0])
    except TypeError: 
        val = test
        
    # Anki variable dynamic tags:
    fields['@interval'] = str(val.ivl)
    fields['@factor'] = str(float(val.factor)/1000)
    fields['@lapses'] = str(val.lapses)
    fields['@type'] = str(val.type)
    fields['@reps'] = str(val.reps)
    fields['@mod'] = str(val.mod)
    fields['@due'] = str(val.due)
    fields['@queue'] = str(val.queue)
    
    # User-defined dynamic tags:
    fields['@trend'] = str(int(_trend(data, col)))
    fields['@leech'] = str(int(_leech(data, col)))
    fields['@tags'] = str(_tags(data))
    fields['@lifetime'] = str(_lifetime(data, col))
    fields['@tottime'] = str(_tottime(data, col))
    fields['@rating'] = str(_rating(data, col))
    fields['@avgrating'] = str(_avgrating(data, col))
    fields['@pcorrect'] = str(_pcorrect(data, col))
    fields['@anstime'] = str(_anstime(data, col))
    fields['@revfreq'] = str(_revfreq(data, col))
    fields['@overdue'] = str(_overdue(val, col.crt))
    fields['@birthday'] = _birthday(data[0])
    
    # User-defined macros:
    fields['@trend!'] = _trend_mac(_trend(data, col))
    fields['@leech!'] = _leech_mac(_leech(data, col))
    fields['@temp!'] = _temp_mac(val.ivl)
    fields['@hard!'] = _hard_mac(val.factor)
    fields['@type!'] = _type_mac(val.type)
    fields['@mod!'] = _mod_mac(val.mod)
    
    return fields

# Tags block:
##############################################################################
    
def _trend(data, col, steps=3, ignore_relearn='no'):
    "Indicator of bad trend - three consecutive failures." 
    subst = 'and type != 2' if ignore_relearn == 'yes' else ''
    item = col.db.scalar("select count(*) from (select * from revlog where \
cid = ? {0} order by id desc limit {1}) where ease = 1".format(subst, steps), \
data[0])
    return item == steps    
           
def _leech(data, col, steps=10, days=21):
    "Modified indicator of leeches - the card interval remains less than the \
'days' over the 'steps' of reviews."
    item = col.db.scalar("select count(*) from (select * from revlog where \
cid = ? order by id desc limit {0}) where ivl < {1}".format(steps, days), \
data[0])
    return item == steps
       
def _tags(data):
    "Presence indicator of the user-specified standard tags."
    tags=set(data[5].split())
    tagStr=["<kbd onclick='py.link(\"tagclick_%s\")'>%s</kbd>" % (tag, tag) for tag in tags]
    return "".join(tagStr)

       
def _lifetime(data, col):
    "The Number of days elapsed since the first reviewing the card."
    item = col.db.scalar("select min(id) from revlog where cid = ?", data[0])
    return round((time.time()-item/1000.0)/86400.0, 1) if item else 0
    
def _tottime(data, col):
    "Total Number of minutes spent on reviewing the card."
    item = col.db.scalar("select sum(time) from revlog where cid = ?", data[0])
    return round(item / 60000.0, 1) if item else 0
    
def _rating(data, col):
    "The latest rating of the card in the 'review' status."
    item = col.db.scalar("select ease from revlog where cid = ? and type = 1 \
order by id desc", data[0])
    return item if item else 0
        
def _avgrating(data, col):
    "The average rating of the card in the 'review' status."
    item = col.db.scalar("select avg(ease) from revlog where cid = ? and \
type = 1", data[0])
    return round(item, 1) if item else 0

def _pcorrect(data, col, steps=5):
    "The percentage of positive answer to the card over the 'steps' of \
reviews in the 'review' status (over all if steps=0)."
    subst = 'limit {0}'.format(steps) if steps else ''
    item_n = col.db.scalar("select count(*) from (select * from revlog \
where cid = ? and type = 1 order by id desc {0}) where ease = 1".format\
(subst), data[0])
    item_t = col.db.scalar("select count(*) from (select * from revlog \
where cid = ? and type = 1 order by id desc {0})".format(subst), data[0])
    return round((item_t-item_n)*100.0/item_t, 1) if item_t else 0
    
def _anstime(data, col):
    "The average answer time to the card in the 'review' status."
    item = col.db.scalar("select avg(time) from revlog where cid = ? \
and type = 1", data[0])
    return round(item / 1000.0, 1) if item else 0
    
def _revfreq(data, col, days=30):
    "The Number of reviews over the last 'days' days to the card in the \
'review' status." 
    item = col.db.scalar("select count(*) from revlog where cid = ? \
and type = 1 and id > {0}".format((time.time()-86400*days)*1000), data[0])
    return item if item else 0

def _overdue(val, crt):
    "The overdue days for review cards and zero in other cases"
    due = val.odue if val.odid else val.due
    overdays = int((time.time() - crt)//86400) - due
    return overdays if val.queue == 2 else 0
    
def _birthday(cid):
    "The card creation date."
    return time.strftime("%Y-%m-%d", time.localtime(cid/1000))
        
    
# Macros block:
##############################################################################
      
def _trend_mac(ind):
    "Dark yellow star in the upper right corner for cards with a bad trend." 
    return '<div style="float:right;"><font color="#ffbb00">&#9733;\
</font></div>' if ind else ''
        
def _leech_mac(ind):
    "Red star in the upper right corner for the modified indicator of leeches."    
    return '<div style="float:right;"><font color="red">&#9733;\
</font></div>' if ind else ''
        
def _temp_mac(ivl):
    "Red hourglass in the upper right corner of the 'mature' card \
(often useful when working with temporary decks)."    
    return '<div style="float:right;"><font color="green">&#8987;</font>\
</div>' if ivl > 21 else ''
        
def _hard_mac(factor, key=1.8):
    "Red exclamation mark in the upper right corner of the card with a low \
(<'key') coefficient of ease."
    return '<div style="float:right;"><font color="red">&#33;</font>\
</div>' if factor < key*1000 else ''

def _type_mac(type):
    "Lexical indicator of the card type."
    types = {0:'new', 1:'learn', 2:'review'}    
    return types[type]
        
def _mod_mac(mod):
    "Last modification time of the card in the comfortable notation." 
    return time.strftime(_("<b>%Y-%m-%d</b> @ %H:%M"), time.localtime(mod))
    

addHook('mungeFields', addFields)


