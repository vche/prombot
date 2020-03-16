from flask import Blueprint

appblueprint = Blueprint('prombot', __name__)

from . import prometheus_alerts
