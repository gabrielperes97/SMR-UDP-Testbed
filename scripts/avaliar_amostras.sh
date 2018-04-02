function avaliar(){
	echo "*********************************************************"
	echo "Avaliando $1"
	python avalia-experimento.py $1
}

for i in `ls 'logs_unsec/'*$1.csv`
do
	#avaliar "logs_unsec/$i"
	avaliar "$i"
done

for i in `ls 'logs_sec/'*$1-sec.csv`
do
	#avaliar "logs_sec/$i"
	avaliar "$i"
done