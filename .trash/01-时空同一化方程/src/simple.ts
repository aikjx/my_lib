/**
 * 简化版本的时空同一化方程可视化
 * 用于测试基础功能
 */

import * as THREE from 'three';
import './styles/main.css';

let scene: THREE.Scene;
let camera: THREE.PerspectiveCamera;
let renderer: THREE.WebGLRenderer;
let cube: THREE.Mesh;
let isAnimating = false;

function init(): void {
  console.log('初始化简化版可视化系统...');

  // 获取画布
  const canvas = document.getElementById('main-canvas') as HTMLCanvasElement;
  if (!canvas) {
    console.error('找不到画布元素');
    return;
  }

  // 创建场景
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a0a0a);

  // 创建相机
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.set(5, 5, 5);

  // 创建渲染器
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);

  // 添加光照
  const ambientLight = new THREE.AmbientLight(0x404080, 0.3);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(10, 10, 5);
  scene.add(directionalLight);

  // 添加坐标轴
  const axesHelper = new THREE.AxesHelper(5);
  scene.add(axesHelper);

  // 添加网格
  const gridHelper = new THREE.GridHelper(10, 10);
  scene.add(gridHelper);

  // 添加立方体
  const geometry = new THREE.BoxGeometry(1, 1, 1);
  const material = new THREE.MeshPhongMaterial({ color: 0x667eea });
  cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  // 设置UI
  setupUI();

  // 开始渲染
  animate();

  // 隐藏加载屏幕
  setTimeout(() => {
    const loadingScreen = document.getElementById('loading-screen');
    if (loadingScreen) {
      loadingScreen.style.display = 'none';
    }
  }, 1000);

  console.log('简化版可视化系统初始化完成');
}

function setupUI(): void {
  // 设置公式显示
  const equationDisplay = document.getElementById('equation-display');
  if (equationDisplay) {
    equationDisplay.innerHTML = `
      <div class="formula-display">
        <strong>时空同一化方程：</strong><br>
        <span style="font-family: 'Times New Roman', serif; font-size: 1.2em;">
          r⃗(t) = C⃗t = x⃗i + y⃗j + z⃗k
        </span>
      </div>
    `;
  }

  // 设置物理洞察
  const physicsInsights = document.getElementById('physics-insights');
  if (physicsInsights) {
    physicsInsights.innerHTML = `
      <div class="physics-insight">
        <h4>🔬 物理意义</h4>
        <p>该方程揭示了时间与空间的统一关系，表明空间位置矢量与时间成正比。</p>
      </div>
    `;
  }

  // 设置控制按钮
  const animationControls = document.getElementById('animation-controls');
  if (animationControls) {
    animationControls.innerHTML = `
      <div style="text-align: center; margin-bottom: 15px;">
        <button class="control-button" id="play-pause-btn">
          ▶️ 开始
        </button>
        <button class="control-button" id="reset-btn">
          🔄 重置
        </button>
      </div>
    `;

    // 添加事件监听
    const playPauseBtn = document.getElementById('play-pause-btn');
    const resetBtn = document.getElementById('reset-btn');

    if (playPauseBtn) {
      playPauseBtn.addEventListener('click', toggleAnimation);
    }

    if (resetBtn) {
      resetBtn.addEventListener('click', resetScene);
    }
  }

  // 设置实时数据
  const realTimeData = document.getElementById('real-time-data');
  if (realTimeData) {
    realTimeData.innerHTML = `
      <div style="font-family: monospace; font-size: 0.9em;">
        <div>系统状态: 运行中</div>
        <div>渲染模式: WebGL</div>
        <div>动画状态: <span id="anim-status">暂停</span></div>
      </div>
    `;
  }
}

function animate(): void {
  requestAnimationFrame(animate);

  if (isAnimating && cube) {
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
  }

  renderer.render(scene, camera);
}

function toggleAnimation(): void {
  isAnimating = !isAnimating;
  const btn = document.getElementById('play-pause-btn');
  const status = document.getElementById('anim-status');

  if (btn) {
    btn.innerHTML = isAnimating ? '⏸️ 暂停' : '▶️ 开始';
  }

  if (status) {
    status.textContent = isAnimating ? '运行中' : '暂停';
  }
}

function resetScene(): void {
  if (cube) {
    cube.rotation.set(0, 0, 0);
  }
  camera.position.set(5, 5, 5);
  isAnimating = false;

  const btn = document.getElementById('play-pause-btn');
  const status = document.getElementById('anim-status');

  if (btn) {
    btn.innerHTML = '▶️ 开始';
  }

  if (status) {
    status.textContent = '暂停';
  }
}

// 窗口大小变化处理
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// 初始化
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}