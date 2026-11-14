const { chromium } = require('playwright');
const S='/tmp/claude-0/-home-claude/78bf741d-87e3-5321-ab17-c985254f55e2/scratchpad/';
(async()=>{ const b=await chromium.launch(); const errs=[]; const rep=[];
 const sites={eureka:['gk','g1','g2','g3','g4','g5'],carnegie:['g6','a7','g8','a1ms','a1hs','a1hsadv','geo','geoadv','a2','a2adv']};
 for(const [site,courses] of Object.entries(sites)) for(const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]){
  const p=await b.newPage({viewport:{width:w,height:h}}); p.on('pageerror',e=>errs.push(site+' '+e.message));
  await p.goto(`http://localhost:8770/${site}/index.html`); await p.waitForTimeout(500);
  for(const c of courses){
   if(!(await p.$(`#courseSel option[value="${c}"]`))) { rep.push(site+' missing course '+c); continue; }
   await p.selectOption('#courseSel',c); await p.waitForTimeout(300);
   const on=await p.evaluate(()=>document.querySelector('.view.on').id);
   if(on!=='view-std'&&!(await p.evaluate(()=>!!document.querySelector('.tabs button[data-view="std"]')))) rep.push(`${site} ${c} opens on ${on}`);
   const code=await p.evaluate(()=>{ const s=DATA.standards.find(s=>DATA.lessons.some(L=>L.marks.some(m=>m[0]===s.code))); return s&&s.code; });
   if(code){ await p.evaluate(c=>selectStd(c),code); await p.waitForTimeout(250); await p.evaluate(()=>document.querySelectorAll('#detail details.sec').forEach(d=>d.open=true)); }
   for(const v of ['les','std','perf','moves','grid']){
     if(!(await p.isVisible(`.tabs button[data-view="${v}"]`))) continue;
     await p.click(`.tabs button[data-view="${v}"]`); await p.waitForTimeout(200);
     if(v==='les') await p.evaluate(()=>document.querySelectorAll('#modlist details').forEach(d=>d.open=true));
     const txt=await p.evaluate(()=>document.querySelector('.view.on').innerText+' '+document.querySelector('.key, #key, .legend')?.innerText);
     const bad=(txt.match(/(Q[1-4] Wk \d+[^\n]{0,20}|Dallas ISD[^\n]{0,30}|not on the 2026-27[^\n]{0,20}|Calendar[^\n]{0,20}|ACP[^\n]{0,20}|2025-26 Q3[^\n]{0,20})/g)||[]);
     const ov=await p.evaluate(()=>document.documentElement.scrollWidth-window.innerWidth);
     if(bad.length||ov>1) rep.push(`${tag} ${site} ${c} ${v}: ${[...new Set(bad)].slice(0,4).join(' | ')} ${ov>1?'overflow '+ov:''}`);
   }
  }
  const calVisible=await p.isVisible('.tabs button[data-view="cal"]'); if(calVisible) rep.push(site+' calendar tab visible');
  if(tag==='d'){ await p.click('.tabs button[data-view="std"]'); await p.screenshot({path:S+'t_'+site+'.png'}); }
  await p.close();
 }
 console.log(rep.join('\n')||'clean'); console.log(errs.join('\n')||'no errors'); await b.close(); })();
