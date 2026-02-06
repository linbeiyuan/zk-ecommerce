<script setup lang='ts'>
  import { defineAsyncComponent,reactive,ref,toRefs,onMounted,onUnmounted } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify} from '@/utils/element';
  import { isAuth } from '@/utils/utils'
  import siteConfig from '@/config/siteConfig';

  // 站点配置
  const config = siteConfig;
  // const indexlunbo=defineAsyncComponent(()=>import('@/layout/indexlunbo.vue'));
  // const indexwz=defineAsyncComponent(()=>import('@/layout/indexwz.vue'));
  // const indexleibiao=defineAsyncComponent(()=>import('@/layout/indexliebiao.vue'));


  const state=reactive({

            shangpinguanliList: [],
            dianpuxinxiList: [],
            jifenshangdianList: [],
                shangpinguanlirecommendList: [],
            dianpuxinxirecommendList: [],
              newsList:[],
        username:'',
    user:{}
  })

  const {
            shangpinguanliList,
            dianpuxinxiList,
            jifenshangdianList,
                shangpinguanlirecommendList,
            dianpuxinxirecommendList,
              newsList,
        username,
    user

  } = {...toRefs(state)};

        getshangpinguanli()
        getdianpuxinxi()
        getjifenshangdian()
            getnews()
            function getnews(){
      const params={
        page: 0,
        limit: 8,
        sort: 'id',
      }
      request({
        url:'news/list',
        method:'get',
        params
      }).then((data)=>{
        state.newsList=data.data.list;
      })
    }

    

        function getshangpinguanli(){
      const params={
        page: 0,
        limit: 8,
        sort: 'id',
      }


      request({
        url:'shangpinguanli/list',
        method:'get',
        params
      }).then((data)=>{
        state.shangpinguanliList=data.data.list;
      })
    }




        function getdianpuxinxi(){
      const params={
        page: 0,
        limit: 8,
        sort: 'id',
      }


      request({
        url:'dianpuxinxi/list',
        method:'get',
        params
      }).then((data)=>{
        state.dianpuxinxiList=data.data.list;
      })
    }




        function getjifenshangdian(){
      const params={
        page: 0,
        limit: 8,
        sort: 'id',
      }


      request({
        url:'jifenshangdian/list',
        method:'get',
        params
      }).then((data)=>{
        state.jifenshangdianList=data.data.list;
      })
    }




    


  state.username=Session.get("adminName");
  if(state.username){
    let sessionTable = Session.get("tableName")
    request({
      url: sessionTable + '/session',
      method: "get"
    }).then((data) => {
      if (data && data.code === 0) {
        state.user = data.data;

                  request({
            url:'shangpinguanli/recommendList',
            method:'POST',
            params:{
              num: 8,
              userId:data.data.id,
            }
          }).then((data)=>{
            state.shangpinguanlirecommendList=data.data;
          })

                  request({
            url:'dianpuxinxi/recommendList',
            method:'POST',
            params:{
              num: 8,
              userId:data.data.id,
            }
          }).then((data)=>{
            state.dianpuxinxirecommendList=data.data;
          })

        

      } else {
        notify(data.msg,{type:'error'});
      }
    });



  }


  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination, Autoplay } from 'swiper/modules';
  const swiperModules = [Pagination, Autoplay];
  const showBackToTop = ref(false);
  const handleScroll = () => {
    showBackToTop.value = window.scrollY > 300;
  };
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };
  onMounted(() => {
    window.addEventListener('scroll', handleScroll);
  });
  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
  });

</script>

