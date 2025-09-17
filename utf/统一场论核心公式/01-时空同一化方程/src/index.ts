/**
 * 时空同一化方程可视化系统主入口
 * 张祥前统一场论 - 3D可视化平台
 */

import './styles/main.css';
import { SpacetimeVisualizationApp } from './core/SpacetimeVisualizationApp';
import { Logger } from './utils/Logger';

// 初始化日志系统
const logger = new Logger('Main');

/**
 * 应用程序初始化
 */
async function initializeApp(): Promise<void> {
  try {
    logger.info('正在初始化时空同一化方程可视化系统...');
    
    // 检查浏览器兼容性
    if (!checkBrowserCompatibility()) {
      throw new Error('浏览器不支持WebGL 2.0，无法运行可视化系统');
    }
    
    // 创建主应用实例
    const app = new SpacetimeVisualizationApp();
    
    // 初始化应用
    await app.initialize();
    
    // 隐藏加载屏幕
    hideLoadingScreen();
    
    logger.info('时空同一化方程可视化系统初始化完成');
    
  } catch (error) {
    logger.error('应用初始化失败:', error);
    showErrorMessage(error instanceof Error ? error.message : '未知错误');
  }
}

/**
 * 检查浏览器兼容性
 */
function checkBrowserCompatibility(): boolean {
  // 检查WebGL 2.0支持
  const canvas = document.createElement('canvas');
  const gl = canvas.getContext('webgl2');
  
  if (!gl) {
    logger.warn('WebGL 2.0不可用，尝试WebGL 1.0');
    const gl1 = canvas.getContext('webgl');
    return !!gl1;
  }
  
  return true;
}

/**
 * 隐藏加载屏幕
 */
function hideLoadingScreen(): void {
  setTimeout(() => {
    const loadingScreen = document.getElementById('loading-screen');
    if (loadingScreen) {
      loadingScreen.classList.add('fade-out');
      setTimeout(() => {
        loadingScreen.style.display = 'none';
      }, 500);
    }
  }, 1000); // 延迟1秒隐藏，确保所有内容都已加载
}

/**
 * 显示错误消息
 */
function showErrorMessage(message: string): void {
  const loadingScreen = document.getElementById('loading-screen');
  if (loadingScreen) {
    loadingScreen.innerHTML = `
      <div class="error-message">
        <h2>❌ 系统初始化失败</h2>
        <p>${message}</p>
        <button onclick="location.reload()" class="retry-button">重试</button>
      </div>
    `;
  }
}

// 当DOM加载完成时初始化应用
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  initializeApp();
}

// 全局错误处理
window.addEventListener('error', (event) => {
  logger.error('全局错误:', event.error);
});

window.addEventListener('unhandledrejection', (event) => {
  logger.error('未处理的Promise拒绝:', event.reason);
});