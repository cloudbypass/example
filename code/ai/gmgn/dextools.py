import hashlib
import json
import cloudbypass
import loguru
from pathlib import Path
from retrying import retry

PROXY = ""
APIKEY = ""

logger = loguru.logger


# 出错后等待两秒重试...
@retry(stop_max_attempt_number=3, wait_fixed=2000)
def get_pool_address(address: str):
    try:
        sess = cloudbypass.Session(proxy=PROXY, apikey=APIKEY, part="0")
        resp = sess.request(
            "GET",
            f"https://gmgn.ai/defi/quotation/v1/tokens/eth/{address}",
            headers={
                "x-cb-origin": "https://gmgn.ai",
                "x-cb-referer": "https://gmgn.ai/",
            }
        )
        resp.raise_for_status()
        resp_json = resp.json()
        logger.debug(f"获取到数据: {resp_json}")
        return resp_json.get("data", {}).get("token", {}).get("pool_info", {}).get("address")
    except cloudbypass.BypassError as e:
        logger.warning(f"BypassError: {e}")
        raise e
    except Exception as e:
        logger.warning(f"Error: {e}")
        raise e


# 出错后等待两秒重试...
def request_transactions(url):
    try:
        sess = cloudbypass.Session(apikey=APIKEY)
        resp = sess.request(
            "GET", url,
            headers={
                "x-cb-origin": "https://www.dextools.io",
                "x-cb-referer": "https://www.dextools.io/",
                "x-api-version": "1",
                "content-type": "application/json",
            }
        )
        resp.raise_for_status()
        return resp
    except cloudbypass.BypassError as e:
        logger.warning(f"BypassError: {e}")
        raise e
    except Exception as e:
        logger.warning(f"Error: {e}")
        raise e


def get_unique_transactions_generator(address: str):
    blockNumber = None
    logIndex = None
    while True:
        if blockNumber is not None:
            url = f"https://core-api.dextools.io/pool/events/ether/{address}/desc?blockNumber={blockNumber}&logIndex={logIndex}&limit=100"
        else:
            url = f"https://core-api.dextools.io/pool/events/ether/{address}/newest?limit=100"

        resp = request_transactions(url)
        resp_json = resp.json()
        logger.debug(f"获取到数据: {resp_json}")
        data = resp_json.get("data", {})
        yield data

        blockNumber = data.get("next", {}).get("blockNumber")
        logIndex = data.get("next", {}).get("logIndex")
        if blockNumber is None:
            break


def hash_md5(text):
    """Compute the hash of a file."""
    md5 = hashlib.md5()  # noqa: S324
    md5.update(text.encode())
    return md5.hexdigest()


if __name__ == '__main__':
    # 获取 Pool Address
    pool_address = get_pool_address("0x3334fb8c058b6964ebae022b5bb750b552bee88a")
    logger.success(f"Pool Address: {pool_address}")
    if pool_address is not None:
        raw_events = []

        # 获取 Transactions 数据
        for data in get_unique_transactions_generator(pool_address):
            for event in data.get("events"):
                raw_events.append(event)

        event_set = set()
        # 如果最后一行是空的，则删除最后一行
        if raw_events[-1] is None:
            del raw_events[-1]

        # 过滤重复数据
        events = []
        for event in raw_events:
            hstr = hash_md5(
                "-".join([
                    str(event.get("blockNumber")),
                    str(event.get("blockHash")),
                    str(event.get("logIndex")),
                    str(event.get("timestamp")),
                    str(event.get("type")),
                    str(event.get("amountToken")),
                    str(event.get("amountETH")),
                    str(event.get("amountRef")),
                    str(event.get("maker")),
                ])
            )
            # 判断event是否不存在集合
            if hstr not in event_set:
                # 不存在则添加
                event_set.add(hstr)
                events.append(event)

        # 写入文件
        Path("transactions.json").write_text(json.dumps(events, indent=4), encoding="utf-8")
        logger.success(f"[{len(events)}]条数据已写入文件")