<template>
  <div class="home-page">
    <!-- 特色服务 -->
    <section class="features-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">{{ config.features.section.title }}</h2>
          <p class="section-desc">{{ config.features.section.desc }}</p>
        </div>
        <div class="features-grid">
          <div v-for="(feature, index) in config.features.items" :key="index" class="feature-card">
            <div class="feature-icon">
              <i :class="feature.icon"></i>
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-desc">{{ feature.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 优惠券专区 -->
    <section class="coupon-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">优惠券专区</h2>
          <p class="section-desc">领取优惠券，享受更多优惠</p>
        </div>
        <div class="coupon-banner">
          <div class="coupon-content">
            
            <div class="coupon-text">
              <h3>新人专享优惠券</h3>
              <p>多种优惠券等你来领，购物更省钱</p>
            </div>
          </div>
          <router-link to="/coupon-receive" class="coupon-btn">
            立即领取
          </router-link>
        </div>
      </div>
    </section>

    <!-- 产品展示 -->
    <section class="products-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">商品管理</h2>
          <p class="section-desc">精选商品管理</p>
        </div>
        <div class="products-grid">
          <div v-for="(item, index) in shangpinguanliList" :key="index" class="product-card">
            <router-link :to="`/shangpinguanlidetail/`+item.id">
              <div class="product-image">
                <span v-for="(value, key, ind) in item" :key="ind">
                  <img v-if="ind === 3" :src="value" alt="图片">
                </span>
                <div class="product-overlay">
                  <span class="view-btn">查看详情</span>
                </div>
              </div>
              <div class="product-info">
                <span v-for="(value, key, ind) in item" :key="ind">
                  <h3 v-if="ind === 2" class="product-name">{{ value }}</h3>
                </span>
              </div>
            </router-link>
          </div>
        </div>
        <div class="section-more">
          <router-link to="/shangpinguanli" class="more-btn">
            查看商品管理 <i class="fas fa-arrow-right"></i>
          </router-link>
        </div>
      </div>
    </section>

      <!-- 产品展示 -->
    <section class="products-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">店铺信息</h2>
          <p class="section-desc">精选店铺信息</p>
        </div>
        <div class="products-grid">
          <div v-for="(item, index) in dianpuxinxiList" :key="index" class="product-card">
            <router-link :to="`/dianpuxinxidetail/`+item.id">
              <div class="product-image">
                <span v-for="(value, key, ind) in item" :key="ind">
                  <img v-if="ind === 3" :src="value" alt="图片">
                </span>
                <div class="product-overlay">
                  <span class="view-btn">查看详情</span>
                </div>
              </div>
              <div class="product-info">
                <span v-for="(value, key, ind) in item" :key="ind">
                  <h3 v-if="ind === 2" class="product-name">{{ value }}</h3>
                </span>
              </div>
            </router-link>
          </div>
        </div>
        <div class="section-more">
          <router-link to="/dianpuxinxi" class="more-btn">
            查看店铺信息 <i class="fas fa-arrow-right"></i>
          </router-link>
        </div>
      </div>
    </section>

      <!-- 产品展示 -->
    <section class="products-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">积分商店</h2>
          <p class="section-desc">精选积分商店</p>
        </div>
        <div class="products-grid">
          <div v-for="(item, index) in jifenshangdianList" :key="index" class="product-card">
            <router-link :to="`/jifenshangdiandetail/`+item.id">
              <div class="product-image">
                <span v-for="(value, key, ind) in item" :key="ind">
                  <img v-if="ind === 3" :src="value" alt="图片">
                </span>
                <div class="product-overlay">
                  <span class="view-btn">查看详情</span>
                </div>
              </div>
              <div class="product-info">
                <span v-for="(value, key, ind) in item" :key="ind">
                  <h3 v-if="ind === 2" class="product-name">{{ value }}</h3>
                </span>
              </div>
            </router-link>
          </div>
        </div>
        <div class="section-more">
          <router-link to="/jifenshangdian" class="more-btn">
            查看积分商店 <i class="fas fa-arrow-right"></i>
          </router-link>
        </div>
      </div>
    </section>

      <!-- 新闻动态 -->
    <section class="news-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">平台通知</h2>
          <p class="section-desc">了解最新的平台通知动态</p>
        </div>
        <div class="news-grid">
          <div v-for="(item, index) in newsList" :key="index" class="news-card">
            <div class="news-image">
              <img :src="item.picture" alt="新闻图片">
            </div>
            <div class="news-content">
              <div class="news-meta">
                <span class="news-date">
                  <i class="far fa-calendar-alt"></i> {{ item.addtime }}
                </span>
              </div>
              <h3 class="news-title">{{ item.title }}</h3>
              <p class="news-excerpt">{{ item.introduction }}</p>
              <router-link :to="`/newsdetail/${item.id}`" class="news-link">
                阅读全文 <i class="fas fa-chevron-right"></i>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

  


  <section class="products-section" v-if="shangpinguanlirecommendList.length > 0">
    <div class="section-container">
      <div class="section-header">
        <h2 class="section-title">商品管理推荐</h2>
        <p class="section-desc">精选商品管理</p>
      </div>
      <div class="products-grid">
        <div v-for="(trip, index) in shangpinguanlirecommendList" :key="index" class="product-card">
          <router-link :to="`/shangpinguanlidetail/`+trip.id">
            <div class="product-image">
                <span v-for="(value, key, ind) in trip" :key="ind">
                  <img v-if="ind === 3" :src="value" alt="图片">
                </span>
              <div class="product-overlay">
                <span class="view-btn">查看详情</span>
              </div>
            </div>
            <div class="product-info">
                <span v-for="(value, key, ind) in trip" :key="ind">
                  <h3 v-if="ind === 2" class="product-name">{{ value }}</h3>
                </span>
            </div>
          </router-link>
        </div>
      </div>
      <div class="section-more">
        <router-link to="/shangpinguanli" class="more-btn">
          查看商品管理 <i class="fas fa-arrow-right"></i>
        </router-link>
      </div>
    </div>
  </section>
   

  <section class="products-section" v-if="dianpuxinxirecommendList.length > 0">
    <div class="section-container">
      <div class="section-header">
        <h2 class="section-title">店铺信息推荐</h2>
        <p class="section-desc">精选店铺信息</p>
      </div>
      <div class="products-grid">
        <div v-for="(trip, index) in dianpuxinxirecommendList" :key="index" class="product-card">
          <router-link :to="`/dianpuxinxidetail/`+trip.id">
            <div class="product-image">
                <span v-for="(value, key, ind) in trip" :key="ind">
                  <img v-if="ind === 3" :src="value" alt="图片">
                </span>
              <div class="product-overlay">
                <span class="view-btn">查看详情</span>
              </div>
            </div>
            <div class="product-info">
                <span v-for="(value, key, ind) in trip" :key="ind">
                  <h3 v-if="ind === 2" class="product-name">{{ value }}</h3>
                </span>
            </div>
          </router-link>
        </div>
      </div>
      <div class="section-more">
        <router-link to="/dianpuxinxi" class="more-btn">
          查看店铺信息 <i class="fas fa-arrow-right"></i>
        </router-link>
      </div>
    </div>
  </section>
       <!-- 回到顶部 -->
    <button v-show="showBackToTop" @click="scrollToTop" class="back-to-top">
      <i class="fas fa-arrow-up"></i>
    </button>
  </div>
</template>

<style scoped>
/* 优惠券专区样式 */
.coupon-section {
  padding: 60px 0;
  background: linear-gradient(135deg, #fff5f5 0%, #ffe8e8 100%);
}

.coupon-banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8787 100%);
  border-radius: 16px;
  padding: 40px;
  box-shadow: 0 8px 24px rgba(255, 107, 107, 0.3);
  transition: transform 0.3s;
}

.coupon-banner:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 32px rgba(255, 107, 107, 0.4);
}

.coupon-content {
  display: flex;
  align-items: center;
  gap: 24px;
}

.coupon-icon {
  font-size: 64px;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.coupon-text h3 {
  font-size: 28px;
  color: white;
  margin: 0 0 8px 0;
  font-weight: bold;
}

.coupon-text p {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
}

.coupon-btn {
  background: white;
  color: #ff6b6b;
  padding: 14px 36px;
  border-radius: 30px;
  font-size: 16px;
  font-weight: bold;
  text-decoration: none;
  transition: all 0.3s;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.coupon-btn:hover {
  background: #fff;
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}
</style>
