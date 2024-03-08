<p align="center">
  <a href="https://cloudbypass.com/" target="_blank" rel="noopener noreferrer" >
    <div align="center">
        <img src="assets/img.png" alt="Cloudbypass" height="50">
    </div>
  </a>
</p>

## 介绍

<p>本仓库用于存放穿云API成功调用的代码示例，以供参考。目前包含<b>直接调用穿云服务</b>以及调用本地<b>穿云代理客户端</b>的代码示例。</p>

## 直接调用穿云服务

通过代码命令行或第三方程序直接调用穿云API服务，适用于简单的接口调用及数据采集等。
> 由于每次调用穿云API时域名都是固定的，因此对于一些复杂的会话请求需要手动管理Cookie等信息。

```shell
# linux
curl --request GET \
--url "https://api.cloudbypass.com/category/memberships" \
--header "x-cb-apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
--header "x-cb-host: opensea.io"



# windows
curl --request GET ^
--url "https://api.cloudbypass.com/category/memberships" ^
--header "x-cb-apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" ^
--header "x-cb-host: opensea.io"
```

[查看Python示例](code%2Fio%2Fopensea%2Fcategory_memberships.py)

## 通过穿云代理客户端调用

通过穿云代理客户端调用穿云API服务，适用于复杂的会话请求，例如登录、会话重定向请求等。用户只需要将原有的请求加上代理参数即可，穿云代理客户端会自动将代理请求转发到穿云API服务。


### 穿云代理客户端

请先下载[穿云代理客户端](releases)并运行。客户端支持以下参数：

| 参数 | 说明                                        |
|----|-------------------------------------------|
| -k | (可选) 穿云API服务密钥，配置默认请求标头x-cb-apikey        |
| -l | (可选) 服务监听地址 (default "0.0.0.0:1087")      |
| -s | (可选) 服务地址 (default "api.cloudbypass.com") |
| -x | (可选) 配置默认请求标头x-cb-proxy                   |

> 穿云代理客户端可以解决用户程序中Cookie等信息的管理问题。http代理在本地运行，无需担心安全问题。
```shell
# linux
curl --request GET \
--url "https://opensea.io/category/memberships" \
--header "x-cb-apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
--proxy "http://127.0.0.1:1087" \
-k



# windows
curl --request GET ^
--url "https://opensea.io/category/memberships" ^
--header "x-cb-apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" ^
--proxy "http://127.0.0.1:1087" ^
-k
```

[查看Python示例](code%2Fio%2Ftlscontact%2Fvisas-fr%2Flogin.py)