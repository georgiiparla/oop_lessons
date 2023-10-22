class Example:
    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')
