
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


watch(() => props.datalist, (newVal: any) => {

   state.dataList = newVal;

})

onMounted(()=>{
    $(".pro-new-show").slide({
				mainCell: ".pro-list ul",
				titCell:".pagination ul",
				autoPage: true,
				effect: "left",
				autoPlay: false,
				vis: 3,
				trigger: "click"
	});
})

onUpdated(()=>{
            $(".pro-new-show").slide({
				mainCell: ".pro-list ul",
				titCell:".pagination ul",
				autoPage: true,
				effect: "left",
				autoPlay: false,
				vis: 3,
				trigger: "click"
	});
})


const state=reactive({
    dataList:props.datalist,
	tablename:props.tablename
})



const {dataList,tablename} =toRefs(state);
console.log("子组件："+state.tablename);
// console.log("子组件执行:"+props.datalist)

</script>

<template>
  

  <div class="pro-new">
			<div class="container">
				<div class="pro-new-show">
					<!--新品列表-->
					<div class="pro-list">
						<ul>
							<li v-for="(item, index) in dataList" :key="item.id">
								<div  v-for="(value, key, ind) in item" :key="ind">
								<router-link :to="`/${tablename}detail/`+item.id">
								<a href="#">
									
										<div class="img" v-show="ind == 3">
										<img :src="value" />
									</div>
									

									<div class="desc" v-show="ind == 2">
										<p class="p-title">{{value}}</p>

									</div>
								</a>
							
							</router-link>
						</div>
							</li>
						
							
						</ul>
					</div>
					<!--轮播左右箭头-->
					<div class="arrow">
						<a class="prev" href="javascript:void(0)"></a>
						<a class="next" href="javascript:void(0)"></a>
					</div>
					
				</div>
			</div>
		</div>
   


</template>


