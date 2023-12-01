<p align="center">
  <a href="https://cloudbypass.com/" style="display: flex; align-items: center; justify-content: center;" target="_blank">
    <img src="assets/logo.png" alt="Cloudbypass" height="100">
    <img src="assets/logo-text.png" alt="Cloudbypass" height="30">
  </a>
</p>


## 介绍
<p>本仓库用于存放穿云API成功调用的代码示例，以供参考。目前包含<b>直接调用穿云服务</b>的代码示例，以及通过调用本地<b>穿云代理客户端</b>的代码示例。</p>

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
> 穿云代理客户端可以解决用户程序中Cookie等信息的管理问题，并且http代理在本地运行，无需担心安全问题。
```shell
# linux
curl --request GET \
--url "https://opensea.io/category/memberships" \
--header "x-cb-apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
--proxy "http://127.0.0.1:1087"



# windows
curl --request GET ^
--url "https://opensea.io/category/memberships" ^
--header "x-cb-apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
--proxy "http://127.0.0.1:1087"
```
