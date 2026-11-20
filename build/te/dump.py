"""dump.py G M  -> per lesson: id, topic TEKS, objective, exit ticket, problem set (short)"""
import sys, json, subprocess, re, glob, os
g, m = sys.argv[1], sys.argv[2]
ov = json.load(open(f'/home/claude/build/ipc/te_overview/{g}_M{m}.json'))
sp = json.load(open(f'/home/claude/build/ipc/te_overview/{g}_supp.json'))
ov.update({k: v for k, v in sp.items() if k.startswith(f'M{m}.')})
def key(k):
    a = re.match(r'M\d+\.([LS])(\d+)(?:-(\d))?', k); return (int(a.group(2)), a.group(1) == 'S', int(a.group(3) or 0))
for k in sorted(ov, key=key):
    a = re.match(r'M\d+\.([LS])(\d+)(?:-(\d))?', k)
    fn = f"/home/claude/te/out/G{g}_M{m}_L{int(a.group(2)):02d}{'-'+a.group(3) if a.group(3) else ''}_TE.pdf"
    print(f"=== {k} [{ov[k]['topic']}] {','.join(ov[k]['teks'])}")
    if not os.path.exists(fn): print('  NO FILE'); continue
    out = subprocess.run(['python3', '/home/claude/dot/extract.py', fn, '10'], capture_output=True, text=True).stdout
    d = dict(re.findall(r'^(OBJ|APP|CD|PS|ET): ?(.*)$', out, re.M))
    obj = d.get('OBJ') or ov[k]['title']
    et = re.sub(r'\b(Name|Date)\b|Lesson \d+(-\d)?:.*?(?=\d•\d|$)', '', d.get('ET', ''))
    print('  OBJ:', obj[:160]); print('  ET:', et[:int(sys.argv[3]) if len(sys.argv) > 3 else 650]); print('  PS:', d.get('PS', '')[:220])
