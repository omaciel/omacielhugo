---

date: 2006-09-14
slug: |
  overheard-at-the-trilug-meeting
tags:
 - trilug
title: Overheard at the TriLUG meeting
---

Interesting:

> **evilaptop**: Dude, CHICKS DIG UNIX **evilaptop**: Everyone knows
> that **evilaptop**: Right?? **JasonF**: that's almost as unattractive
> as someone who scripts festival to sing "99 bottles of beer on the
> wall" at a party

Funny how a lot of the attendees were also chatting on \#trilug! hehehe

What??? You're actually interested in how to do it??? Ok, ok... The
source code was also provided! hehehehe

1.  \#!/usr/bin/python
2.  
3.  \# 99 bottles of beer on the wall.
4.  \# Inspired by (who'd of thunk) beer!
5.  
6.  from os import popen
7.  from time import sleep
8.  
9.  def printsay(sometext):
10. print sometext
11. voicehandle.write(\"(SayText \"\"+sometext+\"")")
12. \# Start talkin' you varmint!
13. voicehandle.flush()
14. \# It'd be nice if festival would tell us when it's done talking.
15. sleep(3)
16. 
17. \# 2 bottles, 1 bottle, no bottles
18. def pluralize(somenumber,sometext):
19. if ( somenumber \> 1 ):
20. retval = str(somenumber)+\" \"+sometext+\"s\"
21. 
22. if ( somenumber == 1):
23. retval = str(somenumber)+\" \"+sometext
24. 
25. if ( somenumber == 0):
26. retval = \"No \"+sometext+\"s\"
27. 
28. return retval
29. 
30. \# Open up a pipe to festival so we don't keep respawning
31. voicehandle = popen(\"festival\",\"w\")
32. 
33. \# Start with 99 bottles
34. num_bottles = 99
35. 
36. \# Do what now?
37. refrain = \"Take one down, pass it around.\"
38. 
39. \# As long as there's beer, we drink!
40. while ( num_bottles \> 0 ):
41. printsay(pluralize(num_bottles,\"bottle\")+\" of beer on the
    wall.\")
42. printsay(pluralize(num_bottles,\"bottle\")+\" of beer.\")
43. printsay(refrain)
44. num_bottles = num_bottles - 1
45. printsay(pluralize(num_bottles,\"bottle\")+\" of beer on the
    wall.\")
46. print \"----\"

**Update**:Ã‚Â  Got to meet [Daniel T
Chen](https://launchpad.net/people/crimsun) at the end of the
meeting.Ã‚Â  What a great guy!Ã‚Â  Hope to see him soon again!
