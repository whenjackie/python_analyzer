import ast

def checkHello(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            if isinstance(node.value, ast.Str):
                if node.value.s == 'Hello, World!':
                    return True
    return False

def main():
	r = open('parse.py','r')
	tree = ast.parse(r.read())
	print(checkHello(tree))

if __name__== "__main__":
	main()