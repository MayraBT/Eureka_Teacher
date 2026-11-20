# Eureka TEKS Lookup for Teachers · Dallas ISD Math

The teacher and campus version of the coordinators' Eureka TEKS chart (`MayraBT/Eureka_DOT_CHART`), Kindergarten through Grade 5.

**What's in it:** every Eureka Math TEKS Edition lesson (supplemental lessons and lessons the district calendar skips included) with the TEKS its Teacher Edition lists for it, and a link to that lesson's Teacher Edition pages; By standard (student expectation, vocabulary in English and Spanish, vertical alignment, released STAAR items with Texas percents); Teaching moves; and the Full grid.

**Grades 3–5 dot chart:** each lesson was read in its Teacher Edition (Concept Development, Problem Set and Exit Ticket; fluency warm-ups not counted). ● means the lesson's Exit Ticket assesses the TEKS; ○ means students use it in the lesson but the Exit Ticket does not assess it. A "Why" line under each lesson gives the evidence. Judgments are in `build/dot_marks/` (one file per grade and module), reviewed by the Grade 3–5 coordinators. Kindergarten–Grade 2 still show the TEKS each Teacher Edition topic lists.

**Independent of the IPC:** lesson TEKS come only from the Teacher Editions (each module's Overview of Module Topics and Lesson Objectives, and the Supplement Overview). No IPC pacing, calendars, dates or Dallas ISD STAAR results. Built with `TE_ONLY=1 DOTS=1 python3 build_data.py && TE_ONLY=1 python3 assemble.py`, then `teacherize.py out/index_te.html index.html eureka` and `te_teacher.py index.html --dots`.

Teaching moves are suggestions, not a complete list, and not a checklist for evaluating teacher instruction or performance.

## Updating
This page is generated from the coordinator version. After any change there:

```
python3 build/teacherize.py ../Eureka_DOT_CHART/index.html index.html eureka
cp -r ../Eureka_DOT_CHART/items .
```
Then test (`build/test_teacher.js`, with a local server on port 8770 serving the parent folder) and push.

Sources: lead4ward IQ Tool (released STAAR items and Texas percents), lead4ward TEKS Scaffold and Academic Vocabulary, 19 TAC §111 (TEKS), Eureka Math TEKS Edition Teacher Editions (lessons and lesson TEKS). Lesson PDFs: Math Department (All) › Eureka individual lesson files › Grade › Module.
