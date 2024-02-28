#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGAM_NAME} <string>"
  exit 1
end

regex = /School/

matches = ARGV[0].scan(regex)

if matches.empty?
  puts ""
else
  puts matches.join
end
