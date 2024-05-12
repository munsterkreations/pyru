# pyru.gemspec

Gem::Specification.new do |spec|
  spec.name          = "pyru"
  spec.version       = "0.1.0"
  spec.authors       = ["munsterkreations"]
  spec.email         = ["k7Gp7@example.com"]
  spec.summary       = "Pyru-friendly interface for Ruby libraries"
  spec.description   = "A Ruby gem that provides a Pyru-friendly interface for Ruby libraries."
  spec.homepage      = "https://github.com/munsterkreations/pyru"
  spec.license       = "MIT"

  spec.files         = [
    "lib/pyru.rb",
    "lib/pyru_ruby_bridge.rb",
    "lib/pyru_examples.rb",
    "lib/pyru_python_bridge.rb",
    "lib/pyru_compiler.rb",
    "lib/pyru_parser.rb",
    "lib/pyru_lexer.rb",


  ]
  # Dependencies
  spec.add_dependency "rubygems", "~> 3.2"
  spec.add_dependency "rake", "~> 13.0"
  spec.add_dependency "rspec", "~> 3.0"
  spec.add_dependency "rubocop", "~> 1.0"
  spec.add_dependency "python", "~> 3.0"

  # Development dependencies
  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "pry", "~> 0.14"
  spec.add_development_dependency "faker", "~> 2.0"
end
