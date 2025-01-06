# Lazy import Charts and shiny_app to avoid circular dependencies
__all__ = ["launch_dynamic_plot_app"]

def launch_dynamic_plot_app(*args, **kwargs):
    from .shiny_app import launch_dynamic_plot_app as app_launcher
    return app_launcher(*args, **kwargs)
