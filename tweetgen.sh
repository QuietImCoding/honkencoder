mymsg="join the cult of the goos";

if [[ ${#mymsg} -gt 35 ]]
then
    echo "MESSAGE TOO LONG TO FIT IN TWEET"
    exit
fi

while count=$(echo "$mymsg" | python3 honkencoder.py honkify p | tee ofile | wc -c); [[ $count -gt 280 ]];
do
    count=$(echo "$mymsg" | python3 honkencoder.py honkify p | tee ofile | wc -c);
    echo $count;
done
