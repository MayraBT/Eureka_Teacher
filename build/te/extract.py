"""Per-lesson evidence for the dot chart: objective, concept development (no fluency), problem set and exit ticket text.
usage: extract.py G3_M2_L05_TE.pdf -> prints compact text"""
import sys, re, subprocess
f = sys.argv[1]; lim = int(sys.argv[2]) if len(sys.argv) > 2 else 2500
t = subprocess.run(['pdftotext', f, '-'], capture_output=True, text=True).stdout
t = re.sub(r'A STORY OF UNITS – TEKS EDITION|© Great Minds PBC TEKS Edition \||greatminds.org/Texas|​', '', t)
def sec(a, b):
    m = re.search(a + r'(.*?)(?:' + b + ')', t, re.S); return re.sub(r'\s+', ' ', m.group(1) or '').strip() if m else ''
obj = sec(r'Objective:', r'Suggested Lesson Structure')
cd = sec(r'\nConcept Development \(\d+ minutes\)', r'\nProblem Set \(\d+ minutes\)')
ap = sec(r'\nApplication Problem \(\d+ minutes\)', r'\n(?:Concept Development|Fluency Practice) \(\d+')
ps = sec(r'Lesson \d+(?:-\d)? Problem Set\n', r'Lesson \d+(?:-\d)? Exit Ticket|\nName\s')
et = sec(r'Lesson \d+(?:-\d)? Exit Ticket\n', r'Lesson \d+(?:-\d)? Homework|$')
print('OBJ:', obj)
print('APP:', ap[:400])
print('CD:', cd[:lim])
print('PS:', ps[:900])
if not et:
    import pypdf
    for p in pypdf.PdfReader(f).pages:
        x = re.sub(r'\s+', ' ', p.extract_text() or '')
        if 'Name' in x and 'Date' in x and re.search(r'Exit Ticket', x) and 'Student Debrief' not in x:
            et = x[x.find('Exit Ticket'):]; break
print('ET:', et[:900])
