/**
 * 物理系统相关的类型定义
 */

import { Vector3 } from 'three';

/**
 * 物理参数接口
 */
export interface PhysicsParameters {
  /** 光速矢量分量 */
  Cx: number;  // x方向光速分量 (m/s)
  Cy: number;  // y方向光速分量 (m/s)
  Cz: number;  // z方向光速分量 (m/s)
  
  /** 时间参数 */
  timeScale: number;     // 时间缩放因子
  timeOffset: number;    // 时间偏移 (s)
  maxTime: number;       // 最大时间 (s)
  
  /** 可视化参数 */
  trajectoryLength: number;  // 轨迹长度
  particleDensity: number;   // 粒子密度
  fieldIntensity: number;    // 场强显示强度
}

/**
 * 时空点数据结构
 */
export interface SpacetimePoint {
  position: Vector3;      // 空间位置 (x, y, z)
  time: number;          // 时间坐标 (t)
  velocity: Vector3;     // 瞬时速度 (m/s)
  acceleration: Vector3; // 瞬时加速度 (m/s²)
}

/**
 * 轨迹数据结构
 */
export interface TrajectoryData {
  points: SpacetimePoint[];
  totalTime: number;
  totalDistance: number;
  averageSpeed: number;
  
  /** 统计信息 */
  statistics: {
    minPosition: Vector3;
    maxPosition: Vector3;
    minSpeed: number;
    maxSpeed: number;
  };
}

/**
 * 物理状态接口
 */
export interface PhysicsState {
  currentTime: number;
  currentPosition: Vector3;
  currentVelocity: Vector3;
  currentAcceleration: Vector3;
  trajectory: TrajectoryData;
  parameters: PhysicsParameters;
}

/**
 * 场矢量数据结构
 */
export interface FieldVector {
  position: Vector3;
  direction: Vector3;
  magnitude: number;
  color: THREE.Color;
}

/**
 * 矢量场数据结构
 */
export interface VectorField {
  gridSize: Vector3;           // 网格尺寸
  resolution: Vector3;         // 分辨率
  vectors: FieldVector[];      // 场矢量数组
  
  /** 场属性 */
  fieldType: 'spacetime' | 'velocity' | 'acceleration';
  intensity: number;
  
  /** 可视化属性 */
  arrowScale: number;
  colorMapping: ColorMap;
}

/**
 * 颜色映射类型
 */
export type ColorMap = 'rainbow' | 'plasma' | 'viridis' | 'cool' | 'warm';

/**
 * 验证结果接口
 */
export interface ValidationResult {
  isValid: boolean;
  errors: string[];
  warnings?: string[];
}

/**
 * 默认物理参数
 */
export const DEFAULT_PHYSICS_PARAMETERS: PhysicsParameters = {
  Cx: 299792458,      // 光速 x 分量 (m/s)
  Cy: 0,              // 光速 y 分量 (m/s)
  Cz: 0,              // 光速 z 分量 (m/s)
  timeScale: 1.0,     // 时间缩放
  timeOffset: 0,      // 时间偏移
  maxTime: 10,        // 最大时间 10秒
  trajectoryLength: 1000,  // 轨迹点数
  particleDensity: 100,    // 粒子密度
  fieldIntensity: 1.0,     // 场强度
};

/**
 * 物理常数
 */
export const PHYSICS_CONSTANTS = {
  LIGHT_SPEED: 299792458,        // 光速 (m/s)
  PLANCK_CONSTANT: 6.62607015e-34, // 普朗克常数 (J⋅s)
  GRAVITATIONAL_CONSTANT: 6.67430e-11, // 引力常数 (m³⋅kg⁻¹⋅s⁻²)
} as const;