# Eureka TEKS Lookup for Teachers · Dallas ISD Math

The teacher and campus version of the coordinators' Eureka dot chart (`MayraBT/Eureka_DOT_CHART`), Kindergarten through Grade 5.

**What's in it:** each Eureka lesson with its TEKS (● the day's TEKS on the weekly IPC, ○ a bundled standard) and its teacher-edition link; By standard (student expectation, vocabulary in English and Spanish, vertical alignment, released STAAR items with Texas percents); Teaching moves; and the Full grid.

**Left out on purpose:** IPC pacing and calendars (no Calendar view, no dates, no "Taught in" quarter filters), lessons from Q3 IPCs and calendars that teachers can't see yet, and Dallas ISD STAAR results.

Teaching moves are suggestions, not a complete list, and not a checklist for evaluating teacher instruction or performance.

## Updating
This page is generated from the coordinator version. After any change there:

```
python3 build/teacherize.py ../Eureka_DOT_CHART/index.html index.html eureka
cp -r ../Eureka_DOT_CHART/items .
```
Then test (`build/test_teacher.js`, with a local server on port 8770 serving the parent folder) and push. When the Q3 weekly IPCs are released to teachers, remove the Q3 filter in `teacherize.py` (the `only_q3` line) and rebuild.

Sources: lead4ward IQ Tool (released STAAR items and Texas percents), lead4ward TEKS Scaffold and Academic Vocabulary, 19 TAC §111 (TEKS), Eureka Math TEKS Edition and Dallas ISD 2026-27 weekly IPCs (lesson TEKS).
