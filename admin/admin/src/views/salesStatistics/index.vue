<template>
  <div class="sales-statistics-container">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span class="title">商品销量统计 TOP10</span>
          <el-button type="primary" @click="refreshData" :loading="loading">
            <el-icon><Refresh /></el-icon>
            刷新数据
          </el-button>
        </div>
      </template>

      <div class="chart-container" ref="chartRef" v-loading="loading"></div>

      <div class="no-data" v-if="!loading && chartData.length === 0">
        <el-empty description="暂无销售数据" />
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue';
import * as echarts from 'echarts';
import { Refresh } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus';
import request from '@/utils/request';

const chartRef = ref<HTMLDivElement>();
let chartInstance: echarts.ECharts | null = null;
const loading = ref(false);
const chartData = ref<any[]>([]);

// 获取销量数据
const fetchSalesData = async () => {
  loading.value = true;
  try {
    // 调用后端接口获取销量统计数据
    const res = await request.get('/shangpinguanli/salesTop10');
    console.log('销量统计接口返回:', res);
    if (res.data && res.data.length > 0) {
      chartData.value = res.data;
      // 按销量从高到低排序
      chartData.value.sort((a: any, b: any) => b.sales - a.sales);
      // 只取前10条
      chartData.value = chartData.value.slice(0, 10);
      await nextTick();
      initChart();
    } else {
      chartData.value = [];
    }
  } catch (error) {
    console.error('获取销量数据失败:', error);
    ElMessage.error('获取销量数据失败');
  } finally {
    loading.value = false;
  }
};

// 初始化图表
const initChart = () => {
  if (!chartRef.value) return;

  // 如果图表实例已存在，先销毁
  if (chartInstance) {
    chartInstance.dispose();
  }

  chartInstance = echarts.init(chartRef.value);

  const productNames = chartData.value.map((item: any) => item.shangpinmingcheng || item.name);
  const salesData = chartData.value.map((item: any) => item.sales || item.xiaoliang || 0);

  const option = {
    title: {
      text: '商品销量排行榜',
      left: 'center',
      top: 10,
      textStyle: {
        fontSize: 18,
        fontWeight: 'bold'
      }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      },
      formatter: (params: any) => {
        const data = params[0];
        return `${data.name}<br/>销量: ${data.value} 件`;
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: 60,
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: productNames,
      axisLabel: {
        interval: 0,
        rotate: 45,
        fontSize: 12
      }
    },
    yAxis: {
      type: 'value',
      name: '销量(件)',
      axisLabel: {
        formatter: '{value}'
      }
    },
    series: [
      {
        name: '销量',
        type: 'bar',
        data: salesData,
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#83bff6' },
            { offset: 0.5, color: '#188df0' },
            { offset: 1, color: '#188df0' }
          ])
        },
        emphasis: {
          itemStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: '#2378f7' },
              { offset: 0.7, color: '#2378f7' },
              { offset: 1, color: '#83bff6' }
            ])
          }
        },
        label: {
          show: true,
          position: 'top',
          formatter: '{c}'
        }
      }
    ]
  };

  chartInstance.setOption(option);

  // 监听窗口大小变化
  window.addEventListener('resize', handleResize);
};

// 处理窗口大小变化
const handleResize = () => {
  if (chartInstance) {
    chartInstance.resize();
  }
};

// 刷新数据
const refreshData = () => {
  fetchSalesData();
};

onMounted(() => {
  fetchSalesData();
});

onBeforeUnmount(() => {
  if (chartInstance) {
    chartInstance.dispose();
    chartInstance = null;
  }
  window.removeEventListener('resize', handleResize);
});
</script>

<style scoped lang="scss">
.sales-statistics-container {
  padding: 20px;

  .box-card {
    min-height: 600px;

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .title {
        font-size: 18px;
        font-weight: bold;
        color: #303133;
      }
    }

    .chart-container {
      width: 100%;
      height: 500px;
      margin-top: 20px;
    }

    .no-data {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 400px;
    }
  }
}
</style>
