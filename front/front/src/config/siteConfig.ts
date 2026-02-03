/**
 * 站点配置文件 - 通用模板配置
 * 修改此文件即可快速定制不同类型的网站
 */

export interface FeatureItem {
  icon: string;      // Font Awesome 图标类名
  title: string;     // 标题
  desc: string;      // 描述
}

export interface SectionConfig {
  title: string;     // 区块标题
  desc: string;      // 区块描述
}

export interface SiteConfig {
  // 站点基本信息
  siteName: string;
  siteType: 'shop' | 'news' | 'portal' | 'blog' | 'service';

  // 特色服务区配置
  features: {
    section: SectionConfig;
    items: FeatureItem[];
  };

  // 推荐区配置
  recommend: {
    section: SectionConfig;
  };
}

// 默认配置 - ZK电商平台
const siteConfig: SiteConfig = {
  siteName: 'ZK电商平台',
  siteType: 'shop',

  // 特色服务区
  features: {
    section: {
      title: '为什么选择我们',
      desc: '品质保障，服务至上，让购物更简单'
    },
    items: [
      {
        icon: 'fas fa-store',
        title: '优质商家',
        desc: '严格筛选入驻商家，确保每一家店铺都是信誉良好的优质商家'
      },
      {
        icon: 'fas fa-truck',
        title: '快速配送',
        desc: '高效物流体系，快速送达，让您的购物体验更加便捷'
      },
      {
        icon: 'fas fa-shield-alt',
        title: '正品保障',
        desc: '所有商品均为正品，假一赔十，让您购物无忧'
      },
      {
        icon: 'fas fa-headset',
        title: '贴心客服',
        desc: '专业客服团队在线服务，随时解答您的疑问'
      }
    ]
  },

  // 推荐区
  recommend: {
    section: {
      title: '为您推荐',
      desc: '根据您的喜好，精心推荐优质商品'
    }
  }
};

export default siteConfig;

// ============ 其他模板示例 ============

// 新闻门户模板
export const newsPortalConfig: SiteConfig = {
  siteName: '新闻门户',
  siteType: 'news',
  features: {
    section: {
      title: '我们的优势',
      desc: '专业、及时、权威的新闻报道'
    },
    items: [
      {
        icon: 'fas fa-bolt',
        title: '实时更新',
        desc: '24小时不间断新闻更新，第一时间掌握全球动态'
      },
      {
        icon: 'fas fa-check-circle',
        title: '权威可靠',
        desc: '专业记者团队，多方核实，确保新闻真实性'
      },
      {
        icon: 'fas fa-globe',
        title: '全球视野',
        desc: '覆盖国内外热点，带您看遍世界大事'
      },
      {
        icon: 'fas fa-comment-dots',
        title: '深度评论',
        desc: '资深评论员解读，帮您深入理解新闻背后的故事'
      }
    ]
  },
  recommend: {
    section: {
      title: '编辑推荐',
      desc: '精选优质内容，值得您阅读'
    }
  }
};

// 企业官网模板
export const corporateConfig: SiteConfig = {
  siteName: '企业官网',
  siteType: 'portal',
  features: {
    section: {
      title: '核心优势',
      desc: '专注品质，追求卓越'
    },
    items: [
      {
        icon: 'fas fa-award',
        title: '行业领先',
        desc: '深耕行业多年，拥有丰富的经验和专业技术'
      },
      {
        icon: 'fas fa-users',
        title: '专业团队',
        desc: '汇聚行业精英，为您提供最专业的服务'
      },
      {
        icon: 'fas fa-cogs',
        title: '技术创新',
        desc: '持续研发投入，始终保持技术领先优势'
      },
      {
        icon: 'fas fa-handshake',
        title: '合作共赢',
        desc: '诚信经营，与客户建立长期稳定的合作关系'
      }
    ]
  },
  recommend: {
    section: {
      title: '成功案例',
      desc: '我们的客户遍布各行各业'
    }
  }
};
