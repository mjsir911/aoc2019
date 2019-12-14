class Recipe does Iterable does Iterator {
    has $.nresult;
    has %.needs{Recipe} of Int;
    method new ($nresult, %needs ) {
        self.bless( :$nresult, :%needs );
    }

		method iterator ( ) { self }

		has Int $!amount_left = 0;
		method pull-one( --> Mu ){
			$!amount_left -= 1;
			if ($!amount_left < 1) {
				$!amount_left = $.nresult;
				if !%.needs {
					$.nresult
				} else {
					sum(map {
						my $need = $_.key;
						my $amount = $_.value;
						sum(map { $need.pull-one }, (1..$amount));
					}, %.needs)
				}
			} else {
				0;
			}
		}

		method get() {
			if (!%.needs) {
				return $.nresult;
			}
		}
 
		# method iterator(DNA:D:){ $.chain.comb.rotor(3).iterator }
};
 
# my $ORE = Recipe.new(1, :{});
# my $a = Recipe.new(2, :{$ORE => 9});
# my $b = Recipe.new(3, :{$ORE => 8});
# my $c = Recipe.new(5, :{$ORE => 7});
# my $ab = Recipe.new(1, :{$a => 3, $b => 4});
# my $bc = Recipe.new(1, :{$b => 5, $c => 7});
# my $ca = Recipe.new(1, :{$c => 4, $a => 1});
# my $FUEL = Recipe.new(1, :{$ab => 2, $bc => 3, $ca => 4});


my %rules;

my regex amount {(\d+) \s (\w+)}
for lines() { 
	my $test = $_ ~~ /[(<amount>)","?\s]+"=>"\s (<amount>)/;
	%rules{$test[1]{"amount"}[1].Str} = $test[1]{"amount"}[0].Int =>  map { $_{"amount"}[1].Str => $_{"amount"}[0].Int }, $test[0];
}

my $ORE = Recipe.new(1, :{});
sub getfactory(%mapping, $GOAL, %known = {"ORE" => $ORE}) {
	if !%known.ACCEPTS($GOAL) {
		my %b{Recipe} = map { getfactory(%mapping, $_.key, %known) => $_.value }, %mapping{$GOAL}.value;
		%known{$GOAL} = Recipe.new(%mapping{$GOAL}.key, %b);
	}
	%known{$GOAL};
}

# my $FUEL = getfactory(%rules, "FUEL");
# my $FUEL = %rules{"yo"};
# say $FUEL;
my $FUEL = getfactory(%rules, "FUEL");
$FUEL.pull-one.say;
