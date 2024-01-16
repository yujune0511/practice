#문제1
class Calculator:
    def __init__(self):
        self.stack = []  # 스택을 초기화하는 생성자 메서드

    def __del__(self):
        del self.stack  # 클래스 인스턴스가 소멸될 때 스택을 제거하는 소멸자 메서드

    def is_empty(self):
        return not bool(self.stack)  # 스택이 비어있는지 확인하는 메서드

    def push(self, item):
        self.stack.append(item)  # 스택에 항목을 추가하는 메서드

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # 스택에서 항목을 꺼내오는 메서드
        else:
            raise ValueError("Stack is empty")

    def calculate(self, expression):
        try:
            for char in expression:
                if char.isdigit():
                    self.push(int(char))  # 숫자인 경우 스택에 추가
                elif char == '(':
                    self.push(char)  # 여는 괄호인 경우 스택에 추가
                elif char == ')':
                    if not self.process_parentheses():
                        raise ValueError("Mismatched parentheses")  # 괄호 쌍의 수가 맞지 않으면 예외 발생
                elif char in {'+', '-', '*', '/'}:
                    if self.is_empty() or self.stack[-1] not in {'+', '-', '*', '/'}:
                        raise ValueError("Invalid expression")  # 연산자가 올바르게 위치하지 않은 경우 예외 발생
                    operand2, operand1 = self.pop(), self.pop()
                    result = self.perform_operation(operand1, operand2, char)
                    self.push(result)
            if '(' in self.stack:
                raise ValueError("Mismatched parentheses")  # 괄호 쌍의 수가 맞지 않으면 예외 발생
            if len(self.stack) != 1:
                raise ValueError("Invalid expression")  # 최종 결과가 하나가 아니면 예외 발생
            return self.pop()
        except Exception as e:
            return str(e)

    def perform_operation(self, operand1, operand2, operator):
        operations = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y,
                      '/': lambda x, y: x / y if y != 0 else 'Division by zero'}
        return operations[operator](operand1, operand2)

    def process_parentheses(self):
        if '(' in self.stack:
            operations = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y,
                          '*': lambda x, y: x * y,
                          '/': lambda x, y: x / y if y != 0 else 'Division by zero'}
            while self.stack[-1] != '(':
                if self.stack[-1] in {'+', '-', '*', '/'}:
                    operand2, operand1, operator = self.pop(), self.pop(), self.pop()
                    result = operations[operator](operand1, operand2)
                    self.push(result)
                else:
                    self.pop()
            self.pop()
            return True
        else:
            return False

#문제2
import math
class EngineerCalculator(Calculator):
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.factorial(n-1)*n
    def sin(self,angle):
        return math.sin(math.radians(angle))
    def cos(self,angle):
        return math.cos(math.radians(angle))
    def tan(self,angle):
        return math.tan(math.radians(angle))
