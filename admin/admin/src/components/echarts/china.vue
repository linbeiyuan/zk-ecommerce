<script setup lang="ts">
     import * as echarts from 'echarts';
     import chinaJSON from '@/assets/dp/json/cityPostion.json'
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
            {name:'北京市',value:290},
            {name:'天津市',value:320},
            {name:'河北省',value:240},
            {name:'山西省',value:5200},
            {name:'内蒙古自治区',value:120},
            {name:'辽宁省',value:210},
            {name:'吉林省',value:620},
            {name:'黑龙江省',value:20},
            {name:'上海市',value:220},
            {name:'江苏省',value:820},
            {name:'浙江省',value:320},
            {name:'安徽省',value:520},
            {name:'福建省',value:120},
            {name:'江西省',value:620},
            {name:'山东省',value:920},
            {name:'河南省',value:220},
            {name:'湖北省',value:720},
            {name:'湖南省',value:210},
            {name:'广东省',value:20},
            {name:'广西壮族自治区',value:20},
            {name:'海南省',value:240},
            {name:'重庆市',value:20},
            {name:'四川省',value:240},
            {name:'贵州省',value:420},
            {name:'云南省',value:320},
            {name:'西藏自治区',value:20},
            {name:'陕西省',value:240},
            {name:'甘肃省',value:920},
            {name:'青海省',value:720},
            {name:'宁夏回族自治区',value:120},
            {name:'新疆维吾尔自治区',value:420},
            {name:'台湾省',value:230},
            {name:'香港特别行政区',value:420},
            {name:'澳门特别行政区',value:210},
            {name:'南海诸岛',value:2100},
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
        echarts.registerMap('china', chinaJSON) //注册可用的地图
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
                map: 'china',
                label: {
                show: false
                },
                data: dataList.value,
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