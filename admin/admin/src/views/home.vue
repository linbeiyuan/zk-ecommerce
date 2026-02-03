<script setup lang="ts" name="Home">
import { ref, onMounted, onUnmounted, computed, shallowRef } from 'vue';
import type { CSSProperties } from 'vue';

// --- Reactive State ---
const mouseX = ref(0);
const mouseY = ref(0);
const canvasRef = shallowRef<HTMLCanvasElement | null>(null);
const containerRef = shallowRef<HTMLElement | null>(null);

interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  radius: number;
  color: string;
}

let particles: Particle[] = [];
const particleCount = 100;
const maxConnectDistance = 120;

// --- Lifecycle Hooks ---
onMounted(() => {
  const canvas = canvasRef.value;
  const ctx = canvas?.getContext('2d');
  if (!canvas || !ctx) return;

  const resizeCanvas = () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    initParticles();
  };

  const initParticles = () => {
    particles = [];
    const colors = ['#42d392', '#647eff', '#ff7ab4', '#f8b400'];
    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 0.5,
        vy: (Math.random() - 0.5) * 0.5,
        radius: Math.random() * 2 + 1,
        color: colors[Math.floor(Math.random() * colors.length)]
      });
    }
  };
  
  const animate = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw connections
    for (let i = 0; i < particleCount; i++) {
      for (let j = i; j < particleCount; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < maxConnectDistance) {
          ctx.beginPath();
          ctx.strokeStyle = `rgba(100, 126, 255, ${1 - distance / maxConnectDistance})`;
          ctx.lineWidth = 0.5;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
    
    // Draw and update particles
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.vy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.fill();
    });

    requestAnimationFrame(animate);
  };

  window.addEventListener('resize', resizeCanvas);
  document.addEventListener('mousemove', handleMouseMove);
  resizeCanvas();
  animate();
});

onUnmounted(() => {
  // Cleanup would go here (remove listeners, cancel animation frame)
});

// --- Mouse & Computed ---
const handleMouseMove = (event: MouseEvent) => {
  mouseX.value = event.clientX;
  mouseY.value = event.clientY;
};

const cardTransformStyle = computed(() => {
  if (!containerRef.value) return {};
  const { clientWidth, clientHeight } = containerRef.value;
  const rotateX = ((mouseY.value / clientHeight) - 0.5) * -30; // Invert for natural feel
  const rotateY = ((mouseX.value / clientWidth) - 0.5) * 30;
  return {
    transform: `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1, 1, 1)`,
    transition: 'transform 0.1s ease-out'
  };
});

const backgroundStyle = computed(() => {
  const xPercent = mouseX.value / window.innerWidth * 100;
  const yPercent = mouseY.value / window.innerHeight * 100;
  return {
    background: `radial-gradient(circle at ${xPercent}% ${yPercent}%, rgba(66, 211, 146, 0.15), transparent 30%), radial-gradient(circle at ${100 - xPercent}% ${100 - yPercent}%, rgba(100, 126, 255, 0.15), transparent 40%)`
  };
});
</script>

<template>
  <div ref="containerRef" class="home-container" :style="backgroundStyle">
    <canvas ref="canvasRef" class="particles-canvas"></canvas>
    <div class="content-wrapper" :style="cardTransformStyle">
      <h1 class="title">基于CI/CD的电商管理平台</h1>
      <p class="subtitle">高效管理，智慧经营，助力商家腾飞。</p>
      <p class="details">
        欢迎使用电商管理平台！在这里，您可以轻松管理店铺信息、商品库存、订单处理和用户评论。我们致力于为商家提供便捷高效的一站式电商管理解决方案，让您专注于业务增长，实现销售目标。开启您的智慧电商之旅吧！
      </p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.home-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 88px);
  width: 100%;
  position: relative;
  overflow: hidden;
  background-color: #010413;
  color: #ffffff;
  transition: background 0.5s ease-out;
}

.particles-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.content-wrapper {
  text-align: center;
  position: relative;
  z-index: 1;
  -webkit-backdrop-filter: blur(5px);
  backdrop-filter: blur(5px);
  padding: 3rem 4rem;
  border-radius: 1.5rem;
  background: rgba(10, 15, 30, 0.5);
  border: 1px solid rgba(100, 126, 255, 0.2);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transform-style: preserve-3d;
}

.title {
  font-size: 4.5rem;
  font-weight: 800;
  letter-spacing: -0.025em;
  background: linear-gradient(315deg, #42d392 10%, #647eff 50%, #ff7ab4 90%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 30px rgba(100, 126, 255, 0.4), 0 0 50px rgba(66, 211, 146, 0.3);
  animation: text-shimmer 4s infinite alternate;
  background-size: 200% auto;
}

@keyframes text-shimmer {
    from { background-position: 200% center; }
    to { background-position: 0% center; }
}

.subtitle {
  margin-top: 1.5rem;
  font-size: 1.25rem;
  color: #e2e8f0;
  max-width: 600px;
  text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
  transform: translateZ(20px); // Give subtitle some 3D depth
}

.details {
  margin-top: 2rem;
  font-size: 1rem;
  color: #e2e8f0;
  max-width: 650px;
  line-height: 1.7;
  text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
  transform: translateZ(40px);
}
</style>
