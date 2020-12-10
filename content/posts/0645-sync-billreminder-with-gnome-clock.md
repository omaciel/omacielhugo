---

date: "2007-09-13 23:30"
slug: |
  sync-billreminder-with-gnome-clock
tags:
 - english
title: Sync BillReminder with GNOME clock
---

In an attempt to integrate [BillReminder](http://billreminder.sf.net) to
the GNOME clock, I set out to learn about the
[evolution-python](http://www.conduit-project.org/wiki/evolution-python)
lib. After messing around for a bit, it became obvious to me that every
event added to the generic .evolution/tasks/local/system/calendar.ics
file gets automatically synched with GNOME clock. The thing is, I want
to create my own separate calendar file, so to not get it mixed with the
generic one. The code below does just that, but... it doesn't show up in
GNOME clock!

I was wondering if anyone out there knows how to achieve my objective?
Is there a proper place where calendar events files need to be saved?
Any feedback will be appreciated.

------------------------------------------------------------------------

\-*- coding: utf-8 -*-=====================

import sys

import evolution import vobject import datetime import time

class Evolutionizer(object):

# Uses the default calendar

source = "/home/omaciel/.evolution/calendar/local/billreminder/"

def add_event(self, summary, start=None, end=None, description=None):
""" Add a new event to the main calendar, and return the uid for the
event. """ vcal = self.\_create_vcal(summary, start, end, description)
ecalcomp = evolution.ECalComponent(evolution.CAL_COMPONENT_EVENT,
vcal.vevent.serialize())

return self.calendar.add_object(ecalcomp)

def \_create_vcal(self, summary, start=None, end=None,
description=None): cal = vobject.iCalendar() cal.add('vevent')

# This is what gets displayed in the calendar

cal.vevent.add('summary').value = summary

# Defaults to today's date if none is provided

if not start: start = datetime.datetime.today()

# Defaults to start if none is provided

if not end: end = start

# Set start and end date/time

cal.vevent.add('dtstart').value = start cal.vevent.add('dtend').value =
end

# Set a more detailed description if provided

if description: cal.vevent.add('description').value = description

return cal

def **init**(self): self.calendar =
evolution.open_calendar_source_new_with_absolute_uri('Bills',
self.source, evolution.CAL_SOURCE_TYPE_EVENT)

if **name** == "**main**": a = Evolutionizer() a.add_event("TriLUG
tonight")
