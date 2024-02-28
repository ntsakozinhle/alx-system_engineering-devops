#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_line>"
  exit 1
end

log_line = ARGV[0]
sender = log_line.match(/\[from:(.*?)\]/)[1]
receiver = log_line.match(/\[to:(.*?)\]/)[1]
flags = log_line.match(/\[flags:(.*?)\]/)[1]

puts "#{sender},#{receiver},#{flags}"
