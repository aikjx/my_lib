/**
 * 日志工具类
 * 提供统一的日志记录功能
 */

export enum LogLevel {
  DEBUG = 0,
  INFO = 1,
  WARN = 2,
  ERROR = 3,
}

export class Logger {
  private static globalLogLevel: LogLevel = LogLevel.INFO;
  private context: string;

  constructor(context: string) {
    this.context = context;
  }

  /**
   * 设置全局日志级别
   */
  public static setLogLevel(level: LogLevel): void {
    Logger.globalLogLevel = level;
  }

  /**
   * 调试日志
   */
  public debug(message: string, ...args: any[]): void {
    this.log(LogLevel.DEBUG, message, ...args);
  }

  /**
   * 信息日志
   */
  public info(message: string, ...args: any[]): void {
    this.log(LogLevel.INFO, message, ...args);
  }

  /**
   * 警告日志
   */
  public warn(message: string, ...args: any[]): void {
    this.log(LogLevel.WARN, message, ...args);
  }

  /**
   * 错误日志
   */
  public error(message: string, ...args: any[]): void {
    this.log(LogLevel.ERROR, message, ...args);
  }

  /**
   * 记录日志
   */
  private log(level: LogLevel, message: string, ...args: any[]): void {
    if (level < Logger.globalLogLevel) {
      return;
    }

    const timestamp = new Date().toISOString();
    const levelName = LogLevel[level];
    const logMessage = `[${timestamp}] [${levelName}] [${this.context}] ${message}`;

    switch (level) {
      case LogLevel.DEBUG:
        console.debug(logMessage, ...args);
        break;
      case LogLevel.INFO:
        console.info(logMessage, ...args);
        break;
      case LogLevel.WARN:
        console.warn(logMessage, ...args);
        break;
      case LogLevel.ERROR:
        console.error(logMessage, ...args);
        break;
    }
  }

  /**
   * 性能计时开始
   */
  public time(label: string): void {
    console.time(`[${this.context}] ${label}`);
  }

  /**
   * 性能计时结束
   */
  public timeEnd(label: string): void {
    console.timeEnd(`[${this.context}] ${label}`);
  }

  /**
   * 分组日志开始
   */
  public group(label: string): void {
    console.group(`[${this.context}] ${label}`);
  }

  /**
   * 分组日志结束
   */
  public groupEnd(): void {
    console.groupEnd();
  }
}