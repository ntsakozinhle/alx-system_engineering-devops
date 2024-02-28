#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

regex = /\bhbt{0,}n\b/
  
matches = ARGV[0].scan(regex)

if matches.empty?
  puts ""
else
  puts "#{matches.join("\n")}"
end
