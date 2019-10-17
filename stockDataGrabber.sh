#Grabbing and manipulating stock data
#Takes in a list of stock tickers
#loop through list, creating a file for each
filelist=()
cat stocks.txt | while read tik;
do
   curl https://api.iextrading.com/1.0/stock/$tik/chart/2y?format=csv > $tik.2y.csv
   filelist+=($tik.2y.csv)
done;
#Returns a file for each stock

for fileLine in $(cat stocks.txt); 
do 
   echo $fileLine; done;  | awk -F "," '{print $5 ","}'

while read ticker; do
   echo "$ticker"
   awk -F "," '{print $5 ","}' $ticker.2y.csv >trim/$ticker.csv
done < stocks.txt
cd trim
paste * > composite.txt
