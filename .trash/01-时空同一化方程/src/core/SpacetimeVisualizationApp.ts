/**
 * 时空同一化方程可视化系统主应用类
 * 负责协调各个子系统的初始化和运行
 */

import { Logger } from '../utils/Logger';
import { PhysicsEngine } from '../physics/PhysicsEngine';
import { VisualizationRenderer } from '../rendering/VisualizationRenderer';
import { UIManager } from '../ui/UIManager';
import { PhysicsParameters } from '../types/PhysicsTypes';

export class SpacetimeVisualizationApp {
  private logger: Logger;
  private physicsEngine: PhysicsEngine;
  private renderer: VisualizationRenderer;
  private uiManager: UIManager;
  private isInitialized: boolean = false;
  private animationId: number | null = null;
  private isAnimating: boolean = false;

  constructor() {
    this.logger = new Logger('SpacetimeVisualizationApp');
    this.physicsEngine = new PhysicsEngine();
    this.renderer = new VisualizationRenderer();
    this.uiManager = new UIManager();
  }

  /**
   * 初始化应用程序
   */
  public async initialize(): Promise<void> {
    try {
      this.logger.info('开始初始化时空同一化方程可视化系统...');

      // 初始化UI管理器
      await this.uiManager.initialize();
      this.logger.info('UI管理器初始化完成');

      // 初始化渲染器
      await this.renderer.initialize();
      this.logger.info('渲染器初始化完成');

      // 初始化物理引擎
      await this.physicsEngine.initialize();
      this.logger.info('物理引擎初始化完成');

      // 设置事件监听
      this.setupEventListeners();

      // 开始渲染循环
      this.startRenderLoop();

      this.isInitialized = true;
      this.logger.info('时空同一化方程可视化系统初始化完成');

    } catch (error) {
      this.logger.error('应用初始化失败:', error);
      throw error;
    }
  }

  /**
   * 设置事件监听器
   */
  private setupEventListeners(): void {
    // 窗口大小变化
    window.addEventListener('resize', () => {
      this.renderer.handleResize();
    });

    // UI参数变化事件
    this.uiManager.on('parameterChange', (params: PhysicsParameters) => {
      this.updateParameters(params);
    });

    // 动画控制事件
    this.uiManager.on('animationToggle', () => {
      this.toggleAnimation();
    });

    this.uiManager.on('animationReset', () => {
      this.resetAnimation();
    });

    // 视角控制事件
    this.uiManager.on('viewChange', (viewType: string) => {
      this.renderer.setView(viewType);
    });
  }

  /**
   * 开始渲染循环
   */
  private startRenderLoop(): void {
    const animate = (timestamp: number): void => {
      this.animationId = requestAnimationFrame(animate);

      if (this.isAnimating) {
        // 更新物理计算
        this.physicsEngine.update(timestamp);

        // 获取当前物理状态
        const physicsState = this.physicsEngine.getCurrentState();

        // 更新可视化
        this.renderer.updateVisualization(physicsState);

        // 更新UI显示
        this.uiManager.updateRealTimeData(physicsState);
      }

      // 始终渲染场景
      this.renderer.render();
    };

    // 开始动画循环
    animate(0);
    
    // 默认开始动画
    this.isAnimating = true;
  }

  /**
   * 更新物理参数
   */
  public updateParameters(params: PhysicsParameters): void {
    if (!this.isInitialized) {
      this.logger.warn('应用未初始化，无法更新参数');
      return;
    }

    try {
      this.physicsEngine.updateParameters(params);
      this.logger.info('物理参数已更新:', params);
    } catch (error) {
      this.logger.error('参数更新失败:', error);
    }
  }

  /**
   * 切换动画状态
   */
  public toggleAnimation(): void {
    this.isAnimating = !this.isAnimating;
    this.logger.info(`动画${this.isAnimating ? '开始' : '暂停'}`);
  }

  /**
   * 重置动画
   */
  public resetAnimation(): void {
    this.isAnimating = false;
    this.physicsEngine.reset();
    this.renderer.reset();
    this.logger.info('动画已重置');
  }

  /**
   * 销毁应用程序
   */
  public destroy(): void {
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
    }

    this.renderer.destroy();
    this.uiManager.destroy();
    
    this.isInitialized = false;
    this.logger.info('应用程序已销毁');
  }

  /**
   * 获取当前状态
   */
  public getStatus(): {
    isInitialized: boolean;
    isAnimating: boolean;
  } {
    return {
      isInitialized: this.isInitialized,
      isAnimating: this.isAnimating,
    };
  }
}