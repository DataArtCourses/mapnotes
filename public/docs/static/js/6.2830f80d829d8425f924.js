webpackJsonp([6],{"5Wgx":function(t,e,a){"use strict";e.a={computed:{chatsList:function(){return this.$store.getters.getChats}},mounted:function(){this.$store.dispatch("reciveChats")}}},O2Ko:function(t,e,a){var s=a("f+CA");"string"==typeof s&&(s=[[t.i,s,""]]),s.locals&&(t.exports=s.locals);a("rjj0")("1de056f7",s,!0)},"f+CA":function(t,e,a){e=t.exports=a("FZ+f")(!0),e.push([t.i,".scroll[data-v-6ab92c59]{height:650px;overflow-y:scroll}ul[data-v-6ab92c59]{list-style-type:none}.item[data-v-6ab92c59]{margin-top:10px;margin-right:40px}.item .circle[data-v-6ab92c59]{border-radius:40px}","",{version:3,sources:["/media/iegor/data/projects/map-test/mapnotes/public/src/components/messenger/Chats.vue"],names:[],mappings:"AACA,yBACE,aAAc,AACd,iBAAmB,CACpB,AACD,oBACE,oBAAsB,CACvB,AACD,uBACE,gBAAiB,AACjB,iBAAmB,CACpB,AACD,+BACI,kBAAoB,CACvB",file:"Chats.vue",sourcesContent:["\n.scroll[data-v-6ab92c59] {\n  height: 650px;\n  overflow-y: scroll;\n}\nul[data-v-6ab92c59] {\n  list-style-type: none;\n}\n.item[data-v-6ab92c59] {\n  margin-top: 10px;\n  margin-right: 40px;\n}\n.item .circle[data-v-6ab92c59] {\n    border-radius: 40px;\n}\n"],sourceRoot:""}])},k47o:function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-aside",{staticStyle:{"background-color":"rgb(238, 241, 246)"},attrs:{width:"450px"}},[a("div",{staticClass:"scroll"},[a("ul",t._l(t.chatsList,function(e){return a("li",{key:e.chatId},[a("el-badge",{staticClass:"item",attrs:{value:e.unread}},[a("img",{staticClass:"circle",attrs:{src:e.chatWith.avatarUrl,width:"80px"}}),a("router-link",{attrs:{to:"/messenger/"+e.chatId}},[a("b",[t._v(t._s(e.chatWith.userName)+" ")])]),a("br"),a("span",[t._v(t._s(e.lastMessage.body))]),a("small",[t._v(t._s(t._f("moment")(e.lastMessage.time,"from","now",!0)))])],1)],1)}))])])},r=[],n={render:s,staticRenderFns:r};e.a=n},wNzW:function(t,e,a){"use strict";function s(t){a("O2Ko")}Object.defineProperty(e,"__esModule",{value:!0});var r=a("5Wgx"),n=a("k47o"),i=a("VU/8"),o=s,c=i(r.a,n.a,!1,o,"data-v-6ab92c59",null);e.default=c.exports}});
//# sourceMappingURL=6.2830f80d829d8425f924.js.map