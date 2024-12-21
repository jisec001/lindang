灵当CRM系统接口wechatSession文件上传漏洞

![image-20241220153351984](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20241220153351984.png)

```
描述:灵当CRM系统接口wechatSession文件上传漏洞，允许攻击者上传恶意文件到服务器，可能导致远程代码执行、网站篡改或其他形式的攻击，严重威胁系统和数据安全。
网络fofa: body="crmcommon/js/jquery/jquery-1.10.1.min.js" || (body="http://localhost:8088/crm/index.php" && body="ldcrm.base.js")
```

