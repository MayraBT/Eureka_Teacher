// Evaluate the coordinator course data (COURSES + HS data + Object.assign), blank pacing, re-emit as JS.
const fs=require('fs'), vm=require('vm');
const src=fs.readFileSync(process.argv[2],'utf8');
const ctx={}; vm.createContext(ctx);
vm.runInContext(src.replace(/\bconst (COURSES|GEO_DATA|A2_DATA)\b/g,'var $1'), ctx);
const C=ctx.COURSES, named={GEO_DATA:ctx.GEO_DATA, A2_DATA:ctx.A2_DATA};
const seen=new Map(); for(const [n,o] of Object.entries(named)) if(o) seen.set(o,n);
let out=''; for(const [n,o] of Object.entries(named)) if(o) out+=`const ${n}=${JSON.stringify(o)};\n`;
out+='const COURSES={};\n';
for(const [k,c] of Object.entries(C)){
  c.pace={lessons:{},cal:{quarters:{},events:[]}}; c.cal=[]; c.unsched='';
  const d=c.data; const ref=seen.get(d);
  const rest=Object.assign({},c); delete rest.data;
  out+=`COURSES[${JSON.stringify(k)}]=Object.assign(${JSON.stringify(rest)},{data:${ref||JSON.stringify(d)}});\n`;
  if(!ref) seen.set(d,`COURSES[${JSON.stringify(k)}].data`);
}
fs.writeFileSync(process.argv[3],out);
