#!/lusr/bin/perl -w

use strict;
use warnings;
use Getopt::Long;

#input: tree with both branch lengths and support values
#)sv:br

#output: see below

sub badInput {
  my $message = "Usage: perl $0
	-i=<tree>
	-o=<output tree>";
  print STDERR $message;
  die "\n";
}

GetOptions(
	"i=s"=>\my $tree,
	"o=s"=>\my $outtree,
  "n=s"=>\my $num_string,
);

badInput() if not defined $tree;
badInput() if not defined $outtree;
my $num = int($num_string) - 1;
open(OUT, ">", $outtree) or die "can't open $outtree: $!";

my @a = (0..$num);
for(@a){

  #my $char = "a-zA-Z0-9.";
  my $tree_contents = `head -n 1 $tree/$_.tre`;
  $tree_contents =~ s/\)(\d+(\.\d+)?):(\d+(\.\d+)?)/):$3/g; #):br  # this is for phylonet  # eta die edge support delet kora hoi
  #$tree_contents =~ s/\)(\d+(\.\d+)?):(\d+(\.\d+)?)/)/g; #)
  $tree_contents =~ s/:(\d+(\.\d+)?)//g; #)                          # eta thaklei hoi  USED THIS TO STRIP RAXML TREES
  #$tree_contents =~ s/:(\d+(\.\d+)?(e-\d+)?)//g; #) (no sv)  #to handle :1.223e-05 type value that includes exponential (e)

  #$tree_contents =~ s/:(-)?(\d+(\.\d+)?(E-\d+)?)//g; # for stripping beast trees  used in simulation-beast_gt_accuracy.pl
  #$tree_contents =~ s/:(-)?(\d+(\.\d+)?(e-\d+)?)//g; # for stripping beast trees  used in simulation-beast_gt_accuracy.pl for pruned ekhane e chhilo

  $tree_contents =~ s/;(.*)/;/g; #

  #=cut
  #############################

  #$tree_contents =~ s/([A-Z])(.*?)(:)/$1.lc($2).$3/eg;   # greatly done! FOR TREE WITH BRANCH LENGTH -- eta holo prothom character OF TAXA as it is rekhe (jeta originally capital) bakigula k lower case kora  . for goloboff data
  #=st
  print OUT $tree_contents;
}
close(OUT);
#=cut
print "output at $outtree\n";
print "done.\n";
