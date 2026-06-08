"""
Mine Microgrid Simulator - Core Modules

This package contains all core modules for the mine microgrid planning simulator:
- Input validation (validation.py)
- Data loading (data_handler.py)
- Energy modeling (simulation_engine.py)
- Simulation and dispatching (simulation.py)
- Visualization and analysis (results_analyzer.py)
"""

__version__ = "1.0.0"

# 导入所有模块的主要函数，方便外部调用
try:
    from .validation import validate_inputs
    from .data_handler import load_mine_load_profile, get_weather_data
    from .simulation_engine import calculate_solar_power, calculate_wind_power, run_simulation
    from .results_analyzer import display_results, calculate_kpis, create_sankey_chart, create_interactive_dispatch_curve
    from .ui_components import create_sidebar, create_main_header, create_default_info
    from .utils import convert_units, calculate_capacity_factor, calculate_lcoe
    from .config import get_config, get_wind_turbine_info, validate_config
    from .performance import PerformanceMonitor, clear_streamlit_cache
    from .async_processor import task_manager, create_progress_ui, async_computation
    from .error_handler import with_error_handling, create_error_recovery_ui, RetryConfig
    from .memory_optimizer import create_memory_monitor_ui, optimize_for_memory, MemoryMonitor

    # 导入高级UI组件
    from .advanced_ui import (
        create_advanced_header, create_status_dashboard, create_advanced_sidebar,
        create_advanced_progress_display, create_advanced_kpi_dashboard
    )

    # 导入高级可视化
    from .advanced_visualization import (
        create_3d_energy_flow_chart, create_animated_daily_profile,
        create_heatmap_analysis, create_radar_chart_comparison, create_waterfall_chart
    )

    # 定义包的公共接口
    __all__ = [
        # 验证模块
        'validate_inputs',
        # 数据处理模块
        'load_mine_load_profile',
        'get_weather_data',
        # 仿真引擎模块
        'calculate_solar_power',
        'calculate_wind_power',
        'run_simulation',
        # 结果分析模块
        'display_results',
        'calculate_kpis',
        'create_sankey_chart',
        'create_interactive_dispatch_curve',
        # UI组件模块
        'create_sidebar',
        'create_main_header',
        'create_default_info',
        # 工具模块
        'convert_units',
        'calculate_capacity_factor',
        'calculate_lcoe',
        # 配置管理模块
        'get_config',
        'get_wind_turbine_info',
        'validate_config',
        # 性能监控模块
        'PerformanceMonitor',
        'clear_streamlit_cache',
        # 异步处理模块
        'task_manager',
        'create_progress_ui',
        'async_computation',
        # 错误处理模块
        'with_error_handling',
        'create_error_recovery_ui',
        'RetryConfig',
        # 内存优化模块
        'create_memory_monitor_ui',
        'optimize_for_memory',
        'MemoryMonitor',
        # 高级UI模块
        'create_advanced_header',
        'create_status_dashboard',
        'create_advanced_sidebar',
        'create_advanced_progress_display',
        'create_advanced_kpi_dashboard',
        # 高级可视化模块
        'create_3d_energy_flow_chart',
        'create_animated_daily_profile',
        'create_heatmap_analysis',
        'create_radar_chart_comparison',
        'create_waterfall_chart'
    ]

except ImportError as e:
    # 如果某些模块还未创建，不影响包的导入
    print(f"Warning: Some modules are not yet available: {e}")
    __all__ = []

# 包的元信息
__package_info__ = {
    "name": "矿区可再生能源与微电网规划模拟器模块包",
    "description": "专业的微电网规划分析工具核心功能模块",
    "version": __version__,
    "author": "Project Contributors",
    "modules": [
        "validation - 输入验证模块",
        "data_handler - 数据处理模块",
        "simulation_engine - 仿真引擎模块",
        "results_analyzer - 结果分析模块",
        "ui_components - UI组件模块",
        "utils - 通用工具模块",
        "config - 配置管理模块",
        "performance - 性能监控模块",
        "async_processor - 异步处理模块",
        "error_handler - 错误处理模块",
        "memory_optimizer - 内存优化模块"
    ]
}

def get_package_info():
    """
    获取包的详细信息
    
    返回:
    - dict: 包含包信息的字典
    """
    return __package_info__

def list_available_functions():
    """
    列出包中所有可用的函数
    
    返回:
    - list: 可用函数名称列表
    """
    return __all__
