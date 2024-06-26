# vim: sw=4 ts=4 et
# cag: 30-6-22, fixed ',' in return (was '.'); added 4 missing __MESSAGES

_MESSAGES = (
    'unexpected_eof',
    'semi_before_stmnt',
    'syntax_error',
    'unterminated_comment',
    'expected_tok',
    'unexpected_char',
	'invalid_catch',
	'expected_statement',
	'invalid_case',
	'invalid_assign',
)

class JSSyntaxError(BaseException):
    def __init__(self, offset, msg, msg_args=None):
        assert msg in _MESSAGES, msg
        self.offset = offset
        self.msg = msg
        self.msg_args = msg_args or {}
    def __unicode__(self):
        return '{}: {}'.format(self.offset, self.msg)
    def __repr__(self):
        return 'JSSyntaxError({!r}, {!r}, {!r})'.format(self.offset, self.msg, self.msg_args)
