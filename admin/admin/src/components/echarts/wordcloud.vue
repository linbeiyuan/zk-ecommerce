<script setup lang="ts">
     import * as echarts from 'echarts';
     import 'echarts-wordcloud';
import { text } from 'stream/consumers';
     import  {ref,markRaw,onMounted,reactive,onActivated,onBeforeUnmount,watch,nextTick} from 'vue';
     interface Data{
        name:string,
        value:string
     }
     //子组件接收父组件参数
     const props=withDefaults(defineProps<{
          width?:string,
          height?:string,
          theme?:string,
          bgColor?:string,
          title?:any,
          data:Data[]
     }>(),{
        whdth:'100%',
        height:'200px',
        data:()=>[],//数组默认值为空  则返回一个函数空数组
     });



      const cartRef=ref();

      const state=reactive({
        chart: null as any, // 图表实例
        nvll:['',null,undefined],//用于判断  图表实例是否为空
      })

        onMounted(()=>{
            //initChart();
           window.addEventListener('resize', echartsResizeFun);

        })

        watch(() => [props.data, props.theme], () => {
    nextTick(() => { // 不加模板未初始化完成，chartRef.value是未定义会报错
        initChart();
    });
}, {deep: true, immediate: true});

        //使用keep-alive缓冲了组件，每次进入组件时重新绘制大小
       onActivated(()=>{
         echartsResizeFun();
      })

     function initChart(){
        //实例存在则销毁
        if(state.nvll.indexOf(state.chart)===-1)state.chart.dispose();
        //获取实例时记得使用markRaw返回实例本身，不然有些option选项会失效，比如：鼠标放上去会失效
        //参数1：容器ref值，参数2：指定主题
        state.chart = markRaw(echarts.init(cartRef.value, props.theme));
        
        const option= {
                title:{
                  textStyle: {
            //图例中文字的样式
            color: "#ffffff",
            fontSize: 12,
          },
                  text:props.title
                },
                series: [{
                type: 'wordCloud',
                shape: 'circle',
                keepAspect: false,
               // maskImage: maskImage,
                left: 'center',
                top: 'center',
                width: '100%',
                height: '90%',
                right: null,
                bottom: null,
                sizeRange: [12, 60],
                rotationRange: [-90, 90],
                rotationStep: 45,
                gridSize: 8,
                drawOutOfBound: false,
                layoutAnimation: true,
                textStyle: {
                    fontFamily: 'sans-serif',
                    fontWeight: 'bold',
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    // focus: 'self',
                    textStyle: {
                        textShadowBlur: 3,
                        textShadowColor: '#333'
                    }
                },
                //data属性中的value值却大，权重就却大，展示字体就却大
                data: props.data
            }]

           }

        state.chart.setOption(option);
     }
// 重置echarts图表大小
function echartsResizeFun() {
    console.log('echartsResizeFun');
    state.chart && state.chart.resize();
}

 //组件销毁前触发
 onBeforeUnmount(()=>{
     window.removeEventListener('resize', echartsResizeFun);
     if(state.chart){
        state.chart.dispose();
        state.chart=null;
     }
 })

</script>

<template>
       
    
              <div ref="cartRef" :style="{height:props.height,width:props.whdth}"></div>
         
</template>

<style scoped>

</style>