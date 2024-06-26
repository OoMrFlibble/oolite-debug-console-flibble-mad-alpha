# vim: sw=4 ts=4 et
# cag: 30-6-22, added LET & CONST
_ALL_TOKENS = []

class TokenType:
    def __init__(self, category, literal):
        self._category = category
        self._literal = literal
        _ALL_TOKENS.append(self)

    def __repr__(self):
        return 'TokenType({!r}, {!r})'.format(self._category, self._literal)

    def getcategory(self):
        return self._category

    def getliteral(self):
        return self._literal

# Symbols
ASSIGN_ULSHIFT = TokenType('sym', '<<<=')
ASSIGN_URSHIFT = TokenType('sym', '>>>=')
EQ_STRICT = TokenType('sym', '===')
NE_STRICT = TokenType('sym', '!==')
URSHIFT = TokenType('sym', '>>>')
ASSIGN_LSHIFT = TokenType('sym', '<<=')
ASSIGN_RSHIFT = TokenType('sym', '>>=')
LE = TokenType('sym', '<=')
GE = TokenType('sym', '>=')
EQ = TokenType('sym', '==')
NE = TokenType('sym', '!=')
INC = TokenType('sym', '++')
DEC = TokenType('sym', '--')
LSHIFT = TokenType('sym', '<<')
RSHIFT = TokenType('sym', '>>')
LOGICAL_AND = TokenType('sym', '&&')
LOGICAL_OR = TokenType('sym', '||')
ASSIGN_ADD = TokenType('sym', '+=')
ASSIGN_SUB = TokenType('sym', '-=')
ASSIGN_MUL = TokenType('sym', '*=')
ASSIGN_MOD = TokenType('sym', '%=')
ASSIGN_BIT_AND = TokenType('sym', '&=')
ASSIGN_BIT_OR = TokenType('sym', '|=')
ASSIGN_BIT_XOR = TokenType('sym', '^=')
ASSIGN_DIV = TokenType('sym', '/=')
LBRACE = TokenType('sym', '{')
RBRACE = TokenType('sym', '}')
LPAREN = TokenType('sym', '(')
RPAREN = TokenType('sym', ')')
LBRACKET = TokenType('sym', '[')
RBRACKET = TokenType('sym', ']')
DOT = TokenType('sym', '.')
SEMI = TokenType('sym', ';')
COMMA = TokenType('sym', ',')
LT = TokenType('sym', '<')
GT = TokenType('sym', '>')
ADD = TokenType('sym', '+')
SUB = TokenType('sym', '-')
MUL = TokenType('sym', '*')
MOD = TokenType('sym', '%')
BIT_OR = TokenType('sym', '|')
BIT_AND = TokenType('sym', '&')
BIT_XOR = TokenType('sym', '^')
LOGICAL_NOT = TokenType('sym', '!')
BIT_NOT = TokenType('sym', '~')
QUESTION = TokenType('sym', '?')
COLON = TokenType('sym', ':')
ASSIGN = TokenType('sym', '=')
DIV = TokenType('sym', '/')

# Keywords
BREAK = TokenType('kw', 'break')
CASE = TokenType('kw', 'case')
CATCH = TokenType('kw', 'catch')
CONST = TokenType('kw', 'const') ###
CONTINUE = TokenType('kw', 'continue')
DEFAULT = TokenType('kw', 'default')
DELETE = TokenType('kw', 'delete')
DO = TokenType('kw', 'do')
ELSE = TokenType('kw', 'else')
FALSE = TokenType('kw', 'false')
FINALLY = TokenType('kw', 'finally')
FOR = TokenType('kw', 'for')
FUNCTION = TokenType('kw', 'function')
IF = TokenType('kw', 'if')
IN = TokenType('kw', 'in')
INSTANCEOF = TokenType('kw', 'instanceof')
LET = TokenType('kw', 'let') ###
NEW = TokenType('kw', 'new')
NULL = TokenType('kw', 'null')
RETURN = TokenType('kw', 'return')
SWITCH = TokenType('kw', 'switch')
THIS = TokenType('kw', 'this')
THROW = TokenType('kw', 'throw')
TRUE = TokenType('kw', 'true')
TYPEOF = TokenType('kw', 'typeof')
TRY = TokenType('kw', 'try')
VAR = TokenType('kw', 'var')
VOID = TokenType('kw', 'void')
WHILE = TokenType('kw', 'while')
WITH = TokenType('kw', 'with')

_unsupported = [ # reserved words from console.script; implement as needed
	'abstract', 'arguments', 'await', 'boolean', 'byte',
	'char', 'class', 'constructor', 'debugger',
	'double', 'enum', 'eval', 'export',
	'extends', 'final', 'float',
	'goto', 'implements', 'import', 'int',
	'interface', 'long', 'native', 'package', 'private',
	'protected', 'prototype', 'public', 'short', 'static', 'super',
	'synchronized', 'throws', 'transient',
	'volatile', 'yield'
] # 'const', 'let',
# for word in _unsupported:
#     TokenType('kw', word)

# Other tokens
C_COMMENT = TokenType('other', '/*')
CPP_COMMENT = TokenType('other', '//')
HTML_COMMENT = TokenType('other', '<!--')
ERROR = TokenType('other', 'err')
EOF = TokenType('other', 'eof')
EOL = TokenType('other', 'eol')
NAME = TokenType('other', '(name)')
NUMBER = TokenType('other', '(num)')
OPERATOR = TokenType('other', '(op)')
REGEXP = TokenType('other', '(re)')
SPACE = TokenType('other', '(sp)')
STRING = TokenType('other', '(str)')

# Freeze the list of keywords
_ALL_TOKENS = tuple(_ALL_TOKENS)

class _Keywords:
    def __init__(self):
        self._d = {}
        for tt in _ALL_TOKENS:
            if tt.getcategory() == 'kw':
                self._d[tt.getliteral()] = tt

    def get(self, literal, default):
        return self._d.get(literal, default)

    def has(self, tok):
        for item in list(self._d.values()):
            if item == tok:
                return True
        return False

keywords = _Keywords()

class _Punctuators:
    def __init__(self):
        self._prefixes = {}
        self._punctuators = {}

        for t in _ALL_TOKENS:
            if t.getcategory() == 'sym':
                literal = t.getliteral()
                for i in range(len(literal)):
                    prefix = literal[:i+1]
                    self._prefixes[prefix] = True
                self._punctuators[literal] = t

    def hasprefix(self, prefix):
        return self._prefixes.get(prefix, False)

    def get(self, literal):
        return self._punctuators.get(literal)

punctuators = _Punctuators()
