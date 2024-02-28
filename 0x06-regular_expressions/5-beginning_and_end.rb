#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

regex = /^h.n$/

matches = ARGV[0].match?(regex)

if matches
  puts "#{ARGV[0]}"
else
  puts ""
end
