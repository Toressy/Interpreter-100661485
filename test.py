    
	def make_equals(self):
		tok_type == TT_EQ
		pos_start = self.pos.copy()
		self.advance()
		if self.current_char == "=":
			self.advance()
			tok_type == TT_EE
		elif self.current_char == "!":
			self.advance()
			tok_type == TT_EQ
		else:
			return [], IllegalCharError(pos_start, self.pos, "'=' should be followed by ':' to form '=:' or '=' to form '=='")
		return Token(tok_type,  pos_start, pos_end=self.pos)
	