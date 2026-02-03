<script setup lang='ts'>

import { defineProps,ref,reactive,toRefs,toRaw,onMounted,watch } from 'vue';
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


    <div class="block news">
	<div class="items">
		<ul>
			<li v-for="item in dataList" :key="item.id">
				<router-link :to="`/${tablename}detail/`+item.id">
				<a href="#">
					<div v-for="(value, key, ind) in item" :key="ind" v-show="ind == 3" class="items-l"><img :src="value" /></div>
					<div class="items-r">
						<p class="title" v-for="(value, key, ind) in item" :key="ind" v-show="ind == 2">{{value}}</p>
						<!-- <p class="time"  v-for="(value, key, ind) in item" :key="ind" v-show="ind == 1">{{value}}</p> -->
					</div>
				</a>
			</router-link>
			</li>
			
		</ul>
	</div>



  </div>
</template>


