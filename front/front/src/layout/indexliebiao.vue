<script setup lang='ts'>

import { defineProps,ref,reactive,toRefs,toRaw,onMounted,watch,onUpdated } from 'vue';
const props = defineProps({
  datalist: {
    type: Array,
    default() {
      return []
    }
  },
  tablename:{
	type:String,
	default(){
		return ""
	}
  }
})

onMounted(()=>{
    	//从底部上升的遮罩效果开始
	$(".con").hover(function(){
		$(this).find(".txt").stop().animate({height:"198px"},200);
		$(this).find(".txt h3").stop().animate({paddingTop:"60px"},200);
	},function(){
		$(this).find(".txt").stop().animate({height:"45px"},200);
		$(this).find(".txt h3").stop().animate({paddingTop:"0px"},200);
	})
	//从底部上升的遮罩效果结束
})

onUpdated(()=>{
     	//从底部上升的遮罩效果开始
	$(".con").hover(function(){
		$(this).find(".txt").stop().animate({height:"198px"},200);
		$(this).find(".txt h3").stop().animate({paddingTop:"60px"},200);
	},function(){
		$(this).find(".txt").stop().animate({height:"45px"},200);
		$(this).find(".txt h3").stop().animate({paddingTop:"0px"},200);
	})
	//从底部上升的遮罩效果结束
})

const state=reactive({
    dataList:props.datalist,
	tablename:props.tablename
})
watch(() => props.datalist, (newVal: any) => {
      state.dataList = newVal;
     
    })
const {dataList,tablename} =toRefs(state);
  console.log("子组件："+state.tablename);
</script>

<template>



	<div class="content">
		<ul class="contentbox">
			<li class="con" v-for="item in dataList" :key="item.id">

				<div  v-for="(value, key, ind) in item" :key="ind">
				<router-link :to="`/${tablename}detail/`+item.id">
				<img  v-show="ind == 3" :src="value" alt="con1"/>
				<div class="txt" v-show="ind == 2">
					<h3>{{value}}</h3>
				</div>
			</router-link>
		       </div>
			</li>
		</ul>
	</div>


  
</template>

