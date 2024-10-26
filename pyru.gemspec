# pyru.gemspec

Gem::Specification.new do |spec|
  spec.name          = "pyru"
  spec.version       = "1.0.0"
  spec.authors       = ["munsterkreations"]
  spec.email         = ["104373517+munsterkreations@users.noreply.github.com"]
  spec.summary       = "Pyru-friendly interface for Ruby libraries"
  spec.description   = "A Ruby gem that provides a Pyru-friendly interface for Ruby libraries and python libraries."
  spec.homepage      = "https://github.com/munsterkreations/pyru"
  spec.license       = "MIT"

  spec.files         = 
    [ "lib/pyru.rb",
      "lib/pyru_ruby_bridge.rb",
      "lib/pyru_examples.rb",
      "lib/pyru_python_bridge.rb",
      "lib/pyru_compiler.rb",
      "lib/pyru_parser.rb",
      "lib/pyru_lexer.rb"
    
  #"lib/pyru/" python files

    "lib/pyru/__init__.py", 
    "lib/pyru/conversions.py",
    "lib/pyru/exceptions.py", 
    "lib/pyru/forum.py", 
    "lib/pyru/pyru_compiler.py",
     "lib/pyru/pyru_examples.py",
      "lib/pyru/pyru_ide_plugin.py",
       "lib/pyru/pyru_importer.py",
        "lib/pyru/pyru_lexer.py",
        "lib/pyru/pyru_module.py", 
        "lib/pyru/pyru_parser.py",
        "lib/pyru/pyru_python_bridge.py",
         "lib/pyru/pyru_ruby_bridge.py",
          "lib/pyru/syntax.py",
           "lib/pyru/test.py",
            "lib/pyru/tokens.py",
            "setup.py",}

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
