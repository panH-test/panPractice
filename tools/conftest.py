#@Author:Hanpan
#@Time:2022/4/14  18:10
#@File:conftest.py

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode().decode('unicode_escape')
        item._nodeid = item.nodeid.encode().decode('unicode_escape')
