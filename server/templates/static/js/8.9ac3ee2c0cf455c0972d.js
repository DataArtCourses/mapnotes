webpackJsonp([8],{NSul:function(e,o,r){"use strict";var t=r("mtWM"),s=r.n(t);o.a={name:"login",data:function(){return{LoginForm:{email:"",password:"",checked:!1},rules:[{required:!0,message:"Please input email address",trigger:"blur"},{type:"email",message:"Please input correct email address",trigger:"blur,change"}]}},methods:{submitForm:function(e){var o=this;this.$refs[e].validate(function(e){if(!e)return o.$message({type:"error",message:"Oops! Something went wrong.."}),!1;s.a.post("http://localhost:8000/api/login",{email:o.LoginForm.email,password:o.LoginForm.password}).then(function(e){console.log(e),200===e.status&&(o.$store.dispatch("login",{token:e.data.token,ch:o.LoginForm.checked}),o.$router.push({path:"/hello"}))}).catch(function(e){o.$message({type:"error",message:""+(e.response?e.response.data.error:e)})})})}}}},P2Px:function(e,o,r){"use strict";var t=function(){var e=this,o=e.$createElement,r=e._self._c||o;return r("el-main",[r("el-row",[r("el-col",{attrs:{span:8,offset:7}},[r("el-form",{ref:"LoginForm",attrs:{model:e.LoginForm,labelWidth:"150px"}},[r("el-form-item",{attrs:{prop:"email",label:"Email",rules:e.rules}},[r("el-input",{attrs:{placeholder:"e-mail"},model:{value:e.LoginForm.email,callback:function(o){e.$set(e.LoginForm,"email",o)},expression:"LoginForm.email"}})],1),e._v(" "),r("el-form-item",{attrs:{prop:"password",label:"Password",rules:[{required:!0}]}},[r("el-input",{attrs:{type:"password",placeholder:"password"},model:{value:e.LoginForm.password,callback:function(o){e.$set(e.LoginForm,"password",o)},expression:"LoginForm.password"}})],1),e._v(" "),r("el-form-item",[r("el-checkbox",{model:{value:e.LoginForm.checked,callback:function(o){e.$set(e.LoginForm,"checked",o)},expression:"LoginForm.checked"}},[e._v("Remember me")])],1),e._v(" "),r("el-form-item",[r("el-button",{attrs:{type:"primary"},on:{click:function(o){e.submitForm("LoginForm")}}},[e._v("Log in")])],1)],1)],1)],1)],1)},s=[],a={render:t,staticRenderFns:s};o.a=a},c0mh:function(e,o,r){"use strict";Object.defineProperty(o,"__esModule",{value:!0});var t=r("NSul"),s=r("P2Px"),a=r("VU/8"),n=a(t.a,s.a,!1,null,null,null);o.default=n.exports}});
//# sourceMappingURL=8.9ac3ee2c0cf455c0972d.js.map