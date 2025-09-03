# pyru.gemspec

Gem::Specification.new do |spec|
  spec.name          = "pyru"
  spec.version       = "1.0.0"
  spec.authors       = ["munsterkreations"]
  spec.email         = ["104373517+munsterkreations@users.noreply.github.com"]

  spec.summary       = "Pyru-friendly interface for Ruby and Python libraries"
  spec.description   = "A Ruby gem that provides a Pyru-friendly interface bridging Ruby and Python libraries."
  spec.homepage      = "https://github.com/munsterkreations/pyru"
  spec.license       = "MIT"

  # Ruby version requirement
  spec.required_ruby_version = ">= 3.0"

  # Files included in the gem
  spec.files = Dir.glob("lib/**/*") + ["setup.py", "lib/pyru/ext/extconf.rb"]

  # Ensure Python check runs during install
  spec.extensions = ["lib/pyru/ext/extconf.rb"]

  # Runtime dependencies
  spec.add_dependency "rake", "~> 13.0"
  spec.add_dependency "rspec", "~> 3.0"
  spec.add_dependency "rubocop", "~> 1.0"

  # Development dependencies
  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "pry", "~> 0.14"
  spec.add_development_dependency "faker", "~> 2.0"

  # Metadata
  spec.metadata = {
    "source_code_uri"   => spec.homepage,
    "changelog_uri"     => "#{spec.homepage}/blob/main/CHANGELOG.md",
    "required_python"   => ">= 3.0",
    "required_ruby"     => ">= 3.0"
  }
end



