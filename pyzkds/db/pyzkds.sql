DROP TABLE IF EXISTS `address`; CREATE TABLE `address` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`address`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '地址' ,
`name`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '收货人' ,
`phone`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '电话' ,
`isdefault`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '是否默认地址[是/否]' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='地址'
AUTO_INCREMENT=7
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `orders`; CREATE TABLE `orders` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`orderid`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '订单编号' ,
`tablename`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT 'ziliaoxinxi' COMMENT '商品表名' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`goodid`  bigint(20) NOT NULL COMMENT '商品id' ,
`goodname`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '商品名称' ,
`picture`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '商品图片' ,
`buynumber`  int(11) NOT NULL COMMENT '购买数量' ,
`price`  float NOT NULL DEFAULT 0 COMMENT '价格/积分' ,
`discountprice`  float NULL DEFAULT 0 COMMENT '折扣价格' ,
`total`  float NOT NULL DEFAULT 0 COMMENT '总价格/总积分' ,
`discounttotal`  float NULL DEFAULT 0 COMMENT '折扣总价格' ,
`type`  int(11) NULL DEFAULT 1 COMMENT '支付类型' ,
`status`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '状态' ,
`address`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '地址' ,
PRIMARY KEY (`id`),
UNIQUE INDEX `orderid` (`orderid`) USING BTREE 
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='订单'
AUTO_INCREMENT=1635842906062
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `cart`; CREATE TABLE `cart` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`tablename`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT 'ziliaoxinxi' COMMENT '商品表名' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`goodid`  bigint(20) NOT NULL COMMENT '商品id' ,
`goodname`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '商品名称' ,
`picture`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '图片' ,
`buynumber`  int(11) NOT NULL COMMENT '购买数量' ,
`price`  float NULL DEFAULT NULL COMMENT '单价' ,
`discountprice`  float NULL DEFAULT NULL COMMENT '会员价' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='购物车表'
AUTO_INCREMENT=1625197454864
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `news`; CREATE TABLE `news` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`title`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '标题' ,
`introduction`  longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '简介' ,
`picture`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '系统公告图片' ,
`content`  longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '内容' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='系统公告'
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `storeup`; CREATE TABLE `storeup` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`refid`  bigint(20) NULL DEFAULT NULL COMMENT '收藏id' ,
`tablename`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '表名' ,
`name`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '收藏名称' ,
`picture`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '收藏图片' ,
`type`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT '1' COMMENT '类型(1:收藏,21:赞,22:踩)' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='收藏表'
AUTO_INCREMENT=1637562662544
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `consultation`; CREATE TABLE `consultation` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`sender`  bigint(20) NOT NULL COMMENT '发送者id' ,
`sender_name`  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '发送者昵称' ,
`receiver`  bigint(20) NOT NULL COMMENT '接收者id' ,
`receiver_name`  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin COMMENT '接收者昵称' ,
`send_time`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '发送时间' ,
`msg`  varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '消息内容' ,
`read_status`  int(11) NOT NULL COMMENT '读取状态' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='问诊表'
AUTO_INCREMENT=1637562662544
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `forum`; CREATE TABLE `forum` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`title`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '帖子标题' ,
`content`  longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '帖子内容' ,
`parentid`  bigint(20) NULL DEFAULT '0' COMMENT '父节点id' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`username`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '用户名' ,
`isdone`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '状态' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='论坛表'
AUTO_INCREMENT=1609987952877
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `messagess`; CREATE TABLE `messagess` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`userid`  bigint(20) NOT NULL COMMENT '留言人id' ,
`username`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '用户名' ,
`content`  longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '留言内容' ,
`cpicture`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '留言图片' ,
`reply`  longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '回复内容' ,
`rpicture`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '回复图片' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='在线留言'
AUTO_INCREMENT=1629368316361
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS crk; CREATE TABLE crk (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`refid`  bigint(20) NOT NULL COMMENT '关联表id' ,
`name`  varchar(200) NOT NULL COMMENT '出入库物品名称' ,
`sl`  bigint(20) NOT NULL COMMENT '出入库数量' ,
`crkzt` varchar(200)   DEFAULT NULL COMMENT '出入库状态' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='出入库表'
AUTO_INCREMENT=1637562662544
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `config`;CREATE TABLE `config` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '轮播图名称',
  `value` varchar(100) DEFAULT NULL COMMENT '轮播图地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='轮播图';INSERT INTO `config` VALUES(null,'genImg/1769062838001.jpg','http://oss.fuqixuan.top/genImg/1769062838001.jpg'),(null,'genImg/1769062833217.jpg','http://oss.fuqixuan.top/genImg/1769062833217.jpg');DROP TABLE IF EXISTS `token`; CREATE TABLE `token` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`username`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '用户名' ,
`tablename`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '表名' ,
`role`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '角色' ,
`token`  varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '密码' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间' ,
`expiratedtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '过期时间' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='token表'
AUTO_INCREMENT=11
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `users`; CREATE TABLE `users` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`username`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '用户名' ,
`password`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '密码' ,
`role`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT '管理员' COMMENT '角色' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='用户表'
AUTO_INCREMENT=2
ROW_FORMAT=DYNAMIC
;
INSERT INTO `users` VALUES ('1', 'admin', 'admin', '管理员', '2025-03-20 10:41:27');DROP TABLE IF EXISTS `yonghu`; CREATE TABLE yonghu( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,yonghuming  varchar(200) COMMENT '用户名',mima  varchar(200) COMMENT '密码',shoujihao  varchar(200) COMMENT '手机号',dizhi  varchar(200) COMMENT '地址',money  float NULL DEFAULT 0 COMMENT '余额',jf  float NULL DEFAULT 0 COMMENT '积分',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='用户';DROP TABLE IF EXISTS `shangjia`; CREATE TABLE shangjia( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,yonghuming  varchar(200) COMMENT '用户名',mima  varchar(200) COMMENT '密码',shoujihao  varchar(200) COMMENT '手机号',shangjiamingcheng  varchar(200) COMMENT '商家名称',money  float NULL DEFAULT 0 COMMENT '余额',jf  float NULL DEFAULT 0 COMMENT '积分',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='商家';DROP TABLE IF EXISTS `Discussshangpinguanli`; CREATE TABLE Discussshangpinguanli (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`refid`  bigint(20) NOT NULL COMMENT '关联表id' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`nickname` varchar(200)   DEFAULT NULL COMMENT '用户名' ,
`content` longtext   COMMENT '评论内容' ,
`reply` longtext  COMMENT '回复内容',
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='商品管理评论表'
;
DROP TABLE IF EXISTS `shangpinguanli`; CREATE TABLE shangpinguanli( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,shangpinmingcheng  varchar(200) COMMENT '商品名称',shangpintupian  varchar(200) COMMENT '商品图片',fenleimingcheng  varchar(200) COMMENT '分类名称',jieshao  longtext COMMENT '介绍',xiangqing  longtext COMMENT '详情',dianpumingcheng  varchar(200) COMMENT '店铺名称', userid  bigint(20) COMMENT '用户id', price float NOT NULL  COMMENT '价格',onelimittimes  int(11)  NULL DEFAULT '-1' COMMENT '单限' ,alllimittimes  int(11) NULL DEFAULT '-1' COMMENT '库存',sfsh  varchar(200)  DEFAULT '否' COMMENT '是否审核',shhf  longtext COMMENT '审核回复',thumbsupnum int(11)  NULL DEFAULT 0  COMMENT '赞',crazilynum int(11)  NULL DEFAULT 0 COMMENT '踩',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='商品管理';DROP TABLE IF EXISTS `shangpinfenlei`; CREATE TABLE shangpinfenlei( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,fenleimingcheng  varchar(200) COMMENT '分类名称',fenleitupian  varchar(200) COMMENT '分类图片',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='商品分类';DROP TABLE IF EXISTS `Discussdianpuxinxi`; CREATE TABLE Discussdianpuxinxi (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`refid`  bigint(20) NOT NULL COMMENT '关联表id' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`nickname` varchar(200)   DEFAULT NULL COMMENT '用户名' ,
`content` longtext   COMMENT '评论内容' ,
`reply` longtext  COMMENT '回复内容',
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='店铺信息评论表'
;
DROP TABLE IF EXISTS `dianpuxinxi`; CREATE TABLE dianpuxinxi( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,dianpumingcheng  varchar(200) COMMENT '店铺名称',tupian  varchar(200) COMMENT '图片',nicheng  varchar(200) COMMENT '昵称',shangjiadianhua  varchar(200) COMMENT '商家电话',dianpujianjie  longtext COMMENT '店铺简介',dianpudizhi  varchar(200) COMMENT '店铺地址', userid  bigint(20) COMMENT '用户id',lat  double(20,6)  NULL DEFAULT '-1' COMMENT 'lat',lnt  double(20,6)  NULL DEFAULT '-1' COMMENT 'lnt',conent  varchar(200)  DEFAULT '否' COMMENT '标记',sfsh  varchar(200)  DEFAULT '否' COMMENT '是否审核',shhf  longtext COMMENT '审核回复',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='店铺信息';DROP TABLE IF EXISTS `jifenshangdian`; CREATE TABLE jifenshangdian( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,shangpinmingcheng  varchar(200) COMMENT '商品名称',shangpintupian  varchar(200) COMMENT '商品图片',shangpinjianjie  longtext COMMENT '商品简介',shangpinxiangqing  longtext COMMENT '商品详情',jifen  int(11)  NULL DEFAULT '-1' COMMENT '积分',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
COMMENT='积分商店';

INSERT INTO `address` (`addtime`, `userid`, `address`, `name`, `phone`, `isdefault`) VALUES ('2026-01-22 09:15:22', 1, '北京市朝阳区建国门外大街1号国贸三期', '张三', '13800138000', '是');
INSERT INTO `address` (`addtime`, `userid`, `address`, `name`, `phone`, `isdefault`) VALUES ('2026-01-22 11:30:45', 2, '上海市浦东新区陆家嘴环路100号环球金融中心', '李四', '13912345678', '是');
INSERT INTO `address` (`addtime`, `userid`, `address`, `name`, `phone`, `isdefault`) VALUES ('2026-01-22 14:05:18', 3, '广东省深圳市南山区深南大道10000号腾讯大厦', '王五', '15098765432', '否');
INSERT INTO `address` (`addtime`, `userid`, `address`, `name`, `phone`, `isdefault`) VALUES ('2026-01-22 16:45:33', 1, '北京市海淀区中关村软件园二期联想总部', '张三', '13800138000', '否');
INSERT INTO `address` (`addtime`, `userid`, `address`, `name`, `phone`, `isdefault`) VALUES ('2026-01-22 20:20:59', 4, '浙江省杭州市余杭区文一西路969号阿里巴巴西溪园区', '赵六', '13755556666', '是');
INSERT INTO `orders` (`addtime`, `orderid`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`, `total`, `discounttotal`, `type`, `status`, `address`) VALUES ('2026-01-22 09:15:22', 'DD202601220001', 'ziliaoxinxi', 1, 1, '有机牛奶 1L装', 'http://localhost:8080/pyzkds/upload/商品_50.png', 2, 15.50, 14.00, 31.00, 28.00, 1, '已支付', '北京市朝阳区建国门外大街1号');
INSERT INTO `orders` (`addtime`, `orderid`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`, `total`, `discounttotal`, `type`, `status`, `address`) VALUES ('2026-01-22 11:30:45', 'DD202601220002', 'ziliaoxinxi', 2, 2, '全麦面包 500g', 'http://localhost:8080/pyzkds/upload/商品_51.png', 1, 12.80, 12.80, 12.80, 12.80, 2, '待发货', '上海市浦东新区陆家嘴环路100号');
INSERT INTO `orders` (`addtime`, `orderid`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`, `total`, `discounttotal`, `type`, `status`, `address`) VALUES ('2026-01-22 14:05:18', 'DD202601220003', 'ziliaoxinxi', 3, 3, '新鲜草莓 250g', 'http://localhost:8080/pyzkds/upload/商品_44.png', 3, 25.00, 22.00, 75.00, 66.00, 1, '已发货', '广州市天河区天河路208号');
INSERT INTO `orders` (`addtime`, `orderid`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`, `total`, `discounttotal`, `type`, `status`, `address`) VALUES ('2026-01-22 16:48:33', 'DD202601220004', 'ziliaoxinxi', 4, 4, '精品咖啡豆 200g', 'http://localhost:8080/pyzkds/upload/商品_31.png', 1, 68.00, 58.00, 68.00, 58.00, 3, '已完成', '深圳市南山区科技园南区');
INSERT INTO `orders` (`addtime`, `orderid`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`, `total`, `discounttotal`, `type`, `status`, `address`) VALUES ('2026-01-22 20:20:59', 'DD202601220005', 'ziliaoxinxi', 5, 5, '儿童保温杯 350ml', 'http://localhost:8080/pyzkds/upload/商品_23.png', 1, 89.90, 79.90, 89.90, 79.90, 1, '待评价', '杭州市西湖区文三路199号');
INSERT INTO `cart` (`addtime`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`) VALUES ('2026-01-22 09:15:22', 'ziliaoxinxi', 1, 1, '【官方正品】Apple iPhone 16 Pro Max 256GB', 'http://localhost:8080/pyzkds/upload/商品_50.png', 1, 9999.00, 9599.00);
INSERT INTO `cart` (`addtime`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`) VALUES ('2026-01-22 14:30:45', 'ziliaoxinxi', 2, 2, '华为 Mate 70 Pro+ 512GB 麒麟芯片', 'http://localhost:8080/pyzkds/upload/商品_51.png', 2, 8999.00, 8699.00);
INSERT INTO `cart` (`addtime`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`) VALUES ('2026-01-22 16:05:18', 'ziliaoxinxi', 3, 3, '小米 15 Ultra 徕卡影像 1TB', 'http://localhost:8080/pyzkds/upload/商品_44.png', 1, 6499.00, 6299.00);
INSERT INTO `cart` (`addtime`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`) VALUES ('2026-01-22 11:48:33', 'ziliaoxinxi', 4, 4, '索尼 PlayStation 6 光驱版', 'http://localhost:8080/pyzkds/upload/商品_31.png', 1, 4999.00, 4799.00);
INSERT INTO `cart` (`addtime`, `tablename`, `userid`, `goodid`, `goodname`, `picture`, `buynumber`, `price`, `discountprice`) VALUES ('2026-01-22 20:22:07', 'ziliaoxinxi', 5, 5, '戴尔 XPS 15 2026款 i9/32G/2TB', 'http://localhost:8080/pyzkds/upload/商品_23.png', 1, 18999.00, 18499.00);
INSERT INTO `news` (`addtime`, `title`, `introduction`, `picture`, `content`) VALUES ('2026-01-22 09:15:23', '关于系统维护升级的通知', '为提升服务质量，系统将于近期进行例行维护升级，期间部分功能可能短暂无法访问。', 'http://localhost:8080/pyzkds/upload/公告_9.png', '尊敬的各位用户：\n\n为提供更稳定、高效的服务体验，技术团队计划于2026年1月25日凌晨02:00至05:00对系统进行例行维护与升级。维护期间，网站及移动端部分功能可能出现短暂中断或访问缓慢的情况。\n\n请您提前安排好相关工作，避免在维护期间进行关键业务操作。维护结束后，所有服务将恢复正常。感谢您的理解与支持！\n\n如有任何疑问，请联系客服。');
INSERT INTO `news` (`addtime`, `title`, `introduction`, `picture`, `content`) VALUES ('2026-01-22 14:30:45', '2026年春节假期服务安排公告', '2026年春节假期期间，客服及物流服务时间将有所调整，敬请广大用户知悉。', 'http://localhost:8080/pyzkds/upload/公告_22.png', '亲爱的用户朋友们：\n\n新春佳节将至，根据国家法定节假日安排，结合我司实际情况，现将2026年春节假期服务时间调整如下：\n\n1. 在线客服：2026年1月28日（除夕）至1月30日（初二）暂停服务，1月31日（初三）起恢复正常。\n2. 电话客服：假期期间提供紧急事务受理服务，服务时间为每日09:00-18:00。\n3. 物流配送：1月27日至2月2日期间下单的商品，将于2月3日起陆续安排发货。\n\n祝您新春快乐，阖家幸福！');
INSERT INTO `news` (`addtime`, `title`, `introduction`, `picture`, `content`) VALUES ('2026-01-22 11:05:18', '新功能上线：智能推荐算法优化', '本次更新优化了商品推荐算法，能够更精准地为您推荐感兴趣的内容，提升使用体验。', 'http://localhost:8080/pyzkds/upload/公告_15.png', '为了给您带来更个性化、更贴心的服务，我们于近日完成了智能推荐算法的重大升级。\n\n**主要优化点包括：**\n- **精准度提升**：基于更丰富的用户行为数据，模型推荐准确率提升约25%。\n- **多样性增强**：在保证相关性的同时，增加了推荐结果的多样性，帮助您发现更多潜在兴趣点。\n- **实时性优化**：推荐结果能够更快地响应您的最新浏览和操作记录。\n\n您可以在“猜你喜欢”、“为您推荐”等板块体验优化后的效果。欢迎提出宝贵意见！');
INSERT INTO `news` (`addtime`, `title`, `introduction`, `picture`, `content`) VALUES ('2026-01-22 16:45:32', '用户隐私保护政策更新说明', '为适应相关法律法规要求，我们更新了《用户隐私保护政策》，请您抽空阅读。', 'http://localhost:8080/pyzkds/upload/公告_25.png', '尊敬的平台用户：\n\n我们始终将用户数据安全与隐私保护置于首位。为更好地保障您的权益，并遵循最新的国家法律法规和行业标准，我们已于2026年1月20日对《用户隐私保护政策》进行了修订。\n\n**本次更新的主要内容涉及：**\n1.  进一步明确了我们收集、使用、存储和保护您个人信息的方式与目的。\n2.  细化了您访问、更正、删除个人信息以及撤回授权同意的权利与路径。\n3.  更新了关于第三方合作伙伴共享信息的管理条款。\n\n更新后的政策已正式生效。请您登录账户，在“设置-隐私政策”中查阅完整内容。继续使用我们的服务，即表示您已阅读并同意更新后的政策。');
INSERT INTO `news` (`addtime`, `title`, `introduction`, `picture`, `content`) VALUES ('2026-01-22 10:20:05', '关于开展“新春送福”活动的预告', '喜迎新春，平台将推出“新春送福”系列优惠活动，多重好礼等您来拿！', 'http://localhost:8080/pyzkds/upload/公告_24.png', '新年新气象，福气满堂春！为感谢广大用户一直以来的支持，平台计划于2026年1月25日至2月10日期间，推出“新春送福”大型主题促销活动。\n\n**活动亮点抢先看：**\n- **福气红包**：每日登录可领取随机现金红包，无门槛使用。\n- **年货秒杀**：精选爆款年货，每日三个时段限时秒杀。\n- **满额赠礼**：订单满额即赠新春定制礼品或优惠券。\n- **分享有礼**：邀请好友注册下单，双方均可获得奖励。\n\n具体活动规则和参与方式将于活动开始前在APP首页公布，敬请期待！祝您购物愉快，福气满满！');
INSERT INTO `storeup` (`addtime`, `userid`, `refid`, `tablename`, `name`, `picture`, `type`) VALUES ('2026-01-22 09:15:22', 1, 101, 'shangpinxinxi', '高端智能手机', 'http://localhost:8080/pyzkds/upload/商品_50.png', '1');
INSERT INTO `storeup` (`addtime`, `userid`, `refid`, `tablename`, `name`, `picture`, `type`) VALUES ('2026-01-22 14:30:45', 2, 25, 'news', '系统维护通知', 'http://localhost:8080/pyzkds/upload/公告_9.png', '1');
INSERT INTO `storeup` (`addtime`, `userid`, `refid`, `tablename`, `name`, `picture`, `type`) VALUES ('2026-01-22 11:05:18', 3, 56, 'shangpinxinxi', '无线蓝牙耳机', 'http://localhost:8080/pyzkds/upload/商品_51.png', '21');
INSERT INTO `storeup` (`addtime`, `userid`, `refid`, `tablename`, `name`, `picture`, `type`) VALUES ('2026-01-22 16:48:33', 4, 12, 'news', '春节放假安排', 'http://localhost:8080/pyzkds/upload/公告_22.png', '22');
INSERT INTO `storeup` (`addtime`, `userid`, `refid`, `tablename`, `name`, `picture`, `type`) VALUES ('2026-01-22 20:20:59', 5, 78, 'shangpinxinxi', '轻薄笔记本电脑', 'http://localhost:8080/pyzkds/upload/商品_44.png', '1');
INSERT INTO `consultation` (`sender`, `sender_name`, `receiver`, `receiver_name`, `send_time`, `msg`, `read_status`) VALUES (1, '张伟', 2, '李医生', '2026-01-22 09:15:22', '李医生您好，我最近三天一直咳嗽，有少量黄痰，需要吃什么药？', 1);
INSERT INTO `consultation` (`sender`, `sender_name`, `receiver`, `receiver_name`, `send_time`, `msg`, `read_status`) VALUES (2, '李医生', 1, '张伟', '2026-01-22 09:18:05', '张先生您好，除了咳嗽，有发烧或者胸闷气短的症状吗？', 1);
INSERT INTO `consultation` (`sender`, `sender_name`, `receiver`, `receiver_name`, `send_time`, `msg`, `read_status`) VALUES (1, '张伟', 2, '李医生', '2026-01-22 09:20:47', '体温正常，就是喉咙有点痛，感觉呼吸有点费力。', 0);
INSERT INTO `consultation` (`sender`, `sender_name`, `receiver`, `receiver_name`, `send_time`, `msg`, `read_status`) VALUES (3, '王芳', 4, '刘主任', '2026-01-22 14:30:11', '刘主任，我上周的体检报告出来了，有几项指标偏高，想请您帮忙看看。', 1);
INSERT INTO `consultation` (`sender`, `sender_name`, `receiver`, `receiver_name`, `send_time`, `msg`, `read_status`) VALUES (4, '刘主任', 3, '王芳', '2026-01-22 16:05:38', '好的，请把报告单拍照发给我看一下。', 0);
INSERT INTO `forum` (`addtime`, `title`, `content`, `parentid`, `userid`, `username`, `isdone`) VALUES ('2026-01-22 09:15:22', '关于Python异步编程的最佳实践讨论', '最近在项目中使用asyncio遇到了一些性能瓶颈，想和大家探讨一下如何优化协程调度和避免阻塞操作。有没有在实际生产环境中大规模使用异步框架的经验可以分享？', 0, 1, '技术达人小明', '进行中');
INSERT INTO `forum` (`addtime`, `title`, `content`, `parentid`, `userid`, `username`, `isdone`) VALUES ('2026-01-22 14:30:45', '回复：关于Python异步编程的最佳实践讨论', '@技术达人小明 我们团队在微服务通信中大量使用了aiohttp和asyncpg。关键点是要确保所有I/O操作都是异步的，并且使用连接池。另外，监控和日志记录也需要适配异步上下文。', 1, 2, '架构师老王', '已完成');
INSERT INTO `forum` (`addtime`, `title`, `content`, `parentid`, `userid`, `username`, `isdone`) VALUES ('2026-01-22 11:05:18', '新手求助：Docker容器网络配置问题', '我在本地搭建了多个服务的Docker容器，但容器间无法通过服务名互相访问。docker-compose.yml文件已经定义了自定义网络，但似乎DNS解析不工作。求排查思路！', 0, 3, '运维小白菜', '进行中');
INSERT INTO `forum` (`addtime`, `title`, `content`, `parentid`, `userid`, `username`, `isdone`) VALUES ('2026-01-22 16:42:33', '回复：新手求助：Docker容器网络配置问题', '检查一下你的docker-compose版本和Docker引擎版本是否兼容。另外，确保所有服务都在同一个自定义网络下，并且使用`depends_on`可能不足以等待服务完全启动，建议增加健康检查。', 3, 4, '容器专家李工', '进行中');
INSERT INTO `forum` (`addtime`, `title`, `content`, `parentid`, `userid`, `username`, `isdone`) VALUES ('2026-01-22 10:20:05', '2026年全栈开发技术栈趋势预测', '结合近期社区动态和招聘需求，预测新的一年里Rust在前端工具链、WebAssembly在边缘计算、以及Serverless数据库可能会成为新的热点。大家怎么看？', 0, 5, '趋势观察员', '已完成');
INSERT INTO `messagess` (`addtime`, `userid`, `username`, `content`, `cpicture`, `reply`, `rpicture`) VALUES ('2026-01-22 09:15:22', 1, '张伟', '这款产品的续航能力真的非常出色，完全满足了我一整天的外出使用需求，充电速度也很快。', 'http://localhost:8080/pyzkds/upload/留言_32.png', '感谢您的认可！我们采用了新一代的电池技术，未来还会在快充方面继续优化，敬请期待。', NULL);
INSERT INTO `messagess` (`addtime`, `userid`, `username`, `content`, `cpicture`, `reply`, `rpicture`) VALUES ('2026-01-22 14:30:45', 2, '李娜', '系统更新后感觉界面流畅了很多，但夜间模式的对比度可以再调整一下吗？长时间看有点刺眼。', 'http://localhost:8080/pyzkds/upload/留言_27.png', '您好，您的反馈已收到。UI团队正在评估夜间模式的色彩方案，预计下个小版本会进行优化。', NULL);
INSERT INTO `messagess` (`addtime`, `userid`, `username`, `content`, `cpicture`, `reply`, `rpicture`) VALUES ('2026-01-22 11:05:18', 3, '王磊', '咨询一下，购买后是否支持跨平台的数据同步？比如在手机端编辑，在电脑端可以实时看到。', 'http://localhost:8080/pyzkds/upload/留言_8.png', '支持的。我们的服务端会实时同步您的数据，只要设备登录同一账号，即可在多端无缝切换使用。', NULL);
INSERT INTO `messagess` (`addtime`, `userid`, `username`, `content`, `cpicture`, `reply`, `rpicture`) VALUES ('2026-01-22 16:48:33', 4, '赵静', '物流速度超快，隔天就收到了。包装也很严实，没有损坏。给配送小哥点个赞！', 'http://localhost:8080/pyzkds/upload/留言_24.png', '谢谢您的表扬！我们会将您的鼓励传达给物流团队，继续为大家提供高效安全的配送服务。', NULL);
INSERT INTO `messagess` (`addtime`, `userid`, `username`, `content`, `cpicture`, `reply`, `rpicture`) VALUES ('2026-01-22 20:12:07', 5, '孙超', '教程视频里的步骤很清晰，跟着操作很快就上手了。建议可以增加一些高级功能的专题教程。', 'http://localhost:8080/pyzkds/upload/留言_13.png', '非常好的建议！我们正在规划一系列进阶教程，涵盖更多专业功能，将在下个月陆续上线。', NULL);
INSERT INTO crk (addtime, refid, name, sl, crkzt) VALUES ('2026-01-22 09:15:22', 1, '联想笔记本电脑', 50, '入库');
INSERT INTO crk (addtime, refid, name, sl, crkzt) VALUES ('2026-01-22 11:30:45', 2, '华为MatePad Pro', 30, '出库');
INSERT INTO crk (addtime, refid, name, sl, crkzt) VALUES ('2026-01-22 14:05:18', 3, '戴尔显示器', 100, '入库');
INSERT INTO crk (addtime, refid, name, sl, crkzt) VALUES ('2026-01-22 16:45:33', 4, '罗技无线鼠标', 200, '出库');
INSERT INTO crk (addtime, refid, name, sl, crkzt) VALUES ('2026-01-22 20:10:07', 5, '苹果iPhone手机', 25, '入库');
INSERT INTO `config` (`name`, `value`) VALUES ('首页主推广告', 'http://localhost:8080/pyzkds/upload/轮播图_29.png');
INSERT INTO `config` (`name`, `value`) VALUES ('新品上市推荐', 'http://localhost:8080/pyzkds/upload/轮播图_24.png');
INSERT INTO `config` (`name`, `value`) VALUES ('节日促销活动', 'http://localhost:8080/pyzkds/upload/轮播图_1.png');
INSERT INTO `config` (`name`, `value`) VALUES ('品牌合作展示', 'http://localhost:8080/pyzkds/upload/轮播图_8.png');
INSERT INTO `config` (`name`, `value`) VALUES ('会员专享福利', 'http://localhost:8080/pyzkds/upload/轮播图_4.png');
INSERT INTO `token` (`userid`, `username`, `tablename`, `role`, `token`, `addtime`, `expiratedtime`) VALUES (1, '张三', 'yonghu', '用户', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c', '2026-01-22 09:15:22', '2026-01-22 12:15:22');
INSERT INTO `token` (`userid`, `username`, `tablename`, `role`, `token`, `addtime`, `expiratedtime`) VALUES (2, '李四', 'yonghu', '用户', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c', '2026-01-22 14:30:45', '2026-01-22 17:30:45');
INSERT INTO `token` (`userid`, `username`, `tablename`, `role`, `token`, `addtime`, `expiratedtime`) VALUES (3, '王五', 'shangjia', '商家', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c', '2026-01-22 11:05:18', '2026-01-22 14:05:18');
INSERT INTO `token` (`userid`, `username`, `tablename`, `role`, `token`, `addtime`, `expiratedtime`) VALUES (4, '赵六', 'yonghu', '用户', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c', '2026-01-22 16:45:33', '2026-01-22 19:45:33');
INSERT INTO `token` (`userid`, `username`, `tablename`, `role`, `token`, `addtime`, `expiratedtime`) VALUES (5, '钱七', 'shangjia', '商家', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c', '2026-01-22 20:10:07', '2026-01-22 23:10:07');
INSERT INTO `users` (`username`, `password`, `role`, `addtime`) VALUES ('admin', 'e10adc3949ba59abbe56e057f20f883e', '超级管理员', '2026-01-22 09:15:22');
INSERT INTO `users` (`username`, `password`, `role`, `addtime`) VALUES ('zhangsan', 'e10adc3949ba59abbe56e057f20f883e', '商品管理员', '2026-01-22 10:30:45');
INSERT INTO `users` (`username`, `password`, `role`, `addtime`) VALUES ('lisi', 'e10adc3949ba59abbe56e057f20f883e', '订单管理员', '2026-01-22 14:05:18');
INSERT INTO `users` (`username`, `password`, `role`, `addtime`) VALUES ('wangwu', 'e10adc3949ba59abbe56e057f20f883e', '客服', '2026-01-22 16:45:33');
INSERT INTO `users` (`username`, `password`, `role`, `addtime`) VALUES ('zhaoliu', 'e10adc3949ba59abbe56e057f20f883e', '普通用户', '2026-01-22 20:22:07');
INSERT INTO yonghu (yonghuming, mima, shoujihao, dizhi, money, jf, addtime) VALUES ('张伟', 'zhangwei123', '13800138001', '北京市朝阳区建国门外大街1号', 1250.50, 150, '2026-01-22 09:15:22');
INSERT INTO yonghu (yonghuming, mima, shoujihao, dizhi, money, jf, addtime) VALUES ('李娜', 'lina456', '13912345678', '上海市浦东新区陆家嘴环路100号', 3200.00, 320, '2026-01-22 14:30:45');
INSERT INTO yonghu (yonghuming, mima, shoujihao, dizhi, money, jf, addtime) VALUES ('王芳', 'wangfang789', '13698765432', '广州市天河区天河路208号', 580.75, 58, '2026-01-22 11:05:18');
INSERT INTO yonghu (yonghuming, mima, shoujihao, dizhi, money, jf, addtime) VALUES ('刘洋', 'liuyang101', '15111223344', '深圳市南山区科技园南区', 2100.00, 210, '2026-01-22 16:48:33');
INSERT INTO yonghu (yonghuming, mima, shoujihao, dizhi, money, jf, addtime) VALUES ('陈静', 'chenjing2026', '18807654321', '杭州市西湖区文三路398号', 50.25, 5, '2026-01-22 20:22:07');
INSERT INTO shangjia (yonghuming, mima, shoujihao, shangjiamingcheng, money, jf, addtime) VALUES ('tech_king', 'e10adc3949ba59abbe56e057f20f883e', '13800138001', '科技数码旗舰店', 12500.50, 1200, '2026-01-22 09:15:22');
INSERT INTO shangjia (yonghuming, mima, shoujihao, shangjiamingcheng, money, jf, addtime) VALUES ('fresh_life', 'd41d8cd98f00b204e9800998ecf8427e', '13912345678', '生鲜果蔬直供', 8560.00, 850, '2026-01-22 11:30:45');
INSERT INTO shangjia (yonghuming, mima, shoujihao, shangjiamingcheng, money, jf, addtime) VALUES ('book_worm', '5f4dcc3b5aa765d61d8327deb882cf99', '13765432109', '书香门第书店', 3200.75, 320, '2026-01-22 14:05:18');
INSERT INTO shangjia (yonghuming, mima, shoujihao, shangjiamingcheng, money, jf, addtime) VALUES ('fashion_guru', '96e79218965eb72c92a549dd5a330112', '13698765432', '潮流服饰精品店', 18900.20, 1890, '2026-01-22 16:45:33');
INSERT INTO shangjia (yonghuming, mima, shoujihao, shangjiamingcheng, money, jf, addtime) VALUES ('home_deco', '25d55ad283aa400af464c76d713c07ad', '13511223344', '家居装饰生活馆', 7420.60, 740, '2026-01-22 20:20:59');
INSERT INTO Discussshangpinguanli (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 09:15:22', 1, 1, '数码爱好者小王', '这款手机的屏幕显示效果非常出色，色彩鲜艳，看视频体验很棒。续航能力也符合官方宣传，中度使用一天没问题。', '感谢您的认可！我们这款手机确实在屏幕和续航上做了大量优化。');
INSERT INTO Discussshangpinguanli (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 14:30:45', 2, 2, '健身达人李姐', '运动手表的心率监测很准，GPS定位也快。就是表带材质夏天出汗后有点闷，希望能有更多透气材质的选择。', '您好，您的反馈非常宝贵。我们已记录您的需求，会反馈给产品团队评估。目前有第三方编织表带可选，透气性更好。');
INSERT INTO Discussshangpinguanli (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 16:05:18', 3, 3, '美食家老陈', '空气炸锅操作简单，烤出来的鸡翅外酥里嫩，而且不用放油，更健康。清洗也很方便。', '很高兴您喜欢！健康烹饪正是我们产品的设计初衷。');
INSERT INTO Discussshangpinguanli (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 11:20:33', 1, 4, '学生小明', '拍照效果不错，特别是夜景模式。但是手机运行大型游戏时，后背发热有点明显。', '您好，关于发热问题，建议在游戏设置中适当调低画质，并确保系统为最新版本，我们持续通过系统更新优化性能与温控。');
INSERT INTO Discussshangpinguanli (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 19:45:07', 4, 5, '白领小雅', '蓝牙耳机音质很好，降噪效果满意，通勤路上很安静。充电仓有点大，如果能做得更小巧便携就更好了。', '感谢您的建议！我们在下一代产品设计中会重点考虑充电仓的便携性优化。');
INSERT INTO shangpinguanli (addtime, shangpinmingcheng, shangpintupian, fenleimingcheng, jieshao, xiangqing, dianpumingcheng, userid, price, onelimittimes, alllimittimes, sfsh, shhf, thumbsupnum, crazilynum) VALUES ('2026-01-22 09:15:23', 'Apple iPhone 16 Pro Max', 'http://localhost:8080/pyzkds/upload/商品_50.png', '手机数码', '新一代A18仿生芯片，6.9英寸超视网膜XDR显示屏，4800万像素主摄，支持5G网络。', '详细参数：屏幕尺寸6.9英寸，分辨率2796x1290，处理器A18仿生芯片，内存1TB，电池容量4500mAh，支持MagSafe无线充电。', '苹果官方旗舰店', 1, 9999.00, 2, 50, '是', '商品信息完整，审核通过。', 125, 3);
INSERT INTO shangpinguanli (addtime, shangpinmingcheng, shangpintupian, fenleimingcheng, jieshao, xiangqing, dianpumingcheng, userid, price, onelimittimes, alllimittimes, sfsh, shhf, thumbsupnum, crazilynum) VALUES ('2026-01-22 14:30:45', '华为 Mate 70 Pro', 'http://localhost:8080/pyzkds/upload/商品_51.png', '手机数码', '搭载麒麟9100芯片，昆仑玻璃2.0，XMAGE影像系统，卫星通信双向收发。', '详细参数：屏幕尺寸6.8英寸OLED，分辨率2848x1312，处理器麒麟9100，内存512GB，电池容量5000mAh，支持100W有线快充。', '华为授权体验店', 2, 7999.00, 1, 30, '是', '国货精品，审核通过。', 89, 5);
INSERT INTO shangpinguanli (addtime, shangpinmingcheng, shangpintupian, fenleimingcheng, jieshao, xiangqing, dianpumingcheng, userid, price, onelimittimes, alllimittimes, sfsh, shhf, thumbsupnum, crazilynum) VALUES ('2026-01-22 11:05:18', '小米14 Ultra 徕卡影像套装', 'http://localhost:8080/pyzkds/upload/商品_44.png', '手机数码', '徕卡全焦段四摄，2K超色准屏，骁龙8 Gen 3处理器，澎湃OS系统。', '详细参数：后置5000万像素主摄+5000万像素超广角+5000万像素长焦，屏幕6.73英寸AMOLED，电池容量5300mAh，支持90W有线快充和50W无线快充。', '小米之家', 3, 6499.00, 3, 45, '是', '影像旗舰，配置齐全，审核通过。', 210, 8);
INSERT INTO shangpinguanli (addtime, shangpinmingcheng, shangpintupian, fenleimingcheng, jieshao, xiangqing, dianpumingcheng, userid, price, onelimittimes, alllimittimes, sfsh, shhf, thumbsupnum, crazilynum) VALUES ('2026-01-22 16:48:32', '索尼 PlayStation 5 Pro', 'http://localhost:8080/pyzkds/upload/商品_31.png', '家用电器', '性能强化版PS5，支持8K分辨率，光线追踪性能大幅提升，配备1TB SSD。', '详细参数：CPU Zen 2 8核心，GPU RDNA 3架构，内存16GB GDDR6，存储1TB NVMe SSD，支持4K 120Hz和8K输出。', '索尼官方专卖店', 4, 4999.00, 1, 25, '否', '商品图片需补充实拍图，暂未审核。', 0, 0);
INSERT INTO shangpinguanli (addtime, shangpinmingcheng, shangpintupian, fenleimingcheng, jieshao, xiangqing, dianpumingcheng, userid, price, onelimittimes, alllimittimes, sfsh, shhf, thumbsupnum, crazilynum) VALUES ('2026-01-22 20:12:07', '戴尔 XPS 15 2026款', 'http://localhost:8080/pyzkds/upload/商品_23.png', '电脑办公', '英特尔酷睿Ultra 9处理器，32GB内存，2TB SSD，15.6英寸4K OLED触控屏。', '详细参数：处理器Intel Core Ultra 9 185H，显卡RTX 4070 Laptop GPU，屏幕分辨率3840x2400，接口Thunderbolt 4 x2，重量1.8kg。', '戴尔官方商城', 5, 15999.00, -1, 15, '是', '高端创作本，配置顶级，审核通过。', 42, 1);
INSERT INTO shangpinfenlei (addtime, fenleimingcheng, fenleitupian) VALUES ('2026-01-22 09:15:22', '新鲜水果', 'http://localhost:8080/pyzkds/upload/分类_19.png');
INSERT INTO shangpinfenlei (addtime, fenleimingcheng, fenleitupian) VALUES ('2026-01-22 10:30:45', '休闲零食', 'http://localhost:8080/pyzkds/upload/分类_20.png');
INSERT INTO shangpinfenlei (addtime, fenleimingcheng, fenleitupian) VALUES ('2026-01-22 14:05:18', '酒水饮料', 'http://localhost:8080/pyzkds/upload/分类_17.png');
INSERT INTO shangpinfenlei (addtime, fenleimingcheng, fenleitupian) VALUES ('2026-01-22 16:45:33', '粮油调味', 'http://localhost:8080/pyzkds/upload/分类_16.png');
INSERT INTO shangpinfenlei (addtime, fenleimingcheng, fenleitupian) VALUES ('2026-01-22 20:20:59', '乳品烘焙', 'http://localhost:8080/pyzkds/upload/分类_9.png');
INSERT INTO Discussdianpuxinxi (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 09:15:23', 1, 1, '美食探索者小王', '这家店的招牌菜味道非常正宗，食材新鲜，分量也足，强烈推荐！', '感谢您的认可，我们会继续坚持品质，期待您的再次光临！');
INSERT INTO Discussdianpuxinxi (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 11:30:45', 2, 2, '周末探店达人', '环境优雅，服务热情，上菜速度很快。就是停车位稍微有点紧张。', '您好，感谢您的宝贵意见。关于停车问题，我们已与周边停车场协商了专属优惠，详情可咨询前台。');
INSERT INTO Discussdianpuxinxi (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 14:08:17', 3, 3, '老顾客张先生', '已经是第三次来了，品质一如既往的稳定，孩子特别喜欢这里的甜品。', '谢谢张先生一家长期以来的支持！我们特意为您预留了一份新品试吃券，下次来可以品尝哦。');
INSERT INTO Discussdianpuxinxi (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 17:45:52', 4, 4, '美食点评家Lisa', '菜品摆盘精致，口味层次丰富。建议可以增加一些适合单人食用的套餐。', '非常感谢您的专业建议！我们正在研发新的单人及双人套餐，预计下个月上线，敬请期待。');
INSERT INTO Discussdianpuxinxi (addtime, refid, userid, nickname, content, reply) VALUES ('2026-01-22 20:20:38', 5, 5, '团建组织者Mike', '上周公司团建订了这里，同事们反馈都很好，场地和菜品都符合要求。', '能为您公司的团建活动提供满意的服务是我们的荣幸，欢迎下次团队活动继续选择我们！');
INSERT INTO dianpuxinxi (addtime, dianpumingcheng, tupian, nicheng, shangjiadianhua, dianpujianjie, dianpudizhi, userid, lat, lnt, conent, sfsh, shhf) VALUES ('2026-01-22 09:15:23', '星巴克咖啡(人民广场店)', 'http://localhost:8080/pyzkds/upload/商品_50.png', '咖啡达人', '13800138001', '提供高品质的咖啡与轻食，舒适的环境适合商务洽谈与朋友小聚。', '上海市黄浦区人民大道100号', 1, 31.230416, 121.473701, '是', '是', '资料齐全，审核通过。');
INSERT INTO dianpuxinxi (addtime, dianpumingcheng, tupian, nicheng, shangjiadianhua, dianpujianjie, dianpudizhi, userid, lat, lnt, conent, sfsh, shhf) VALUES ('2026-01-22 14:30:45', '海底捞火锅(北京路店)', 'http://localhost:8080/pyzkds/upload/商品_51.png', '火锅爱好者', '13900139002', '以极致服务闻名的火锅连锁品牌，提供多种锅底和新鲜食材。', '广州市越秀区北京路168号', 2, 23.129110, 113.264385, '否', '是', '经营资质已验证。');
INSERT INTO dianpuxinxi (addtime, dianpumingcheng, tupian, nicheng, shangjiadianhua, dianpujianjie, dianpudizhi, userid, lat, lnt, conent, sfsh, shhf) VALUES ('2026-01-22 11:05:18', '西西弗书店', 'http://localhost:8080/pyzkds/upload/商品_44.png', '书虫小张', '13600136003', '集图书、咖啡、文创于一体的复合式文化空间，定期举办读书沙龙。', '深圳市南山区深南大道9668号', 3, 22.543099, 114.057868, '是', '否', '等待补充文化经营许可证。');
INSERT INTO dianpuxinxi (addtime, dianpumingcheng, tupian, nicheng, shangjiadianhua, dianpujianjie, dianpudizhi, userid, lat, lnt, conent, sfsh, shhf) VALUES ('2026-01-22 16:48:32', '外婆家(杭州大厦店)', 'http://localhost:8080/pyzkds/upload/商品_31.png', '杭帮菜主厨', '13700137004', '主打杭帮菜，口味地道，价格亲民，是家庭聚餐的热门选择。', '杭州市拱墅区武林广场1号杭州大厦C座', 4, 30.274085, 120.155070, '否', '是', '审核通过，已上架。');
INSERT INTO dianpuxinxi (addtime, dianpumingcheng, tupian, nicheng, shangjiadianhua, dianpujianjie, dianpudizhi, userid, lat, lnt, conent, sfsh, shhf) VALUES ('2026-01-22 20:12:05', '苹果官方零售店', 'http://localhost:8080/pyzkds/upload/商品_23.png', 'TechGeek', '400-666-8800', 'Apple产品官方直营店，提供全系列产品体验、购买及技术支持服务。', '成都市锦江区红星路三段1号IFS国际金融中心', 5, 30.659462, 104.065735, '是', '是', '品牌官方授权，资料完备。');
INSERT INTO jifenshangdian (addtime, shangpinmingcheng, shangpintupian, shangpinjianjie, shangpinxiangqing, jifen) VALUES ('2026-01-22 09:15:23', '无线蓝牙降噪耳机', 'http://localhost:8080/pyzkds/upload/商品_50.png', '高品质主动降噪，续航长达30小时，支持无线充电。', '采用混合主动降噪技术，可消除高达95%的环境噪音。内置12mm驱动单元，音质清晰饱满。支持蓝牙5.2，连接稳定。配备Type-C充电接口，充电10分钟可使用2小时。', 1500);
INSERT INTO jifenshangdian (addtime, shangpinmingcheng, shangpintupian, shangpinjianjie, shangpinxiangqing, jifen) VALUES ('2026-01-22 11:30:45', '便携式咖啡随行杯', 'http://localhost:8080/pyzkds/upload/商品_51.png', '双层不锈钢保温保冷，一键开盖，防漏设计。', '采用304不锈钢内胆，保温效果长达12小时，保冷效果长达24小时。杯口设计圆润，饮用舒适。密封硅胶圈，倒置不漏水。容量为480ml，满足日常饮水需求。', 800);
INSERT INTO jifenshangdian (addtime, shangpinmingcheng, shangpintupian, shangpinjianjie, shangpinxiangqing, jifen) VALUES ('2026-01-22 14:22:18', '多功能智能手环', 'http://localhost:8080/pyzkds/upload/商品_44.png', '心率监测、睡眠分析、多种运动模式，彩屏显示。', '1.47英寸AMOLED彩色触摸屏，显示清晰。支持24小时心率监测、血氧检测。内置GPS，可独立记录运动轨迹。支持50米防水，游泳时可佩戴。续航时间可达14天。', 1200);
INSERT INTO jifenshangdian (addtime, shangpinmingcheng, shangpintupian, shangpinjianjie, shangpinxiangqing, jifen) VALUES ('2026-01-22 16:05:37', '经典文学名著套装', 'http://localhost:8080/pyzkds/upload/商品_31.png', '精选世界文学经典作品，精装典藏版。', '套装包含《百年孤独》、《傲慢与偏见》、《悲惨世界》等10部世界名著。采用环保纸张印刷，字体清晰护眼。精装硬壳封面，适合收藏与馈赠。', 2500);
INSERT INTO jifenshangdian (addtime, shangpinmingcheng, shangpintupian, shangpinjianjie, shangpinxiangqing, jifen) VALUES ('2026-01-22 20:48:59', '家用多功能空气炸锅', 'http://localhost:8080/pyzkds/upload/商品_23.png', '无油健康烹饪，智能触控，大容量设计。', '5.5升大容量，满足3-5人家庭需求。采用360度热风循环技术，食物受热均匀。支持煎、炸、烤、烘多种功能。预设8种常用菜单，一键操作。分离式炸篮，清洗方便。', 1800);