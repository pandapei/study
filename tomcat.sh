#!/bin/sh

JRE_HOME=/home/shiyanlou/jre1.8.0_121
CATALINA_HOME=/home/shiyanlou/apache-tomcat-9.0.0.M18
export JRE_HOME
export CATALINA_HOME

start_tomcat=$CATALINA_HOME/bin/startup.sh
stop_tomcat=$CATALINA_HOME/bin/shutdown.sh

start() {                                                             
        echo -n -e "启动Tomcat：\n"
        ${start_tomcat}
        echo "Tomcat启动完成！"
}

stop() {
        echo -n -e "正在关闭Tomcat：\n "
        ${stop_tomcat}
        echo "Tomcat关闭完成！"
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart)
        stop
        sleep 10
        start
        ;;
  *)
        echo "使用： $0 {start|stop|restart}"
esac
exit 0
