#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit 1
end

regex = /[A-Z]/

matches = ARGV[0].scan(regex)

concatenated = matches.join

puts concatenated
