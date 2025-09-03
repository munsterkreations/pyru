require "mkmf"

# Check if Python 3 is available
python_version = `python3 --version 2>&1`.strip
if $?.success?
  puts "✓ Found #{python_version}"
else
  abort "❌ Python 3 is required to install this gem. Please install Python 3 first."
end

# Try to detect Python 3
python_cmds = ["python3", "python"]
python_found = nil
python_version = nil

python_cmds.each do |cmd|
  version_output = `#{cmd} --version 2>&1`.strip
  if $?.success? && version_output =~ /^Python (\d+\.\d+\.\d+)/
    version = Gem::Version.new($1)
    if version >= Gem::Version.new("3.0.0")
      python_found = cmd
      python_version = version_output
      break
    end
  end
end

if python_found
  puts "✓ Found #{python_version} (#{python_found})"
else
  abort "❌ Python 3.0 or newer is required to install this gem. Please install Python 3."
end


# Create a dummy Makefile (required for RubyGems to proceed)
create_makefile("pyru/pyru")
