# Lazy import Charts and shiny_app to avoid circular dependencies
__all__ = ["run_app"]

def run_app(*args, **kwargs):
    from .shiny_app import run_app as app_launcher
    return app_launcher(*args, **kwargs)
