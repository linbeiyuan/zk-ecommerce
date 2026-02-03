<script setup lang="ts">
     import * as echarts from 'echarts';
     import chinaJSON from '@/assets/dp/json/china.json'
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
        height:'700px',
        data:()=>[],//数组默认值为空  则返回一个函数空数组
     });

    
     

      const cartRef=ref();
      const dataList=ref([{}]);
      const state=reactive({
        chart: null as any, // 图表实例
        nvll:['',null,undefined],//用于判断  图表实例是否为空
      })

        onMounted(()=>{
           dataList.value = [
            {name:'忻州市',value:290},
            {name:'太原市',value:320},
            {name:'长治市',value:240},
            {name:'临汾市',value:520},
            {name:'运城市',value:120},
            {name:'大同市',value:210},
            {name:'朔州市',value:620},
            {name:'吕梁市',value:20},
            {name:'晋中市',value:220},
            {name:'晋城市',value:820},
            {name:'阳泉市',value:320},
          
        ]


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
        echarts.registerMap('shanxi', chinaJSON) //注册可用的地图
        const option= {
            title: {
                textStyle: {
            //图例中文字的样式
            color: "#ffffff",
            fontSize: 12,
          },
            text: props.title,
            sublink:
                'http://zh.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E8%A1%8C%E6%94%BF%E5%8D%80%E5%8A%83#cite_note-12'
            },
            tooltip: {
            trigger: 'item',
            formatter: '{b}<br/>{c} '
            },
            toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                dataView: { readOnly: false },
                restore: {},
                saveAsImage: {}
            }
            },
            visualMap: {
            min: 0,
            max: 1000,
            text: ['High', 'Low'],
            realtime: false,
            calculable: true,
            inRange: {
                color: ['lightskyblue', 'yellow', 'orangered']
            }
            },
            series: [
            {
                name: '中国',
                type: 'map',
                map: 'shanxi',
                label: {
                show: false
                },
                data: props.data,
            }
            ]
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