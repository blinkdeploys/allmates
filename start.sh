#!/bin/sh
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
base_app_path="/home/simcaservers/private/legalease"
source "$base_app_path/bin/activate"
exec env FLASK_APP=$base_app_path/run.py flask run --host=$HOST --port=$PORT --debug

