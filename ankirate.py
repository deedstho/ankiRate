# Tom Deeds
# GNU public license

rating_shortcuts = {

'1': {'tags': 'easy'},
'2': {'tags': 'medium'},
'3': {'tags': 'hard'}

}

from aqt import mw
from aqt.utils import showInfo, getTag, tooltip
from aqt.qt import *
from aqt.reviewer import Reviewer


def addTags(note, tagString):
    tagList = mw.col.tags.split(tagString)
    for tag in tagList:
        note.addTag(tag)
    note.flush()

#replace _keyHandler in reviewer.py to add a keybinding
def newKeyHandler(self, evt): 
    key = unicode(evt.text())
    note = mw.reviewer.card.note()
    
    if key in rating_shortcuts:
        if 'bury' in rating_shortcuts[key] and rating_shortcuts[key]['bury']:
            mw.chekcpoint("Add Tags and Bury")
            addTags(note, rating_shortcuts[key]['tags'])
            mw.col.sched.buryNote(note.id)
            mw.reset()
            tooltip('Added tag(s) "%s" and buried note'
                    % rating_shortcuts[key]['tags'])
        else:
            mw.checkpoint(_("Add Tags"))
            addTags(note, rating_shortcuts[key]['tags'])
            tooltip('Added tags(s) "%s"' % rating_shortcuts[key]['tags'])
    else:
        origKeyHandler(self,evt)

origKeyHandler = Reviewer._keyHandler
Reviewer._keyHandler = newKeyHandler
