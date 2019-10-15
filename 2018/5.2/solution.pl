my $text = <STDIN>;
chomp $text;
my $pat = join "|" => map {"$_\u$_|\u$_$_"} 'a' .. 'z';
1 while $text =~ s/$pat//g;

my $minLength = length($text);
for my $c ('a' .. 'z') {
    my $text2 = $text; 
    $text2 =~ s/$c|\u$c//g;
    1 while $text2 =~ s/$pat//g;
    $minLength = length($text2) if length($text2) < $minLength;
}
print($minLength);
