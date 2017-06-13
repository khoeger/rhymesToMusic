set Phonemes;
set ScaleDegrees;

param phonemeProportions {p in Phonemes};
param scaleDegProportions {s in ScaleDegrees};

param heavyWeight;
param assignmentsAllowed;

var amountPlaced {ScaleDegrees, Phonemes} >=0 ;
var forceDegree {ScaleDegrees, Phonemes} binary;


minimize unallocated_phonemes:
    sum{s in ScaleDegrees}(scaleDegProportions[s] - sum{p in Phonemes}amountPlaced[s,p]);

subject to degree_capacity {s in ScaleDegrees}:
    sum{p in Phonemes}amountPlaced[s,p] <= scaleDegProportions[s];

subject to content_bounds {p in Phonemes}:
    sum{s in ScaleDegrees}amountPlaced[s,p] <= phonemeProportions[p];

subject to limit_degrees{p in Phonemes}:
    sum{s in ScaleDegrees}forceDegree[s,p] <= assignmentsAllowed;

subject to on_off_switch{s in ScaleDegrees, p in Phonemes}:
    amountPlaced[s,p] <= heavyWeight * forceDegree[s,p];
