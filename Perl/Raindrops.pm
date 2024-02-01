package Raindrops;

use v5.38;

use Exporter qw<import>;
our @EXPORT_OK = qw<raindrop>;

sub raindrop ($number) {

use constant Pli	=> "Pling";
use constant Pla	=> "Plang";
use constant Plo	=> "Plong";

    if ($number % 3 == 0 and $number % 5 == 0 and $number % 7 == 0) {
        return Pli . Pla . Plo;
    } elsif ($number % 3 == 0 and $number % 5 == 0){
        return Pli . Pla;
    } elsif ($number % 3 == 0 and $number % 7 == 0){
        return Pli . Plo;
    } elsif ($number % 5 == 0 and $number % 7 == 0){
        return Pla . Plo;
    } elsif ($number % 3 == 0){
        return Pli;
    } elsif ($number % 5 == 0){
        return Pla;
    } elsif ($number % 7 == 0){
        return Plo;
    } else {
        return $number;
    }
}
