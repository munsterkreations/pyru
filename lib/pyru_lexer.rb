# pyru_lexer.rb

class PyruLexer
  def initialize(code)
    @code = code
    @position = 0
    @tokens = []
  end

  def tokenize
    while @position < @code.length
      case @code[@position]
      when /\s/
        # Skip whitespace
        @position += 1
      when /[a-zA-Z]/
        # Identify identifiers
        identifier = ''
        while @code[@position] =~ /[a-zA-Z0-9_]/
          identifier += @code[@position]
          @position += 1
        end
        @tokens << { type: :IDENTIFIER, value: identifier }
      # Add other token types and their respective cases as needed
      else
        # Skip unknown characters
        @position += 1
      end
    end
    @tokens
  end
end
