FILENAME=$1
OUTPUT=$2
NUM=$3
if [ -e $OUTPUT  ]
then
	echo ${OUTPUT} " existed and is overwritten"
	rm $OUTPUT
fi
sed -ie 's/0/\./g' $FILENAME
less ${FILENAME} | awk -F'|' 'BEGIN{print "count", "lineNum"}{print gsub(/\./,"") "\ " NR}' | awk '{if ($1 == '${NUM}') print $2;}' > ${FILENAME}_index_${NUM}
while read line; do
  sed -n ${line}p $FILENAME >> $OUTPUT
done <${FILENAME}_index_${NUM}
rm ${FILENAME}_index_${NUM}
