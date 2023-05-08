from app import app, xray

from app.utils.xray import xray_config_from_db


@app.on_event("startup")
def app_startup():
    xray.core.start(xray_config_from_db(xray.config))


@app.on_event("shutdown")
def app_shutdown():
    xray.core.stop()
