"""Make the Grades 3-5 dot chart review page from the teacher build.
usage: review_page.py IN.html OUT.html"""
import sys, re
s = open(sys.argv[1]).read()
R = [
    ('module focus standard</span>', 'assessed on the Exit Ticket</span>'),
    ('also listed for the topic</span>', 'used in the lesson, not assessed</span>'),
    ('<option value="gk">Kindergarten', ''), ('<option value="g1">Grade 1', ''), ('<option value="g2">Grade 2', ''),
    ("if(!COURSES[ck]) ck=", "if(!COURSES[ck]||!/^g[345]$/.test(ck)) ck="),
]
for a, b in R:
    assert a in s, a
    s = s.replace(a, b)
s = re.sub(r'(<select id="courseSel"[^>]*>)(</option>)+', r'\1', s)
s = s.replace('<option value="gk"></option>', '').replace('<option value="g1"></option>', '').replace('<option value="g2"></option>', '')
banner = ('<div id="dotDraft" style="background:#fff8e1;border-bottom:2px solid #f2b705;color:#1c2330;'
          'font:14px/1.45 system-ui,-apple-system,Segoe UI,sans-serif;padding:10px 16px">'
          '<b>Draft dot chart for review, Grades 3–5.</b> Each lesson was read in its Teacher Edition. '
          '<b>●</b> the lesson’s Exit Ticket assesses the TEKS. <b>○</b> students use it in the lesson, but the Exit Ticket does not assess it. '
          'Fluency warm-ups are not counted. Open <b>By lesson</b> to see a “Why” line under each lesson; send corrections by grade, module and lesson.</div>')
s = re.sub(r'(<body[^>]*>)', r'\1' + banner, s, count=1)
open(sys.argv[2], 'w').write(s)
print('ok', len(s))
