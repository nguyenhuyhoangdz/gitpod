import requests

proxies = []

# Get proxies from raw text files
raw_proxy_sites = [ "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
	"https://api.openproxylist.xyz/http.txt",
	"http://alexa.lr2b.com/proxylist.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
	"https://proxy-spider.com/api/proxies.example.txt",
	"http://worm.rip/http.txt",
	"https://sheesh.rip/http.txt",
	"https://www.freeproxychecker.com/result/http_proxies.txt",
	"https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
	"https://proxyspace.pro/http.txt",
	"https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/http.txt",
	"https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/https.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
	"https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
	"https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
	"https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
	"https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
	"https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
	"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
	"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
	"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
	"https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/http.txt",
	"https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/https.txt",
	"https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
	"https://raw.githubusercontent.com/tahaluindo/proxy-list/main/proxy-list/data.txt",
	"https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
	"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
	"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
	"https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt",
	"https://openproxylist.xyz/http.txt",
	"https://proxyspace.pro/http.txt",
	"https://proxyspace.pro/https.txt",
	"https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all",
	"https://api.proxyscrape.com/?request=displayproxies&proxytype=https&country=all",
	"https://www.proxy-list.download/api/v1/get?type=http",
	"https://www.proxy-list.download/api/v1/get?type=https",
	"http://rootjazz.com/proxies/proxies",
	"https://openproxy.world/http.txt",
	"http://olaf4snow.com/public/proxy.txt",
	"https://api.openproxylist.xyz/http.txt",
	"https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
	"https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
	"https://api.openproxylist.xyz/http.txt",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"]
for site in raw_proxy_sites:
    response = requests.get(site)
    for line in response.text.split('\n'):
        if ':' in line:
            ip, port = line.split(':', maxsplit=2)[:2]
            proxies.append(f'{ip}:{port}')

with open('http.txt', 'w') as f:
    for proxy in proxies:
        f.write(proxy + '\n')
print("đã lưu vào file http.txt")