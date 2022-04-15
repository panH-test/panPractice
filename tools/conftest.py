#@Author:Hanpan
#@Time:2022/4/14  18:10
#@File:conftest.py

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = items.name.encode().decode('unicode_escape')
        item.nodeid = items.nodeid.encode().decode('unicode_escape')
