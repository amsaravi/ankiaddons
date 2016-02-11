# Tag Toggler 1.1.1 (2016-02-06)
# Copyright: Don March <don@ohspite.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
# Tag Toggler is an Anki 2 add-on for quickly adding tags while reviewing.

# Based in part on Quick Tagging by Cayenne Boyer
# (https://github.com/cayennes/Quick_Tagging)

########################################
## CONFIGURATION OPTIONS

## There are two variables to edit--tag_dialog_shortcut and tag_shortcuts.

## Lines with a leading `#` are comments and have no effect.  Lines with a
## single `#` are code examples that you can use by removing the leading `#`.

## You can overwrite some previously existing shortcuts, but it's easiest if
## you pick keys that are unused or that are shortcuts when reviewing cards
## only (defined in Reviewer._keyHandler).  Some keys (such as 'a' for Add or
## 'b' for Browse are defined elsewhere; the effect of adding Tag Toggle
## functionality to these keys is undefined.

## Change `tag_dialog_shortcut` to the key you want to open a dialog to
## quickly edit tags.  Set `tag_dialog_shortcut = None` to disable the
## shortcut.

tag_dialog_shortcut = 't'
# tag_dialog_shortcut = None

## Add items to the `tag_shortcuts` dict to create shortcuts that modify
## tags. The dict keys are the key for the keyboard shortcut, and each should
## refer to a dict to specify the command.  Valid keys in that dict are
## 'tags', 'action', and 'after'.
##
## 'tags': Specify tags to modify in a string; separate multiple tags in the
## string with spaces.
##
## 'action': How to modify tags; options are 'add' (the default), 'delete',
## and 'toggle' (delete tag if present, add it if absent).
##
## 'after': What to do to a card after modifying the tags; options are
## 'bury-card', 'bury-note', 'suspend-card' or 'suspend-note'.  Also 'suspend'
## and 'bury, which are the same as the '-note' versions.
##
## Example keybinding to add tags:
##    'h': {'tags': 'hard'}
## 'add' is the default action, so this is the same:
##    'h': {'tags': 'hard', 'action': 'add'}
## Modify multiple tags by separating them with spaces:
##    'h': {'tags': 'hard marked'}
## Keybinding to delete tags (if they are present):
##    'h': {'tags': 'hard marked', 'action': 'delete'}
## Keybinding to toggle tag:
##    'H': {'tags': 'hard', 'action': 'toggle'}
## Bury a card after adding a tag:
##    'T': {'tags': 'TODO', 'after': 'bury-card'}
## Suspend a note after adding a tag:
##    'A': {'tags': 'easy', 'after': 'suspend-note'}

tag_shortcuts = {
    '5': {'tags': 'Conflict', 'action': 'toggle'},
    '.': {'tags': '',  'after': 'bury'},
    'm': {'tags': 'marked',  'action': 'toggle'}
#    'H': {'tags': 'hard', 'action': 'toggle'},
#    '0': {'tags': 'Hard', 'action': 'add'},
#    'T': {'tags': 'TODO', 'after': 'bury-note'},
#    'A': {'tags': 'easy', 'after': 'suspend-card'},
}

## END CONFIGURATION OPTIONS
########################################

# Testing:

# As far as I know, there is no easy way to automatically test this.  Here are
# some keybindings to add to `tag_shortcuts` that cover most cases.  (Be sure
# to test `tag_dialog_shortcut` as well).

# The first two should cause an graceful error when Anki is starting up.
    # 'z': {'tags': 'test-a', 'action': 'blah'},
    # 'Z': {'tags': 'test-a', 'after': 'blah'},
    # 'z': {'tags': 'test-a'},
    # 'Z': {'tags': 'test-b'},
    # 'x': {'tags': 'test-a', 'action': 'delete'},
    # 'X': {'tags': 'test-b', 'action': 'delete'},
    # 'c': {'tags': 'test-a test-b'},
    # 'q': {'tags': 'test-a test-b', 'action': 'delete'},
    # 'Q': {'tags': 'test-a test-b', 'action': 'toggle'},
    # 'r': {'tags': 'test-a test-b', 'after': 'bury-note'},
    # 'R': {'tags': 'test-a test-b', 'after': 'suspend-note'},
    # 's': {'tags': 'test-a test-b', 'after': 'bury-card'},
    # 'S': {'tags': 'test-a test-b', 'after': 'suspend-card'},


from aqt import mw
from aqt.utils import getTag, tooltip, showInfo
from aqt.reviewer import Reviewer
from anki.hooks import wrap


