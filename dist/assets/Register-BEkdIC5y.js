import{r as t,u as g,a as m,j as s,N as x,b as j}from"./main-BiQHBlKm.js";const b=()=>{const[a,l]=t.useState(""),[r,u]=t.useState(""),[n,d]=t.useState(""),p=g(),{user:c,loading:i,error:o}=m(e=>e.auth),h=e=>{e.preventDefault(),p(j({username:a,email:r,password:n}))};return c?s.jsx(x,{to:"/dashboard"}):s.jsxs("div",{children:[s.jsx("h2",{children:"Register"}),s.jsxs("form",{onSubmit:h,children:[s.jsx("input",{type:"text",placeholder:"Username",value:a,onChange:e=>l(e.target.value)}),s.jsx("input",{type:"email",placeholder:"Email",value:r,onChange:e=>u(e.target.value)}),s.jsx("input",{type:"password",placeholder:"Password",value:n,onChange:e=>d(e.target.value)}),s.jsx("button",{type:"submit",disabled:i,children:i?"Registering...":"Register"}),o&&s.jsx("p",{children:o})]})]})};export{b as default};