sudo sysctl -w net.ipv4.ip_forward=1
sudo groupadd docker
sudo usermod -aG docker juanjo
service docker restart


autenticarse como juanjo
docker pull jenkins

firewall-cmd --zone=public --add-port=2888/tcp --permanent
firewall-cmd --reload

Referencias
https://dougvitale.wordpress.com/2011/12/21/deprecated-linux-networking-commands-and-their-replacements/
https://mikewilliamson.wordpress.com/2013/10/06/docker-networking/



---
firewall-cmd --get-active-zones
firewall-cmd --zone=dmz --add-port=2888/tcp --permanent