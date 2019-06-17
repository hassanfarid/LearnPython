import base64

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

def override_transformer(metric_script):
    file = open("src/data/metric_script.b64")
    query = file.read()
    file.close()

    file = open("src/common/transform.py", "w")
    file.write(base64ToString(query))
    file.close()
    return True