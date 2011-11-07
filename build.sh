#!/bin/bash

function usage {
cat <<EOF
 Usage: ./build.sh [COMMAND]
 COMMAND:
    ut:run all unit tests
    ft:run all functional tests
    run:start server
    dbreset:reset database
EOF
}

function unit_test {
    echo "--------start to run all unit tests--------"
    cd pairstairs
    nosetests
    cd ..
}

function function_test {
    echo "--------start to run all function tests--------"
    cd func_test
    nosetests -a "function_test" --with-progressive
    cd ..
}

function run_server {
    xterm -e "python manage.py runserver" & sleep 2
}

function db_reset {
    echo "----------reset database-------------------"
}

function set_env {
    set -e
    set -u
    DIR="$( cd "$( dirname "$0" )" && pwd )"
    cd $DIR
    set +u
    source ve/bin/activate
}

function main {
  set_env
  case $1 in
    ut) unit_test ;;
    ft) function_test ;;
    run) run_server ;;
    dbreset) db_reset;;
	*) usage && exit 1;;
  esac
}

main $@