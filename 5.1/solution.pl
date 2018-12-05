my $text = <STDIN>;
chomp $text;
my $pat = join "|" => map {"$_\u$_|\u$_$_"} 'a' .. 'z';
1 while $text =~ s/$pat//g;
print length($text);
