
use strict;

opendir D, ".";
while( readdir D )
{
	print;
	my $file = $_;
	my $on = 0;

	open( F, "<".$file );
	while( <F> )
	{
		if( /^(\-|\*)/ )
		{
			if( $on == 1 )
			{
				print $file."::".$_."\n";
				$on = 2;
			}
			if( $on == 0 )
			{
				$on = 1;
			}
		}
		else
		{
			$on = 0;
		}
	}
}
		
		
