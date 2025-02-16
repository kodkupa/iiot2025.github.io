import{S as ue,i as he,s as fe,a as b,k as i,q as y,K as ce,Q as ve,h as t,c as g,l as d,m as c,r as D,L as ne,n as a,b as R,D as e,u as ie,G as de,I as me}from"../chunks/index.05bf19d7.js";import{p as pe}from"../chunks/stores.d3948bd9.js";import{b as _e}from"../chunks/paths.876e52cd.js";function be(n){let l;return{c(){l=y("An unexpected error happened. Try refreshing the page or come back later.")},l(s){l=D(s,"An unexpected error happened. Try refreshing the page or come back later.")},m(s,r){R(s,l,r)},d(s){s&&t(l)}}}function ge(n){let l;return{c(){l=y("This is not the page you are looking for.")},l(s){l=D(s,"This is not the page you are looking for.")},m(s,r){R(s,l,r)},d(s){s&&t(l)}}}function Ee(n){let l,s,r,u,v,E=n[0].status+"",$,j,H,K,I,M=n[0].error.message+"",q,N,h,T,m,S,O,V,z,Q,U,k,F,p,w,J,P,x,W;document.title=l=n[0].status+" - "+n[0].error.message;function X(o,_){return o[0].status==404?ge:be}let C=X(n),f=C(n);return{c(){s=b(),r=i("div"),u=i("div"),v=i("h2"),$=y(E),j=b(),H=i("div"),K=b(),I=i("h3"),q=y(M),N=b(),h=i("div"),T=i("div"),m=ce("svg"),S=ce("path"),O=b(),V=i("div"),z=i("time"),Q=y(n[1]),U=b(),k=i("div"),f.c(),F=b(),p=i("div"),w=i("button"),J=y("Go back"),P=b(),x=i("a"),W=y("Return home"),this.h()},l(o){ve("svelte-1rlnzzk",document.head).forEach(t),s=g(o),r=d(o,"DIV",{class:!0});var A=c(r);u=d(A,"DIV",{class:!0});var B=c(u);v=d(B,"H2",{class:!0});var Y=c(v);$=D(Y,E),Y.forEach(t),j=g(B),H=d(B,"DIV",{class:!0}),c(H).forEach(t),K=g(B),I=d(B,"H3",{class:!0});var Z=c(I);q=D(Z,M),Z.forEach(t),B.forEach(t),N=g(A),h=d(A,"DIV",{class:!0});var G=c(h);T=d(G,"DIV",{class:!0});var ee=c(T);m=ne(ee,"svg",{xmlns:!0,class:!0,viewBox:!0});var te=c(m);S=ne(te,"path",{d:!0}),c(S).forEach(t),te.forEach(t),ee.forEach(t),O=g(G),V=d(G,"DIV",{class:!0});var ae=c(V);z=d(ae,"TIME",{class:!0});var se=c(z);Q=D(se,n[1]),se.forEach(t),ae.forEach(t),U=g(G),k=d(G,"DIV",{class:!0});var re=c(k);f.l(re),re.forEach(t),G.forEach(t),F=g(A),p=d(A,"DIV",{class:!0});var L=c(p);w=d(L,"BUTTON",{onclick:!0,class:!0});var le=c(w);J=D(le,"Go back"),le.forEach(t),P=g(L),x=d(L,"A",{href:!0,class:!0});var oe=c(x);W=D(oe,"Return home"),oe.forEach(t),L.forEach(t),A.forEach(t),this.h()},h(){a(v,"class","text-7xl font-bold"),a(H,"class","divider m-0"),a(I,"class","self-center text-3xl"),a(u,"class","card-title self-center flex flex-col w-full"),a(S,"d","M399 384.2C376.9 345.8 335.4 320 288 320H224c-47.4 0-88.9 25.8-111 64.2c35.2 39.2 86.2 63.8 143 63.8s107.8-24.7 143-63.8zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256zm256 16a72 72 0 1 0 0-144 72 72 0 1 0 0 144z"),a(m,"xmlns","http://www.w3.org/2000/svg"),a(m,"class","w-10 fill-base-content"),a(m,"viewBox","0 0 512 512"),a(T,"class","chat-image avatar"),a(z,"class","text-sm opacity-75 ml-1"),a(V,"class","chat-header"),a(k,"class","chat-bubble chat-bubble-error"),a(h,"class","chat chat-start"),a(w,"onclick","history.back()"),a(w,"class","btn btn-secondary rounded-full"),a(x,"href",_e+"/"),a(x,"class","btn btn-primary rounded-full"),a(p,"class","card-actions flex-wrap gap-4 grow items-center justify-center"),a(r,"class","w-full grow max-w-2xl flex flex-col gap-8 px-4 pb-8 pt-12")},m(o,_){R(o,s,_),R(o,r,_),e(r,u),e(u,v),e(v,$),e(u,j),e(u,H),e(u,K),e(u,I),e(I,q),e(r,N),e(r,h),e(h,T),e(T,m),e(m,S),e(h,O),e(h,V),e(V,z),e(z,Q),e(h,U),e(h,k),f.m(k,null),e(r,F),e(r,p),e(p,w),e(w,J),e(p,P),e(p,x),e(x,W)},p(o,[_]){_&1&&l!==(l=o[0].status+" - "+o[0].error.message)&&(document.title=l),_&1&&E!==(E=o[0].status+"")&&ie($,E),_&1&&M!==(M=o[0].error.message+"")&&ie(q,M),C!==(C=X(o))&&(f.d(1),f=C(o),f&&(f.c(),f.m(k,null)))},i:de,o:de,d(o){o&&t(s),o&&t(r),f.d()}}}function ke(n,l,s){let r;me(n,pe,E=>s(0,r=E));var u=new Date,v=u.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"});return[r,v]}class De extends ue{constructor(l){super(),he(this,l,ke,Ee,fe,{})}}export{De as component};
