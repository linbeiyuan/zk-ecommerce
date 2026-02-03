<script setup lang="ts">
   import {useEcharts} from '@/hooks/useEcharts';
   import * as echarts from 'echarts';
   import { reactive, computed } from 'vue';

   interface Data{
    name: string;
    value: number;
}

   const props=  withDefaults(defineProps<{

      
        width?: string,
        height?: string,
        theme?: string,
        bgColor?: string,
        title: string,
        subtitle?: string,
        data:Data[]
     }>(),{
        width: '100%',
        height: '380px',
        data: () => []
     })


     const name=computed(()=>props.data.map(item=>item.name));
     const value=computed(()=>props.data.map(item=>item.value));
     //柱状图选项
     const option=reactive({
     
      title:{
        textStyle: {
            //图例中文字的样式
            color: "#ffffff",
            fontSize: 12,
          },
         text:props.title,
         subtext:props.subtitle,
         x:'left'
      },
      tooltip:{
         trigger:'axis',
         axisPointer:{
            type:'shadow'
         }
      },
      xAxis: {
    type: 'category',
    data: name,
    axisLabel: {//x轴文字的配置
                show: true,
                textStyle: {
                    color: "#fff",
                }
            },
  },
  yAxis: {
    type: 'value',
    axisLabel: {//x轴文字的配置
                show: true,
                textStyle: {
                    color: "#fff",
                }
            },
  },
  series: [
    {
      data: value,
      type: 'bar',
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: '#83bff6' },
          { offset: 0.5, color: '#188df0' },
          { offset: 1, color: '#188df0' }
        ])
      },
    }
  ]
      })
      
    
    const {
      chartRef,
      chart,nvll,echartsResizeFun
      }= useEcharts({props,option});
</script>

<template>
      
              <div ref="chartRef" :style="{height:props.height,width:props.width}"></div>
          
</template>

<style scoped>

</style>