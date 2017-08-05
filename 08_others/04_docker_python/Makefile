host_port_web='8080'
host_port_slave='50000'
for i in {8080..8088}
do
        c="docker run -d -p $i:$host_port --name jenkins_$i jenkins_pro"
        echo $c
        #eval $c
done
