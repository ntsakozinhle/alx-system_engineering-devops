#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <phone_number>"
  exit 1
end

regex = /^\d{10}$/

if ARGV[0].match?(regex)
  puts "#{ARGV[0]}"
else
  puts "#{ARGV[0]}"
end
