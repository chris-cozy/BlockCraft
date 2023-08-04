from lark import Lark, Transformer

# BlockScript Grammar
blockscript_grammar = """
    start: stmt+

    // Statements
    ?stmt: var_declaration
        | if_statement
        | while_loop
        | assignment
        | expr ";"?

    var_declaration: "let" NAME "=" expr

    if_statement: "if" "(" expr ")" block ("else" block)?

    while_loop: "while" "(" expr ")" block

    block: "{" stmt+ "}"

    // Expressions
    ?expr: comp_expr

    comp_expr: arith_expr
        | comp_expr ">" arith_expr -> greater_than
        | comp_expr "<" arith_expr -> less_than
        | comp_expr ">=" arith_expr -> greater_than_or_equal
        | comp_expr "<=" arith_expr -> less_than_or_equal

    arith_expr: term
        | arith_expr "+" term -> add
        | arith_expr "-" term -> sub

    term: mul_expr
        | term "*" mul_expr -> mul
        | term "/" mul_expr -> div

    mul_expr: factor
        | mul_expr "*" factor -> more_than
        | mul_expr "/" factor -> less_than

    factor: NUMBER -> number
          | NAME -> var
          | STRING -> string
          | "-" factor -> neg
          | "(" expr ")"

    assignment: NAME "=" expr

    print_statement: "print" "(" expr ")"

    STRING: /".*?"/

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

# Custom AST Nodes


class VarNode:
    def __init__(self, name):
        self.name = name


class NegNode:
    def __init__(self, item):
        self.item = item

# Custom Transformer to convert Lark AST to BlockScript AST


class BlockScriptTransformer(Transformer):
    def start(self, stmts):
        return stmts

    def var_declaration(self, items):
        return VarDeclarationNode(items[0], items[1])

    def if_statement(self, items):
        condition, if_block, else_block = items
        return IfStatementNode(condition, if_block, else_block)

    def while_loop(self, items):
        condition, loop_block = items
        return WhileLoopNode(condition, loop_block)

    def block(self, stmts):
        return stmts

    def add(self, items):
        return BinaryOpNode(items[0], TokenType.PLUS, items[1])

    def sub(self, items):
        return BinaryOpNode(items[0], TokenType.MINUS, items[1])

    def mul(self, items):
        return BinaryOpNode(items[0], TokenType.MULTIPLY, items[1])

    def div(self, items):
        return BinaryOpNode(items[0], TokenType.DIVIDE, items[1])

    def number(self, token):
        return NumberNode(token[0])

    def var(self, token):
        return VarNode(token[0].value)

    def neg(self, item):
        return NegNode(item)

    def print_statement(self, expression):
        return PrintNode(expression)


# Lexer and Parser instances
lexer = Lark(blockscript_grammar, parser='lalr',
             transformer=BlockScriptTransformer())


def parse_blockscript(code):
    return lexer.parse(code)


class BlockScriptInterpreter:
    def __init__(self):
        self.variables = {}
        self.printed_values = []

    def visit(self, node):
        if isinstance(node, list):
            for stmt in node:
                self.visit(stmt)
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, BinaryOpNode):
            left_val = self.visit(node.left)
            right_val = self.visit(node.right)
            if node.op.type == TokenType.PLUS:
                return left_val + right_val
            elif node.op.type == TokenType.MINUS:
                return left_val - right_val
            elif node.op.type == TokenType.MULTIPLY:
                return left_val * right_val
            elif node.op.type == TokenType.DIVIDE:
                return left_val / right_val
        elif isinstance(node, VarDeclarationNode):
            var_name = node.var_token.value
            self.variables[var_name] = self.visit(node.expression)
        elif isinstance(node, IfStatementNode):
            condition = self.visit(node.condition)
            if condition:
                self.visit(node.if_block)
            else:
                self.visit(node.else_block)
        elif isinstance(node, WhileLoopNode):
            while self.visit(node.condition):
                self.visit(node.loop_block)
        elif isinstance(node, PrintNode):
            value = self.visit(node.expression)
            print(value)
            self.printed_values.append(value)

    def execute(self, syntax_tree):
        self.visit(syntax_tree)
        return self.printed_values


# Token types
class TokenType:
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    LET = 'LET'
    IF = 'IF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    PRINT = 'PRINT'
    VAR = 'VAR'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    LBRACE = 'LBRACE'
    RBRACE = 'RBRACE'
    SEMICOLON = 'SEMICOLON'


# AST nodes
class NumberNode:
    def __init__(self, token):
        self.token = token
        self.value = token.value


class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class VarDeclarationNode:
    def __init__(self, var_token, expression):
        self.var_token = var_token
        self.expression = expression


class IfStatementNode:
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block


class WhileLoopNode:
    def __init__(self, condition, loop_block):
        self.condition = condition
        self.loop_block = loop_block


class PrintNode:
    def __init__(self, expression):
        self.expression = expression


# BlockScript Code to Interpret
blockscript_code = """
let x = 10
let y = 5

if (x > y) {
    print("x is greater than y");
} else {
    print("y is greater than or equal to x");
}

let i = 1
while (i <= 5) {
    print(i);
    i = i + 1
}
"""

# Interpreter Usage
interpreter = BlockScriptInterpreter()
syntax_tree = parse_blockscript(blockscript_code)
result = interpreter.execute(syntax_tree)
# Output: "y is greater than or equal to x" followed by numbers from 1 to 5
print(result)