def tagKeyHandler(self, event, _old):
    """Wrap default _keyHandler with new keybindings."""
    key = unicode(event.text())
    note = mw.reviewer.card.note()
    if tag_dialog_shortcut and key in tag_dialog_shortcut:
        mw.checkpoint(_("Edit Tags"))
        import win32api
        win32api.LoadKeyboardLayout('00000409',1) # to switch to english
        edit_tag_dialog(note)
    elif key in tag_shortcuts:
        binding = tag_shortcuts[key]
        if 'action' not in binding:
            binding['action'] = 'add'

        if ('after' in binding and
            binding['after'] in ['suspend', 'suspend-note']):
            mw.checkpoint("Edit Tags and Suspend Note")
            tooltip_message = 'Suspended note and edited tags: {}'
            self.mw.col.sched.suspendCards(
                [card.id for card in self.card.note().cards()])
        elif 'after' in binding and binding['after'] in ['bury', 'bury-note']:
            mw.checkpoint("Edit Tags and Bury Note")
            tooltip_message = 'Buried note and edited tags: {}'
            mw.col.sched.buryNote(note.id)
        elif 'after' in binding and binding['after'] == 'suspend-card':
            mw.checkpoint("Edit Tags and Suspend Card")
            tooltip_message = 'Suspended card and edited tags: {}'
            self.mw.col.sched.suspendCards([self.card.id])
        elif 'after' in binding and binding['after'] == 'bury-card':
            mw.checkpoint("Edit Tags and Bury Card")
            tooltip_message = 'Buried card and edited tags: {}'
            mw.col.sched.buryCards([self.card.id])
        else:
            mw.checkpoint(_("edit Tags"))
            tooltip_message = 'Edited tags: {}'
        tag_edits = edit_note_tags(note, binding['tags'], binding['action'])   
        if 'after' in binding:
            mw.reset()
        else:
            redraw_card()
        tooltip(tooltip_message.format(tag_edits))
    else:
        _old(self, event)


def edit_tag_dialog(note):
    """Prompt for tags and add the results to note."""
    prompt = _("Edit tag list:")
    (tag_string, dialog_status) = getTag(mw, mw.col, prompt, default=note.stringTags())
    if dialog_status != 0:  # means "Cancel"
        note.setTagsFromStr(tag_string)
        note.flush()
        redraw_card()
        tooltip('Tags set to: "{}"'.format(tag_string))

def redraw_card():
    """Refresh the card in case {{Tags}} is in the template."""
    # TODO It would be better to do this without resetting the state.
    r = mw.reviewer
    try:
        r.card.load()
    except:
        # card was removed by clayout
        pass
    else:
        mw.reviewer.cardQueue.append(mw.reviewer.card)
    mw.moveToState("review")


def edit_note_tags(note, tags, action='add'):
    """Apply action to each space separated tag in the string `tags`."""
    tag_list = mw.col.tags.split(tags)
    additions = []
    deletions = []
    for tag in tag_list:
        if action == 'delete':
            if note.hasTag(tag):
                note.delTag(tag)
                deletions.append(tag)
        elif action == 'toggle':
            if note.hasTag(tag):
                note.delTag(tag)
                deletions.append(tag)
            else:
                note.addTag(tag)
                additions.append(tag)
        else:  # action == 'add'
            if not note.hasTag(tag):
                note.addTag(tag)
                additions.append(tag)
    note.flush()

    messages = []
    if additions:
        messages.append("added: \"{}\"".format(" ".join(additions)))
    if deletions:
        messages.append("removed: \"{}\"".format(" ".join(deletions)))
    if messages:
        return "\n".join(messages)
    else:
        return "(no changes)"


def shortcuts_are_okay():
    error_message = (
        "The Tag Toggle add-on will not be started.\n\n"
        "Check the configuration for an undefined '{}' "
        "value '{}' in tag_shortcuts:\n\n"
        "{}")

    def check_command(command, command_type, options):
        if command_type in command:
            value = command[command_type]
            if value not in options:
                showInfo(error_message.format(command_type, value, command))
                return False
        return True

    for shortcut in tag_shortcuts:
        command = tag_shortcuts[shortcut]
        if not check_command(command, 'action', ['add', 'delete', 'toggle']):
            return False
        if not check_command(command, 'after',
                             ['bury', 'bury-card', 'bury-note',
                              'suspend', 'suspend-card', 'suspend-note']):
            return False

    return True


if shortcuts_are_okay():
    Reviewer._keyHandler = wrap(Reviewer._keyHandler, tagKeyHandler, "around")
