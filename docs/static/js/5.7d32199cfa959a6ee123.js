webpackJsonp([5],{"1kS7":function(t,e){e.f=Object.getOwnPropertySymbols},"6t24":function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=r("ZIgP"),o=r("uYhV"),a=r("VU/8"),l=a(i.a,o.a,!1,null,null,null);e.default=l.exports},NpIQ:function(t,e){e.f={}.propertyIsEnumerable},R4wc:function(t,e,r){var i=r("kM2E");i(i.S+i.F,"Object",{assign:r("To3L")})},To3L:function(t,e,r){"use strict";var i=r("lktj"),o=r("1kS7"),a=r("NpIQ"),l=r("sB3e"),n=r("MU5D"),s=Object.assign;t.exports=!s||r("S82l")(function(){var t={},e={},r=Symbol(),i="abcdefghijklmnopqrst";return t[r]=7,i.split("").forEach(function(t){e[t]=t}),7!=s({},t)[r]||Object.keys(s({},e)).join("")!=i})?function(t,e){for(var r=l(t),s=arguments.length,f=1,p=o.f,c=a.f;s>f;)for(var u,m=n(arguments[f++]),d=p?i(m).concat(p(m)):i(m),v=d.length,_=0;v>_;)c.call(m,u=d[_++])&&(r[u]=m[u]);return r}:s},V3tA:function(t,e,r){r("R4wc"),t.exports=r("FeBl").Object.assign},ZIgP:function(t,e,r){"use strict";var i=r("woOf"),o=r.n(i);e.a={data:function(){return{editForm:!1,profile:{first_name:"",last_name:"",phone:"",bio:"",avatar_url:""}}},computed:{profileForm:function(){return this.$store.getters.getProfile}},methods:{editMode:function(){o()(this.profile,this.$store.getters.getProfile),this.editForm=!this.editForm},saveEdit:function(){this.profileForm&&this.$store.dispatch("sendProfile",this.profile),this.editForm=!this.editForm}}}},uYhV:function(t,e,r){"use strict";var i=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("el-main",[t.editForm?r("div",[r("el-form",{ref:"profile",attrs:{model:t.profile,"label-width":"100px"}},[r("el-button",{attrs:{type:"primary"},on:{click:t.saveEdit}},[t._v("Save")]),r("el-form-item",{attrs:{label:"Avatar"}},[r("el-input",{attrs:{type:"url"},model:{value:t.profile.avatar_url,callback:function(e){t.$set(t.profile,"avatar_url","string"==typeof e?e.trim():e)},expression:"profile.avatar_url"}})],1),r("el-form-item",{attrs:{label:"First Name"}},[r("el-input",{attrs:{type:"text"},model:{value:t.profile.first_name,callback:function(e){t.$set(t.profile,"first_name","string"==typeof e?e.trim():e)},expression:"profile.first_name"}})],1),r("el-form-item",{attrs:{label:"Surname"}},[r("el-input",{attrs:{type:"text"},model:{value:t.profile.last_name,callback:function(e){t.$set(t.profile,"last_name","string"==typeof e?e.trim():e)},expression:"profile.last_name"}})],1),r("el-form-item",{attrs:{label:"Phone"}},[r("el-input",{attrs:{type:"phone"},model:{value:t.profile.phone,callback:function(e){t.$set(t.profile,"phone","string"==typeof e?e.trim():e)},expression:"profile.phone"}})],1),r("el-form-item",{attrs:{label:"Bio"}},[r("el-input",{attrs:{type:"textarea"},model:{value:t.profile.bio,callback:function(e){t.$set(t.profile,"bio","string"==typeof e?e.trim():e)},expression:"profile.bio"}})],1)],1)],1):r("div",[r("el-row",[r("el-col",{attrs:{span:8,offset:8}},[r("el-card",[r("img",{attrs:{src:t.profileForm.avatar_url||"http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png"}}),r("br"),r("el-button",{attrs:{type:"primary",icon:"el-icon-edit"},on:{click:t.editMode}},[t._v("Edit")]),r("div",{staticStyle:{"text-align":"left"}},[r("p",[t._v("First name: "),r("span",[t._v(t._s(t.profileForm.first_name))])]),r("p",[t._v("Surname: "),r("span",[t._v(t._s(t.profileForm.last_name))])]),r("p",[t._v("Phone: "),r("span",[t._v(t._s(t.profileForm.phone))])]),r("p",[t._v("Info: "),r("span",[t._v(t._s(t.profileForm.bio))])])])],1)],1)],1)],1)])},o=[],a={render:i,staticRenderFns:o};e.a=a},woOf:function(t,e,r){t.exports={default:r("V3tA"),__esModule:!0}}});
//# sourceMappingURL=5.7d32199cfa959a6ee123.js.map