
pytest_plugins = ["pytester"]

def pytest_load_initial_conftests(args):
    for i in range(30):
        print("**************************")
    print(args)