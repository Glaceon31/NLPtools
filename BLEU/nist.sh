TRANS=$1
REF=$2
Y=$3

perl multi-bleu.perl -lc $REF/nist$Y/nist$Y.en0 $REF/nist$Y/nist$Y.en1 $REF/nist$Y/nist$Y.en2 $REF/nist$Y/nist$Y.en3 < $TRANS