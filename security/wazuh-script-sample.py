import json, subprocess

result = subprocess.run(['last', '-a'], stdout=subprocess.PIPE)
users = [line.split()[0] for line in result.stdout.decode().split('\n') if line]
alert = {"integration": "custom", "users": users}
print(json.dumps(alert))